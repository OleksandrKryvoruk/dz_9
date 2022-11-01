#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
1. Напишіть клас автомобіля з атрибутами: марка, колір, об'єм двигуна.
та методами:іхати вперед, їхати назад. 
Написати ще один клас автомобіля, який є успадкованим від першого. Додайте в
нього методи повороту праворуч і ліворуч.
"""
class Car:

    def __init__(self, brend, color, engine):
        self.brend = brend
        self.color = color
        self.engine = engine

    def drive_ahead(self):
        return (f"This car {self.brend} - {self.color} - {self.engine} drive ahead")

    def drive_behind(self):
        print(f"This car {self.brend} - {self.color} - {self.engine} drive behind")


class DrivingSides(Car):
    
    def turn_left(self):
        print(f"This car {self.brend} - {self.color} - {self.engine} turn left")

    def turn_right(self):
        print(f"This car {self.brend} - {self.color} - {self.engine} turn right")
        

benz = DrivingSides("Mercedes", "Black", 3500)

print(benz.drive_ahead())
print(benz.turn_left())

