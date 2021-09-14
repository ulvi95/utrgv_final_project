import pandas as pd
import numpy as np
import os
import matplotlib.pyplot


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
    
    k_nearest_neighbours_results_no_duplicates_all_results_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_results_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_all_2_results_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Two = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Three = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Four = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Five = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Six = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Seven = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Eight = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Nine = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_no_duplicates_m_f_only_2_Ten = [i for i in csv_files if "no_duplicates" in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" in i]    
    k_nearest_neighbours_results_with_duplicates_all_results_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_results_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_all_2_results_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" not in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Two = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Two" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Three = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Three" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Four = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Four" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Five = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Five" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Six = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Six" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Seven = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Seven" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Eight = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Eight" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Nine = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Nine" in i and "_2" in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" not in i and "M_F" in i]
    k_nearest_neighbours_results_with_duplicates_m_f_only_2_Ten = [i for i in csv_files if "no_duplicates" not in i and "K_Nearest_Neighbours_Ten" in i and "_2" in i and "M_F" in i]
    
    condition_to_be_tested = [k_nearest_neighbours_results_no_duplicates_all_results_Two,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Two,
                              k_nearest_neighbours_results_no_duplicates_all_results_Three,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Three,
                              k_nearest_neighbours_results_no_duplicates_all_results_Four,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Four,
                              k_nearest_neighbours_results_no_duplicates_all_results_Five,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Five,
                              k_nearest_neighbours_results_no_duplicates_all_results_Six,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Six,
                              k_nearest_neighbours_results_no_duplicates_all_results_Seven,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Seven,
                              k_nearest_neighbours_results_no_duplicates_all_results_Eight,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Eight,
                              k_nearest_neighbours_results_no_duplicates_all_results_Nine,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Nine,
                              k_nearest_neighbours_results_no_duplicates_all_results_Ten,
                              k_nearest_neighbours_results_no_duplicates_all_2_results_Ten,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Two,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Two,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Three,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Three,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Four,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Four,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Five,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Five,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Six,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Six,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Seven,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Seven,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Eight,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Eight,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Nine,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Nine,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_Ten,
                              k_nearest_neighbours_results_no_duplicates_m_f_only_2_Ten,
                              k_nearest_neighbours_results_with_duplicates_all_results_Two,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Two,
                              k_nearest_neighbours_results_with_duplicates_all_results_Three,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Three,
                              k_nearest_neighbours_results_with_duplicates_all_results_Four,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Four,
                              k_nearest_neighbours_results_with_duplicates_all_results_Five,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Five,
                              k_nearest_neighbours_results_with_duplicates_all_results_Six,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Six,
                              k_nearest_neighbours_results_with_duplicates_all_results_Seven,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Seven,
                              k_nearest_neighbours_results_with_duplicates_all_results_Eight,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Eight,
                              k_nearest_neighbours_results_with_duplicates_all_results_Nine,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Nine,
                              k_nearest_neighbours_results_with_duplicates_all_results_Ten,
                              k_nearest_neighbours_results_with_duplicates_all_2_results_Ten,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Two,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Two,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Three,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Three,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Four,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Four,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Five,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Five,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Six,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Six,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Seven,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Seven,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Eight,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Eight,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Nine,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Nine,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_Ten,
                              k_nearest_neighbours_results_with_duplicates_m_f_only_2_Ten
                              ]


    for condition in condition_to_be_tested:
        if len(condition) == 0:
            continue
        fig, ax = matplotlib.pyplot.subplots()
        fig.set_figheight(15)
        fig.set_figwidth(15)

        for condition_check in condition:
            list1 = pd.read_csv(condition_check,header=None).values.tolist()
            if "_names_only" in condition_check:
                ax.plot(range(1, 100), list1[0], color='r', label='Names only')
            elif "_surnames_only" in condition_check:
                ax.plot(range(1, 100), list1[0], color='g', label='Surnames only')
            elif "surname_name" in condition_check:
                ax.plot(range(1, 100), list1[0], color='b', label='Names and Surnames')

        ax.set_xticks(np.arange(0, 105, 5))
        ax.set_yticks(np.arange(-0.1, 1.2, 0.1))
        ax.set_xlabel("Training data size in percents", fontsize=16)
        ax.set_ylabel("Accuracy fraction (percentage/100)", fontsize=16)
        ax.set_yticklabels(("", "0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", ""), fontsize=16)
        ax.set_xticklabels(("0", "5", "10", "15", "20", "25", "30", "35",
                            "40", "45", "50", "55", "60", "65", "70", "75",
                            "80", "85", "90", "95", "100"), fontsize=16)
        ax.legend(fontsize=16)
        text = get_variable_name(condition, locals())
        ax.set_title(text[0], fontsize=16)
        image_with_plotters = folder_with_results + text[0] + ".png"
        matplotlib.pyplot.savefig(image_with_plotters, bbox_inches=ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()).expanded(1.3, 1.2))
