import pandas as pd
import os
import sys
import datetime
import numpy as np
import matplotlib.pyplot

#file_with_names.csv

if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    folder_path_one_level_up = os.path.dirname(os.getcwd())
    
    textfile_log = folder_path + "logFile3.txt"

    if os.path.exists(textfile_log):
        file_results_log = open("logFile3.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile3.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    
    csv_file = folder_path_one_level_up + os.sep + "CSV_Files" + os.sep + "file_with_names.csv"

    csv_with_years = folder_path_one_level_up + os.sep + "Results" + os.sep + "file_with_years_count_sorted.csv"
    image_with_years = folder_path_one_level_up + os.sep + "Results" + os.sep + "graph_with_years.png"
    
    if os.path.exists(csv_file):
        print("\"file_with_names.csv\" exists.")
        file_results_log = open("logFile3.txt","a+")
        file_results_log.write("\"file_with_names.csv\" exists.\n")
        file_results_log.close()
    else:
        print("Error: \"file_with_names.csv\" doesn't exist.")
        file_results_log = open("logFile3.txt","a+")
        file_results_log.write("Error: \"file_with_names.csv\" doesn't exist.\n")
        file_results_log.close()
        sys.exit(0)
    if not os.path.exists(folder_path_one_level_up+os.sep+"Results"):
        os.makedirs(folder_path_one_level_up+os.sep+"Results")
    
    data_to_analyze = pd.read_csv(csv_file,header=None)

    year_to_count = {}

    for year in data_to_analyze[7]:
        if year in year_to_count:
            year_to_count[year] += 1
        else:
            year_to_count[year] = 1

    test = list(year_to_count.items())

    year_to_count_sorted_by_years = sorted(test, key = lambda x: x[0], reverse=False)
    (pd.DataFrame(year_to_count_sorted_by_years)).to_csv(csv_with_years, header=False, index=False)
    
    years_by_values = data_to_analyze[7].copy()
    
    years_by_values.sort_values(inplace=True)
    years_by_values.reset_index(drop=True, inplace=True)
    
    print(str(len(year_to_count)) + " year entries with statistics were counted successfully")

    
    years_x = np.array([i[0] for i in year_to_count_sorted_by_years])
    count_y = np.array([i[1] for i in year_to_count_sorted_by_years])
    
    
    average_age = 0
    for i in range(len(years_x)):
        average_age+=((2020-years_x[i])*count_y[i])
    average_age/=len(data_to_analyze[7])
    
    
    file_results_log = open("logFile3.txt","a+")
    text_to_write = "The average age of a voter is equal to " + str(round(average_age, 2))
    print(text_to_write)
    file_results_log.write(text_to_write + "\n")
    file_results_log.close()
    
    file_results_log = open("logFile3.txt","a+")
    if (len(years_by_values) % 2)==0:
        median = 2020-((years_by_values[len(years_by_values)/2] 
                  + years_by_values[(len(years_by_values)/2)+1]) / 2)
        text_to_write = "The median age of people is " + str(median)
        print(text_to_write)
        file_results_log.write(text_to_write + "\n")
    else:
        median = 2020-years_by_values[len(years_by_values)//2]
        text_to_write = "The median age of people is " + str(median)
        print(text_to_write)
        file_results_log.write(text_to_write + "\n")
    file_results_log.close()

    fig, ax = matplotlib.pyplot.subplots()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    
    ax.bar(years_x,count_y)
    
    ax.xaxis.set_tick_params(pad=1)
    ax.yaxis.set_tick_params(pad=1)
    ax.set_ylabel("The number of people", fontsize=16, fontdict=dict(weight='bold'))
    ax.set_xlabel("The year of birth", fontsize=16, fontdict=dict(weight='bold'))
    ax.set_yticks(np.arange(10000, 140001, 10000))
    ax.set_yticklabels(("10000", "20000", "30000", "40000", "50000", "60000", "70000", "80000",
                        "90000", "100000", "110000", "120000", "130000", "140000"), fontsize=16)
    ax.set_xticks(np.arange(1890, 2011, 10))
    ax.set_xticklabels(("1890", "1900", "1910", "1920", "1930", "1940", "1950", "1960", "1970", 
                        "1980", "1990", "2000", "2010"), fontsize=16)

    matplotlib.pyplot.savefig(image_with_years, bbox_inches=ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted()).expanded(1.3, 1.2))
