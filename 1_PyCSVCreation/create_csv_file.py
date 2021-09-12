import os
import sys
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import multiprocessing as mp

#Getting HTML files from the \HTMLfilestoprocess folder
#The files are sorted first
def file_list_to_process(folder_path_to_process):
    
    list_to_work = list((image_file for image_file in os.listdir(folder_path_to_process) \
    if (image_file.endswith('.' + 'htm') \
    or image_file.endswith('.' + 'html'))))
    pairs = []
    for file in list_to_work:

        location = os.path.join(folder_path_to_process, file)
        
        size = os.path.getsize(location)
        pairs.append((size, file))
        
        
        pairs.sort(key=lambda s: s[0])
    
    final_list = []

    for file in range(len(pairs)):
        final_list.append(pairs[file][1])
    
    return final_list

#function to process HTML files
def process_html_file(folder_path_to_process, HTML_file):
    
    List_of_names = [] #List to output
    Intermediate_list = [] #To separate Name, Surname, and Patronymic
    total_entries=0 #Total number of entries
    problematic_entries=0 #The number of problematic entries with # sign
    check_string = "" #The test string to find problematic entries
    with open(folder_path_to_process+os.sep+HTML_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        for records in range(1, len(soup.findAll('table')[1].findAll('tr'))):
            for columns in range(0, len(soup.findAll('table')[1].findAll('tr')[1].findAll('td'))):
                td = soup.findAll('table')[1].findAll('tr')[records].findAll('td')[columns]
                reworked_string = (td.text).replace('Г‡' , 'Ç').replace('ЖЏ' , 'Ə').replace('Дћ' , 'Ğ').replace('I' , 'I').replace('Д°' , 'İ').replace('Г–' , 'Ö').replace('Ећ' , 'Ş').replace('Гњ' , 'Ü')

                # The column with Name, Surname, and Patronymic
                if columns == 3:
                    reworked_string = reworked_string.replace(' ' , '#')
                    reworked_string = reworked_string.split('#', 2)
                    
                    for string_part in reworked_string:
                        check_string += string_part
                        if string_part != "":
                            Intermediate_list.append(string_part)
                        else:
                            print("Empty string part. Added \"XXX\" ")
                            Intermediate_list.append("XXX")
                        
                    if "#" in check_string:
                        problematic_entries+=1
                    check_string = ""
                else:
                    Intermediate_list.append(reworked_string)
            List_of_names.append(Intermediate_list)
            Intermediate_list = []
            total_entries+=1
    result_text_1 = str(folder_path_to_process+os.sep+HTML_file) + " is processed " + '\n'
    print(str(folder_path_to_process+os.sep+HTML_file) + " is processed")
    file_log = open("logFile.txt","a+")
    file_log.write(result_text_1)
    file_log.close()
    return (List_of_names, total_entries, problematic_entries)

if __name__ == "__main__":

    folder_path = os.path.dirname(os.getcwd()) + os.path.sep
    csv_file = folder_path + os.path.sep + "CSV_Files" + os.path.sep + 'file_with_names.csv'

    textfile_log = folder_path + os.path.sep + "python" + os.path.sep + "logFile.txt"
    textfile_results_log = folder_path + os.path.sep + "python" + os.path.sep + "ResultslogFile.txt"
    
    
    # Checking the existence of log files
    if os.path.exists(textfile_log):
        file_results_log = open("logFile.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
    if os.path.exists(textfile_results_log):
        file_results_log = open("ResultslogFile.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("ResultslogFile.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    
    # Checking the existence of the folder with HTML files
    folder_path_to_process = folder_path + "HTMLfilestoprocess"
    if not os.path.exists(folder_path_to_process):
        print("Error: There is no '/HTMLfilestoprocess' folder. The program is ended.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Error: There is no '/HTMLfilestoprocess' folder. The program is ended.\n")
        file_results_log.close()
        sys.exit(0)
    if not os.path.exists(folder_path+os.sep+"CSV_Files"):
        os.makedirs(folder_path+os.sep+"CSV_Files")

    HTML_files_list = file_list_to_process(folder_path_to_process)

    List_of_names = []
    Intermediate_list = []
    
    total_entries=0
    problematic_entries=0

    
    pool = mp.Pool() # Multiprocessing execution to increase speed
    # Applying multiprocessing to the function
    results = [pool.apply_async(process_html_file, args=(folder_path_to_process,HTML_file)) for HTML_file in HTML_files_list]
    output = [p.get() for p in results] # getting results

    for tuple_with_arguments in range(len(output)):
        List_of_names.extend(output[tuple_with_arguments][0])
        total_entries+=output[tuple_with_arguments][1]
        problematic_entries+=output[tuple_with_arguments][2]

    print("The total number of entries is " + str(total_entries))
    print("The number of problematic entries is " + str(problematic_entries))
    
    problematic_entries_percent = (problematic_entries/total_entries)*100
    
    print("The percentage of problematic entries is probably " + str(round(problematic_entries_percent, 2)) + "%")

    (pd.DataFrame(List_of_names)).to_csv(csv_file, header=False, index=False)
    
    result_text = "The total number of entries is " + str(total_entries) + "\n" + "The problematic number of entries is " + str(problematic_entries) + "\n" + "The percentage of problematic entries is probably " + str(round(problematic_entries_percent, 2)) + "%" + "\n"
    
    file_results_log = open("ResultslogFile.txt","a+")
    file_results_log.write(result_text)
    file_results_log.close()
    file_log = open("logFile.txt","a+")
    file_log.write(result_text)
    file_log.close()
    