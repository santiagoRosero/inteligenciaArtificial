#!/usr/bin/env python
# coding: utf-8

# 
# # Python exercises, practice

# Student: Santiago Alejandro Rosero Cordoba.

# ## 1 exercise

# print hello world

# In[2]:


print("hello world")


# ## 2 exercise
# Let's create a variable with the name variable and assign it the value "hello world".
# 
# ## 3 exercise
# Print the type of variable
# 

# In[3]:


variable="hello world"
type(variable)


# ## 4 exercise
#  Let's remove the word " world" from variable

# In[7]:


variable="hello world"
print(variable[0:5])


# ## 2 exercise
# 
# Let's make a function which receives a list of number from 1 to 20 and prints only the number that are odd.

# In[301]:


def onlyOdd():
    list1=[]
    for i in range(20):
        if i%2!=0:       
            list1.append(i)
    return list1

print(onlyOdd())


# ## 3 exercise
# 
# Let's make a method in a Python file which receives two parameters:
# 
# A list of integers
# 
# An exponent number
# 
# $b^{n} = b \times \dots \times b$
# 
# The method allows us to calculate the exponentiation of each number in the list.
# 
# We must import the file and use it to call the method

# In[266]:


def exponents(lista, expo):
    list1=lista
    for i in range(len(lista)):
        for j in range(expo-1):
            list1[i]=list1[i]*list1[i]   #para exponentes>0
    return list1
lista=[2,4,6,22,7,8,4]
print(exponents(lista, 2))
        


# ## 4 exercise
# 
# The idea is to do a dictionary diccionario with the next keys and values:
# 
# variableUno: [1,2,3,4]
# 
# variableDos: ["1","a","?"]

# In[145]:


lista1=[1,2,3,4]
lista2=["1","a","?"]
diccionario = {"variableUno":lista1, "variableDos":lista2}
print(diccionario['variableUno'])


# ## 5 exercise
# 
# Change the first letter of "Spam" to "z"

# In[147]:


palabra="Spam"
print(palabra.replace("S", "Z"))


# ## 6 exercise
# 
# let's do a program which receives some parameters in order to calculate the perimeter of a rectangle.
# 
# $p = 2x + 2y$

# In[148]:


def perimetro(x,y):
    per=(2*x)+(2*y)
    return per
largo=5
ancho=3
print(perimetro(largo, ancho))


# ## 7 exercise
# 
# Create a class that saves the name of a person, his height in meters and weights in kilograms.
# This class must have a operation which calculate the Body mass index (BMI).
# Define a list of 5 persons and print their BMI.

# In[237]:


class person(object):
    def __init__(self,nombre,altura,peso):
        self.nombre=nombre
        self.altura=altura
        self.peso=peso
        
    def getNombre(self):
        return self.nombre
    
    def getAltura(self):
        return self.altura
    
    def getPeso(self):
        return self.peso
    
    def calculaBmi(person):
        masa=person.getPeso()/person.getAltura()
        return masa
       

    person1=person("Pedro", 1.70, 68)
    person2=person("María", 1.75, 71)
    person3=person("Fernando", 1.69, 66)
    person4=person("Cristina", 1.57, 69)
    person5=person("Sofia", 1.68, 65)

    for i in range(5):
        print(calculaBmi(lista[i]))
   


# ## 8 exercise
# 
# make a program that prints the numbers from 1 to 100 If the number is divisible by 2 then print "whiz" if the number is divisible by 3 then print "bang"

# In[216]:


for i in range(100):
    if i%2==0:
        print("whiz")

    elif i%3==0:
            print("bang")
    else:
        print(i)
   
    

