#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Dictionary 
#In dictionaries we can add name to remember the data without using defult index

D= {'A':1,'B':2,'C':6,'D':'x','S':'Weera'}
print(D)
print(D['S'])


# In[9]:


#Change VALUE IN Dictionary
D= {'A':1,'B':2,'C':6,'D':'x','S':'Weera'}
D['D'] = 'Sasa'
print(D)

#Adding Value to Dictionary (Extend Dictionary)
D['sum'] = D['A'] + D['B'] + D['C']
print(D)

#deleting value using key name
del D['B']
print(D)

#Clear all values in Dictionary
D.clear()
print(D)

#to delete the dictionary
del D


# In[20]:


#Get the length in Dictionary
D= {'A':1,'B':2,'C':6,'D':'x','S':'Weera'}
print(len(D))

#get A Copy of dictionary
D2 = D.copy()
print(D2)

#get the Key Value Only
D3 = D.fromkeys(D)
print(D3)

#Convert tuples and a list values to Dictionary Tuplea as keys and list as Value
t=('hello','a',25,'Er')
l=['Sasa','weera',678,98.09]

D4 = dict(zip(t,l))
print(D4)

#Only Print items
print(D2.items())

#Only print Values
print(D2.values())

#Only print keys
print(D2.keys())

#Enter Dictionary Values to Variables
D5 = {'A':34, 'B': 'Why'}
a,b = D5.items()
print(a)
print(b)

#Connect two Dictionaries together(Extend D4 dictionary by adding D5 dictionary)
D4.update(D5)
print(D4)


# In[ ]:




