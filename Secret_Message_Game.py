import os
import string

file_list = os.listdir("C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\secret_message")
saved_path = os.getcwd()
os.chdir("C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\secret_message")

for file in file_list:
	trans_table = str.maketrans('','','0123456789')
	os.rename(file, file.translate(trans_table))

file_list = os.listdir("C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\secret_message")
print('Renamed files are:')
print(file_list)
