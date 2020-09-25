# -*- coding: utf-8 -*-
"""
@File  :Serialization.py
@Author:Sapphire
@Date  :2020/9/25 15:09
@Desc  :python序列化：
我们把变量从内存中变成可存储或传输的过程称之为序列化，把变量内容从序列化的对象重新读到内存里称之为反序列化
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
序列化类的实例：
无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
可通过default参数传入实例的序列化方式，例如 default=lambda obj: obj.__dict__
"""
import json
import pickle


class Student(object):
    def __init__(self, name, age, hobbit):
        self.name = name
        self.age = age
        self.hobbit = hobbit

    def introduction(self):
        print("My name is {} , i`m  {} years old , i like {}".format(self.name, self.age, self.hobbit))


student = Student("sapphire", 12, "吃饭睡觉打游戏")

print(dir(student))
print(repr(student))
print(student.__dict__)
print(json.dumps(student.__dict__))
print(json.dumps(student, default=lambda obj: obj.__dict__))
print(pickle.dumps(student.__dict__))
