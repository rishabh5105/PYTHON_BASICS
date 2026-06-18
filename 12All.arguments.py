#### ARGS,KWARGS

#### topic contain
# *args
# **kwargs
# kay words arguments
# defult arguments
# closer
# executor
# decorator
# 

# * = argument      = args
# ** = key arguments= kwargs
# all- data type = tuple = args
# all2 - dictionary = dict = krags



# def add(age,*all,email,**all2):
#     print(all,all2)
#     return  sum(all)
# add(28,49,20,50,33,email="risjanjmanefhewfiuh4967",age2 = "34",gen = "k0")


# def add (*all):
#     return sum(all)
# res =  add(2,4,5,6,7,9,10)
# print(res)

# def add(a):
#     x = a * a
#     print(x)
#     return x
# add(10)

# def city(name="Bhopal"):
#     print(name)
# city()
# city("Delhi")

# def display(func):
#     func()
# def hello():
#     print("Hello")
# display(hello)    

# def display(*numbers):
#     print(numbers)
#     print(sum(numbers))
# display(10,20,30,40,50)

# def asd(*details):
#     print(details)
# asd(name ,age ,work ,city)

# def show(*args):
#     for i in args:
#         print(i)
# show(1,2,3,4,5)    


# def totle(*S):
#     # S = sum(totle)
#     print(sum(S))
#     return 
# totle(20,90,80,10,40)

# def sortl(l,D):
#     if D == "ASE":
#         l.sort()
#         return l
#     l.sort(reverse=True)
#     return l
# l = [2,3,4,5,6,7,8,9]
# print(sortl(l,D = "ASE"))       


### DEFAULT ARGUMENTS

# def ispassed(marks = 0):
#     if marks >= 33:
#         return True           ## call 
#     return False
# print(ispassed())             ## isme no pass akernge

 
#^ this is the hint of uper code in the same  
# def ispassed(a,b=0):         # b ki value def h 
#     print(a + b              ## return karnna padega
# print(ispassed(30))          # a ki value put in this  ## return pass nhgi kiye hn to None a rha h 
                        
    
### CLOSER-{logical terms}

# def parentfunction():
#     age = 23
#     def child():               ## def fun ke ander bhi or func bna skte hn 
#         print(age)
#     return child               ## agr return call nhi karenge to none dega that is not call the value 
# res = parentfunction()
# # print(res())               
# print(res)                     ## ()parenthesis   YEE LOCUL adress dega  
# print(res()()()())
# ^NOTE^ - this is the process of closer a closer is chiulde func. are access the parentionfunction
#          jo parentfunction ke arguments ko access kar rha h 


# make a three func.sum ka addb ,avge % *arg list 
# excuter kon sa func call hota return  


# def Sum(lst = []):
#     print(sum(list))
# def avg(lst=[]):
#     s = sum(list)
#     print(s/len(list))
# def parcentage(lst=[]):
#     s = sum(list)
#     parcentage = s*100/500
#     print(parcentage)
# def executor(func,*all):
#     func(list(all))
# executor(parcentage,60,70,88,90,93)




# three dict - a b c sum avg p
# dict = {
# "A":sum,
# "B":avg,
# "C":parcentage,    
# }
# def executor(key,*all):
#     func = function.get(key)
#     func(all)    
# # executor("a",30,40,50,66,90)

# def getage():
#     return int(input("enter your age: "))


# def Exe
# import tim
# def parents(func):
#     def child(*args,**kwargs
        



# def parcentage(m1,m2,m3):
#     S = (m1+m2+m3)
#     print(S)
#     return S
# parcentage(89,90,47)
# def par_child(name,age):
#     print(name,age)
#     return 
# par_child("rishabh",56)
# def executor(key,*all):
#     func = function.get(key)
#     func(all)    
# def totle(*S):
#     # S = sum(totle)
#     print(sum(S))
#     return 
# totle(20,90,80,10,40)
# def average(*SUM):
#     totel = sum(SUM)
#     avg = totel/len(SUM)
#     print("average=",avg)
# average(10,20,30,40,50)    
# def data(*args):
#     for i in args:
#         print(i , type(i))
# data(10,"python",9.9,True)





#### DECORATOR

# def islogin(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return 
#     return wrapper
# @islogin
# def add(a,b):
#     return a + b 
# res = add(2,8)
# print(res)


# def islogin(func):                         ## ye first wale line me func hi likhnge 
#     def wrapper(*args,**kwargs):           ## ye sec . me wrapper or *args **kwargs hi likhnge
#         res = func(*args,**kwargs)
#         return 
#     return wrapper
# @islogin
# def add(a,b):
#     return a + b 
# res = add(2,8)
# print(res)


##qus 1
# def greet_user(func):
#     def usage(*args, **kwrgs):
#         print("WELCOME TO TECHSIMPLUSH")
#         func(*args, **kwrgs)
#     return usage
# @greet_user
# def getage(name):
#     print("python course started")
#     return 45
# getage("gjkgkjgkjg") 


# ## qus 2
# def admin_only(func):
#     def wrapper(role):
#         if role == "admin":
#             func(role)
#         else:
#             print("Access Denied")
#     return wrapper
# @admin_only
# def delete_user(role):
#     print("User Deleted")
# delete_user("admin")
# delete_user("student")


## qus 3
# def vailedate_positive(func):
#     def wrapper(*args,**kwargs):
#         for num in args:
#             if num <= 0:
#                 print("nagative no found")
#                 return 
#         func(*args, **kwargs)
#     return wrapper   
# @vailedate_positive
# def multiply(a,b):
#     print(a*b) 
# multiply(3,4)
# multiply(-3,-4)    



## qus 4
# def massage(func):
#     def wrapper(*args,**kwargs):
#         for i in args:
#             message = True
#             if message == True:
#                 print("scful")
#             else:
#                 print("failed")
#                 func(*args,**kwargs)
#     return wrapper                
# @massage
# def send_massage():
#     print("order next to the northern army ")
#     return
# send_massage("right")



# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("start")
#         res = func(*args,**kwargs)
#         print("end")
#         return res 
#     return wrapper
# @decorator
# def add(a,b):
#     return a + b 
# res = add(12 ,3)
# print(res)



# def superdecorator(num):                   ### ye multiple decorator ke ander num ags yaert nam kuch bhi lga skte hn 
#     def decorator(func,*args,**kwargs):
#         def wrapper(*args,**kwargs):
#             res = func(*args,**kwargs)
#             return res + num
#         return wrapper
#     return decorator
# @superdecorator(50)
# def add (a,b):
#     return a+b
# res = add(12,4)
# print(res)


### make a dec. role execute no passadmin ya staff to run nhi to  superdecorator("admin")

# def superdecorator(role):                                                                       #   ↓ superdecorator("admin")                                                                                                                                                     # 
#     def decorator(func):                                                                        #   ↓ returns decorator                                                 
#         def wrapper(*args,**kwargs):                                                            #   ↓ decorator(add)
#             if role == "admin" or role == "staff":                                              #   ↓ return wrapper
#                 res = func(*args,**kwargs)                                                      #   ↓ add = wrapper
#                 return res                                                                      #   ↓ add(10,40)             
#             else:                                                                               #   ↓ wrapper(10,40)             
#                 print("not allowed")                                                            #   ↓ conditional check                      
#         return wrapper                                                                          #   ↓ func(*Args,**kwargs)    
#     return decorator                                                                            #   ↓ original add         
# @superdecorator("staff")  ### ynha kuch bhi de skte hn (admin ya staff)
# def add (a,b):
#     return a+b
# res = add(10,40)
# print(res)



# ###1 - (easy) Ek decorator banao jo function call hone se pehle "Function Started" print kare 
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("function started")
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def asd():
#     print("hello all")
# asd()   


###2 - ek decorator bnao jo function call hone ke baad "function ended" print ho ?
# def decorator(func):
#     def end(*args,**kwargs):
#         func(*args,**kwargs)
#         print("functoin ended")
#     return end 
# @decorator
# def asd():
#     print("hello everyone")   
# asd()    


### 3 - Ek decorator banao jo function ka result double kar de
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


