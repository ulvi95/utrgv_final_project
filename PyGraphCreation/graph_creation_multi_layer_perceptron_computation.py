import pandas as pd
import numpy as np
import os
import matplotlib.pyplot


def get_variable_name(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def get_list_of_files(folder_with_results):
    results = []
    for file in os.listdir(folder_with_results):
        if file.startswith("Multi_Layer_Perceptron_") and file.endswith(".csv"):
            results.append(folder_with_results+file)
    return results


if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_with_results = os.path.dirname(os.getcwd()) + os.sep + "Results" + os.sep
    csv_files = get_list_of_files(folder_with_results)
    
    multi_layer_perceptron_results_no_duplicates_all_results_OneLayer_96 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" not in i and "M_F" not in i]
    multi_layer_perceptron_results_no_duplicates_all_2_results_OneLayer_96 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" in i and "M_F" not in i]
    multi_layer_perceptron_results_no_duplicates_all_results_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" not in i and "M_F" not in i]
    multi_layer_perceptron_results_no_duplicates_all_2_results_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" in i and "M_F" not in i]
    multi_layer_perceptron_results_no_duplicates_all_results_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" not in i and "M_F" not in i]
    multi_layer_perceptron_results_no_duplicates_all_2_results_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" in i and "M_F" not in i]
    multi_layer_perceptron_results_no_duplicates_m_f_only_OneLayer_96 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" not in i and "M_F" in i]
    multi_layer_perceptron_results_no_duplicates_m_f_only_2_OneLayer_96 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" in i and "M_F" in i]
    multi_layer_perceptron_results_no_duplicates_m_f_only_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" not in i and "M_F" in i]
    multi_layer_perceptron_results_no_duplicates_m_f_only_2_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" in i and "M_F" in i]
    multi_layer_perceptron_results_no_duplicates_m_f_only_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" not in i and "M_F" in i]
    multi_layer_perceptron_results_no_duplicates_m_f_only_2_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" in i and "M_F" in i]
    multi_layer_perceptron_results_with_duplicates_all_results_OneLayer_96 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" not in i and "M_F" not in i]
    multi_layer_perceptron_results_with_duplicates_all_2_results_OneLayer_96 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" in i and "M_F" not in i]
    multi_layer_perceptron_results_with_duplicates_all_results_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" not in i and "M_F" not in i]
    multi_layer_perceptron_results_with_duplicates_all_2_results_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" in i and "M_F" not in i]
    multi_layer_perceptron_results_with_duplicates_all_results_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" not in i and "M_F" not in i]
    multi_layer_perceptron_results_with_duplicates_all_2_results_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" in i and "M_F" not in i]
    multi_layer_perceptron_results_with_duplicates_m_f_only_OneLayer_96 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" not in i and "M_F" in i]
    multi_layer_perceptron_results_with_duplicates_m_f_only_2_OneLayer_96 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_OneLayer_" in i and "_2" in i and "M_F" in i]
    multi_layer_perceptron_results_with_duplicates_m_f_only_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" not in i and "M_F" in i]
    multi_layer_perceptron_results_with_duplicates_m_f_only_2_TwoLayer_48_48 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_TwoLayer_" in i and "_2" in i and "M_F" in i]
    multi_layer_perceptron_results_with_duplicates_m_f_only_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" not in i and "M_F" in i]
    multi_layer_perceptron_results_with_duplicates_m_f_only_2_ThreeLayer_32_32_32 = [i for i in csv_files if "no_duplicates" not in i and "Multi_Layer_Perceptron_ThreeLayer_" in i and "_2" in i and "M_F" in i]
    
    condition_to_be_tested = [multi_layer_perceptron_results_no_duplicates_all_results_OneLayer_96,
                              multi_layer_perceptron_results_no_duplicates_all_2_results_OneLayer_96,
                              multi_layer_perceptron_results_no_duplicates_all_results_TwoLayer_48_48,
                              multi_layer_perceptron_results_no_duplicates_all_2_results_TwoLayer_48_48,
                              multi_layer_perceptron_results_no_duplicates_all_results_ThreeLayer_32_32_32,
                              multi_layer_perceptron_results_no_duplicates_all_2_results_ThreeLayer_32_32_32,
                              multi_layer_perceptron_results_no_duplicates_m_f_only_OneLayer_96,
                              multi_layer_perceptron_results_no_duplicates_m_f_only_2_OneLayer_96,
                              multi_layer_perceptron_results_no_duplicates_m_f_only_TwoLayer_48_48,
                              multi_layer_perceptron_results_no_duplicates_m_f_only_2_TwoLayer_48_48,
                              multi_layer_perceptron_results_no_duplicates_m_f_only_ThreeLayer_32_32_32,
                              multi_layer_perceptron_results_no_duplicates_m_f_only_2_ThreeLayer_32_32_32,
                              multi_layer_perceptron_results_with_duplicates_all_results_OneLayer_96,
                              multi_layer_perceptron_results_with_duplicates_all_2_results_OneLayer_96,
                              multi_layer_perceptron_results_with_duplicates_all_results_TwoLayer_48_48,
                              multi_layer_perceptron_results_with_duplicates_all_2_results_TwoLayer_48_48,
                              multi_layer_perceptron_results_with_duplicates_all_results_ThreeLayer_32_32_32,
                              multi_layer_perceptron_results_with_duplicates_all_2_results_ThreeLayer_32_32_32,
                              multi_layer_perceptron_results_with_duplicates_m_f_only_OneLayer_96,
                              multi_layer_perceptron_results_with_duplicates_m_f_only_2_OneLayer_96,
                              multi_layer_perceptron_results_with_duplicates_m_f_only_TwoLayer_48_48,
                              multi_layer_perceptron_results_with_duplicates_m_f_only_2_TwoLayer_48_48,
                              multi_layer_perceptron_results_with_duplicates_m_f_only_ThreeLayer_32_32_32,
                              multi_layer_perceptron_results_with_duplicates_m_f_only_2_ThreeLayer_32_32_32
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
