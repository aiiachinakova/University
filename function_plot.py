#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
# Импорт библиотеки math
import numpy
# Импорт библиотеки numpy
import matplotlib.pyplot as mpp
# Импорт библиотеки matplotlib

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]
    # Возможно, задаёт аргумент
    mpp.plot(
        arguments,
        [0.3*math.cos(a) + 0.3*math.sin(a/20.0) for a in arguments]
    )
    # Считает значения функции
    mpp.show()
    # Выводит график
    


# In[ ]:




