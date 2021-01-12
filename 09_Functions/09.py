#!/usr/bin/env python
# coding: utf-8

# In[1]:


#functions
#functions can used for save time and minimize lines of program
def sum(a,b,c):
    print("Value : ",(a+b+c))


# In[2]:


sum(a=10,b=40,c=49)


# In[3]:


sum(a='Sasa',b='nka',c='Weera')


# In[4]:


def SumD(a='',b=32,c=0):
    print('A', a)
    print('B',b)
    print('C',c)


# In[5]:


SumD(10,30)


# In[6]:


SumD('Xyz')


# In[9]:


#Used for store unlimuted values using *
def printNum(N,*v):
    print('Number of values:' , N)
    print('Value : ', v)


# In[10]:


printNum(5,1,2,3,4,5)


# In[11]:


#Return type functions
def Add(a,b):
    t = a+b
    return t


# In[13]:


v = Add(10,56)
print('Value : ',v)


# In[14]:


def Cal(a,b):
    add= a+b
    sub = a-b
    mul= a*b
    Div = a/b
    rem = a%b
    
    return add,sub,mul,Div,rem


# In[15]:


v = Cal(10,20)
print(v)


# In[16]:


a,s,m,d,v = Cal(12,4)
print(a)
print(s)
print(m)
print(d)
print(v)


# In[22]:


fun = lambda a,b:a+b
v= fun(20,30)
print(v)


# In[ ]:




