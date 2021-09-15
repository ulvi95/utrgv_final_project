import pandas as pd
import numpy as np
import os
import matplotlib.pyplot
import sys

def get_variable_name(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def get_list_of_files(folder_with_results):
    results = []
    for file in os.listdir(folder_with_results):
        if file.startswith("K_Nearest_Neighbours") and file.endswith(".csv"):
            results.append(folder_with_results+file)
    return results


if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_with_results = os.path.dirname(os.getcwd()) + os.sep + "Results" + os.sep
    csv_files = get_list_of_files(folder_with_results)
    
    k_nearest_neighbours_results_no_duplicates_all_results_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" in i and "Canberra" not in i]    
    k_nearest_neighbours_results_with_duplicates_all_results_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" not in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" in i and "Canberra" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" in i and "Canberra" not in i]

    all_results_no_duplicates = [k_nearest_neighbours_results_no_duplicates_all_results_Two,
                           k_nearest_neighbours_results_no_duplicates_all_results_Three,
                           k_nearest_neighbours_results_no_duplicates_all_results_Four,
                           k_nearest_neighbours_results_no_duplicates_all_results_Five,
                           k_nearest_neighbours_results_no_duplicates_all_results_Six,
                           k_nearest_neighbours_results_no_duplicates_all_results_Seven,
                           k_nearest_neighbours_results_no_duplicates_all_results_Eight,
                           k_nearest_neighbours_results_no_duplicates_all_results_Nine,
                           k_nearest_neighbours_results_no_duplicates_all_results_Ten]

    all_results_2_no_duplicates = [k_nearest_neighbours_results_no_duplicates_all_2_results_Two,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Three,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Four,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Five,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Six,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Seven,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Eight,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Nine,
                           k_nearest_neighbours_results_no_duplicates_all_2_results_Ten]

    m_f_only_no_duplicates = [k_nearest_neighbours_results_no_duplicates_m_f_only_Two,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Three,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Four,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Five,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Six,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Seven,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Eight,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Nine,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_Ten]

    m_f_only_2_no_duplicates = [k_nearest_neighbours_results_no_duplicates_m_f_only_2_Two,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Three,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Four,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Five,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Six,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Seven,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Eight,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Nine,
                           k_nearest_neighbours_results_no_duplicates_m_f_only_2_Ten]

    all_results_with_duplicates = [k_nearest_neighbours_results_with_duplicates_all_results_Two,
                           k_nearest_neighbours_results_with_duplicates_all_results_Three,
                           k_nearest_neighbours_results_with_duplicates_all_results_Four,
                           k_nearest_neighbours_results_with_duplicates_all_results_Five,
                           k_nearest_neighbours_results_with_duplicates_all_results_Six,
                           k_nearest_neighbours_results_with_duplicates_all_results_Seven,
                           k_nearest_neighbours_results_with_duplicates_all_results_Eight,
                           k_nearest_neighbours_results_with_duplicates_all_results_Nine,
                           k_nearest_neighbours_results_with_duplicates_all_results_Ten]

    all_results_2_with_duplicates = [k_nearest_neighbours_results_with_duplicates_all_2_results_Two,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Three,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Four,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Five,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Six,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Seven,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Eight,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Nine,
                           k_nearest_neighbours_results_with_duplicates_all_2_results_Ten]

    m_f_only_with_duplicates = [k_nearest_neighbours_results_with_duplicates_m_f_only_Two,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Three,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Four,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Five,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Six,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Seven,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Eight,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Nine,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_Ten]

    m_f_only_2_with_duplicates = [k_nearest_neighbours_results_with_duplicates_m_f_only_2_Two,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Three,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Four,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Five,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Six,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Seven,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Eight,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Nine,
                           k_nearest_neighbours_results_with_duplicates_m_f_only_2_Ten]

    condition_to_be_tested = [all_results_no_duplicates,
                           all_results_2_no_duplicates,
                           m_f_only_no_duplicates,
                           m_f_only_2_no_duplicates,
                           all_results_with_duplicates,
                           all_results_2_with_duplicates,
                           m_f_only_with_duplicates,
                           m_f_only_2_with_duplicates]

    for variable in range(len(condition_to_be_tested)):
        for condition in range(len(condition_to_be_tested[variable])):
            if len(condition_to_be_tested[variable][condition]) == 0:
                continue

            for condition_check in range(len(condition_to_be_tested[variable][condition])):
                list1 = pd.read_csv(condition_to_be_tested[variable][condition][condition_check],header=None).values.tolist()
                list1 = [np.max(list1), np.argmax(list1)+1]
                if "_Two" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(1)
                elif "_Three" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(2)
                elif "_Four" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(3)
                elif "_Five" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(4)
                elif "_Six" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(5)
                elif "_Seven" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(6)
                elif "_Eight" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(7)
                elif "_Nine" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(8)
                elif "_Ten" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(9)
                    
                if "_names_only" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append("Names only")
                elif "_surnames_only" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append("Surnames only")
                elif "surname_name" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append("Names and Surnames")
                condition_to_be_tested[variable][condition].append(list1)



    
    for variable in range(len(condition_to_be_tested)):
        name_results = []
        surname_results = []
        surname_name_results = []
        for condition in range(len(condition_to_be_tested[variable])):
            if len(condition_to_be_tested[variable][condition]) == 0:
                continue
            for result in range(len(condition_to_be_tested[variable][condition])):
                if isinstance(condition_to_be_tested[variable][condition][result], list) is True:
                    if condition_to_be_tested[variable][condition][result][3] == "Names only":
                        name_results.append(condition_to_be_tested[variable][condition][result])
                    if condition_to_be_tested[variable][condition][result][3] == "Surnames only":
                        surname_results.append(condition_to_be_tested[variable][condition][result])
                    if condition_to_be_tested[variable][condition][result][3] == "Names and Surnames":
                        surname_name_results.append(condition_to_be_tested[variable][condition][result])
        if len(name_results) == 0 and len(surname_results) == 0 and len(surname_name_results) == 0:
            continue
      
        fig, ax = matplotlib.pyplot.subplots()
        fig.set_figheight(15)
        fig.set_figwidth(15)


        if len(name_results) !=0:
            name_results_x = []
            name_results_y = []
            for rs in range(len(name_results)):
                name_results_x.append(name_results[rs][2])
                name_results_y.append(name_results[rs][0])
                ax.text(name_results[rs][2], name_results[rs][0]+0.2, str(name_results[rs][1]), size=12, color='r')
            ax.plot(name_results_x, name_results_y, color='r', label='Names only', marker='o')
        if len(surname_results) !=0:
            surname_results_x = []
            surname_results_y = []
            for rs in range(len(surname_results)):
                surname_results_x.append(surname_results[rs][2])
                surname_results_y.append(surname_results[rs][0])
                ax.text(surname_results[rs][2], surname_results[rs][0]+0.25, str(surname_results[rs][1]), size=12, color='g')
            ax.plot(surname_results_x, surname_results_y, color='g', label='Surnames only', marker='o')
        if len(surname_name_results) !=0:
            surname_name_results_x = []
            surname_name_results_y = []
            for rs in range(len(surname_name_results)):
                surname_name_results_x.append(surname_name_results[rs][2])
                surname_name_results_y.append(surname_name_results[rs][0])
                ax.text(surname_name_results[rs][2], surname_name_results[rs][0]+0.35, str(surname_name_results[rs][1]), size=12, color='b')
            ax.plot(surname_name_results_x, surname_name_results_y, color='b', label='Names and Surnames', marker='o')
        
        handles, labels = matplotlib.pyplot.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), fontsize=26)

        ax.set_xticks(np.arange(1, 11))
        ax.set_yticks(np.arange(-0.1, 1.2, 0.1))
        ax.set_xlabel("Number of N's (in the points, the proper result with training data size percent)", fontsize=16)
        ax.set_ylabel("Maximum accuracy fraction with training data size (percentage/100)", fontsize=16)
        ax.set_yticklabels(("", "0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", ""), fontsize=16)
        ax.set_xticklabels(("2", "3", "4", "5", "6", "7", "8", "9", "10", ""), fontsize=16)

        text = get_variable_name(condition_to_be_tested[variable], locals())
        ax.set_title("K_nearest_neighbors_n_compare_"+text[0], fontsize=22)
        image_with_plotters = folder_with_results + "K_nearest_neighbors_n_compare_" + text[0] + ".png"
        matplotlib.pyplot.savefig(image_with_plotters, bbox_inches=ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()).expanded(1.3, 1.2))
