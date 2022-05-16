# class Student(object):
#     # 初始化中给对象属性赋值
#     def __init__(self):
#         self.name = None
#         self.age = None
#
# class stu1(Student):
#     def setName(self):
#         self.name = input("请输入姓名：")
#         self.age = input("请输入年龄：")
#     def __str__(self):
#         return (self.name + ' ' + self.age)
#
# stu = stu1();
# stu.setName()
# print(stu)
#
# print("\n--------欢迎来到图书馆借阅管理系统-------")
# print("---         1.用户信息维护页          ---")
# print("---         2.图书管理页             ---")
# print("--------------------------------------\n")

import os
path = os.getcwd()
fileName = "1" + ".json"
dir = os.path.join(path,fileName)
print(dir)