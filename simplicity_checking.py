#!/usr/bin/env python
# coding: utf-8

# In[19]:


print ( 'Input one number' )
print()
a = int (input () )

def isNumberPrime(n):
    if n % 2 == 0: #если число делится на 2, то будет простым, только если равно 2
        return n == 2 
    else: #проверяю нечётные делители до корня из числа
        div = 3
        while div * div <= n and n % div != 0:
            div += 2
        return div * div > n

b = isNumberPrime(a)
print()
print(a, 'Is prime number:',b)


# In[ ]:





# In[ ]:




