
# topic contain
# ATRIBUTES   
# CONSTRUCTOR 
# DECORATOR  --> DEC. FUN. KOP RETURN KAREGA OR MODIFY KAR KE RETURN KAR DEGA 
# INHERITANSE ---> YE ADDITIONAL CHEEZE ADD KARNE KE LIYE H 
# LAMBDA 
# error find


# class user:
#     name = "rishabh" 
#     age = 20
#     Email = "email.23@g.com"
#     otp = 1234
#     def sendEmail(self):
#         print(self.Email)
#         print("email send successfully")
#     def sendotp(self):
#         print(self.otp) 
#         print("otp send correctly")
# user1 = user()
# user1.sendEmail()
# user2 = user() 
# user2.sendotp()                                          


####GAME
# class Game:
#     life = 5 
#     def attack(self):
#         self.life = self.life - 1
#     def health(self):
#         self.life = self.life + 1
#     def getlife(self):
#         print(self.life)
# p1 = Game()
# p1.attack()
# p1.attack()
# p1.attack()

# p1.health()
# p1.health()
# p1.health()

# p1.getlife()



# class name bank account pro.....name, aa no., available balance  method.... deposit, withdraw, checkbalance
# deposit time will be multiple of 100 200 500, withdraw will be of 100 200 500 and balance will also be same 
# if balance not sufficient it will print balance is unavialable.


# class Bank:
#     name = "rishabh namdev"
#     bank_acc = "SBI"
#     balence = 41000
#     def deposite(self,balance):
        
#         self.deposite += balance
#         print("deposite: " , balance)





# ### CONSTRUCTOR -  class ke obj ko bnne me help krte hn or 
# # __inti__ = intialization 

# class User:
#     firstName = ""
#     lastname = ""
#     age = 9 

#     def __init__(self,fn ,ln):    #
#         self.firstName = fn 
#         self.lastName  = ln 
   
#     def setname(self,name):
#         self.firstName = name.split(" ")[0]
#         self.lastName =  name.split(" ")[1]

#     def getName(self):
#         return self.firstName.upper() + " " + self.lastName.lower()
    
#     def __str__(self):                       # str tb chalegi jab print 
#         return self.firstName 
#         return self.lastName
# u1 =  User("pari","princess")
# print(u1)
# u1.setname("hello madam ")
# print(u1)
# print(u1.getName())
    


# modification jab user account creat karnega tb  "pan no" or 
#  ye charo cheze account bnate time hpoga pura nho hona chaiye or
#  ac no 16 digite ka hona chaiye or sare no hone chaiye 
#  pen no h jo 10 no ka hi hona chaiye
#  pen ka formett sahi hona choyaie 5 char,4 digit , 1 char
#  agr ye charo me se kisi condition ko satisfie nhi karega to vo dega een co 

# class Bank:
#     balance = 0
#     def __init__(self,name,acc_no,pan_no):
#         self.name = name
#         self.acc_no = acc_no
#         self.pan_no = pan_no
#         self.correct = True
#         if len(self.name.split()) != 2:
#             self.correct = False
#             print("Enter Correct Name...")
#         if len(str(self.acc_no)) != 16 or not str(self.acc_no).isdigit():
#             self.correct = False
#             print("Enter the correct Ac No.....")
#         if len(self.pan_no)!=10 or not self.pan_no[:5].isalpha() or not self.pan_no[5:9].isdigit() or not self.pan_no[-1].isalpha():
#             self.correct = False
#             print("Enter correct pan No......")
#     def deposit(self,amount):
#         if self.correct:
#             self.balance+=amount
#     def withDrow(self,amount):
#         if self.correct:
#             if amount <= self.balance and amount % 100 == 0:
#             # if (amount%100==0 or amount%200==0 or amount%500==0) and amount<self.balance :
#                 self.balance-=amount
#             else:
#                 print("insufficient amount")
#     def checkBalance(self):
#         if self.correct:
#             print("balance: " , self.balance)
# u1 = Bank("rishabh_namdev ",4589673215456982,"gdgd4455d")
# u1.deposit(500)
# u1.withDrow(100)
# u1.checkBalance()



# class Product:
#     def __init__(self, name , price):
#         self.price = price
#         self.name = name
# class Cart:
#         items = []
#         def add_product(self, p):
#              self.items.append(p)
#         @property              #it will change total in attributes
#         def total(self):
#              alltotal = 0      #to get total of product and contain in cart
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



# ####
# class Product:
#     item = ""
#     price = 0
#     def __init__(self, name, price):
#         self.price = price
#         self.name = name
# class Cart:
#     def __init__(self):
#         self.items = []
#     def add_product(self, p):
#         self.items.append(p)
#     @property
#     def total(self):
#         self.alltotal = 0
#         for i in self.items:
#             self.alltotal += i.price
#         return self.alltotal
# class User:
#     name = ""


# class User:
#     name = "gsugsuydg" 
#     age = 0
#     def getUpperName(self):
#         return self.name.upper()
#     @classmethod
#     def getage(self):
#         return self.age
#     def setAge(self,age):
#         self.age = age
#     @staticmethod
#     def getdiscount(self,amount,percentage):
#         price = amount * (100-percentage)/100
#         print(self)
#         return price
# u1= User()
# print(u1.age)
# u1.setAge(21)
# print(u1.age)
# print(u1.getage())
# print(User.getage())
# print(u1.getUpperName())
# print(u1.getdiscount(u1,1000,10))
# #print(User.getdiscount(1000,10))

###09/06/26
# homework create two class 1. product => price,title,discription  2. DiscountCupon => cuponcode,discountpercentage,minimumprice 
# 3. Order => name,products = [product obj], method -> addproduct(self,product):products.apend(pro obj),checkout(self,coupon) return discountprice

# class Product:
#     def __init__(self,title,price,discription):
#         self.title = title
#         self.price = price
#         self.discription = discription

# class Coupon:
#     def __init__(self,code,percentage,minimumprice):
#         self.code = code
#         self.percentage = percentage
#         self.minimumprice = minimumprice

# class Order:
#     def __init__(self,name):
#         self.name = name
#         self.products = []
        
#     def addProduct(self,p):
#         self.products.append(p)

#     def checkOut(self,coupon):
#         total = 0
#         for p in self.products:
#             total+=p.price

#         if total >= coupon.minimumprice:
#             print(coupon.minimumprice , coupon.percentage)
#             return total * coupon.percentage/100
#         else :
#             return "add product in list"

# p1 = Product("mango",650,"sweet")
# p2 = Product("apple",1000,"red")

# c1 = Coupon("bhih88",10,1000)

# o1 = Order("roshan")
# o1.addProduct(p1)
# o1.addProduct(p2)
# print(o1.checkOut(c1))



## 12/06/26
# class TaskManager:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         self.tasks = []
#         self.totalTask = 0
#     def decorator(fumc):
#         def wrap(self,*all):
#             if all[0]> len(self.tasks)-1:
#                 print("Enter currect index")
#             else:
#                 fumc(self,*all)
#         return wrap
#     def limitTask(func):
#         def wrap(*all):
#             if len(all[0].tasks) >= 10:
#                    print("your limit is ens")
#             else:
#                  func(*all)
#         return wrap
#     @limitTask
#     def addtask(self,task):
#         self.tasks.append(task)
#         self.totalTask += 1
#     @decorator
#     def deleteTask(self,index):
#             self.tasks.pop(index)
#             self.totalTask -= 1
#     @decorator
#     def updateTask(self,index,task):
#             self.tasks[index] = task
#     @decorator
#     def getTaskByIndex(self,index):
#         return self.tasks[index]
#     def getTotalTask(self):
#         return self.totalTask
# tm = TaskManager("Roshan","yuds8487")
# tm.addtask("go to spoken class")
# tm.addtask("read fastapi")
# tm.addtask("go to data science class")
# tm.addtask("go to spoken class")
# tm.addtask("read fastapi")
# tm.addtask("go to data science class")
# tm.addtask("go to spoken class")
# tm.addtask("read fastapi")
# tm.addtask("go to data science class")
# tm.addtask("go to spoken class")
# tm.addtask("read fastapi")
# tm.addtask("go to data science class")
# # tm.updateTask(6,"read ml")
# # print(tm.getTaskByIndex(2))
# # print(tm.getTotalTask())

# 15/06/26

######INHAERITANCE 

# class Vehical:
#     maxspeed = 0
#     milage = 0 
#     fuletype = "" 

#     def __init__(self,sp,ml,tp):
#         self.maxspeed = sp
#         print("i am a vehical cos .. ")    ### this is constructor __init__

#     def start(self):
#         print("Lets go .. ")


# class Car(Vehical):    ### this is inharitance 
#     model = "i20"
#     def __init__(self,model,sp,ml,tp):
#         self.model = model
#         self.milage = ml
#         super().__init__(sp,ml,tp)            ### child class ko call karna h toparents  class 
#         print(" i am a car cos .....")

#     def playsong(self):
#         print("i'm a song....")    

#     def __add__(self , other):



# # class Bike:
# #     def start(self):
# #         print("Lets go .. ")
# #     def sidestanddetector(self):
# #         if self.maxspeed > 60 :
# #             print("side stand is detector ")
# #         else:
# #             print("no side stand detector ")    

# car = Car("i20",120,20,"petrol")
# print(car.maxspeed)
# bike = 
# bike.maxspeed



####  LAMBDA 


# def sqr(a):
#     return a*a
#             or 
# sqr = lambda a : a*a                ### jo ek libne me run kiya ja ske vo lambda hota h 
# print(sqr(5))


# students = [
#     {"name" : "pari" , "age" : 100},
#     {"name" : "rishabh" , "age" :  10},
#     {"name" : "abhishek" , "age" : 25},
#     ]
# students.sort(key = lambda obj : obj.get("age"))       ### reverse , map 
# print(students)
#### LAMBDA   ka use ->
# newdata = map(lambda obj : {"age":obj ["age"] ,"name": f"mr.{obj["name"]}"}, students )
##newdata = map(lambda obj : {"age": obj["age"] + 2 , "name": f"Mr. {obj['name']}"}, students)                                                                 
# print(list(newdata))



#### error ka solution h ye 
# def add(a,b):
#     try:
#         print(a+b)
#     except:
#         print("correct pass in password ")
# add(20,10)            