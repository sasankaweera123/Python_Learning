#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Tuples

#The main difference between the tuples and the lists is that the tuples cannot be changed unlike lists.

t = ('Sasa', 'Weera', 'S',1, 5 , 9)
print(t)
print(t[4])
print(t[:3])
print(t[1:])
print(t[1:4])


# In[3]:


#In tuples we cant update it.
t = ('Sasa', 'Weera', 'S',1, 5 , 9)
#So we cant use these,
#t.append()
#t[3]=20


# In[4]:


#But we we need to update tuples we can convert it into list and then update it.
t = ('Sasa', 'Weera', 'S',1, 5 , 9)
l=list(t)
l.append('X')
l[3]='python'
print(l)


# In[6]:


#We can Add tuples , So we can extend tuples Using this method
t1 = ('Sasa', 'Weera', 'S',1, 5 , 9)
t2 = (1,5,7,3,5,9)

t3 = t1+t2
print('New Tuples : ',t3)


# In[10]:


#As Same as list We can Still get the length and Max and Min obj

t = (1,5,7,3,4,9,0,4,8,3,7,2,9)
print('Length : ',len(t))
print('Max and Min : ')
print('Max : ',max(t),' Min : ',min(t))
print(t)


# In[ ]:




