import pandas as pd
import os
import sys
import datetime


if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_path_one_level_up = os.path.dirname(os.getcwd())
    
    textfile_log = folder_path + "logFile4.txt"

    if os.path.exists(textfile_log):
        file_results_log = open("logFile4.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile4.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
           
    csv_file = folder_path_one_level_up + os.sep + "CSV_Files" + os.sep + "file_with_names.csv"
    
    csv_with_all_surnames = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_all.csv"
    csv_with_M_F_surnames = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_M_F_only.csv"
    
    if os.path.exists(csv_file):
        print("\"file_with_names.csv\" exists.")
        file_results_log = open("logFile4.txt","a+")
        file_results_log.write("\"file_with_names.csv\" exists.\n")
        file_results_log.close()
    else:
        print("Error: \"file_with_names.csv\" doesn't exist.")
        file_results_log = open("logFile4.txt","a+")
        file_results_log.write("Error: \"file_with_names.csv\" doesn't exist.\n")
        file_results_log.close()
        sys.exit(0)
    if not os.path.exists(folder_path_one_level_up+os.sep+"Results"):
        os.makedirs(folder_path_one_level_up+os.sep+"Results")
    
    data_to_analyze = pd.read_csv(csv_file,header=None)
    surnames_names_only = pd.DataFrame({'Surname': data_to_analyze[3], 'Name': data_to_analyze[4],"Gender": ""})
    
    for row in surnames_names_only.iterrows():
        if (row[1]["Surname"][-2:] == "OV") or (row[1]["Surname"][-2:] == "EV"):
            row[1]["Gender"] = "M"
        elif (row[1]["Surname"][-3:] == "OVA") or (row[1]["Surname"][-3:] == "EVA"):
            row[1]["Gender"] = "F"
        else:
            row[1]["Gender"] = "CBD"
        if ((row[0]+1) % 1000 == 0):
            print(str((row[0]+1)) + " values processed.")
    
    surnames_names_M_F_only = surnames_names_only[(surnames_names_only.Gender == 'M') | (surnames_names_only.Gender == 'F')]
    
    (pd.DataFrame(surnames_names_only)).to_csv(csv_with_all_surnames, header=False, index=False)
    (pd.DataFrame(surnames_names_M_F_only)).to_csv(csv_with_M_F_surnames, header=False, index=False)
    
    print(str(len(surnames_names_M_F_only)) + " \"M\" and \"F\" surname entries were written successfully")
    print(str(len(surnames_names_only)) + " surname entries with genders were written successfully")

    file_results_log = open("logFile4.txt","a+")
    file_results_log.write(str(len(surnames_names_M_F_only)) + " \"M\" and \"F\" surname entries were written successfully" + "\n")
    file_results_log.write(str(len(surnames_names_only)) + " surname entries with genders were written successfully" + "\n")
    file_results_log.close()