# lec01 : Introduction & IO
### by ZHAO Jing  [zj@wetburing.com]

## Introduction of Python

1. What is Python?
2. What is Git/GitHub? [About Mr ZHAO?](!https://github.com/webturing/)
3. 开发工具: Python

## Useful resources:

- 作业、练习、考试/竞赛[安科OJ](https://oj.ahstu.cc)
- 上课资料同步： [MrZHAO's Github]https://github.com/webturing/]
- 课程群
- 菜鸟网站： https://www.runoob.com/python3/python3-tutorial.html
- Python中文手册 :https://www.runoob.com/manual/pythontutorial3/docs/html
## Python环境安装
- Linux/Mac内置
- Windows
## Python工作模式:(IDLE)
### 交互式：（类似于Matlab）
- ex. 计算器
- 测试表达式 中间计算结果
### 程序式
```
n = 567
c = n % 10
b = (n // 10) % 10
a = n // 100 % 10
print(a, b, c)
m = 100 * c + 10 * b + a
print(m)

```
## IO:
### Output:
- print(exp)
- print(exp,sep=" ");
### Formatted Output:
- print(format%(args1,args2...))  
```print("%d+%d=%d"%(a,b,c))```
```print("%8.2f%(x)")```
### Input: 
- input()函数


## Expression ：

### DataType

- 整型int
- 浮点型 float
- 字符串

### Constant
- 1 1L
- 0.5   +0.21e+8
- ‘a'  "abc"  '''b'''
- #
### Variable  变量无需声明，且类型可以变化 
```
x=3
x="hello"
```

### Arithmetic operator

- 加 ```+``` 数值相加或者字符串连接
- 减  ```-```
- 乘 ```*```  数值相乘或者字符串重复
- 除  ```/```   精度除法 &&  // 商
- 模 ```%``` 余数或者（*格式化输出*)
- 幂  ```**```



## Excise ：

- 输出helloworld
- 计算A+B

