#!/usr/bin/env python
# coding: utf-8

# In[60]:


"""
3. Напишіть клас Рагаїеіо5гат, який приймає два аргументи міаї і епріП і метод
бе! агеа, який вираховує площу паралелограму. Успадкуйте від нього клас
5амаге, перевизначіть в ньому метод 5еї агеа таким чином, щоб він вираховував
площу квадрату.
"""

class Parallelogram:
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def get_area(self):
        s = self.width * self.length
        return f"Parallelogram square = {s}"
        

class Square(Parallelogram):
    
    def get_area(width):
        s = width * width
        return f"Square = {s}"
             
 
paral_one = Parallelogram(10, 7)

print(paral_one.get_area())

square_one = Square.get_area(10)
print(square_one)

