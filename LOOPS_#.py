#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=0
b=10
while a<b:
    print("hello")
    a=a+1


# In[3]:


for _ in range(20):
    print("hi")


# 

# In[5]:


list(range(20))


# In[8]:


list(range(0,5))


# In[13]:


list(range(5,50,5))


# In[5]:


k=[11,14,16,15,19]
for i in k:
    print("hi")


# In[7]:


for m in [6,10,11,15]:
    print(m)
    print(m+2)


# In[10]:


a=0
for i in range(4):
    a=a+i
    print(a)


# In[20]:


a=1
for i in range(1,6):
    a=a*i
print(a)


# In[1]:


a=1
print(a)


# In[2]:


a=0
b=1
while a<b:
    print("hello")
    a=a+1
    


# In[5]:


for i in range(10):
    print("hi")


# In[4]:


for m in [6,10,11,15]:
    print(m)
    print(m+2)
    
    


# In[8]:


a=0
for i in range(50,1100,10):
    a=a+1
    print(a)


# In[14]:


a=1
b=5
while a<b:
    print(a)
    a=a+1


# In[17]:


for i in(6,10,11,15):
    print(i)
    print(i+2)
    


# In[20]:


a=0
for i in range(50,1101,10):
    a=a+1
    print(a)


# In[23]:


a=1
for i in range(1,7):
    a=a*i
    print(a)


# In[25]:


k=[11,19,16,15,19]
for i in k:
    print("hi")


# In[32]:


for i in list(range(9,9,8)):
    print(i)
    


# In[33]:


print("hello world")
a=10
b=10
print(id(a))
print(id(b))


# In[34]:


print("hello world")
a="hello"
b=10
print(id(a))
print(id(b))


# In[39]:


a=10
b=20
c=30
print((a<b)or(a<c))
print((a<b)and(a>c))
print(not(a>b))


# In[ ]:


a=0
b=1
while a>b:
    a=a+1
    print(a)


# In[ ]:


i=int(input("enter the value"))
flag=True
for t in range(2,i):
    if i% t==0:
        flag=False
if flag:
    print(str(i)+"is a prime number.")
else:
    print(str(i)+"is not a prime number.")
                


# In[ ]:


num=int(input("enter a number"))
ip=False
i=2
while i<num:
    if num%i==0:
        ip=True
        break
        i=i+1
if ip:
    print("{} is not a prime number".format(num))
else:
    print("{} is a prime number".format(num))
        


# ###### 

# In[3]:


"{1},{0},{2}".format(1,2,3)


# In[5]:


for i in range(3,33,3):
    print("{}*{}={}".format(3,int(i/3),i))


# In[6]:


for i in range(10):
    for j in range(110):
        print(i,j)


# In[7]:


for z in range(5):
    for k in range(3):
        for s in range(4):
            for p in range(3):
                print(z,k,s,p)


# In[7]:


st=int(input())
ed=int(input())
for tk in range(st,ed+1):
    if tk>1:
        flag=True
        for i in range(2,tk):
            if tk%i==0:
                flag=False
        if flag:
            print("{}. is prime".format(tk))


# ###### 

# In[ ]:





# In[ ]:




