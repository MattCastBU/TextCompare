import collections
import re 
import string
import os
import sys

f=open(os.path.join(os.getcwd(),"pg1404.txt"),"r",encoding='utf-8')

fl =f.read().split()


Trump=open(os.path.join(os.getcwd(),"Trump.txt"),"r",encoding='utf-8')


fs =Trump.read().split()

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter.lower()
    return s_without_punct

orderT = []
orderH=[]
for x in fs:
    a=remove_punctuation(x)
    orderT.append(a)
for y in fl:
    b=remove_punctuation(y)
    orderH.append(b)    

a = orderH
b = orderT
counter = collections.Counter(a)
counters = collections.Counter(b)

intersection = counter & counters

for key,val in intersection.most_common():
        if len(key) > 5 and val > 200:
            print("{} = {}".format(key, val)) 


