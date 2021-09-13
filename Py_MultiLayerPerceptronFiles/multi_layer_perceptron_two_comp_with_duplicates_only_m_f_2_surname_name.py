import pandas as pd
import numpy as np
import os
import sys
import datetime
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing


def get_variable_name(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def check_existing_file(file):
    if os.path.exists(file):
        text = "\"" + file + "\" exists."
        print(text)
        file_results_log = open("logfile11.txt","a+")
        file_results_log.write(text + "\n")
        file_results_log.close()
    else:
        text = "Error: \"" + file + "\" doesn't exist."
        print(text)
        file_results_log = open("logfile11.txt","a+")
        file_results_log.write(text + "\n")
        file_results_log.close()
        sys.exit(0)


if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_path_one_level_up = os.path.dirname(os.getcwd())
    
    textfile_log = folder_path + "logfile11.txt"
    textfile_log_results = folder_path + "Results_logfile11.txt"

    if os.path.exists(textfile_log):
        file_results_log = open("logfile11.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logfile11.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
    if os.path.exists(textfile_log_results):
        file_results_log = open("Results_logfile11.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("Results_logfile11.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
    csv_with_M_F_surnames = folder_path_one_level_up + os.sep + "Results" + os.sep + "surnames_labeled_M_F_only_2.csv"
    csv_Multi_Layer_Perceptron_TwoLayer_results = folder_path_one_level_up + os.sep + "Results" + os.sep + "Multi_Layer_Perceptron_TwoLayer_results_surname_name_M_F_only_2.csv"

    check_existing_file(csv_with_M_F_surnames)
    
    total_accuracy_scores = []
    

    data_to_be_tested = pd.read_csv(csv_with_M_F_surnames,header=None)
    column_names = ['Surname', 'Name', 'Gender']
    data_to_be_tested.columns=column_names
    
    surname_and_name = data_to_be_tested.drop('Gender',axis=1)
    genders=data_to_be_tested['Gender']
    
    del(data_to_be_tested)
    
    surname_and_name = surname_and_name.apply(lambda x: pd.factorize(x)[0])
    genders=genders.factorize()
    genders=genders[0].copy()

    accuracy_score = []

    for test_percent in range(99, 0, -1):
        x_train, x_test, y_train, y_test = train_test_split(surname_and_name, genders, test_size=(test_percent/100), shuffle=False)
        x_train = preprocessing.scale(x_train)
        x_test = preprocessing.scale(x_test)
        classifier_Multi_Layer_Perceptron = Sequential()
        classifier_Multi_Layer_Perceptron.add(Dense(48, input_dim=2, activation='sigmoid'))
        classifier_Multi_Layer_Perceptron.add(Dense(48, activation='sigmoid'))
        classifier_Multi_Layer_Perceptron.add(Dense(2, activation='sigmoid'))
        classifier_Multi_Layer_Perceptron.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        classifier_Multi_Layer_Perceptron.fit(x_train, y_train, epochs=150, batch_size=200, verbose=0)
        y_pred_Multi_Layer_Perceptron_TwoLayer = np.argmax(classifier_Multi_Layer_Perceptron.predict(x_test), axis=-1)
        Multi_Layer_Perceptron_TwoLayer_accuracy_score = round(metrics.accuracy_score(y_test, y_pred_Multi_Layer_Perceptron_TwoLayer), 3)
        text = "Accuracy of Multi-Layer Perceptron with two layers for " + str(get_variable_name(surname_and_name, locals())[0]) + " with training data fraction " + str(100-test_percent) + "% in " + str(csv_with_M_F_surnames.split(os.sep)[-1]) + " is: " + str(Multi_Layer_Perceptron_TwoLayer_accuracy_score)
        print(text)
        file_results_log = open("logfile11.txt","a+")
        file_results_log.write(text + "\n")
        file_results_log.close()
        accuracy_score.append(Multi_Layer_Perceptron_TwoLayer_accuracy_score)
    accuracy_score_max = "Maximum accuracy of Multi-Layer Perceptron with two layers for " + str(get_variable_name(surname_and_name, locals())[0]) + " in " + str(csv_with_M_F_surnames.split(os.sep)[-1]) + " is: " + str(max(accuracy_score)) + " with training data fraction " + str(accuracy_score.index(max(accuracy_score))+1) + "%"
    print(accuracy_score_max)
    file_results_log = open("logfile11.txt","a+")
    file_results_log.write(accuracy_score_max + "\n")
    file_results_log.close()
    file_results_log2 = open("Results_logfile11.txt","a+")
    file_results_log2.write(accuracy_score_max + "\n")
    file_results_log2.close()
    accuracy_score_min = "Minimum accuracy of Multi-Layer Perceptron with two layers for " + str(get_variable_name(surname_and_name, locals())[0]) + " in " + str(csv_with_M_F_surnames.split(os.sep)[-1]) + " is: " + str(min(accuracy_score)) + " with training data fraction " + str(accuracy_score.index(min(accuracy_score))+1) + "%"
    print(accuracy_score_min)
    file_results_log = open("logfile11.txt","a+")
    file_results_log.write(accuracy_score_min + "\n")
    file_results_log.close()
    file_results_log2 = open("Results_logfile11.txt","a+")
    file_results_log2.write(accuracy_score_min + "\n")
    file_results_log2.close()
    accuracy_score_average = "Average accuracy of Multi-Layer Perceptron with two layers for " + str(get_variable_name(surname_and_name, locals())[0]) + " in " + str(csv_with_M_F_surnames.split(os.sep)[-1]) + " is: " + str(round((sum(accuracy_score) / len(accuracy_score)),2))
    print(accuracy_score_average)
    file_results_log = open("logfile11.txt","a+")
    file_results_log.write(accuracy_score_average + "\n")
    file_results_log.close()
    file_results_log2 = open("Results_logfile11.txt","a+")
    file_results_log2.write(accuracy_score_average + "\n")
    file_results_log2.close()
    total_accuracy_scores.append(accuracy_score)

    (pd.DataFrame(total_accuracy_scores)).to_csv(csv_Multi_Layer_Perceptron_TwoLayer_results, header=False, index=False)
