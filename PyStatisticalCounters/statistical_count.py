import pandas as pd
import os
import sys
import datetime

#file_with_names.csv

if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_path_one_level_up = os.path.dirname(os.getcwd())
    
    textfile_log = folder_path + "logFile2.txt"

    if os.path.exists(textfile_log):
        file_results_log = open("logFile2.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile2.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
        
    
    csv_file = folder_path_one_level_up + os.sep + "CSV_Files" + os.sep + "file_with_names.csv"

    csv_surnames_sorted_by_value = folder_path_one_level_up + os.sep + "Results" + os.sep + "file_with_surnames_count_sorted.csv"
    csv_surnames_sorted_by_alphabet = folder_path_one_level_up + os.sep + "Results" + os.sep + "file_with_surnames_alphabet_sorted.csv"
    
    csv_first_names_sorted_by_value = folder_path_one_level_up + os.sep + "Results" + os.sep + "file_with_first_names_count_sorted.csv"
    csv_first_names_sorted_by_alphabet = folder_path_one_level_up + os.sep + "Results" + os.sep + "file_with_first_names_alphabet_sorted.csv"

    csv_patronymic_sorted_by_value = folder_path_one_level_up + os.sep + "Results" + os.sep + "file_with_patronymic_count_sorted.csv"
    csv_patronymic_sorted_by_alphabet = folder_path_one_level_up + os.sep + "Results" + os.sep + "file_with_patronymic_alphabet_sorted.csv"
    
    if os.path.exists(csv_file):
        print("\"file_with_names.csv\" exists.")
        file_results_log = open("logFile2.txt","a+")
        file_results_log.write("\"file_with_names.csv\" exists.\n")
        file_results_log.close()
    else:
        print("Error: \"file_with_names.csv\" doesn't exist.")
        file_results_log = open("logFile2.txt","a+")
        file_results_log.write("Error: \"file_with_names.csv\" doesn't exist.\n")
        file_results_log.close()
        sys.exit(0)
    if not os.path.exists(folder_path_one_level_up+os.sep+"Results"):
        os.makedirs(folder_path_one_level_up+os.sep+"Results")
    
    data_to_analyze = pd.read_csv(csv_file,header=None)

    surname_to_count = {}    
    name_to_count = {}
    patronymic_to_count = {}

    for surname in data_to_analyze[3]:
        if surname in surname_to_count:
            surname_to_count[surname] += 1
        else:
            surname_to_count[surname] = 1

    for name in data_to_analyze[4]:
        if name in name_to_count:
            name_to_count[name] += 1
        else:
            name_to_count[name] = 1
            
    for patronymic in data_to_analyze[5]:
        if patronymic in patronymic_to_count:
            patronymic_to_count[patronymic] += 1
        else:
            patronymic_to_count[patronymic] = 1
    
    test = list(surname_to_count.items())
    test2 = list(name_to_count.items())
    test3 = list(patronymic_to_count.items())


    surname_to_count_sorted_by_values = sorted(test, key = lambda x: x[1], reverse=True)
    surname_to_count_sorted_by_alphabet = sorted(test, key = lambda x: x[0], reverse=False)
    (pd.DataFrame(surname_to_count_sorted_by_values)).to_csv(csv_surnames_sorted_by_value, header=False, index=False)
    (pd.DataFrame(surname_to_count_sorted_by_alphabet)).to_csv(csv_surnames_sorted_by_alphabet, header=False, index=False)

    name_to_count_sorted_by_values = sorted(test2, key = lambda x: x[1], reverse=True)
    name_to_count_sorted_by_alphabet = sorted(test2, key = lambda x: x[0], reverse=False)
    (pd.DataFrame(name_to_count_sorted_by_values)).to_csv(csv_first_names_sorted_by_value, header=False, index=False)
    (pd.DataFrame(name_to_count_sorted_by_alphabet)).to_csv(csv_first_names_sorted_by_alphabet, header=False, index=False)

    patronymic_to_count_sorted_by_values = sorted(test3, key = lambda x: x[1], reverse=True)
    patronymic_to_count_sorted_by_alphabet = sorted(test3, key = lambda x: x[0], reverse=False)
    (pd.DataFrame(patronymic_to_count_sorted_by_values)).to_csv(csv_patronymic_sorted_by_value, header=False, index=False)
    (pd.DataFrame(patronymic_to_count_sorted_by_alphabet)).to_csv(csv_patronymic_sorted_by_alphabet, header=False, index=False)

    
    print(str(len(surname_to_count)) + " surname entries with statistics were written successfully")
    print(str(len(name_to_count)) + " name entries with statistics were written successfully")
    print(str(len(patronymic_to_count)) + " patronymic entries with statistics were written successfully")
    
    file_results_log = open("logFile2.txt","a+")
    file_results_log.write(str(len(surname_to_count)) + " surname entries with statistics were written successfully" + "\n")
    file_results_log.write(str(len(name_to_count)) + " name entries with statistics were written successfully" + "\n")
    file_results_log.write(str(len(patronymic_to_count)) + " patronymic entries with statistics were written successfully" + "\n")
    file_results_log.close()

