import string
import maskpass
import json
import os

class Person:

    # 类属性
    Name = ["张三", "李四","1"]  # 存储姓名的列表
    Password = ["L2015105000", "W2015105001","111qqq"]  # 存储学号的列表
    Sensitive_Words = ["傻", "蠢", "笨", "呆", "愚"]  # 敏感词库
    Number_Bank = list(string.digits)  # 数字库
    Letter_Bank = list(string.ascii_letters)  # 字母库（含大写小写）
    Book_Name = ["水浒传","西游记","离散数学","概率论"]       # 书的名字
    Book_Number = [2,3,2,4]     # 书的剩余量

    def __init__(self):
        self.name = None
        self.password = None

class User(Person):

    def __init__(self):
        # 用户已借阅书籍
        self.book_name = []

    def menu1(self):
        print("\n---欢迎来到图书馆借阅管理系统---")
        print("---          1.注册          ---")
        print("---          2.登录          ---")
        print("---          3.退出          ---")
        print("--------------------------------\n")
        self.a = eval(input("请输入你的选择："))
        if self.a == 1:
            self.register()
        elif self.a == 2:
            self.login()
        elif self.a == 3:
            exit(1)
        else:
            print("输入有误,请重新输入")
            self.menu1()

    # 注册
    def register(self):
        print("开始注册")

        self.name = input("请输入你的姓名：")
        self.flag = 0  # 记录要注册的用户名是否已存在或存在敏感词

        # 判断Name列表中是否存在要注册的用户名
        for i in Person.Name:
            if i == self.name:
                print("该用户名已存在")
                print("请重新输入")
                self.flag += 1
                break

        # 判断要注册的用户名是否存在敏感词
        for i in Person.Sensitive_Words:
            if self.name == ("大" + i + "子"):
                print('"' + "大*子" + '"' + "用户名不可注册，请重新输入")
                self.flag += 1

        # 要注册的用户名已存在或存在敏感词，重新注册
        if self.flag == 1:
            self.register()
        else:
            # 用户名可用，开始设置密码
            while 1:
                self.password = maskpass.askpass(prompt='请设置你的密码（最少6位且字母数字混合）：')
                # self.password = input('请设置你的密码（最少6位且字母数字混合）：')

                self.flag_in_Number_Bank = 0
                self.flag_in_Letter_Bank = 0

                # 记录密码中字母和数字的个数  self.flag_in_Letter_Bank(字母)  self.flag_in_Number_Bank(数字)
                for i in self.password:
                    for j in Person.Number_Bank:
                        if i == j:
                            self.flag_in_Number_Bank += 1
                    for k in Person.Letter_Bank:
                        if i == k:
                            self.flag_in_Letter_Bank += 1

                # 控制密码不少于6位
                if len(self.password) < 6:
                    print("密码不可少于6位，请重新输入")
                    continue

                # 控制密码应至少为字母+数字的组合
                elif self.flag_in_Number_Bank == 0:
                    print("密码不可为纯字母，请重新输入")
                    continue
                elif self.flag_in_Letter_Bank == 0:
                    print("密码不可为纯数字，请重新输入")
                    continue

                # 密码符合要求，则将用户名和密码分别保存到Name库和Password库
                else:
                    Person.Name.append(self.name)
                    Person.Password.append(self.password)

                    # 将密码保存到data.json文件中
                    # data = {
                    #     "name":Person.Name,
                    #     "password":Person.Password
                    # }

                    # with open("D:\\Python\\pythonProject\\venv\\面向对象程序设计\\data.json","w") as f:
                    #     json.dump(data,f)

                    # with open("D:\\Python\\pythonProject\\venv\\面向对象程序设计\\data.json", "r") as f:
                    #     result = json.load(f)
                    #     print(result)
                    #     print(result["name"][1])

                    print("注册成功！\n")
                    print("Name:", Person.Name)
                    print("Password:", Person.Password)
                    break
            self.menu1()

    # 登录
    def login(self):

        self.flag_Name_flase = 0  # 记录输入用户名错误的次数
        self.flag_password_flase = 0  # 记录输入密码错误的次数

        print("开始登录")

        while self.flag_Name_flase < 3:
            self.name = input("请输入你的姓名：")

            self.flag = 0  # 记录列表中是否有输入的姓名（1有，0没有）
            self.index = 0  # 记录当前姓名的索引

            # 遍历Name列表，查看是否有输入的姓名
            for i in Person.Name:
                if i == self.name:
                    self.flag += 1
                    self.index = Person.Name.index(i)

            # Name列表中有输入的姓名
            if self.flag == 1:
                while self.flag_password_flase < 3:
                    # self.password = maskpass.askpass(prompt='请输入你的密码：')
                    self.password = input('请输入你的密码：')

                    if self.password == Person.Password[self.index]:
                        print("登录成功！")
                        # 跳转到图书借阅页
                        self.menu1_book()
                    else:
                        self.flag_password_flase += 1
                        if self.flag_password_flase == 3:
                            print("密码错误三次，禁止登录本系统！")
                            exit(1)
                        print("密码错误，请重新输入")

            # 列表中无输入的姓名
            else:
                self.flag_Name_flase += 1
                if self.flag_Name_flase == 3:
                    print("\n用户名错误三次，禁止登录本系统！")
                    print("是否需要回到欢迎界面？（1：回到欢迎界面  2：退出）")

                    # 判断输入是否有误
                    while 1:
                        self.change = eval(input("请输入你的选择："))
                        if self.change == 1 or self.change == 2:
                            break
                        else:
                            print("输入有误，请重新输入")
                            continue

                    if self.change == 1:
                        self.flag_Name_flase = 0  # 重置该值为0，防止下次无法进入输入名字的循环
                        self.menu1()
                    elif self.change == 2:
                        print("退出成功！")
                        exit(1)

                print("该用户不存在，请重新输入")
                continue

    # user图书借阅页
    def menu1_book(self):
        print("\n--------欢迎来到图书借阅页-------")
        print("---        1.借阅书籍        ---")
        print("---        2.归还书籍        ---")
        print("---        3.查看已借阅      ---")
        print("---        4.退出登录        ---")
        print("-------------------------------\n")
        self.a = eval(input("请输入你的选择："))
        if self.a == 1:
            self.borrow_book()
        elif self.a == 2:
            self.repaid_book()
        elif self.a == 3:
            self.show_myBook()
        elif self.a == 4:
            exit(1)
        else:
            print("输入有误,请重新输入")
            self.menu1_book()

    # 借阅书籍
    def borrow_book(self):

        # 从文件中读取已借阅书籍
        self.book_name = self.read_my_book()

        # 标识Book_Nama中是否存在要借阅的书籍
        self.flag = 0

        # 标识要借阅书的索引
        self.index = 0

        # 标识是否已借阅过本书
        self.flag2 = 0

        self.borrow_book_name = input("请输入要借阅的书名：")

        # 在借阅前查看是否已借阅过本书
        for m in self.book_name:
            if m == self.borrow_book_name:
                self.flag2 += 1
                break

        if self.flag2 == 1:
            print(f"你已经借阅过'{self.borrow_book_name}'了，不可再借阅本书，请重新输入！")
            self.borrow_book()
        else:
            # 没有借阅过本书，开始借阅
            for i in Person.Book_Name:
                if i == self.borrow_book_name:
                    # 有要借阅的书籍
                    self.flag += 1
                    # 获取要借阅书的索引
                    self.index = Person.Book_Name.index(i)
                    break

            if self.flag == 1:
                # 有要借阅的书籍
                # 向book_name中添加已借阅书籍的名字
                print("借阅成功！")
                self.book_name.append(self.borrow_book_name)

                # 从Book_Number中减少一本
                Person.Book_Number[self.index] -= 1

                # print("已借阅书：",self.book_name)
                # print("剩余量：",Person.Book_Number[self.index])

                self.save_my_book()
                self.menu1_book()
            else:
                # 没有要借阅的书籍
                print("没有要借阅的书籍")
                print(f"你可以借阅如下几本书:\n{Person.Book_Name}")
                self.borrow_book()

    # 归还书籍
    def repaid_book(self):

        # 从文件中读取已借阅书籍
        self.book_name = self.read_my_book()

        # 标识是否已借阅要归还的书籍
        self.flag = 0

        # 标识书籍库中是否有要归还的书
        self.flag2 = 0

        # 标识要归还书在书籍库中的索引
        self.index = 0

        # 归还书籍前查找是否已借阅书籍
        if len(self.book_name) == 0:
            print("没有借阅书籍，无法归还！")
            self.menu1_book()

        else:
            self.repaid_book_name = input("请输入要归还的书名：")

            for i in self.book_name:
                if i == self.repaid_book_name:
                    # 已借阅本书
                    self.flag += 1

                    # 查找书籍库中是否有要归还的书
                    for j in Person.Book_Name:
                        if i == j:
                            self.flag2 += 1
                            break

                    # 获取要归还书在书籍库中的索引
                    self.index = Person.Book_Name.index(i)
                    break

            if self.flag == 1:
                # 已借阅本书
                # 从已借阅书中删除要归还的书籍
                self.book_name.remove(self.repaid_book_name)
                if self.flag2 == 1:
                    # 书籍库中有要归还的书，则书的个数+1
                    Person.Book_Number[self.index] += 1
                    print(f"{self.repaid_book_name}归还成功!")
                else:
                    # 书籍库中没有要归还的书，则向书籍库中添加书名，并且书籍的个数+1
                    Person.Book_Name.append(self.repaid_book_name)
                    Person.Book_Number.append(1)
                    print(f"{self.repaid_book_name}归还成功!")
                self.save_my_book()
                self.menu1_book()

            else:
                # 没有借阅本书
                print("没有借阅本书，请重新输入！")
                self.repaid_book()

    # 查询已借阅
    def show_myBook(self):
        # print(self.book_name)
        print(self.read_my_book())
        self.menu1_book()


    # 保存借阅的书到当前登录用户名开头的json文件
    def save_my_book(self):
        self.my_book = {"my_book":self.book_name}

        # 获取json文件的绝对路径
        self.path = os.getcwd()
        self.fileName = self.name + ".json"
        self.dir = os.path.join(self.path,self.fileName)

        with open(self.dir,"w") as save:
            json.dump(self.my_book,save)

    # 从 .json文件 中读取已借阅书籍
    def read_my_book(self):

        # 获取json文件的绝对路径
        self.path = os.getcwd()
        self.fileName = self.name + ".json"
        self.dir = os.path.join(self.path, self.fileName)

        # 没有该json文件则创建
        if not(os.path.exists(self.fileName)):
            self.empty_content = {"my_book":[]}
            with open(self.fileName,"w") as found:
                json.dump(self.empty_content,found)

        with open(self.fileName, "r") as read:
            self.my_book = json.load(read)
            # print(self.my_book)
            return self.my_book["my_book"]


class Root(Person):

    def root_menu(self):
        print("\n--------欢迎来到图书馆借阅管理系统-------")
        print("---          1.用户信息维护页         ---")
        print("---          2.图书管理页             ---")
        print("-----------------------------------------\n")

        self.s = eval(input("请输入你的选择："))

        if self.s == 1:
            self.menu2()
        elif self.s == 2:
            self.menu2_2()
        else:
            print("输入有误，请重新输入！")
            self.root_menu()

    def menu2(self):
        print("|", "-".center(31, "-"), "|")
        print("|", " ---用户信息维护页---".center(24), "|")
        print("|", "1.添加用户信息".center(25), "|")
        print("|", "2.删除用户信息".center(25), "|")
        print("|", "3.修改用户信息".center(25), "|")
        print("|", "4.显示用户信息".center(25), "|")
        print("|", "5.退出系统".center(27), "|")
        print("|", "-".center(31, "-"), "|\n")

        self.b = eval(input("请输入你的选择："))

        if self.b == 1:
            self.add_Info()
        elif self.b == 2:
            self.del_Info()
        elif self.b == 3:
            self.change_Info()
        elif self.b == 4:
            self.show_Info()
        elif self.b == 5:
            exit(1)
        else:
            print("输入有误，请重新输入！")
            self.menu2()

    def menu2_2(self):
        print("|", "-".center(29, "-"), "|")
        print("|", "   ---图书管理页---".center(24), "|")
        print("|", "1.添加书籍".center(25), "|")
        print("|", "2.删除书籍".center(25), "|")
        print("|", "3.修改书籍".center(25), "|")
        print("|", "4.查询书籍".center(25), "|")
        print("|", "5.退出系统".center(25), "|")
        print("|", "-".center(29, "-"), "|\n")

        self.b = eval(input("请输入你的选择："))

        if self.b == 1:
            self.add_book()
        elif self.b == 2:
            self.del_book()
        elif self.b == 3:
            self.change_book()
        elif self.b == 4:
            self.show_book()
        elif self.b == 5:
            exit(1)
        else:
            print("输入有误，请重新输入！")
            self.menu2_2()


    # 添加用户信息
    def add_Info(self):
        print("开始添加用户信息")

        self.name = input("请输入用户名：")

        for i in Person.Name:
            if self.name == i:
                print("该用户名已存在，请重新输入！")
                self.add_Info()

        # 用户名可用，开始设置密码
        while 1:
            self.password = maskpass.askpass(prompt='请设置密码（最少6位且字母数字混合）：')
            # self.password = input('请设置密码（最少6位且字母数字混合）：')

            self.flag_in_Number_Bank = 0
            self.flag_in_Letter_Bank = 0

            # 记录密码中字母和数字的个数  flag_in_Letter_Bank(字母)  flag_in_Number_Bank(数字)
            for i in self.password:
                for j in Person.Number_Bank:
                    if i == j:
                        self.flag_in_Number_Bank += 1
                for k in Person.Letter_Bank:
                    if i == k:
                        self.flag_in_Letter_Bank += 1

            # 控制密码不少于6位
            if len(self.password) < 6:
                print("密码不可少于6位，请重新输入")
                continue

            # 控制密码应至少为字母+数字的组合
            elif self.flag_in_Number_Bank == 0:
                print("密码不可为纯字母，请重新输入")
                continue
            elif self.flag_in_Letter_Bank == 0:
                print("密码不可为纯数字，请重新输入")
                continue

            # 密码符合要求，则将用户名和密码分别保存到Name库和Password库
            else:
                Person.Name.append(self.name)
                Person.Password.append(self.password)
                print("添加成功！\n")
                # print("Name:", Person.Name)
                # print("Password:", Person.Password)
                break
        self.menu2()

    # 删除用户信息
    def del_Info(self):
        # 标识user.Name中是否存在要删除的用户（1：有 0：无）
        self.flag = 0

        # 记录要删除的用户名在user.Name中的索引
        self.index = 0

        # 记录删除成功的用户名
        self.removed_name = ""

        print("开始删除用户信息")

        self.name = input("请输入要删除用户的用户名：")

        # 查找用户名并删除其信息
        for i in Person.Name:
            if i == self.name:
                self.flag += 1
                self.index = Person.Name.index(i)
                self.removed_name = i
                Person.Name.remove(i)
                Person.Password.pop(self.index)
                break

        if self.flag == 0:
            print("该用户不存在，请重新输入！")
            self.del_Info()
        else:
            print(f'{self.removed_name}的信息已删除')
            # print("Name:", Person.Name)
            # print("Password:", Person.Password)
            self.menu2()

    # 修改用户信息
    def change_Info(self):
        # 修改后的用户名
        self.new_name = ""

        # 修改的用户名的索引
        self.index = 0

        # 标识列表中是否有要修改的用户名（1：有 0：没有）
        self.flag = 0

        # 判断学生信息表user.Name是否为空
        if len(Person.Name) == 0:
            print("学生信息表为空")
            self.menu2()
        else:
            print("开始修改用户信息")

            self.name = input("请输入要修改用户的用户名：")

            for i in Person.Name:
                if i == self.name:
                    self.flag += 1
                    self.index = Person.Name.index(i)

                    self.select = eval(input("请输入要修改的内容（1：用户名  2：密码  3：用户名和密码）："))

                    if self.select == 1:

                        # 修改用户名
                        while 1:
                            # 标识新的用户名是否可用
                            self.index1 = 0

                            self.new_name = input("请输入新的用户名：")

                            if self.new_name == Person.Name[self.index]:
                                print("新的用户名和旧的用户名不可以相同，请重新输入")
                                continue

                            for i in Person.Name:
                                if self.new_name == i:
                                    self.index1 += 1
                                    break

                            # 新的用户名可用
                            if self.index1 == 0:
                                # 修改用户名
                                Person.Name[self.index] = self.new_name
                                print("用户名修改成功！")
                                break
                            elif self.index1 == 1:
                                # 新用户名已存在
                                print("该用户名已存在，请重新输入！")
                                continue
                        self.menu2()

                    elif self.select == 2:

                        # -------------------判断密码是否符合要求-----------------------
                        while 1:
                            self.new_password = maskpass.askpass(prompt="请输入新的密码（最少6位且字母数字混合）：")
                            # self.new_password = input("请输入新的密码（最少6位且字母数字混合）：")

                            self.flag_in_Number_Bank = 0
                            self.flag_in_Letter_Bank = 0

                            # 记录密码中字母和数字的个数  flag_in_Letter_Bank(字母)  flag_in_Number_Bank(数字)
                            for i in self.new_password:
                                for j in Person.Number_Bank:
                                    if i == j:
                                        self.flag_in_Number_Bank += 1
                                for k in Person.Letter_Bank:
                                    if i == k:
                                        self.flag_in_Letter_Bank += 1

                            # 控制密码不少于6位
                            if len(self.new_password) < 6:
                                print("密码不可少于6位，请重新输入")
                                continue

                            # 控制密码应至少为字母+数字的组合
                            elif self.flag_in_Number_Bank == 0:
                                print("密码不可为纯字母，请重新输入")
                                continue
                            elif self.flag_in_Letter_Bank == 0:
                                print("密码不可为纯数字，请重新输入")
                                continue
                            elif self.new_password == Person.Password[self.index]:
                                print("新密码和旧密码不可以相同，请重新输入")
                                continue

                            # 密码符合要求，修改密码
                            else:
                                Person.Password[self.index] = self.new_password
                                print("密码修改成功！\n")
                                break

                        # ---------------------------------------
                        self.menu2()

                    elif self.select == 3:

                        # 修改用户名
                        while 1:
                            # 标识新的用户名是否可用
                            self.index1 = 0

                            self.new_name = input("请输入新的用户名：")

                            if self.new_name == Person.Name[self.index]:
                                print("新的用户名和旧的用户名不可以相同，请重新输入")
                                continue

                            for i in Person.Name:
                                if self.new_name == i:
                                    self.index1 += 1
                                    break

                            # 新的用户名可用
                            if self.index1 == 0:
                                # 修改用户名
                                Person.Name[self.index] = self.new_name
                                break
                            elif self.index1 == 1:
                                # 新用户名已存在
                                print("该用户名已存在，请重新输入！")
                                continue

                        # -------------------判断密码是否符合要求-----------------------
                        while 1:
                            self.new_password = maskpass.askpass(prompt="请输入新的密码（最少6位且字母数字混合）：")
                            # self.new_password = input("请输入新的密码（最少6位且字母数字混合）：")

                            self.flag_in_Number_Bank = 0
                            self.flag_in_Letter_Bank = 0

                            # 记录密码中字母和数字的个数  flag_in_Letter_Bank(字母)  flag_in_Number_Bank(数字)
                            for i in self.new_password:
                                for j in Person.Number_Bank:
                                    if i == j:
                                        self.flag_in_Number_Bank += 1
                                for k in Person.Letter_Bank:
                                    if i == k:
                                        self.flag_in_Letter_Bank += 1

                            # 控制密码不少于6位
                            if len(self.new_password) < 6:
                                print("密码不可少于6位，请重新输入")
                                continue

                            # 控制密码应至少为字母+数字的组合
                            elif self.flag_in_Number_Bank == 0:
                                print("密码不可为纯字母，请重新输入")
                                continue
                            elif self.flag_in_Letter_Bank == 0:
                                print("密码不可为纯数字，请重新输入")
                                continue
                            elif self.new_password == Person.Password[self.index]:
                                print("新密码和旧密码不可以相同，请重新输入")
                                continue

                            # 密码符合要求，修改密码
                            else:
                                Person.Password[self.index] = self.new_password
                                break

                        # ---------------------------------------

                        print("用户名和密码修改成功！")

                        self.menu2()

                    else:
                        print("输入有误，请重新输入！")
                        continue

            if self.flag == 0:
                print("该用户不存在，请重新输入！")
                self.change_Info()

    # 查询显示用户信息
    def show_Info(self):

        # 记录是否存在要查询的用户名（1：存在  0：不存在）
        self.flag = 0

        # 记录查询到的用户名的索引
        self.index = 0

        # 记录查询到的用户名
        self.sname = ""

        self.a = eval(input("请输入查询的方式（1：单个用户  2：全部用户）："))

        if self.a == 1:
            self.name = input("请输入要查询的用户名：")
            for i in Person.Name:
                if i == self.name:
                    self.flag += 1
                    self.index = Person.Name.index(i)
                    self.sname = i
                    break

            if self.flag == 1:
                print("查找成功！")
                print(f'name:{self.sname}\tpassword:{Person.Password[self.index]}')
                self.menu2()
            else:
                print("该用户信息不存在，请重新输入!")
                self.show_Info()



        elif self.a == 2:
            print("查找成功，全部用户信息如下：")
            print("name\tpassword")
            for i in range(len(Person.Name)):
                print(f'{Person.Name[i]}\t{Person.Password[i]}')
            self.menu2()

        else:
            print("输入有误，请重新输入！")
            self.show_Info()

    # 添加书籍
    def add_book(self):

        # 标识是否已存在要添加的书籍
        self.flag = 0

        # 要添加书的个数
        self.book_number = 0

        self.book_name = input("请输入要添加的书籍名称：")

        # 添加书籍前查找是否已存在要添加的书籍
        for i in Person.Book_Name:
            if i == self.book_name:
                self.flag += 1
                break

        if self.flag == 1:
            print(f"'{self.book_name}'已存在，若要修改库存请选择3.修改书籍")
            self.menu2_2()
        else:
            # 开始添加书籍
            Person.Book_Name.append(self.book_name)
            self.book_number = eval(input("请输入该书的数量："))
            Person.Book_Number.append(self.book_number)
            print("添加成功！")
            self.menu2_2()

    # 删除书籍
    def del_book(self):

        # 标记是否存在要删除的书名
        self.flag = 0

        # 标记要删除的书的索引
        self.index = 0

        self.book_name = input("请输入要删除的书名：")

        # 查找是否存在要删除的书名
        for i in Person.Book_Name:
            if i == self.book_name:
                self.flag += 1
                self.index = Person.Book_Name.index(i)
                break

        if self.flag == 1:
            # 从书籍库中删除书
            Person.Book_Name.remove(self.book_name)
            Person.Book_Number.pop(self.index)
            print(f"'{self.book_name}'删除成功！")

            self.menu2_2()
        else:
            print(f"'{self.book_name}'不存在，无法删除！")
            self.menu2_2()

    # 修改书籍
    def change_book(self):

        # 修改后的书名
        self.new_book_name = ''

        # 修改后的书的库存
        self.new_book_number = 0

        # 标识要修改的书名是否存在
        self.flag = 0

        # 标识要修改书的索引
        self.index = 0

        # 标识新的书名是否存在
        self.flag2 = 0

        self.book_name = input("请输入要修改的书名：")

        # 判断要修改的书名是否存在
        for i in Person.Book_Name:
            if i == self.book_name:
                # 有该书
                self.flag += 1
                self.index = Person.Book_Name.index(i)
                break

        if self.flag == 1:
            while 1:
                self.a = eval(input("请输入要修改的内容（1：书名  2：库存  3：书名和库存）："))
                if self.a == 1:
                    while 1:
                        # 修改书名
                        self.new_book_name = input("请输入新的书名：")

                        # 判断新的书名是否已存在
                        for j in Person.Book_Name:
                            if j == self.new_book_name:
                                self.flag2 += 1

                        if self.flag2 == 1:
                            print("新的书名已存在，请重新输入！")
                            self.flag2 = 0
                            continue
                        else:
                            Person.Book_Name[self.index] = self.new_book_name
                            print("修改成功！")
                            break
                    break
                elif self.a == 2:
                    while 1:
                        # 修改库存
                        self.new_book_number = eval(input("请输入新的库存："))

                        # 判断新的库存和旧的库存是否相同
                        if self.new_book_number == Person.Book_Number[self.index]:
                            print("新的库存不可和旧的库存相同，请重新输入！")
                            continue
                        else:
                            Person.Book_Number[self.index] = self.new_book_number
                            print("修改成功！")
                            break
                    break
                elif self.a == 3:
                    # 修改书名和库存

                    while 1:
                        # 修改书名
                        self.new_book_name = input("请输入新的书名：")

                        # 判断新的书名是否已存在
                        for j in Person.Book_Name:
                            if j == self.new_book_name:
                                self.flag2 += 1

                        if self.flag2 == 1:
                            print("新的书名已存在，请重新输入！")
                            self.flag2 = 0
                            continue
                        else:
                            Person.Book_Name[self.index] = self.new_book_name
                            break

                    while 1:
                        # 修改库存
                        self.new_book_number = eval(input("请输入新的库存："))

                        # 判断新的库存和旧的库存是否相同
                        if self.new_book_number == Person.Book_Number[self.index]:
                            print("新的库存不可和旧的库存相同，请重新输入！")
                            continue
                        else:
                            Person.Book_Number[self.index] = self.new_book_number
                            break

                    print("修改成功！")
                    break
                else:
                    print("输入有误，请重新输入！")
                    continue
            self.menu2_2()

        else:
            print(f"'{self.book_name}'不存在，无法进行修改！")
            self.menu2_2()

    # 查询书籍
    def show_book(self):

        # 标识是否存在要查询的书
        self.flag = 0

        # 标识查询到的书籍的索引
        self.index = 0

        self.a = eval(input("请输入查询的模式（1：单个  2：全部）："))
        if self.a == 1:
            self.book_name = input("请输入要查询的书名：")

            for i in Person.Book_Name:
                if i == self.book_name:
                    self.flag += 1
                    self.index = Person.Book_Name.index(i)
                    break

            if self.flag == 1:
                print("查询结果如下：")
                print(f"书名：{self.book_name}\n库存：{Person.Book_Number[self.index]}")
            else:
                print(f"'{self.book_name}'不存在！")
            self.menu2_2()

        elif self.a == 2:
            print("查询结果如下：")
            print("书名\t\t库存".center(20))
            for i in range(0,len(Person.Book_Number)):
                print(f"{Person.Book_Name[i]}\t\t{Person.Book_Number[i]}".center(20))

            self.menu2_2()

# 判断是普通用户还是管理员
def user_or_root():
    print("\n----请选择你的身份----")
    print("--    1.普通用户    --")
    print("--    2.管理员      --\n")
    a = eval(input("请输入你的选择："))
    if a == 1:
        user = User()
        user.menu1()
    elif a == 2:
        root = Root()
        root.root_menu()
    else:
        print("输入有误,请重新输入")
        user_or_root()


if __name__ == "__main__":
    user_or_root()

