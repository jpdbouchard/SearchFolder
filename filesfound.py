import csv
import os
user_path = input("Enter the path of your file: ")
assert os.path.exists(user_path), "I did not find the path at: "+str(user_path)
os.chdir(user_path)
results  = open('files_found.csv', "wt")
writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
headers = ('Location','Size','Name')
writer.writerow(headers)
for root, dirs, files in os.walk(user_path, onerror=OSError):
    for file in files:
        filepath = os.path.join(root, file)
        row = root, os.path.getsize(filepath) >> 20, file
        writer.writerow(row)
results.close()