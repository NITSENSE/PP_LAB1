import os
import csv
anatation_list = []
main_folder = os.getcwd()
with open("anatation.csv", "w", encoding="utf-8") as table:
    os.chdir('Dataset')
    folders_list = os.listdir()
    writer = csv.writer(table)
    for i in folders_list:
        print(i)
        os.chdir(i)
        anatation = os.listdir()
        for i in anatation:
            anatation_list.append([os.getcwd() + '/' + i, os.path.relpath(os.getcwd(), main_folder)+'/' + i, os.path.basename(os.getcwd())])
        os.chdir("..")
    writer.writerows(anatation_list)


