import pandas as pd
import numpy as np
import os
import sys
import datetime
import matplotlib.pyplot
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
import datetime


def get_variable_name(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def check_existing_files(array):
    for file in array:
        if os.path.exists(file):
            text = "\"" + file + "\" exists."
            print(text)
            file_results_log = open("logFile5_2.txt","a+")
            file_results_log.write(text + "\n")
            file_results_log.close()
        else:
            text = "Error: \"" + file + "\" doesn't exist."
            print(text)
            file_results_log = open("logFile5_2.txt","a+")
            file_results_log.write(text + "\n")
            file_results_log.close()
            sys.exit(0)


if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_path_one_level_up = os.path.dirname(os.getcwd())
    
    textfile_log = folder_path + "logFile5_2.txt"
    textfile_log_results = folder_path + "Results_logFile5_2.txt"

    if os.path.exists(textfile_log):
        file_results_log = open("logFile5_2.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile5_2.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()

    if os.path.exists(textfile_log_results):
        file_results_log = open("Results_logFile5_2.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("Results_logFile5_2.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()

    csv_with_all_surnames = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_all.csv"
    csv_with_all_surnames2 = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_all_2.csv"
    csv_with_M_F_surnames = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_M_F_only.csv"
    csv_with_M_F_surnames2 = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_M_F_only_2.csv"
    csv_decision_tree_results_gini = folder_path_one_level_up + os.sep + "Results" + os.sep + "Decision_Tree_results_gini_no_duplicates.csv"
    csv_decision_tree_results_entropy = folder_path_one_level_up + os.sep + "Results" + os.sep + "Decision_Tree_results_entropy_no_duplicates.csv"

    Files_to_be_tested = [csv_with_all_surnames, csv_with_all_surnames2, 
                          csv_with_M_F_surnames, csv_with_M_F_surnames2]

    check_existing_files(Files_to_be_tested)
    
    total_accuracy_scores = []
    
    for file in Files_to_be_tested:
        data_to_be_tested = pd.read_csv(file,header=None)
        data_to_be_tested = data_to_be_tested.drop_duplicates()
        column_names = ['Surname', 'Name', 'Gender']
        data_to_be_tested.columns=column_names
        
        surname_and_name = data_to_be_tested.drop('Gender',axis=1)
        surnames_only = data_to_be_tested.drop(['Name', 'Gender'],axis=1)
        names_only = data_to_be_tested.drop(['Surname', 'Gender'],axis=1)
        genders=data_to_be_tested['Gender']
        
        del(data_to_be_tested)
        
        names_only = preprocessing.OneHotEncoder(dtype=np.uint8).fit_transform(names_only)
        surnames_only = preprocessing.OneHotEncoder(dtype=np.uint8).fit_transform(surnames_only)
        surname_and_name = preprocessing.OneHotEncoder(dtype=np.uint8).fit_transform(surname_and_name)
        genders=genders.values.reshape(-1,1)
        genders=preprocessing.OneHotEncoder().fit_transform(genders).toarray()
        
    
        variables_to_be_tested = [surname_and_name, surnames_only, names_only]
        
        splitting_criterias = ['gini', 'entropy']
        for splitting_criteria in splitting_criterias:
            for variable in variables_to_be_tested:
                accuracy_score = []
                for test_percent in range(99, 0, -1):
                    x_train, x_test, y_train, y_test = train_test_split(variable, genders, test_size=(test_percent/100), shuffle=False)
                    classifier_decision_tree = DecisionTreeClassifier(criterion=splitting_criteria)
                    classifier_decision_tree = classifier_decision_tree.fit(x_train, y_train)
                    y_pred_decision_tree = classifier_decision_tree.predict(x_test)
                    decision_tree_accuracy_score = round(metrics.accuracy_score(y_test, y_pred_decision_tree), 3)
                    text = "Accuracy of Decision tree with no duplicates in data and splitting criterion '" + splitting_criteria + "' for " + str(get_variable_name(variable, locals())[0]) + " with training data fraction " + str(100-test_percent) + "% in " + str(file.split(os.sep)[-1]) + " is: " + str(decision_tree_accuracy_score)
                    print(text)
                    file_results_log = open("logFile5_2.txt","a+")
                    file_results_log.write(text + "\n")
                    file_results_log.close()
                    accuracy_score.append(decision_tree_accuracy_score)
                accuracy_score_max = "Maximum accuracy of Decision tree with no duplicates and splitting criterion '" + splitting_criteria + "' for " + str(get_variable_name(variable, locals())[0]) + " in " + str(file.split(os.sep)[-1]) + " is: " + str(max(accuracy_score)) + " with training data fraction " + str(accuracy_score.index(max(accuracy_score))+1) + "%"
                print(accuracy_score_max)
                file_results_log = open("logFile5_2.txt","a+")
                file_results_log.write(accuracy_score_max + "\n")
                file_results_log.close()
                file_results_log2 = open("Results_logFile5_2.txt","a+")
                file_results_log2.write(accuracy_score_max + "\n")
                file_results_log2.close()
                accuracy_score_min = "Minimum accuracy of Decision tree with no duplicates and splitting criterion '" + splitting_criteria + "' for " + str(get_variable_name(variable, locals())[0]) + " in " + str(file.split(os.sep)[-1]) + " is: " + str(min(accuracy_score)) + " with training data fraction " + str(accuracy_score.index(min(accuracy_score))+1) + "%"
                print(accuracy_score_min)
                file_results_log = open("logFile5_2.txt","a+")
                file_results_log.write(accuracy_score_min + "\n")
                file_results_log.close()
                file_results_log2 = open("Results_logFile5_2.txt","a+")
                file_results_log2.write(accuracy_score_min + "\n")
                file_results_log2.close()
                accuracy_score_average = "Average accuracy of Decision tree with no duplicates and splitting criterion '" + splitting_criteria + "' for " + str(get_variable_name(variable, locals())[0]) + " in " + str(file.split(os.sep)[-1]) + " is: " + str(round((sum(accuracy_score) / len(accuracy_score)),2))
                print(accuracy_score_average)
                file_results_log = open("logFile5_2.txt","a+")
                file_results_log.write(accuracy_score_average + "\n")
                file_results_log.close()
                file_results_log2 = open("Results_logFile5_2.txt","a+")
                file_results_log2.write(accuracy_score_average + "\n")
                file_results_log2.close()
                total_accuracy_scores.append(accuracy_score)
    
    Titles = ['All Entries', 'All Entries and Entries with Entries labeled "F" in the names ending "Ə"',
              'Only M and F labeled Entries', 'Only M and F labeled Entries with Entries labeled "F" in the names ending "Ə"']
    Subtitles = ['Names and Surnames', 'Surnames only', 'Names only']
    
    
    for i in range(0, 13, 12):
            dictionary_with_results = {Titles[0]:
                                   {Subtitles[0]: total_accuracy_scores[0+i],
                                    Subtitles[1]: total_accuracy_scores[1+i],
                                    Subtitles[2]: total_accuracy_scores[2+i]},
                                   Titles[1]:
                                       {Subtitles[0]: total_accuracy_scores[3+i],
                                    Subtitles[1]: total_accuracy_scores[4+i],
                                    Subtitles[2]: total_accuracy_scores[5+i]},
                                   Titles[2]:
                                       {Subtitles[0]: total_accuracy_scores[6+i],
                                    Subtitles[1]: total_accuracy_scores[7+i],
                                    Subtitles[2]: total_accuracy_scores[8+i]},
                                    Titles[3]:
                                           {Subtitles[0]: total_accuracy_scores[9+i],
                                    Subtitles[1]: total_accuracy_scores[10+i],
                                    Subtitles[2]: total_accuracy_scores[11+i]}}
            if i<12:
                (pd.DataFrame(dictionary_with_results)).to_csv(csv_decision_tree_results_gini, header=True, index=False)
            else:
                (pd.DataFrame(dictionary_with_results)).to_csv(csv_decision_tree_results_entropy, header=True, index=False)
    
    
    for i in range(0, 24, 3):

        fig, ax = matplotlib.pyplot.subplots()
        fig.set_figheight(15)
        fig.set_figwidth(15)
        
        ax.plot(total_accuracy_scores[0+i], color='r', label=Subtitles[0])
        ax.plot(total_accuracy_scores[1+i], color='g', label=Subtitles[1])
        ax.plot(total_accuracy_scores[2+i], color='b', label=Subtitles[2])        

        ax.set_xticks(np.arange(0, 105, 5))
        ax.set_yticks(np.arange(0, 1.1, 0.1))
        ax.set_xlabel("Training data size in percents", fontsize=16)
        ax.set_ylabel("Accuracy fraction (percentage/100)", fontsize=16)
        ax.set_yticklabels(("0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"), fontsize=16)
        ax.set_xticklabels(("0", "5", "10", "15", "20", "25", "30", "35",
                            "40", "45", "50", "55", "60", "65", "70", "75",
                            "80", "85", "90", "95", "100"), fontsize=16)
        ax.legend(fontsize=16)
        if i<12:
            text = Titles[i//3] + " (Splitting criteria=" + splitting_criterias[i//12] + ", no duplicates)"
            ax.set_title(text, fontsize=16)
            image_with_plotters = folder_path_one_level_up + os.sep + "Results" + os.sep + Titles[i//3].replace(" ", "_").replace("\"", "_") + "_" + splitting_criterias[i//12] + "_no_duplicates.png"
            matplotlib.pyplot.savefig(image_with_plotters, bbox_inches=ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()).expanded(1.3, 1.2))
        else:
            text = Titles[(i//3)-4] + " (Splitting criteria=" + splitting_criterias[i//12] + ", no duplicates)"
            ax.set_title(text, fontsize=16)
            image_with_plotters = folder_path_one_level_up + os.sep + "Results" + os.sep + Titles[(i//3)-4].replace(" ", "_").replace("\"", "_") + "_" + splitting_criterias[i//12] + "_no_duplicates.png"
            matplotlib.pyplot.savefig(image_with_plotters, bbox_inches=ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()).expanded(1.3, 1.2))