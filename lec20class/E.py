class Student:
    MATH, ENGLISH, POLITICAL, SPECIALTY, FIRST_VIEW, ID = 0, 0, 0, 0, 0, 0  # 类静态数据初始化

    def __init__(self, _name, _math, _english, _political, _specialty, _review):  # 构造函数
        self.name, self.math, self.english, self.political, self.specialty, self.review = _name, _math, _english, _political, _specialty, _review
        self.id = Student.ID
        Student.ID += 1

    def first_view(self):  # 初试成绩
        return self.math + self.english + self.political + self.specialty

    def total(self):  # 总成绩
        return self.first_view() * 0.6 + self.review * 0.4

    def ok(self):  # 是否通过
        return self.math >= Student.MATH and self.english >= Student.ENGLISH and self.political >= Student.POLITICAL and self.first_view() >= Student.FIRST_VIEW

    def __lt__(self, other):  # 默认排序规则
        if self.total() != other.total(): return self.total() > other.total()  # 第一个关键字，总分降序
        return self.id < other.id  # 第二关键字,姓名

    def __repr__(self):  # 输出格式
        return '%s %.0f %0.f %.1f' % (self.name, self.first_view(), self.review, self.total())


import sys

lines = sys.stdin.readlines()  # 读取所有输入，简化IO异常判断

students = []  # 录取的学生名单
Student.MATH, Student.ENGLISH, Student.POLITICAL, Student.SPECIALTY, Student.FIRST_VIEW = map(float, lines[
    0].strip().split())  # 用输入的第一行来初始化类数据
for line in lines[1:]:  # 跳过第一行，从第二行读入
    name, math, english, political, specialty, review = line.split()  # 数据解析
    math, english, political, specialty, review = map(float, [math, english, political, specialty, review])  # 数据转化
    student = Student(name, math, english, political, specialty, review)  # 生成对象
    if student.ok(): students.append(student)  # 检查满足复试要求

students.sort()  # 按照 默认规则排序
rank = 1
for student in students:
    print(student, rank)
    rank += 1
