#!/usr/bin/env python
# coding: utf-8

# In[4]:


#there are 3 types of arrays
#List
#Truples
#Dictionaries


#List
#Saving values starting with index 0

l=[1,4,5,6,2,9]
print(l)
print(l[3])
print(l[2:])
print(l[:5])
print(l[1:3])


# In[5]:


#We can enter any Kind of Data type as we like to list
A= ['Sasa',21,'S',13,64,'Weera']
print('The Value of the list is : ',A)


# In[9]:


#Updating
A= ['Sasa',21,'S',13,64,'Weera']
print('Without Changing',A)
#For Update any Kind of data in list
A[4]=23
print('After Changing ',A)

#Deleting
del A[1]
print('After Deleting ',A)

#get the length of the list
print(len(A))


# In[15]:


#Sum,Max,Min
B=[1,4,7,3,9,4,0]
print(sum(B))
print(max(B))
print(min(B))

C=['Animal','Dog','Cat','bird','zoo','Life']
print(max(C))
print(min(C))


# In[16]:


#Save data until 5 begining from 0 - [0-4]
D=list(range(5))
print(D)


# In[18]:


#list methods

l=['x','y','z','m','z','m','z'] 
l.append('n')#add obj to the list
print(l)

print(l.count('z'))#get the count of the obj


# In[9]:


#Connecting twi lis to a One list(Extend list)
l1 = ['Sasa','Weera','ICT','Python']
l2 = list(range(7))
l1.extend(l2)
print('New list : ',l1)

#Geting the index of list obj
print('Index :',l1.index(0))
print('Index :',l1.index('ICT'))

#Removing the obj in the list(but as java stack
l1.pop()
print('List : ',l1)
l1.pop(1)
print('List : ',l1)

#Using remove() methos for remove obj
l1.remove('ICT')
print('List : ', l1)

#Reverse list
l1.reverse()
print('List : ',l1)


# In[11]:


#Sorting list
l= [1,5,8,3,4,0,5,8]
l.sort()
print('List : ',l)

#reverse sorting list
l.sort(reverse = True)
print('List : ',l)






