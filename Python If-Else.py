#!/bin/python3

import math
import os
import random
import re
import sys



n=int(input())
if n%2==0 and n<=5 and n>=2:
    print("Not Weird")
elif n%2!=0:
    print("Weird")
if n%2==0 and n>=6 and n<=20:
    print("Weird")
if n%2==0 and n>20:
    print("Not Weird")            
