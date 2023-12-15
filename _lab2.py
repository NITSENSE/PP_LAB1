import os
import csv
import shutil

def anatation_script(dataset_dir_name):
    while not os.path.isdir(dataset_dir_name):
        print("Введи корректное название датасета")
        dataset_dir_name = input()
    anatation_list = []
    main_folder = os.getcwd()
    os.chdir(dataset_dir_name)
    folders_list = os.listdir()    
    with open("anatation.csv", "w", encoding="utf-8") as table:
        writer = csv.writer(table)
        writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])
        for i in folders_list:
            os.chdir(i)
            anatation = os.listdir()
            for i in anatation:
                anatation_list.append([os.getcwd() + '/' + i, os.path.relpath(os.getcwd(), main_folder)+'/' + i, os.path.basename(os.getcwd())])
            os.chdir("..")
        writer.writerows(anatation_list)
    os.chdir("..")

def copy_script(source_dir, to_dir_name):
    while not os.path.isdir(source_dir):
        print("Введи корректное название исходного датасета")
        source_dir = input()
    if not os.path.isdir(to_dir_name):
        os.mkdir(to_dir_name)
    main_folder = os.getcwd()
    os.chdir(source_dir)
    with open("anatation.csv", newline="") as table:
        reader = csv.DictReader(table)
        os.chdir('..')
        os.chdir(to_dir_name)
        to_dir_csw = os.getcwd()
        with open("anatation.csv", "w", encoding="utf-8") as table2:
            writer = csv.writer(table2)
            writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])
            for row in reader:
                new_name = row["Относительный путь"].split('/') 
                old_name = new_name[-1]
                _class = new_name[-2]
                new_name = new_name[-2] + "_" + new_name[-1]
                shutil.copy(row['Абсолютный путь'], to_dir_csw)
                os.rename(old_name, new_name)
                writer.writerow([os.getcwd() + '/' + new_name, os.path.relpath(os.getcwd(), main_folder)+'/' + new_name, _class])


anatation_script('Dataset')
copy_script("Dataset", "New_dataset")