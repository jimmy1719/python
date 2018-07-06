#!/usr/local/bin/python3.6
import os
from shutil import copy

print('Utility code to create new directories and copy files into them.')
str1=input("Please enter a prefix for the directories: ")
#print('\n')
str2=int(input("Please enter the starting number: "))
#print('\n')
str3=int(input("Please enter the ending number: "))
rang=str3-str2

src=[]
cwd=os.getcwd()
cont=True
while cont==True:
	dec=input("Add new file? (y/n): ")
	if dec=="y":
		src.append(cwd+'/'+input("Enter requested file name: "))
	elif dec=="n":
		cont=False

print(src)
for x in range(rang+1):
	directory=str1+str(str2+x).zfill(3)
	if not os.path.exists(directory):
		os.makedirs(directory)
		for item in src:
			copy(item,directory)
			




