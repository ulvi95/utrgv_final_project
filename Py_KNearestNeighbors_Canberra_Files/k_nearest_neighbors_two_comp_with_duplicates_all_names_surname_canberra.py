import pandas as pd
import numpy as np
import os
import sys
import datetime
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing


def get_variable_name(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def check_existing_file(file):
    if os.path.exists(file):
        text = "\"" + file + "\" exists."
        print(text)
        file_results_log = open("logfile9_2.txt","a+")
        file_results_log.write(text + "\n")
        file_results_log.close()
    else:
        text = "Error: \"" + file + "\" doesn't exist."
        print(text)
        file_results_log = open("logfile9_2.txt","a+")
        file_results_log.write(text + "\n")
        file_results_log.close()
        sys.exit(0)


if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_path_one_level_up = os.path.dirname(os.getcwd())
    
    textfile_log = folder_path + "logfile9_2.txt"
    textfile_log_results = folder_path + "Results_logfile9_2.txt"

    if os.path.exists(textfile_log):
        file_results_log = open("logfile9_2.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logfile9_2.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
    if os.path.exists(textfile_log_results):
        file_results_log = open("Results_logfile9_2.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("Results_logfile9_2.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
    csv_with_all_surnames = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_all.csv"
    csv_K_Nearest_Neighbours_Two_results = folder_path_one_level_up + os.sep + "Results" + os.sep + "K_Nearest_Neighbours_Two_results_surnames_only_Canberra.csv"

    check_existing_file(csv_with_all_surnames)
    
    total_accuracy_scores = []
    

    data_to_be_tested = pd.read_csv(csv_with_all_surnames,header=None)
    column_names = ['Surname', 'Name', 'Gender']
    data_to_be_tested.columns=column_names
    
    surnames_only = data_to_be_tested.drop(['Name', 'Gender'],axis=1)
    genders=data_to_be_tested['Gender']
    
    del(data_to_be_tested)
    
    surnames_only = surnames_only.apply(lambda x: pd.factorize(x)[0])
    genders=genders.factorize()
    genders=genders[0].copy()

    accuracy_score = []
    n_neigbors=2
    for test_percent in range(99, 0, -1):
        x_train, x_test, y_train, y_test = train_test_split(surnames_only, genders, test_size=(test_percent/100), shuffle=False)
        x_train = preprocessing.scale(x_train)
        x_test = preprocessing.scale(x_test)
        classifier_K_Nearest_Neighbours_Two = KNeighborsClassifier(n_neighbors=n_neigbors, metric='canberra')
        classifier_K_Nearest_Neighbours_Two = classifier_K_Nearest_Neighbours_Two.fit(x_train, y_train)
        y_pred_K_Nearest_Neighbours_Two = classifier_K_Nearest_Neighbours_Two.predict(x_test)
        K_Nearest_Neighbours_Two_accuracy_score = round(metrics.accuracy_score(y_test, y_pred_K_Nearest_Neighbours_Two), 3)
        text = "Accuracy of K Nearest Neighbours with " + str(n_neigbors) + " neighbors and Canberra distance " + "for " + str(get_variable_name(surnames_only, locals())[0]) + " with training data fraction " + str(100-test_percent) + "% in " + str(csv_with_all_surnames.split(os.sep)[-1]) + " is: " + str(K_Nearest_Neighbours_Two_accuracy_score)
        print(text)
        file_results_log = open("logfile9_2.txt","a+")
        file_results_log.write(text + "\n")
        file_results_log.close()
        accuracy_score.append(K_Nearest_Neighbours_Two_accuracy_score)
    accuracy_score_max = "Maximum accuracy of K Nearest Neighbours with " + str(n_neigbors) + " neighbors and Canberra distance " + "for " + str(get_variable_name(surnames_only, locals())[0]) + " in " + str(csv_with_all_surnames.split(os.sep)[-1]) + " is: " + str(max(accuracy_score)) + " with training data fraction " + str(accuracy_score.index(max(accuracy_score))+1) + "%"
    print(accuracy_score_max)
    file_results_log = open("logfile9_2.txt","a+")
    file_results_log.write(accuracy_score_max + "\n")
    file_results_log.close()
    file_results_log2 = open("Results_logfile9_2.txt","a+")
    file_results_log2.write(accuracy_score_max + "\n")
    file_results_log2.close()
    accuracy_score_min = "Minimum accuracy of K Nearest Neighbours with " + str(n_neigbors) + " neighbors and Canberra distance " + "for " + str(get_variable_name(surnames_only, locals())[0]) + " in " + str(csv_with_all_surnames.split(os.sep)[-1]) + " is: " + str(min(accuracy_score)) + " with training data fraction " + str(accuracy_score.index(min(accuracy_score))+1) + "%"
    print(accuracy_score_min)
    file_results_log = open("logfile9_2.txt","a+")
    file_results_log.write(accuracy_score_min + "\n")
    file_results_log.close()
    file_results_log2 = open("Results_logfile9_2.txt","a+")
    file_results_log2.write(accuracy_score_min + "\n")
    file_results_log2.close()
    accuracy_score_average = "Average accuracy of K Nearest Neighbours with " + str(n_neigbors) + " neighbors and Canberra distance " + "for " + str(get_variable_name(surnames_only, locals())[0]) + " in " + str(csv_with_all_surnames.split(os.sep)[-1]) + " is: " + str(round((sum(accuracy_score) / len(accuracy_score)),2))
    print(accuracy_score_average)
    file_results_log = open("logfile9_2.txt","a+")
    file_results_log.write(accuracy_score_average + "\n")
    file_results_log.close()
    file_results_log2 = open("Results_logfile9_2.txt","a+")
    file_results_log2.write(accuracy_score_average + "\n")
    file_results_log2.close()
    total_accuracy_scores.append(accuracy_score)    

    (pd.DataFrame(total_accuracy_scores)).to_csv(csv_K_Nearest_Neighbours_Two_results, header=False, index=False)
