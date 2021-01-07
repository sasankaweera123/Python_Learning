#!/usr/bin/env python
# coding: utf-8

# In[3]:


a= 20;
b = eval(input('Enter Value : '))

#if else methods are used for get selection

if(b>a):
    print('Max value : ' , b)
else:
    print('Max value : ', a)
print('Weldone')


# In[4]:


a=eval(input('Enter First Value : '))
b=eval(input('Enter First Value : '))
c=eval(input('Enter First Value : '))

if(a>b):
    if(a>c):
        print('Max Value : ',a)
    else:
        print('Max Value : ',c)
else:
    if(b>c):
        print('Max Value : ',b)
    else:
        print('Max Value : ',c)
print('Sum : ',(a+b+c))


# In[5]:


#Loops Can use for do Continus work

#For loop are used when you know the range of loop

for i in range(0,10,1):
    print('Value : ',i)
print('End of Loop!')


# In[8]:


#while loop used until the statement in loop false
i=0
N = eval(input('Enter Value: '))
while(N>=i):
    print('Value : ',i)
    i=i+1
print('Loop End !')


# In[11]:


l =[10.23,45.6,67.5,34.5,0.78]
for i in range(len(l)):
    print('Value of i : ',i)
    print('Value of list : ',l[i])
    
print('End!')


# In[13]:


l=[1,3,4,2,5,6,1,7,8,2]

for i in l:
    if(i>5):
        print('Loop Need to End!')
        break
    else:
        print('Please Continue Value : ',i)
print('End!')
    


# In[17]:


l = list(range(10))

for i in range(0,5):
    for j in range(0,3):
        print(i,j)
        print('*')
    l.append(i)
print(l)


# In[23]:


i=1
for word in 'Sasanka':
    if word == 'n':
        print('Found : ',word , 'After ',i,'attempts')
    elif(word == 'k'):
        print('try again , Attemmpt :',i)
        break
    else:
        print('Not yet')
        i = i+1
print('Weldone')


# In[26]:


for i in range(0,10,2):
    if i ==4:
        continue
        print ('This letter need to continue',i)
    print('letter',i)
    
print('Weldone')
    


# In[27]:


for i in range(10):
    if i ==3:
        pass
        print('Value must pass',i)
    print('Value : ',i)
print('End!')


# In[ ]:




