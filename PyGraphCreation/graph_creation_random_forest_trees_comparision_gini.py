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
        if file.startswith("Random_Forest") and file.endswith(".csv"):
            results.append(folder_with_results+file)
    return results


if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_with_results = os.path.dirname(os.getcwd()) + os.sep + "Results" + os.sep
    csv_files = get_list_of_files(folder_with_results)
    
    Random_Forest_Ten_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "Ten" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_Ten_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "Ten" in i and "_2" in i and "M_F" not in i]
    Random_Forest_Ten_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "Ten" in i and "_2" not in i and "M_F" in i]
    Random_Forest_Ten_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "Ten" in i and "_2" in i and "M_F" in i]
    Random_Forest_Ten_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "Ten" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_Ten_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "Ten" in i and "_2" in i and "M_F" not in i]
    Random_Forest_Ten_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "Ten" in i and "_2" not in i and "M_F" in i]
    Random_Forest_Ten_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "Ten" in i and "_2" in i and "M_F" in i]
    Random_Forest_TwentyFive_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwentyFive" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_TwentyFive_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwentyFive" in i and "_2" in i and "M_F" not in i]
    Random_Forest_TwentyFive_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwentyFive" in i and "_2" not in i and "M_F" in i]
    Random_Forest_TwentyFive_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwentyFive" in i and "_2" in i and "M_F" in i]
    Random_Forest_TwentyFive_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwentyFive" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_TwentyFive_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwentyFive" in i and "_2" in i and "M_F" not in i]
    Random_Forest_TwentyFive_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwentyFive" in i and "_2" not in i and "M_F" in i]
    Random_Forest_TwentyFive_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwentyFive" in i and "_2" in i and "M_F" in i]
    Random_Forest_Fifty_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "_Fifty_" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_Fifty_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "_Fifty_" in i and "_2" in i and "M_F" not in i]
    Random_Forest_Fifty_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "_Fifty_" in i and "_2" not in i and "M_F" in i]
    Random_Forest_Fifty_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "_Fifty_" in i and "_2" in i and "M_F" in i]
    Random_Forest_Fifty_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "_Fifty_" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_Fifty_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "_Fifty_" in i and "_2" in i and "M_F" not in i]
    Random_Forest_Fifty_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "_Fifty_" in i and "_2" not in i and "M_F" in i]
    Random_Forest_Fifty_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "_Fifty_" in i and "_2" in i and "M_F" in i]
    Random_Forest_SeventyFive_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "SeventyFive" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_SeventyFive_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "SeventyFive" in i and "_2" in i and "M_F" not in i]
    Random_Forest_SeventyFive_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "SeventyFive" in i and "_2" not in i and "M_F" in i]
    Random_Forest_SeventyFive_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "SeventyFive" in i and "_2" in i and "M_F" in i]
    Random_Forest_SeventyFive_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "SeventyFive" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_SeventyFive_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "SeventyFive" in i and "_2" in i and "M_F" not in i]
    Random_Forest_SeventyFive_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "SeventyFive" in i and "_2" not in i and "M_F" in i]
    Random_Forest_SeventyFive_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "SeventyFive" in i and "_2" in i and "M_F" in i]
    Random_Forest_OneHundred_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundred_" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_OneHundred_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundred_" in i and "_2" in i and "M_F" not in i]
    Random_Forest_OneHundred_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundred_" in i and "_2" not in i and "M_F" in i]
    Random_Forest_OneHundred_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundred_" in i and "_2" in i and "M_F" in i]
    Random_Forest_OneHundred_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundred_" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_OneHundred_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundred_" in i and "_2" in i and "M_F" not in i]
    Random_Forest_OneHundred_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundred_" in i and "_2" not in i and "M_F" in i]
    Random_Forest_OneHundred_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundred_" in i and "_2" in i and "M_F" in i]
    Random_Forest_OneHundredFifty_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundredFifty" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_OneHundredFifty_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundredFifty" in i and "_2" in i and "M_F" not in i]
    Random_Forest_OneHundredFifty_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundredFifty" in i and "_2" not in i and "M_F" in i]
    Random_Forest_OneHundredFifty_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "OneHundredFifty" in i and "_2" in i and "M_F" in i]
    Random_Forest_OneHundredFifty_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundredFifty" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_OneHundredFifty_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundredFifty" in i and "_2" in i and "M_F" not in i]
    Random_Forest_OneHundredFifty_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundredFifty" in i and "_2" not in i and "M_F" in i]
    Random_Forest_OneHundredFifty_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "OneHundredFifty" in i and "_2" in i and "M_F" in i]
    Random_Forest_TwoHundred_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwoHundred" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_TwoHundred_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwoHundred" in i and "_2" in i and "M_F" not in i]
    Random_Forest_TwoHundred_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwoHundred" in i and "_2" not in i and "M_F" in i]
    Random_Forest_TwoHundred_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "TwoHundred" in i and "_2" in i and "M_F" in i]
    Random_Forest_TwoHundred_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwoHundred" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_TwoHundred_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwoHundred" in i and "_2" in i and "M_F" not in i]
    Random_Forest_TwoHundred_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwoHundred" in i and "_2" not in i and "M_F" in i]
    Random_Forest_TwoHundred_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "TwoHundred" in i and "_2" in i and "M_F" in i]
    Random_Forest_ThreeHundred_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "ThreeHundred" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_ThreeHundred_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "ThreeHundred" in i and "_2" in i and "M_F" not in i]
    Random_Forest_ThreeHundred_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "ThreeHundred" in i and "_2" not in i and "M_F" in i]
    Random_Forest_ThreeHundred_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "ThreeHundred" in i and "_2" in i and "M_F" in i]
    Random_Forest_ThreeHundred_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "ThreeHundred" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_ThreeHundred_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "ThreeHundred" in i and "_2" in i and "M_F" not in i]
    Random_Forest_ThreeHundred_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "ThreeHundred" in i and "_2" not in i and "M_F" in i]
    Random_Forest_ThreeHundred_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "ThreeHundred" in i and "_2" in i and "M_F" in i]
    Random_Forest_FiveHundred_results_no_duplicates_all_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "FiveHundred" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_FiveHundred_results_no_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "FiveHundred" in i and "_2" in i and "M_F" not in i]
    Random_Forest_FiveHundred_results_no_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "FiveHundred" in i and "_2" not in i and "M_F" in i]
    Random_Forest_FiveHundred_results_no_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" in i and "gini" in i and "FiveHundred" in i and "_2" in i and "M_F" in i]
    Random_Forest_FiveHundred_results_with_duplicates_all_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "FiveHundred" in i and "_2" not in i and "M_F" not in i]
    Random_Forest_FiveHundred_results_with_duplicates_all_2_results = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "FiveHundred" in i and "_2" in i and "M_F" not in i]
    Random_Forest_FiveHundred_results_with_duplicates_m_f_only = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "FiveHundred" in i and "_2" not in i and "M_F" in i]
    Random_Forest_FiveHundred_results_with_duplicates_m_f_only_2 = [i for i in csv_files if "no_duplicates" not in i and "gini" in i and "FiveHundred" in i and "_2" in i and "M_F" in i]

    all_results_no_duplicates_gini = [Random_Forest_Ten_results_no_duplicates_all_results,
                           Random_Forest_TwentyFive_results_no_duplicates_all_results,
                           Random_Forest_Fifty_results_no_duplicates_all_results,
                           Random_Forest_SeventyFive_results_no_duplicates_all_results,
                           Random_Forest_OneHundred_results_no_duplicates_all_results,
                           Random_Forest_OneHundredFifty_results_no_duplicates_all_results,
                           Random_Forest_TwoHundred_results_no_duplicates_all_results,
                           Random_Forest_ThreeHundred_results_no_duplicates_all_results,
                           Random_Forest_FiveHundred_results_no_duplicates_all_results]

    all_results_2_no_duplicates_gini = [Random_Forest_Ten_results_no_duplicates_all_2_results,
                           Random_Forest_TwentyFive_results_no_duplicates_all_2_results,
                           Random_Forest_Fifty_results_no_duplicates_all_2_results,
                           Random_Forest_SeventyFive_results_no_duplicates_all_2_results,
                           Random_Forest_OneHundred_results_no_duplicates_all_2_results,
                           Random_Forest_OneHundredFifty_results_no_duplicates_all_2_results,
                           Random_Forest_TwoHundred_results_no_duplicates_all_2_results,
                           Random_Forest_ThreeHundred_results_no_duplicates_all_2_results,
                           Random_Forest_FiveHundred_results_no_duplicates_all_2_results]

    m_f_only_no_duplicates_gini = [Random_Forest_Ten_results_no_duplicates_m_f_only,
                           Random_Forest_TwentyFive_results_no_duplicates_m_f_only,
                           Random_Forest_Fifty_results_no_duplicates_m_f_only,
                           Random_Forest_SeventyFive_results_no_duplicates_m_f_only,
                           Random_Forest_OneHundred_results_no_duplicates_m_f_only,
                           Random_Forest_OneHundredFifty_results_no_duplicates_m_f_only,
                           Random_Forest_TwoHundred_results_no_duplicates_m_f_only,
                           Random_Forest_ThreeHundred_results_no_duplicates_m_f_only,
                           Random_Forest_FiveHundred_results_no_duplicates_m_f_only]

    m_f_only_2_no_duplicates_gini = [Random_Forest_Ten_results_no_duplicates_m_f_only_2,
                           Random_Forest_TwentyFive_results_no_duplicates_m_f_only_2,
                           Random_Forest_Fifty_results_no_duplicates_m_f_only_2,
                           Random_Forest_SeventyFive_results_no_duplicates_m_f_only_2,
                           Random_Forest_OneHundred_results_no_duplicates_m_f_only_2,
                           Random_Forest_OneHundredFifty_results_no_duplicates_m_f_only_2,
                           Random_Forest_TwoHundred_results_no_duplicates_m_f_only_2,
                           Random_Forest_ThreeHundred_results_no_duplicates_m_f_only_2,
                           Random_Forest_FiveHundred_results_no_duplicates_m_f_only_2]

    all_results_with_duplicates_gini = [Random_Forest_Ten_results_with_duplicates_all_results,
                           Random_Forest_TwentyFive_results_with_duplicates_all_results,
                           Random_Forest_Fifty_results_with_duplicates_all_results,
                           Random_Forest_SeventyFive_results_with_duplicates_all_results,
                           Random_Forest_OneHundred_results_with_duplicates_all_results,
                           Random_Forest_OneHundredFifty_results_with_duplicates_all_results,
                           Random_Forest_TwoHundred_results_with_duplicates_all_results,
                           Random_Forest_ThreeHundred_results_with_duplicates_all_results,
                           Random_Forest_FiveHundred_results_with_duplicates_all_results]

    all_results_2_with_duplicates_gini = [Random_Forest_Ten_results_with_duplicates_all_2_results,
                           Random_Forest_TwentyFive_results_with_duplicates_all_2_results,
                           Random_Forest_Fifty_results_with_duplicates_all_2_results,
                           Random_Forest_SeventyFive_results_with_duplicates_all_2_results,
                           Random_Forest_OneHundred_results_with_duplicates_all_2_results,
                           Random_Forest_OneHundredFifty_results_with_duplicates_all_2_results,
                           Random_Forest_TwoHundred_results_with_duplicates_all_2_results,
                           Random_Forest_ThreeHundred_results_with_duplicates_all_2_results,
                           Random_Forest_FiveHundred_results_with_duplicates_all_2_results]

    m_f_only_with_duplicates_gini = [Random_Forest_Ten_results_with_duplicates_m_f_only,
                           Random_Forest_TwentyFive_results_with_duplicates_m_f_only,
                           Random_Forest_Fifty_results_with_duplicates_m_f_only,
                           Random_Forest_SeventyFive_results_with_duplicates_m_f_only,
                           Random_Forest_OneHundred_results_with_duplicates_m_f_only,
                           Random_Forest_OneHundredFifty_results_with_duplicates_m_f_only,
                           Random_Forest_TwoHundred_results_with_duplicates_m_f_only,
                           Random_Forest_ThreeHundred_results_with_duplicates_m_f_only,
                           Random_Forest_FiveHundred_results_with_duplicates_m_f_only]

    m_f_only_2_with_duplicates_gini = [Random_Forest_Ten_results_with_duplicates_m_f_only_2,
                           Random_Forest_TwentyFive_results_with_duplicates_m_f_only_2,
                           Random_Forest_Fifty_results_with_duplicates_m_f_only_2,
                           Random_Forest_SeventyFive_results_with_duplicates_m_f_only_2,
                           Random_Forest_OneHundred_results_with_duplicates_m_f_only_2,
                           Random_Forest_OneHundredFifty_results_with_duplicates_m_f_only_2,
                           Random_Forest_TwoHundred_results_with_duplicates_m_f_only_2,
                           Random_Forest_ThreeHundred_results_with_duplicates_m_f_only_2,
                           Random_Forest_FiveHundred_results_with_duplicates_m_f_only_2]

    condition_to_be_tested = [all_results_no_duplicates_gini,
                           all_results_2_no_duplicates_gini,
                           m_f_only_no_duplicates_gini,
                           m_f_only_2_no_duplicates_gini,
                           all_results_with_duplicates_gini,
                           all_results_2_with_duplicates_gini,
                           m_f_only_with_duplicates_gini,
                           m_f_only_2_with_duplicates_gini]



    for variable in range(len(condition_to_be_tested)):
        for condition in range(len(condition_to_be_tested[variable])):
            if len(condition_to_be_tested[variable][condition]) == 0:
                continue

            for condition_check in range(len(condition_to_be_tested[variable][condition])):
                list1 = pd.read_csv(condition_to_be_tested[variable][condition][condition_check],header=None).values.tolist()
                list1 = [np.max(list1), np.argmax(list1)+1]
                if "_Ten_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(10)
                elif "_TwentyFive_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(25)
                elif "_Fifty_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(50)
                elif "_SeventyFive_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(75)
                elif "_OneHundred_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(100)
                elif "_OneHundredFifty_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(150)
                elif "_TwoHundred_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(200)
                elif "_ThreeHundred_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(300)
                elif "_FiveHundred_" in condition_to_be_tested[variable][condition][condition_check]:
                    list1.append(500)
                    
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
            for rs in range(len(name_results)):
                ax.scatter(name_results[rs][2], name_results[rs][0], color='r', label='Names only', s=30)
                ax.text(name_results[rs][2]+0.005, name_results[rs][0]+0.005, str(name_results[rs][1]), size=12)
        if len(surname_results) !=0:
            for rs in range(len(surname_results)):
                ax.scatter(surname_results[rs][2], surname_results[rs][0], color='g', label='Surnames only', s=30)
                ax.text(surname_results[rs][2]+0.005, surname_results[rs][0]+0.005, str(surname_results[rs][1]), size=12)
        if len(surname_name_results) !=0:
            for rs in range(len(surname_name_results)):
                ax.scatter(surname_name_results[rs][2], surname_name_results[rs][0], color='b', label='Names and Surnames', s=30)
                ax.text(surname_name_results[rs][2]+0.005, surname_name_results[rs][0]+0.005, str(surname_name_results[rs][1]), size=12)
        
        handles, labels = matplotlib.pyplot.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), fontsize=26)

        ax.set_xticks([0, 10, 25, 50, 75, 100, 150, 200, 300, 500])
        ax.set_yticks(np.arange(0, 1.1, 0.1))
        ax.set_xlabel("Number of Trees", fontsize=16)
        ax.set_ylabel("Accuracy fraction with training data size (percentage/100)", fontsize=16)
        ax.set_yticklabels(("0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"), fontsize=16)
        ax.set_xticklabels(("0", "10", "25", "50", "75", "100", "150", "200", "300", "500"), fontsize=16)

        text = get_variable_name(condition_to_be_tested[variable], locals())
        ax.set_title(text[0], fontsize=26)
        image_with_plotters = folder_with_results + text[0] + "_n_of_trees_compare.png"
        matplotlib.pyplot.savefig(image_with_plotters, bbox_inches=ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()).expanded(1.3, 1.2))
    #isinstance(condition_to_be_tested[0][1][2], list)
    '''
    for condition_to_be_tested_final_results in condition_to_be_tested[0]:
        if len(condition_to_be_tested_final_results[2]) == 0:
            continue
        fig, ax = matplotlib.pyplot.subplots()
        fig.set_figheight(15)
        fig.set_figwidth(15)
        name_results = [results for results in condition_to_be_tested_final_results if results[3] == 'Names only']
        surname_results = [results for results in condition_to_be_tested_final_results if results[3] == 'Surnames only']
        surname_name_results = [results for results in condition_to_be_tested_final_results if results[3] == 'Names and Surnames']

        if len(name_results) !=0:
            ax.scatter([res[2] for res in name_results], [res[0] for res in name_results], color='r', label='Names only', s=20)
#            for res in name_results:
#                ax.text(res[2]+0.01, res[0]+0.01, str(res[1]), size=16)
        if len(surname_results) !=0:
            ax.scatter([res[2] for res in surname_results], [res[0] for res in surname_results], color='g', label='Surnames only', s=20)
#            for res in surname_results:
#                ax.text(res[2]+0.01, res[0]+0.01, str(res[1]), size=16)
        if len(surname_name_results) !=0:
            ax.scatter([res[2] for res in surname_name_results], [res[0] for res in surname_name_results], color='b', label='Names and Surnames', s=20)
#            for res in surname_name_results:
#                ax.text(res[2]+0.01, res[0]+0.01, str(res[1]), size=16)

        ax.set_xticks([10, 25, 50, 75, 100, 150, 200, 300, 500])
        ax.set_yticks(np.arange(0, 1.1, 0.1))
        ax.set_xlabel("Number of Trees", fontsize=16)
        ax.set_ylabel("Accuracy fraction with training data size (percentage/100)", fontsize=16)
        ax.set_yticklabels(("0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"), fontsize=16)
        ax.set_xticklabels(("10", "25", "50", "75", "100", "150", "200", "300", "500"), fontsize=16)
        ax.legend(fontsize=16)
        text = get_variable_name(condition, locals())
        ax.set_title(text[0], fontsize=16)
        image_with_plotters = folder_with_results + text[0] + "comparision.png"
        matplotlib.pyplot.savefig(image_with_plotters, bbox_inches=ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()).expanded(1.3, 1.2))
'''