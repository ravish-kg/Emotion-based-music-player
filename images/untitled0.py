# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 23:45:27 2016

@author: ravi
"""

import os
import copy

i = 0
 
for file in os.listdir("F:/dm/FACIAL_EXPRESSION/yalefaces"):
    file = copy.copy(file[:7]+str(i)+file[9:]) 
    print file
    path = os.path.join("F:/dm/FACIAL_EXPRESSION/images/",file+".png")
    i+=1
    print path
     
     