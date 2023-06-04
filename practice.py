import pandas as pd
import numpy as np


# Loops are a set of instructions which repeat until termination conditions are met.
# fruits=["Apple","Mango","CustodApple","Banana"]
# for fruit in range(len(fruits)):
#     print(fruits[fruit])

# for i in range(10 * 2):
#     print(i)

# def add(a, b):
#     return a + b
#
#
# print(add(("shiva", "Shankar"), (5, 4)))

# Multithreading
# import time
# import threading
# def list_count(count, sign=1, list1=None):
#     if list1 is None:
#         list1 = list()
#     for i in range(count):
#         list1.append(sign*i)
#         sum(list1)
#     return  list1
#
# size = 1000
# list1=list()
# t1=threading.Thread(target=list_count,args=(size, 1, list1,))
# starttime = time.time()
# t1.start()
# t1.join()
# print(starttime - time.time())
# print(list1[0:20])

# import itertools
# import time
# starttime=time.time()
# list1=[2,2,3,4,5,5,6,7,9]
# kl=[k for k,s in itertools.groupby(list1)]
# print(kl)
# endtime=time.time()
# print("Total time taken:%f" %(endtime-starttime))
from pandas import concat
str1="Shiva"
str2="shankar"
newstr="".join((str1,"Yes"))
print(newstr)



