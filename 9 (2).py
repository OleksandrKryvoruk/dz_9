#!/usr/bin/env python
# coding: utf-8

# In[51]:


"""
2. Напишіть клас ТехеРгосез5ог для обробки текстових даних, Клас повинен мати
публічний метод 8еї сіеап, 5їгіп8, який видалить усі знаки пунктуації з рядка, який
передається йому аргументом, та приватним методом із рипКіїапіїап, який
безпосередньо перевіряє символ на рівність зі знаками пунктуації та повертає
тгце/Каїзе, який, у свою чергу, є приватним або захищеним атрибутом.
Потім напишіть клас Техії оадег, який має приватний атрибут гехі ргосез5ог, який
є об'єктом класу ТехіРгосез5о0г. Клас Техії оадег повинен мати приватний атрибут
деап 5ігіпе і публічний метод 5еї. сіеап Кехі, який буде викликати метод класу
техіРгосез5ог, через свій атрибут кехі, ргосез5ог і записує значення в сіеап, 5їгіпб.
створіть додатковий ргорегіу для сіеап, 5ігіп5, який буде виводити повідомлення
в консоль про те, що виводиться вже очищений текст, Напишіть клас
Datalnterface, B akomy буде захищений атрибут, що є екземпляром класу
TextLoader, a Taxox публічний метод ргосез55 їехіз, який буде приймати список
рядків, опрацьовує їх у циклі і виводить значення в консоль.
"""
import re

class TextProcessor:
    
    def __init__(self, str1):
        self.str1 = str1
        
    def get_clean_string(self):
        s = re.sub(r'[.,!?\'\"]', '', self.str1)
        print("get_clean_string called")
        return s

    def _is_punktiantian(self):
        
        if "." in self.str1:
            print("_is_punktiantian called")
            return True
        if "," in self.str1:
            print("_is_punktiantian called")
            return True
        if ":" in self.str1:
            print("_is_punktiantian called")
            return True
        else:
            return False

class TextLoader(TextProcessor):
    
    def __init__(self, str1):
        self.str1 = str1
    
    @property
    def set_clean_text(self):
        __text_pocessor = TextProcessor(self.str1)
        __clean_string = __text_pocessor.get_clean_string()
        print("set_clean_text called")
        print("This is clean text:")
        return __clean_string
        
class DataTnterface(TextLoader):
        
    __srin2 = TextLoader("Напишіть клас Datalnterface, B akomy буде захищений атрибут, що є екземпляром класу TextLoader.")
   
    def process_text(lst):
        print("process_text called")
        for i in lst:
            print(i)
 
strings = TextProcessor("Taxox публічний метод ргосез55 їехіз, який буде приймати список рядків, опрацьовує їх у циклі і виводить значення в консоль.")

print(strings._is_punktiantian())
print(strings.get_clean_string())

srin = TextLoader("Напишіть клас ТехеРгосез5ог для обробки текстових даних, Клас повинен мати публічний метод 8еї сіеап, 5їгіп8,")

print(srin.set_clean_text)

srin2 = DataTnterface.process_text("Складне завдання")

