import os, os.path
import re

files = os.listdir('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\employee_info\\')

class Employee:
    def __init__(self,name,id,title):
        self.name = name
        self.id = id
        self.title = title
    def __str__(self):
        return '{}, {} ({})'.format(self.name, self.title, self.id)

for file in files:
    # go to a folder where all the txt files are:
    os.chdir('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\employee_info\\')
    txt_file = open(file).readlines()
    # extract all characters that follow the pattern 'Name: ' in a greedy way:
    name = re.findall('^Name: (.+)',txt_file[0])
    # extract all characters that follow the pattern 'Title: ' in a greedy way:
    title = re.findall('^Title: (.+)',txt_file[1])
    # extract only id from the filename:
    id = os.path.basename(file)[0:3]
    employee = Employee(name[0],id,title[0])
    print(employee)
