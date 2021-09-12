# utrgv_final_project
 The data creation, data analysis, gender labeling, and the analyses of different ML methods with their execution.

**This is the final project by Ulvi Bajarani at UTRGV, the MS in Information Technology. The project that is in Python 3.8.8 consists of:**

1) The data creation from HTML files with Azerbaijani electors. The result file is in the **_"CSV_Files"_** folder, with the file named **_"file_with_names.csv"_**. If you want to create the file on your own, or see the Python file, go to **_"1_PyCSVCreation"_** and work with the file named **_"create_csv_file.py"_**. To do the last step, make sure that there are some file(s) from the **_"HTMLfilestoprocess"_** folder is/are already in **_"HTMLfilestoprocess"_** folder.

2) The data analyses. This is done by the .py files in the **_"PyStatisticalCounters"_** folder.

3) The creation of data labeled with genders. This is done by .py files in the **_"2_PyGenderDataCreation"_** folder (2 variants differing from each other with 1 condition.). Make sure that "file_with_names.csv" is generated, otherwise the files don't work.

4) Various Machine Learning methods for the Classificion. All files in the folders starting with **_"Py_"_** .Make sure that at least one of the file from the list (**_surnames_labeled_all.csv, surnames_labeled_all_2.csv, surnames_labeled_M_F_only.csv, surnames_labeled_M_F_only_2.csv_**) is generated, otherwise the files don't work. 

5) Plot creation. This is done by the files in **_"PyGraphCreation"_** folder. If the step 4 is not done, nothing will be generated.

All results are saved in the **"Results"** folder.

Required packages for the project and their installation by Pip:

1) **BeautifulSoup4 (pip install beautifulsoup4)**
2) **Skicit-Learn (pip install scikit-learn)**
3) **scikit-learn-intelex (pip install scikit-learn-intelex)** (Only for SVM Accelerated)
4) **matplotlib.pyplot (pip install matplotlib)**
5) **numpy (pip install numpy)**
6) **pandas (pip install pandas)**
