#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def evenNumber(list):
    for number in list:
        print(type(number))
        #if type(number)=='int':
        if number % 2 != 0:
            list.remove(number)
    return list

def myFilter(function,list):
    return function(list)

l = [1,3,6,4,7,8]
myFilter(evenNumber,l)
        


# In[ ]:


def addNumbers(list):
    for number in list:
        print(type(number))
        #if type(number)=='int':
        number = number + number
    return number

def myReduce(function,list):
    return function(list)

l = [1,3,6,4,7,8]
myReduce(addNumbers,l)


# In[ ]:


l = ['a','c','a','d','g','i','l','d']
[x.upper() for x in l]


# In[63]:


my_list=[['X'],['Y'],['Z']]
my_l=[[k*i for j in my_list for k in j for i in range(1,5)]]
my_l[0]


# In[49]:


my_list=['X','Y','Z']
my_l = []
my_l.append([[j*k for j in my_list] for k in range(1,5)])
#print(my_l)

merged_l = []
for g in my_l[0]:
    #print(g)
    for h in g:
        merged_l.append(h)
print(merged_l)
        


# In[ ]:


def longestWord(l):
    longestword = ''
    longetwordlenght = 0
    for word in l:
        if longetwordlenght < len(word):
            longetwordlenght = len(word)
            longestword = word
    return word

l = ['Ashish','Ashish Kumar','Ashish Kumar yadav']
print(longestWord(l))
            
        
        
    


# In[3]:


[[i+j+h for i in range(1,2)]for j in range (1,4) for h in range (0,3)]


# In[4]:


[[val+j for val in range(1,5)] for j in range (1,5)]


# In[12]:


[(y,x) for x in range(1,4) for y in range(1,4)]


# In[ ]:


class UserInput:
    
    a = 0.0
    b = 0.0
    c = 0.0
    
    def __init__(self):
        self.a = float(input("Please provide first side of trangle"))
        self.b = float(input("Please provide second side of trangle"))
        self.c = float(input("Please provide third side of trangle"))
        print(self.a)

class TriangleArea(UserInput) :
    
    def __init__(self):
        UserInput.__init__(self)
        
    def calculateArea(self):
        s = (self.a+self.a+self.a)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        #print('The area of the triangle is %0.2f' % area)
        print("The area of the triangle is {}".format(area))
    
area = TriangleArea() 
area.calculateArea()


# In[ ]:


def filter_long_words(listofword,wordlength):
    return list(filter(lambda x : wordlength < len(x),listofword))
    
l = ['Ashish','Ashish Kumar','Ashish Kumar yadav']  
filter_long_words(l,12)  
    
    


# In[ ]:


def wordLengthMap(listofwords):
    wordlength=[]
    for word in listofwords:
        wordlength.append(len(word))
    return wordlength

l = ['Ashish','Ashish Kumar','Ashish Kumar yadav'] 
wordLengthMap(l)


# In[ ]:


def vowelCheck(word):
    if word in 'AEIOU':
        print(word)
        return True
    else:
        return False
    
vowelCheck('B')


# In[ ]:


data = [['Wolfe Lane Community Garden', 'X', 'XXX', 'XX', 
         'XXXXX', 'XX', 'XXX', '0.05', 'XXXX']]

indices = [0, 7]

[[x for i, x in enumerate(sublist) if i in indices] for sublist in data]

