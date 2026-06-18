### type casting 



# a = 28
# b ="python"
# a = int(28)
# b = str("python")
# print(list(b))
# print(str(a))

# x = 'practice file and revision'
# y = 87567.94874
# x = ('practice file and revision')
# y = (87657.94874)
# print(list(x))
# print(int(y))

# num1 = "this is one and only piece in the world"     # iske jo likhana ho vo
# num1 = str("this is one and only piece in the world")  # or isme btana padega ki kon sa data type h ye 
# print(tuple(num1))                                      #tuple me ye wala () braket lgta h 
# print(list(num1))                                       # list me ye wala [] braket lgta h 
# print(set(num1))                                        # set me ye wala {} braket lagega 

# # A = 0
# A = int(A)     
# print(bool(A))

# a = 75
# a = int(75)
# print(b(a))

# f = "100" 
# f = int("100")
# print(str(f))


### uer se input lena 

# username = (input("username: "))
# age      = (input("age: "))
# salery   = (input("salery: "))
# print(username,age, salery)

# work   = str(input("enter you work: "))
# company = str(input("enter you company: "))
# print(work,company)

# salery = int(input("salery: "))
# train =str(input("train: "))
# print(salery,train)


### f = formet is a string                                          

# name = input("name: ")
# age  = input("age: ")
# print(f"Hi my name is {name}")
# print(f"And my age {age}")

# name = input("name: ")              ## sir se puchna h ye 
# age  = input("age: ")
# hobbies = input("hobbies: ")
# print(f"hi my name is" f"my age"f"my fevret"{name,age,hobbies})


### string ki function methods 

# reply = "how are you and where are you" 
# reply = reply.capitalize()
# print(reply)

# message = "ajj me ghar me meggie khaunga thik h"
# message = message.title()
# print(message)

# result = "kab ayega tera result"
# result = result.upper()
# print(result)

# word = "i founr the very most googles in powr glass"
# word = word.lower()
# print(word)

### index no ye letter aayega  

# asus = "welcome to my seflobbserved life"
# print(asus[0])
# print(asus[4])
# print(asus[15])
# print(asus[2:9])
# print(asus[17:0:-1])



### 
## lenght
# list = [12,44,50,68,98,89,43]
# print(len(list))

# array = "rishabhnamdev"
# print(len(array))

# b = 190284.28373678        # len float ki find nhi hoti h 
# print(len(b))              

# # maximum value 
# tuf = [20,30,50,10,30,87.56,87.55]
# print(max(tuf))

# list = ["apple","baloo","maango","nextt"]   # letter ke hisab se max value dega
# print(max(list))

#  ## minimum value 
# arr = [80,9000,876,8765,5436,9410]
# print(min(arr))

## round - approx ya roubndfiguer

# xyz = 2.66665
# print(round(xyz))

##pow -power 

# a = 2
# b = 2
# print(pow(a,b))

## append 

# ages = [10,20,30,40,50]
# print(ages.append())

# ## insert 
# ages = [10,20,30,40,50]                 # index 2 no.  me ja ke ye no add krna h
# ages.insert(5,60)
# print(ages)

# ages = ["parii",'rishu',800,90,3785.98,39037]   # insert me koi data type add ho jayeg abs index no sahi hona chaiye 
# ages.insert(4,9000)
# print(ages)

# ## pop 
# ages = [10,100,29,"ram",90,60,90.09982,70,50]
# ages.pop(6)
# print(ages)


# url = input("enter your vailed website")
# print("https")





###  opretor 

# a = 100
# b = 50
# print(a--b)
# print(a-+b)
# print(a---b)
# print(a-++b)
# print(a* - b)
# print(a % - b)
# print(a % + b)
# print(a / b)              # ye float me answer dega 
# print(a//b)               # ye integer me op dga 
# print(a**b)                # power me  ho jayega 

# a = 40
# a -= 20
# print(a) 

# b = 100
# b %= 21
# print(b-70)
# print(b)

# x = 216
# x //= 4
# print(x)

# v = 100 
# v *= 2
# print(v*2)

# f = 5
# f %= 100
# print(f)


### function programm 

# def message():
#     print("hello rishabh")
#     print("I'm superman")
#     print("my fev. hanuman")
# for i in range(0,10):
#     message()


# student = input("enter the your name :")
# def student():
#     if student >= 10:     
#      print("looginsucessesfully")
# for i in range(0,5):
#     student()       

## dictionary 
# engeeniers = {
#     "qual":"b tech in ai",
#     "belong":"chandiya",
#     "adress":{ 
#         "city":"chandiya",
#         "area":"bhoj",
#         "road":"mainroad",
#         "home":{
#             "wn.":12,
#             "no":43,
#             "pin":484660,
#         }
#     }
# }

# print(engeeniers["adress"]["home"]["no"])# []- ye ander to ander vaue dega
# print(engeeniers.get("adress").get("area"))# ()- jo chaiye uska key or bbalue dodno dega opadega pint me 

# office = {
#     "city":"banglore",
#     "biuldno":"3790",
#     "work":{
#         "name":"AI ENG.",
#     },
#     "second work":"enter the office",
#     "gym":{
#         "jana h ki nhi":"yass"
#     }
# }
# # print(office.get("city",office.get("work","name")))
# print(office.get("work"),office.get("second work","gym"))


# update mthods 

# details = {
#     "name":"Rishabh",
#     "age":"34",
# }
# newdetails = {
#     "name":"Bishu",
#     "email":"rishhabhnamdev@56789gmial.com",
#     "salery":"45468798",
# }
# details.update(newdetails)
# print(details)


##### arguments 

# def cal (m1,m2,m3):
#     S = m1+m2+m3
#     print(S)
#     return cal
# cal(78,90,88)

# def office ():
#     print("what is your name: ")
#     print("enter the password: ")
#     print("you connected this device: ")
# for i in range(0,5):
#     office()    

# def function(X,Y,Z):
#     s = (X+Y+Z)
#     print(s)
#     return(s)
# function(59,90,60)

# def add(a,b):
#     print(a+b)
#     return(a,b)
# add(60,60)
# add(19,60)

# def sub(a,b):
#     if a <= b :
#         print(a+b)
#     elif a >= b :
#         print(a-b)
#         return(a,b)
# sub(10,20)
# sub(40,20)    

# def user(a,b):
#     D = a/b
#     print(D)
#     return(a,b)
# user(20,60)



# def student (m1,m2,m3):
#     print(m1+m2+m3)
#     return(m1,m2,m3)



# def add(a,b):
#     print(a+b)
# def sub (a,b):
#     print(a-b)
# u1 = int(input("v1 : "))
# u2 = int(input("v2 : "))
# opr = input("enter the type : ")
# if opr == "+":
#     add (u1,u2)
# else :
#     sub(u1,u2)    

# def loop(a,b):
#     if a<b:
#         print(a-b)
#     else:
#         print(a+b)
#     return(a,b)    
# loop(700,900)            

# userdetails = {
#     "username":"parish",
#     "password":"150806",
#     "boimatric":"fingure",
# }
# def user(username,password):
#     if userdetails.get("username")==username and userdetails.get("password")==password:
#         print("login successfull")
#     elif userdetails.get("username")==username and userdetails.get("password")!= password:
#         print("wrough,pw")
#     elif userdetails.get("username")!=username and userdetails.get("password")==password:
#         print("not match")
#     else:
#         print("wrough person")           
# user("pish" , "1508k06")


# Railone = {
#     "sl":"1",
#     "ac":"3",
#     "3ac":"5",
# }
# def bookticket(sl,ac):
#     if Railone.get("sl")== sl and Railone.get("ac")== ac:
#         print("avelible")
#     elif Railone.get("sl")== sl and Railone.get("ac")!= ac:
#         print("not aveliable")
#     else:
#         print("waiting")
# bookticket("1","3")

##################  OOPS FUNCTION 

# def add(a,b):
#     return a + b
# result = add(15,5)
# result1 = add(result , 20)
# print(result1)

# def boat(age):
#     if age >=18:
#         return True
#     return False
# asd = boat(20)
# print(asd)

# def boting(age):
#     if age >= 18:
#         print("allowed")
#     else:
#         print("notallowed")
# boting(10)        

# def creator(videogrphy):
#     if videogrphy >= 20 :
#         return ("selected")
#     return ("notselected")
# res = creator(19)
# print(res)

# def student():
#     m1 = int(input("m1 :"))
#     m2 = int(input("m2 :"))
#     totel = (m1+m2)
#     agv = totel/2
#     if  agv >= 150:
#         return True
#     return False
# res = student()
# print(res)

# def Sum(marks):
#     print(sum(marks))
# def avg(marks):
#     T = sum(marks)
#     print(T/len(marks))
# def per(marks):
#     T = sum(marks)
#     P = (T*100)/500
#     print(P)
# def executor(func,*all):
#     func((all))   

# # executor(78,89,49,30,89)

# def func(n):
#     if (n==0):
#         return
#     print(n)
#     func(n-1)
# func(5)    

# a = 28 
# b = "49089"
# print(int(b))
# print(float(a))

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("strt")
#         res = func(*args,**kwargs)
#         print("ends")
#         return res 
#     return wrapper
# @decorator
# def add(a,b):
#     return a + b 
# res = add(80 , 80)
# print(res)


# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("function started")
#         func()
#     return wrapper
# @decorator
# def asd():
#     print("hello all")
# asd()    

# def decorator(func):
#     def end(*args,**kwargs):
#         func()
#         print("functoin ended")
#     return end 
# @decorator
# def asd():
#     print("hello everyone")   
# asd()    


# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,*kwargs)
#         res = func(*args,**kwargs)
#         return res*2
#     return wrapper    
# @decorator 
# def add(a,b):
#     return a+b
# res = add(20,30)
# print(res)

# Ek decorator banao jo function ke arguments print kare.
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         res = func(*args,**kwargs)
#         return res
#     return wrapper
# @decorator
# def give(a,b):
#     return a,b
# res = give(10,20)
# print(res)

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("sending message")
#         res = func(*args,**kwargs)
#         return res
#     return wrapper
# @decorator
# def mas(a):
#     return mas
# res = mas("message sent")
# print(res)

# class User:
#     name = "parish"
#     age = 80 
#     bankname = "SBI"

#     def sendname(self):
#         print(self.name)
#         print("name is right")

#     def takeage(self):
#         print(self.age)

# User = User()
# User.sendname()
# User.takeage()
# user1 = user1()




# class User:
#     name = "Roshan"
#     age = 21
#     email = "gdgwdyugwe2565"
#     otp = 9598985

#     def sendEmail(self):
#         print(self.email)
#         print("send email successsfully")
    
#     def opt(self):
#         print(self.otp)
#         print("send OTP successfully")


# user1 = User()
# user1.opt()


# class Game:

#     life = 5

#     def attack(self):
#         self.life -=1
#         if self.life == 0:
#             print("your life is 0")

#     def health(self):
#         self.life += 1

#     def getLife(self):
#         print(self.life)

# p1 = Game()

# p1.attack()
# p1.attack()
# p1.attack()

# p1.health()
# p1.health()
# p1.health()

# p1.getLife()

# lass Product:

# #     def __init__(self, name , price):
#         self.price = price
#         self.name = name

# class Cart:
#         items = []

#         def add_product(self, p):
#              self.items.append(p)
#         @property        #it will change total in attributes
#         def total(self):
#              alltotal = 0        #to get total of product and contain in cart
#              for i in self.items:
#                   alltotal += i.price
#              return alltotal
        
        
# p1 = Product("Mobile", 120000)
# p2 = Product("Ac", 2100)
# p3 = Product("Remote", 210)
# c1 = Cart()
# c1.add_product(p1)
# c1.add_product(p3)

# print(c1.total)

# ******************************************

# class Product:
#     item = "" 
#     price = 0
#     def __init__(self, name , price):
#         self.price = price
#         self.name = name
# class Cart:
#     def __init__(self):
#         self.items = []
#     def add_product(self, p):
#         self.items.append(p)
#     @property                 #it will change total in attributes
#     def total(self):
#         self.alltotal = 0      #to get total of product and contain in cart
#         for i in self.items:
#            self.alltotal += i.price
#         return self.alltotal
# class User:
#      name = ""
#      cart = None
#      def __init__(self, name = ""):
#       self.name = name
#       self.cart = Cart
# p1 = Product("Mobile", 120000)
# p2 = Product("Ac", 2100)
# p3 = Product("Remote", 210)
# u1 = User("ajay")
# u2 = User("bishuu")
# u1.cart.add_product(p1)
# u1.cart.add_product(p3)
# u2.cart.add_product(p2)
# print(u1.total)
# print



# class Game:
#     name = "parish"
#     id = "aadhar"
#     email = "sdfghjk5105email.com"
#     age = 70
#     college_name = "LNCT"
#     def sendname(self):
#         print(self.name)
#         print("verify your name")
#     def sendid (self):
#         print(self.id)
#         print("right your id ")
#     def sendage(self):
#         print(self.age)
#         print("vailedate your age")        
# game1 = Game()
# game1.sendname()
# game2 = Game()
# game2.sendid()
# game3 = Game()
# game3.sendage()

# Create a class Student
# Attributes: name, roll_no, marks
# Methods:
#   show_details()
#   check_result() -> Pass if marks >= 33 else Fail


# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name   = name
#         self.rollno = rollno
#         self.marks  = marks
#     def show_details(self):
#         print("name: ",self.name)
#         print("rollno: ",self.rollno)
#         print("marks: ",self.marks) 
#     def check_result(self):
#         if self.marks >= 33:
#             print("your are pass ")
#         else :
#             print("fail")    
# s1 = Student("rishabh", 123456 , 66)
# s1.check_result()
# s1.show_details()



# Create a class Employee
# Attributes: name, emp_id, salary
# Methods:
#   display_info()
#   annual_salary()

# class Employee:
#     def __init__(self,name,emp_id,salary):
#         self.name = name
#         self.emp_id = emp_id 
#         self.salary = salary 
#     def display_info(self):
#         print("name: ",self.name)
#         print("emp_id: ",self.emp_id)
#         print("salary: ", self.salary)
#     def annual_salary(self):
#         print("self.annual_salary: " , self.salary * 12)   
# E1 = Employee("rishabh_namdev",908623191062 , 200000) 
# E1.display_info()
# E1.annual_salary()       




# Create a class Mobile
# Attributes: brand, model, price
# Methods:
#   show_mobile()
#   discount() -> 10% discount on price

# class Mobile:
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model 
#         self.price = price
#     def show_mobile(self):
#         print("brand: ",self.brand)
#         print("model: ",self.model)
#         print("price: ",self.price)
#     def discount(self):
#         print("price_15%discount :" , self.price - (self.price*15/100))        

# M1 = Mobile("Nothing", 7893, 45000)
# M1.show_mobile()
# M1.discount()


# Create a class BankAccount
# Attributes: account_no, holder_name, balance
# Methods:
#   deposit(amount)
#   withdraw(amount)
#   check_balance()

# class Bankaccount:
#     def __init__(self,account_no,holder_name,balance):
#         self.account = account_no
#         self.holder_name = holder_name
#         self.balance = balance 
#     def deposite(self,amount):
#         self.balance += amount 
#         print("deposite: ",amount) 
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("withdraw: " ,amount) 
#         else:
#             print("insuffieantamount ")
#     def check_balance(self):
#         print("check_balance:",self.balance)
# B1 = Bankaccount(200000,"rishabh" , 800) 
# B1.check_balance() 
# B1.deposite(500)
# B1.withdraw(100)
# B1.check_balance()



# Create a class Car
# Attributes: brand, color, speed
# Methods:
#   start()
#   stop()
#   show_speed()

# class Car:
#     def __init__(self,brand,color,speed):
#         self.brand = brand
#         self.color = color 
#         self.speed = speed 
#     def start(self):
#         print(self.brand,"car started")
#     def stop(self):
#         print(self.brand,"car stoped")
#     def show_speed(self):
#         print("show_speed: ", self.speed, "km/h")
# Car = Car("bougathi","olivegreen",320)
# Car.start()
# Car.stop()
# Car.show_speed()               



# Create a class Game
# Attributes: player_name, level, health
# Methods:
#   attack() -> decrease health by 10
#   heal() -> increase health by 10
#   show_health()

# class Game:
#     def __init__(self,playername,level,health):
#         self.playername = playername 
#         self.level = level 
#         self.health = health
#     def attack(self):
#         self.health -= 1
#     def heal(self):
#         self.health += 1
#     def show_health(self):
#         print("health: ", self.health)
# G = Game("cake willamsance" , 10 , 20)
# G.attack()
# G.attack()
# G.heal()
# G.show_health()



# Create a class College
# Attributes: college_name, city, students
# Methods:
#   show_details()
#   add_students(count)






# Run Command:
# python -m streamlit run weather_app.py

import requests
import streamlit as st
city = st.chat_input("Enter City")
if city:
    apiKey = "YOUR_API_KEY"
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
    response = requests.get(apiUrl)
    data = response.json()
    temp = data.get("main", {}).get("temp", 0)
    tempInCelsius = round(temp - 273.15, 2)
    st.chat_message("user").markdown(f"Current Temperature in **{city}** is **{tempInCelsius}°C**")
    

