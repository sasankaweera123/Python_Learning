#!/usr/bin/env python
# coding: utf-8

# In[1]:


#String Addition

n1 = 'Sasa'
n2 = 'Weera'

print('Value = ',n1+n2)


# In[4]:


#Integer ,Double , float Calculation
n1=20
n2=13

print('Add = ',n1+n2)
print('Sub = ',n1-n2)
print('Multi = ',n1*n2)
print('Div = ' , n1/n2)
print('Remi = ' , n1%n2)

n3= 30.5
n4= 74.897

print('Add = ',n3+n4)
print('Div = ',n1/n4)
print('Multi = ',n3*n2)
print('Expnt = ' , n3**n2) #this is use for get the power of value


# In[8]:


#User Input Calculation

n1= input('Enter Value = ')
n2= input('Enter Value = ')

#Addition Only give as String Addition Others are errors Because Input from user program get it as a String value
print('Add = ',n1+n2)
#print('Sub = ',n1-n2)
#print('Multi = ',n1*n2)
#print('Div = ' , n1/n2)
#print('Remi = ' , n1%n2)

#To get the User Inputs as according to the type We can use eval() Function
#After using eval() Function We can do Our Calculations

n3= eval(input('Enter Your Value = '))
n4= eval(input('Enter Your Value = '))
print('Add = ',n3+n4)
print('Div = ',n3/n4)
print('Multi = ',n3*n4)
print('Expnt = ' , n3**n4)


# In[ ]:




