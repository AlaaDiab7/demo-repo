# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 00:08:28 2025

@author: Alaa Diab
"""

import os
import shutil
import subprocess
import datetime

# Get the current date and time
now = datetime.datetime.now()
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')


print("This is just the beginning ...")
a = 5
b = 3

c = a*b

print("c=", c)
print("This is working well.") # Here is a check for the update
# it looks like it is not running by the schedular
#
# on a second thought, it worked once!
# Let us see if it works after that again, in five minutes :) 

# Actually, i did it manually now, let us see if it runs automatically...
print(datetime.date.today())
# will this come?
if a > b:
    print("it is dinner time!")
else: 
    print("let us work further!")
    
myString = "Today, there is not time to waste."