## 8.元组

- tuple与list类似，不同之处在于tuple的元素`不能修改`。tuple写在小括号里，元素之间用逗号隔开。
- 元组的元素不可变，但可以包含可变对象，如list

> 定义一个只有一个元素的tuple，必须加逗号



```python
tup1=()		#创建空的元组
print(type(tup1))
tup2=(50)		
print(type(tup2))		#<class 'int'>
tup3=(50,)
print(type(tup3))		#<class 'tuple'>
```



```python
tup1=("abc",111,222,3,43,54,66)
print(tup1[1:5])	#左闭右开
```



***增：***(连接)

```python
tup1=(12,23)
tup2=("abc","qwe")
tup=tup1+tup2
print(tup)
```



***删：***

```python
tup=(12,23,23)
del tup		#删除整个变量
print(tup)		#会报错
```



## 9.字典

> - 字典是无序的对象集合，使用键-值（key-value）存储，具有极快的查找速度
> - 键(key)必须使用不可变类型
> - 同一字典中，键（key）必须是唯一的

```python
info={"name":"A","age":"18"}		#字典的定义
print(info["name"])		#字典的访问

print(info.get("gender"))	#使用get方法，没有找到对应键，默认返回none

print(info.get("gender","m"))	#没找到的时候可以设定默认值
```



```python
# 增
info={"name":"A","age":"18"}
newId=input("输入新学号")
info["id"]=newId
print(info["id"])
```



```python
# 删（del）
info={"name":"A","age":"18"}
del info["name"]		#直接删除整个键，再次访问会报错
print(info["name"])
```

![](C:\Users\15821\AppData\Roaming\Typora\typora-user-images\image-20210129124811867.png)



```python
# 删（清空）
info={"name":"A","age":"18"}
info.clear()		#清空里面内容
print(info)
```



```python
# 改
info={"name":"A","age":"18"}
info["age"]=20
print(info["age"])
```



> 查：查分为`键`的查询和`值`的 查询

```python
# 查（遍历）
info={"name":"A","age":"18"}
print(info.keys())		#得到所有的键
print(info.values())	#得到所有的值
print(info.items())		#得到所有的项，每个键值是一个元组
```



```python
# 遍历所有的键值对
info={"name":"A","age":"18"}
for key,value in info.items():
	print("key=%s,value=%s"%(key,value))
```

![](C:\Users\15821\AppData\Roaming\Typora\typora-user-images\image-20210129192636466.png)



```python
# 使用枚举函数，同时拿到列表中的下标和元素内容
mylist=["a","b","c","d"]
for i,x in enumerate(mylist):		#enumerate,枚举函数
	print(i,x)
```

![](C:\Users\15821\AppData\Roaming\Typora\typora-user-images\image-20210129193027364.png)



|        | 是否有序 |     是否可变类型     |
| :----: | :------: | :------------------: |
| 列表[] |   有序   |       可变类型       |
| 元组() |   有序   |      不可变类型      |
| 字典{} |   无序   | key不可变，value可变 |
| 集合{} |   无序   |  可变类型（不重复）  |



## 10.函数

**函数定义**

```python
def 函数名()：
	代码
```



```python
# 带参数的函数
def add(a,b):
	c=a+b
	print(c)
add(2,3)
```



```python
# 带返回值的函数
def add(a,b):
	return a+b
result=add(3,2)
print(result)
```

```python
# 返回多个值函数
def divid(a,b):
	shang=a/b
	yu=a%b
	return shang,yu
shang,yu=divid(5,2)
print("shang:%d,yu:%d"%(shang,yu))
```



> 局部变量优先于全局变量，若要在函数中使用全局变量，只需在变量名前加一个`global`



## 11.文件操作

```python
f=open("文件名","w")		#打开文件，w模式（写模式），文件不存在就新建
						  #		   r模式（读模式）
f.write("hello world,i am here!")		#将字符串写入文件中 
f=close()		#关闭文件
```



```python
f=open("文件名","r")
content=f.read(5)		#读五个字符
print(content)
content=f.read(5)		#接着读五个字符
print(content)
```



```python
f=open("文件名","r")
content=f.readlines() 		#一次性读取全部文件为列表，每行一个字符串元素
print(content)
i=1
for temp in content:
	print(""%d:%s"%(i,temp))
	i+=1
f.close()
```

![](C:\Users\15821\AppData\Roaming\Typora\typora-user-images\image-20210131155251952.png)



```python
f=open("文件名","r")
content=f.readline()		#读取一行
print("1:%s"%content,end="")
content=f.readline()		#继续读取一行
print("2:%s"%content)
f.close
```



## 12.异常处理

```python
#捕获异常
try:		#将可能错误的代码块包起来
	print("---test---1")
	f=open("123.txt","r")
	print("---test---2")
except IOError:		#文件没找到，属于IO异常（输入输出异常）
	pass		#捕获异常后，执行的代码
```

> 异常类型想要被捕获，需要类型一致

```python
try:
	print(num)
except NameError:		#名字错误
	print("产生错误了")
```



```python
try:		
	print("---test---1")
	f=open("123.txt","r")
	print("---test---2")
	print(num)
except (NameError,IOError):		#将可能产生的所有异常类型都放到小括号中
	print("产生错误了")
'''
except (NameError,IOError) as result: 	#as result 可以体现出哪里错了,但不是以报错的形式		
	print("产生错误了")
'''
```



```python
try:		
	print("---test---1")
	f=open("123.txt","r")
except Exception as result:		#except Exception为错误类型
	print("发生异常")
finally：		#finally为强制执行，不管有没有错误发生
	f.close()
	print("文件关闭")
```

