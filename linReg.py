#!/usr/local/bin/python3.6
"""
Created on Sun Jun 24 14:56:47 2018
NEEDS TO ONLY USE NUMPY, NOT PANDASS
@author: Jimmy
"""

import os.path
import numpy as np
import pandas as pd

#Function Definitions
def linReg():
    print('This only supports simple linear regression (SLR).','\n',
          'Please enter two valid column names, pressing enter after each entry: ')
    col1=input()
    col2=input()
    dat1=dat[col1]
    dat2=dat[col2]
    
    if len(dat1) != len(dat2):
        return("Mismatching lengths in columns")
    l1=len(dat1)
    m1=dat1.mean()
    m2=dat2.mean()
    #Pearson correlation
    print(' The length of both columns is ', l1,'\n')
    print(' The mean of column ',col1, ' is: ', m1,'\n',
          'The mean of column ',col2, ' is: ', m2,'\n')
    numer=[]
    denom1=[]
    denom2=[]
    for x in range(1,l1-1):
        numer.append((dat1[x]-m1)*(dat2[x]-m2))
        denom1.append((dat1[x]-m1)**2)
        denom2.append((dat2[x]-m2)**2)
            
          
    numer_sum=sum(numer)
    denom1_sum=np.sqrt(sum(denom1))
    denom2_sum=np.sqrt(sum(denom2))
    
    print(' The Pearson correlation of the data is: ', numer_sum/(denom1_sum*denom2_sum))
    
    
    
#Determine path validity 
cont=True
while cont==True:
    address="C:/Users/Jimmy/OneDrive/Cluster/pyScripts/rdata.csv"
    #address=input("Please enter the filepath of the data file, or 'z' to exit:  ")
    if os.path.isfile(address):
        print("File path is valid.",'\n')
        cont=False
    elif address == "z":
        print("You chose to exit.")
        break
    else:
        print("The file path doesn't exist!")
if address=='z':
    exit()

#Read in data file
dat=pd.read_csv(address,index_col=0)
print('Here is the head of your imported file: ','\n',dat.head(3),'\n')

#Start Menu
print('Options Menu:','\n',
      ' (1) Linear Regression', '\n',
      ' (z) to quit!','\n')
inp=input()
if inp=='1':
    linReg()
elif inp=='z':
    exit()


