#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    res=""
    temp=sentence
    length=len(sentence)
    for i in  range (length):
        if i==0 or sentence[i]==' ' or sentence[i-1]==' ' or i==length-1:
            res+=sentence[i]
        elif ord(sentence[i])>ord(sentence[i-1]):
            res+=temp[i].upper()
        elif ord(sentence[i])<ord(sentence[i-1]):
            res+=temp[i].lower()
        elif ord(sentence[i])==ord(sentence[i-1]):
            res+=sentence[i]
    return res
if __name__ == '__main__':
    sentence = input()
    result = transformSentence(sentence)
    print(result)
