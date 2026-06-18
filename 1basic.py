# ## new day start now  
                                                                                                            
# print("Hello All ! ")               ##   ' ', " "  iske ander jo put karenge vo str hoga
# print("hows you ?")

# ## new line bnana 
# print ("Hello All ! /n Hows are you ?")

# ## line me space karna 
# print("hello world /t how are you ?")

# x  = 30
# y =  x
# print(id(x),id(y))
# # y = 55

# a = 50
# b = 40
# print( a + b + "")                 ## {"" - type error} ayega q ki int or str dono diff data type nhi judega  
# print( a + b + True*False)         ## work on bool q ki  true 1 or false 0 ki value h

# a = 20 
# b = 40
# print((a+b+True) * "False")        ## many type or print of the "iske ander hoga "
# print((a+b/True)*False)
# print((4,) * 3)
# print(("4",)*3)


## ref(refrance) , s ,d



# ## Any more data types             ## veriable = store the data      
                                               
# age = 25 
# print("age")

# marks = 35.79
# print("marks")

# name = 'python'
# print("name")

# ispass = True
# print("ispass")

# ## differnt data type   - diff data type kabhi bhi add nhi hote hn tyep error ata h 

# m1 =  30 
# m2 = "Hello"

# # print(m1 + m2)             ## plus nhi hoga 
# print(m1 * m2)               ## do different data type me * hoga 

# ### data type casting    
# # there are the two type, type casting   
# # 1 implicit type convergen - ye python khud karega                                                                     ## python kabhii bhi data ka lose nhi krta h usko type cast se bdl deta h 
# # 2 explicit type convergen - ye human karega    
# #                                                                      [int, str, bool,float]  
#     #1 int-(integer)number,name = 63,49,ah,fjf
#     #2 str-(string)name,no      = "a","vlkh","098345"
#     #3 flt-(float no.)point     = 490.42049
#     #4 bool-(boolean)True false = True/False



# ## implicity isme python khud higher se lower data type me convert karta h    
# a = 28
# b ='python'

# b = int(a)
# a = str(b)

# print(int(a))
# print(str(b))

# age = 13 
# marks = "12.12" 
# age = str (age)
# print (int(float(marks)))

# a = 28
# b ="python"
# a = int(28)
# b = str("python")
# print(list(b))
# print(str(a))               


# ### take a user input 

# m1 = input()
# m2 = input()
# m1 = int(m1)
# m2 = int(m2)
# print(m1  +  m2 )


# ### take a user  input /HW

# m1 = input()
# m2 = input()
# m3 = input()
# m4 = input()
# m1 = int(m1)
# m2 = int(m2)
# m3 = int(m3)
# m4 = int(m4)
# print(m1*m2)
# print(m3+m4)


# ### user se details wala input lena 

# username = input("username: ")
# name     = input("name: ")
# passward = input("pass: ")
# print(username,name,passward)

# name = input("inter your name: ")
# age  = input("inter your age ")
# # print(name,age)

# name = input("name: ")
# age = 20 
# print("Hi, my name is " + name + "\n and my age is " + str(age))

# m1 = input()
# m2 = input()
# m3 = input()
# m1 = int(m1)
# m2 = int(m2)
# m3 = int(m3)
# print(m1 + m2 +m3)...      ## it will take 3 input from user and covert it into integer and give sum of all 3 inputs

# m1 = input()
# m2 = input()
# print(m1 + m2)

# name = input("enter your name")
# age = input("enter your age")
# print(f"hi my name is {name} and age is {age} " )

# name = input("enter your name")
# age = input("enter your age")
# marks = input("enter your marks")
# print(f"my name is {name} and my age is {age} and i score marks  {marks} ") 


# ### f = formet is a string 

# name = input("name: ")
# age  = 20 
# print(f"Hi my name is {name}")


# ###  string ke methods - str  ye ek function h jo letter ko chota bada any type se karega 

# # captalize methodds  - line ka first letter sirf capitl me hoga baki nhi 
# msg = "Welcome to tsp"
# msg = msg.capitalize()
# print(msg)

# # title methodds       - line ka phla cpt. hoga baki sab as its 
# msg = "Welcome to tsp"
# msg = msg.title()
# print(msg)

# # upper methodds       - line ke pure word capitel honga
# msg = "Welcome to tsp"
# msg = msg.upper()
# print(msg)

# # lower methodds       - line ka 
# msg = "Welcome to tsp"
# msg = msg.lower()
# print(msg)

## strip:- rstrip and lstrip , left and right 
# email ="parimourya00@gmail.com     "
# print(email.rstrip())

# ##strip remove the unnecessary space of the text and lstrip remove left side data and rstrip remove right side of Data 
# email ="parimourya00@gmail.com"
# print(email.lstrip())

# email =" parimourya00@gmail.com "

# email.endswith

# email.startswith    ## true ya false

# email.find

# print(email.endswith)


# ## strip:- rstrip and lstrip  left and right 
# email ="parimourya00@gmail.com     "
# print(email.rstrip())

# ##strip remove the unnecessary space of the text and lstrip remove left side data and rstrip remove right side of Data 
# email ="parimourya00@gmail.com"
# print(email.lstrip())

# email =" parimourya00@gmail.com "

# email.endswith

# email.startswith    ## true ya false

# email.find

# print(email.endswith)

# url = input("https://www.hotstar.com/in/sports/cricket/dc-vs-gt/1540065721/video/live/watch#w-DialogWidget")
# print(input)

# url = input ("enter your valid website")
# print(url.find("https")== 0)


# ### its check whether your website is secure or unsecure

# url = input ("enter your valid website" )  ## web me agr {https} hoga to ye true dega or nhi hoga to false dega 
# print("https" in url)






# ### jis letter ko chaiye vo type hoga is no se                                                                                               ## python me 1 bytes hota g jo 1 byts= 8 bit

# msg = "Welcome to tsp"
# print(msg[0])

# msg = "Welcome to tsp"
# print(msg[1])

# msg = "Welcome to tsp"
# print(msg[2])

# msg = "Welcome to tsp"
# print(msg[3])

# msg = "Welcome to tsp"
# print(msg[4])

# msg = "Welcome to tsp"
# print(msg[5])

# #as soon again
# msg = "Welcome to tsp"
# print(msg[12])

# ## slice methods - starting se last tak                                                         ## py me scile hota h [start jnha se chaiye : jnha tk chaiye]
#                                                                                                 ## as a       [0:10]  [start:stop]

# msg = "Welcome to tsp"
# print(msg[0:14])
# print(msg[3:8])

# ## method str method sss 
# mgs = "Welcome to TSP"
# print(mgs[10::-1])

# mgs = "Welcome to tsp"                                                                            ## [ : : ]=[start:stop:end] wala formula
# print(mgs[14:0:-1])

# mgs = "Welcome to tsp"
# print(mgs[::-1])                  # reverse puri line 

# mgs = "Welcome to tsp"
# print(mgs[14::-1])


# ### opretors - arithmetical, assignment ,logical, relational(com), bit ,wise
# ## + - * % / ** // 
# ##    = 
# ## /  -singal divide ko float bolenge hamesha float m output dega 
# ## // - double divide output hamesha integre me value dega

# x = 5 
# x += 3
# print(x)

# x = 4 
# x +=2
# print(x+3)

# x = 5 
# x -= 2
# print(x)

# x = 10 
# x *= 3
# print(x/3)

# y = 100
# y -= 50
# print(y/5)



## relational oprators - true ya to false ans dega hamesha 
## <, >, ==, !=, <= >=

# m1 = 50 
# m2 = 40 
# print(m1 > m2)

# m1 = 50 
# m2 = 40 
# print(m1 < m2)

# m1 = 50
# m2 = 40
# print(m1 == m2)

# m1 = 200
# m2 = 200
# print(m1 != m2)


### logical oprators
##  and,or                       { ## ture , 1 baki sab truthy value hoge        - false, none ,mtstr("") ye space mtstg h , zero = folsi value h }
## 'or'ki condition me ture hone ke baad agge nhi badenge baki kuch bhi sahi ho ya galat true hone ke bad nhi jayegnge 
## 'and' ki condition me jab tk dekhnge ki false hone tk dekhng or uske agge nhi jayegnge 

# age = 20
# city = "Bhopal"
# name = "Rishabh" 
# print(age >= 20 and city == "Bhopal")

# age = 20
# city = "Bhopal"
# name = "Rishabh" 
# print(age <= 20 and city != "Bhopal")

# age = 20
# city = "Bhopal"
# name = "Rishabh" 
# print(age <  20 or city != "Bhopal")

# age = 10
# city = "Bhopal"
# print(age>20 a)




# ##non primitive data types--list , tuple , set , dict(dictionary)

### array -list 
# ages = [65,70,7,30,10]
# print(ages[ : :-1])                        # [start:stop:step] wala formula lagega
# print(ages[4:3:1])                         # space dega q ki aage ja rha h but piche nhi 
# # print(ages[40])                          # error dega 
# print(ages[40:40])                         # space output 
# print(ages[0:4])                           # ye ek no age wale index se hoga but no just piche tk hi print hoga 

 
# ages = [22,45,70,90,199]
# print(id(ages))
# ages.append(90)
# print(id(ages) , ages)                                   # ages-append ki methods h sirf, or kisi ki nhi jo ki str ki method h 

# msg = "Hello"                                                 
# print(id(msg))
# msg = msg + "Hi"
# print(id(msg))                                                  # split str ki methos h
#                                                                 # split kbhi bhi error nhi dega 



###list 

# age = [23,45 66, 48,30]

### print,input,sum = specific globle methods 
### len,max,min,round,pow =  

##len (lenght) int ki hogi find the len(lenght)int,str dono ki nikalti h but not find the float no. of the lenght
##max (maximum) str,int,floatno.list sab deti h 
##min (minimum)
##round nearest complete no.roundfiuger
##pow power ek no ke liye dusre no ki power dega 

## len       
# a = ("rishabhnamdev")
# print(len(a))
# array = [12, 23,45,67,89,10]
# print(len(array))

# ## max=list ki sabse badi value dega 
# list = [10,19,27,36,55,77]
# print(max(list))

# ## min=list ki minmum value dega 
# list = [10,89,90,66,45,23,11,]
# print(min(list))

# ## round=ye roundfiuger output dega 
# pointno = 50.78
# print(round(pointno))

# ##pow= ye kisi ki power chada dega 
# a = 4 
# b = 2
# print(pow(a,b))

### list ki metrhod - list ki sari methods m phle us class ya func ka naam hoga as ā[list.pop]  hi lagega iske bina use nhi hoga 


## append = structure  -  last me data put kkar dega append methods kuch bhi reponse nhi deti h - retunn data type none
## insert = unstructure -  none
## pop    = mixup str+unstru- last ki value remove 
## remove =
## reverce =
## index = tuple me bhi h  - ek baar me ek 
## sort = arsending order me karega 
## clear = all data clear spcase

## response methods 
# res = input("Hello")                    # print(koi bhi response nhi dega)
# res2 = print(res)                 
# print(res2) 
   

# ## but isme dega                ## 
# a = input("Hello")
# res2 = a
# print(res2)


# ages = [22,23,45,67,89,10]
# res = ages.append(50)
# res = ages.pop
# print(res)

# res = ages.pop(2)                  # ye return dega 
# print(res)       


# ## insert -                  # ji index me humko ja ke rkhna h uder ja ke add ho jayega ji no me bhi 
#                              # insert me koi bhi chalega any data types                             
# ages =[22,33,44,55,77]                                                                                                      
# ages.insert(2,78867)             
# print(ages)


# ages =["rishu",45,'ram',90,84689,0409.49]
# ages.insert(3,70)
# print(ages)


## pop methods                          ## pop methods me any data type  work karega  - retunr type -value 
##                                        ## pop item - return - 
# ages = [30,90,70,"rishabh",'pari',"queen",80.98890]
# ages.pop(5) ## ye index no h jisse remove karna h 
# print(ages)


## remove methods                       ## remove sabi data types ke liye h 

# ages = [90,4000,40,203,59,430,443220]
# ages.remove(90)  ## remove methods me index no nhi balki pura data typ likhenge jisse remove karwana hoga 
# print(ages)             - return -none 


# ages = ["rishu",90,048.448839,32927, 'efoejvo']
# ages.remove("rishu")
# print(ages)


## reverse=  suppoted any data type 
# ages = [60,50,40,30,20,10]
# ages.reverse()
# print(ages)


# arr = ["parii",70,'rishu',800,79,3739,39173,]
# arr.reverse()
# print(arr)

## methods - sort
# ages.sort(reverse=True)
# # ages = ages[::-1]
# print(ages)



### str ki methods h -join 

# msg = ["rishu","how","are","you","?"]
# string = "_".join(msg)
# print(string)


### user se name lena h 

# name = input("name: ")
# string  = "".join(name)
# print(string.upper()[0:7],string.lower()[-29:-1])

# fName = name.split()[0].upper()
# lName = name.split()[1:]
# lname = " ".join(lname).lower()

# marks.append
# print(marks,backup)
# ###
# d = [ [1,2]]* 3 

# ##
# lst = []
# print(lst.append(9))



#### obj.py 
### dicstinary = collection of key value 

# dict1 = {"name" : "Rishu","ags" : 20, "city" : "bangloare","pin" : 57897}
# print(dict1["name"])

# dict2 = {"name" : "Rishu","ags" : 20, "city" : "bangloare","pin" : 57897, "name":"rishabh"}
# print(dict2["name"])                                           # ye overflow wala op dega       
# print(dict2["Name"])                                             # jo key exist nhi karegi vo error dega
# print(12 / 0)                                                   # ye zero error 

### ye multiple disc ek sath 

# dics5 = {"name" : "pari",
#         "age" : 20,
#         "name" :"Rishabh",
#         "address": {
#             "city" : "piplani",
#             "area" : "milkha singh park",
#             "home" : {
#                 "pin" : 462026,
#                 "no" : 80,
#                 "street" : {
#                     "landmark" : "hanuman mandir",
#                 }
#            } 
#         }
# }
# print(dics5["address"]["home"]["street"])                    ## ye sirf of to of to of  karenge to ander se ander ka hi milega 

#### get  methods 
# get methods  dicstionary ki mthd h  =  chenching of methods 
# note-key error ka soltion h  .get

# dics5 = {"name" : "pari",
#         "age" : 20,
#         "name" :"Rishabh",
#         "address": {
#             "city" : "piplani",
#             "area" : "milkha singh park",
#             "home" : {
#                 "pin" : 462026,
#                 "no" : 80,
#                 "street" : {
#                     "landmark" : "hanuman mandir",
#                 }
#            } 
#         }
# }
# print(dics5.get("street", 0))   ## first layar dekhta h issme nhi h to second layara ka op dega matlab dusra dega 

# print(dics5.get("name").get("address").get("area").get("home").get("no").get("street").get("landmark","Not found"))
# ## "Not found" isliye likhenge q ki apn jaise address ki speligh glt kar diye to not found print ho jaye 


# details_direc = {"name":"madhav",
#                  "age":"50",
#                  "qualification":"phd"{
#                      "college":"jnct",
#                      "work":"ghumna"{
#                          "hometoun":"bhopal"
#                      }
#                  }
# }
# print(details_direc.get("name").get("work").get("office","not found"))


# college = {
#     "name":"BIST",
#     "directer":{
#         "name":"Y.K Sharma",
#     },
#     "secondDirector":{
#         "name":"Sk jain",
#     }
# }

# # college.get("director",{"secondDirector"})
# print(college.get("director",college.get("secondDirector",{})))



# college = {
#     "name":"BIST",
#     "directer":{
#         "name":"Y.K Sharma",
#     },
#     "secondDirector":{
#         "name":"Sk jain",
#     },
#     "Hod":{
#         "name":"Dean",
#     }
# }

# # print(college.get("director",college.get("secondDiertor",college.get("Hod","name"))))
# print("college")




### update methods

# details = {
#     "name":"Parii",
#     "age":70
# }

# newdetails = {
#     "name":"parii namdev",
#     "emails":"rishabhnamdev@gmail.com"
# }

# details.update
# print(details.update)


# ### override
# details = {
#     "name":"Parii",
#     "age":70
# }

# newdetails = {
#     "name":"parii namdev",
#     "emails":"rishabhnamdev@gmail.com"
# }

# # updateDetails {}
# # updateDetails.update(Details)
# # updateDetails.update(newDetails)

# updatedetails ={**details ,**newdetails}
# print(updatedetails)

### get ek baar me ek baar hi key dega 



## if else 
## if elif 
## if elif else

# temp =32 
# if temp > 22
#      print("NO")
# else:
#      print("off")




# if temp >32:
#      print("26")

# elif temp >24 and temp <32 :
#      print("22") 

# elif temp >= 18 and temp <=24:
#      print("18") 

# else:
#      print("off")     





# list dict tuple set

### tuple ke ye change nhi kiya ja skta  = inmutae 
## methods 
# 1 index 
# 2 count 



## dict key value put 3 name enrol no marks(5) 

# dict = {
#         "marks" : [40,70,60,30,20]
#     }
# print(sum(dict))



#### loop.py 

##### content -
# enumarate - ye index nikal ke deta h  
# zip -     ye do diff data type ko connect karta h 
# sorted - ye koi bhi no. ko sortr kar ke greater then m rkhta h 
# breck -  koui bhi keyward ko rok deti h 
# clear - 
# range - 




## for loop  - jab break karna ho - maximum baar - limeted access
## while loop - kab break nhi hoga - jab condition pta n ho - breack point n pta ho 

###### for { start,stop,step}

#  others language in for {int = state                               }

## for i in range(0,10,2)(start,stop,step)= python me ye condition h 
## rnage jab use karte hn jab [no.,index ] dono print karwana hoga 


# ## i is a veriables 
# for i in range(0,10,2):    ## (start,stop,step)
#     print(i)
#     print(i ,end=",")
#     print(i,end="+")

# ## note end loop me ek baar hi chal skta h 

# ##jo 3 ki table me aye vo print karwana h 
# for i in range(0,20,3):
#     print(i)

# ## reverce karwana h 10 se 0 tk 
# for i in range(10,0,-1):
#     print(i)     

# ## code     

# ags = [58,68,48,49,98,90]
# for i in range(0,len(ags)):
#     print(ags[i])



##hw-list ka sum print karwan h but sum ka use nhi karna h 
# list = [40,30,20,80,10]
# a = 0
# for i in range(len(list)):
#     a = a+list[i]   
#     print(a)


# for i in range(-10,0,1):
#     print(i)

## puri list print hogi 
# li = [78,49,20,57,90,100,38]
# for i in range(len(li)):
#     print(li[i])

## ye multiple time print hoga jiten baar list me element honge
### for ko loop ko infinte time tk chgalange 


# li = [80,30,20,10,40,60]
# for i in li:
#     if i % 2 == 0:
#         print(i)


# msg = "good morning"
# for i in msg:
#     print(i)

# tup = (34,690,49,2,39,40)
# for i in tup:
#     print(i)


## dict me veriable nilana 
# dict = {
#     "name":"rishabh",
#     "age":"34",
#     "income":"90000"
# }
# for i in dict:
#     print(i)


# jab dict me key print karwana hoo 
# dict = {
#     "name":"rishabh",
#     "age":"34",
#     "income":"90000"
# }
# for key in dict:
#     print(key,dict[key])


## break 
## list se element ate hn negative h to yas 
# li = [80,48,48,-2,-39,-29,-189]
# for i in li:
#     if i < 0:
#         print("yas")
# #         break
# print("Bayee...")    



# li = [80,48,48,-2,-39,-29,-189]
# v = "no"
# for i in li:
#     if i < 0:
#         v = "yas"
#         break
# print(v)
# print("bayy")    
       

### list me negative no h ki nhi vo dekhna ?
# li = [80,48,48,2,39,29,-189]
# for li in li:
#     if li < 0:
#         print("yas")
#         break
# else :
#     print("no")    



# for i in range(9,50):
#     if i % 3 == 0:
#         print(i)


### qus - 
## jab kisi loop m count karna ho tb ek alg veriable bna denge 
# li = [90,39,29,1,40,220,2]
# a = 0
# for i in li:
#     a = a + 1
# print(a)    
    

### list me kitne no h vo conut karena h 
##- 2 jinti baar aya h utne baar count kar ke batega ye 

# li = [90,39,2,29,1,2,40,220,2] 
# c = 0 
# target = 2
# for i in li:
#     if i ==2:
#         c = c+1
# print(c)  


## qus - * karna h reverce pattern wala or forward wala and space wala less then and greater then wala bhi 

###9FUNCTION

#### function contain (def=define)
#1 def function 
# define
# add sub mul dev.
# return 
# def- if elif else combine  
# def message():this line explain-def(define)mes(jo ki function ka naam h)()(iske ander koi bhi 1,2,3.. value input le rhe ho )
# ()-(iske ander parameter bolte hn)


### def


# def table(a,b):
#     sum = a + b
#     print(sum)
#     return table
# table(45,55)

# def message():        
#     print("hello rishabh")
#     print("I'm superman")
#     print("my fev. hanuman")
# for i in range(0,10):
#     message()


# def add(a,b):
#     print(a+b)
#     return 
# add(20,30)
# add(10,20)
# add(30,90)

# def sub(a,b):
#     print(a-b)
# sub(20,10)
# sub(60,40)


### user se input le kr type dena ki kya karna h 
# def multiple(a,b):
#     print(a*b)
# def devide(a,b):
#     print(a/b) 
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b) 
# v1 = int(input("v1: "))
# v2 = int(input("v2: "))
# opr  = input("enter the type : ")
# if opr == "+":
#     add(v1,v2)
# elif opr == "-":
#     sub(v1,v2)    
# elif opr == "*":
#     multiple(v1,v2)        
# else:
#     devide(v1,v2)  



## create a fun. to take two fun. and inside a fun. we  should have 
## if a>b print(a-b) ,else (b-a)     

# def loop(a,b):
#     if a>b:
#         print(a-b)
#     else:
#         print(a+b)
#     return(a,b)
# loop(399,900)        



### a dict in put the user details and make a function in that of match pw and match user name when print now login elif wroung username and pw ?
# userdetails ={
#     "username":"rishu",
#     "pw":"44444",
#     "selery":"2000000"
# }
# def validate(username, password):
#     if userdetails.get("username") == username and userdetails.get("pw") == password:
#         print("LoggedIn Successfully")
#     elif userdetails.get("username") != username and userdetails.get("pw") != password:
#         print("not match")
#     elif userdetails.get("username") == username and userdetails.get("pw") != password:
#         print("qwerty")
#     else:
#         print("Wrong Username and password")
# validate("rishu", "44444")      # ider se input denge jo bhi lena hoga vo ider 



## make a dict samee upper wale jaise - 
# userdetails = {
#     "rishabh":"5678",
#     "rishu":"12345"
#     }
# def vailedate(username,password):
#     realpassword = userdetails.get(username)
#     if not realpassword or realpassword != password:
#         print("Does not ")
#     else:
#         print("pass")
# vailedate("rishabh","5678")


### ADVANCE FUNCTION 
# def add(a,b):                          ## har baar chnage karne 
#     return a + b
# def multiple(a,b):
#     return a * b
# result = add(12,3)
# result2 = add(result,5)
# result3 = multiple(result2,2)          ## is line se hum kuch bhi add karwa skte hn but uper fun. bnana padega 
# print(result)


###qus - if 18 is smaller than when not allowed in the boting and greater than is allowed of boting ?
# def isAllowed(age):
#     if age > 18:
#         return True 
#     # else:
#     #     return False
#     # OR                   # is dono me se koi bhi kar skte hn else condition se ya return se kisi se bhi 
#     return False
# res = isAllowed(80)
# print(res)



### user se marks ke no lena h or uska avg small h ya big ye dekh ke true false print karwana h 
# def processstudent():
#     name = input("enter the name :")
#     m1 = int(input("m1 : "))
#     m2 = int(input("m2 : "))
#     m3 = int(input("m3 : "))
#     m4 = int(input("m4 : "))
#     m5 = int(input("m5 : "))
#     totle = (m1+m2+m3+m4+m5)
#     average = totle/5
#     if average > 20: # ye return method se else ka rule hi hat jata h or return ke baad koi bhi line nhi chalegi return last h 
#         return True
#     return False
# result = processstudent()
# print(result)


# tem drg selcias huminity ye fun. do argument dega city tem,unit se
# def whether():
#     import requests 
#     import streamlit
#     apiKey = "c8b922f9e4e3eb1bf2a778a976701b67"
#     city = input("Enter Your City Name: ")
#     # tempInCel = 50
#     apiUrl = f"https://api.openweathermap.org/data/2.5/weather?&appid={apiKey}&q={city}"
#     response = requests.get(apiUrl)
#     data = response.json()
#     temp = data.get("main",[]).get("temp",0)
#     humenity = data.get("main",[]).get("humenity",0)
#     ("weather",[{}])[0].get("icon","none"),("main",[{}][].get("humidity","none")))                  #....(to print weather icon no.)
#     print(f"current temeprature in {city} :{temp:.2f}.C")
#     print(f"humenity:{humenity}%")
# whether()



# ### isse city ka tem or unit(cel) me btana padega to ans dega
# import requests
# def weather(city,unit):
#      apiKey = "c8b922f9e4e3eb1bf2a778a976701b67"
#      apiUrl = f"https://api.openweathermap.org/data/2.5/weather?&appid={apiKey}&q={city}"
#      res = requests.get(apiUrl)
#      data = res.json()
#      temp = data.get("main",{}).get("temp",{})
#      humidity =  data.get("main",{}).get("humidity",{})
#      print(f"Humidity : {humidity}")
#      if unit=="C":
#           print(f"temp in C : {temp-273}")
#      elif unit=="F":
#           print(f"temp in F : {(9/5)*(temp-273)+32}")
#      else :
#           print(f"temp in k : {temp}")
# city = input("Enter city: ")
# tempU = input("Enter temp unit: ")
# weather(city,tempU)


























### power 

# ages = [89,20,10,60,50,69,47]
# for i in ages:
#     if i % 2 == 0:
#         print(i*i)
#or   if i % 2 == 0:
#         print(i*i*i)
#         #or
#     # else: 
#     #     print(i*i*i)   



### list me se age 2 se dev ho rhi h to name printed ho ? 
# list = [
#     {"name":"rishabh","age":"40"},
#     {"name":"pari","age":"90"},
#     {"name":"ravi","age":"20"},
#     {"name":"anup","age":"25"},
#     {"name":"abhishek","age":"56"},
# ]
# for list in list:
#     if int (list["age"]) % 2 ==0: 
#      print(list["name"])



## sort - arsendind order me dega ye 
## revercse - disanding  = []     

# ages = [89,20,10,60,50,69,47]
# ages.sort(reverse=True)
# # ages = ages[::-1]
# print(ages)



### enumarate methods - list me se index find karna h us list ka , do value return deta h 

# fruits = ["apple", "banana", "mango"]
# index = 0
# for fruit in fruits:
#     print(index, fruit)
#     index += 1


# marks = [59,90,30,28,10,50,100]
# index = 0
# for marks in marks:
#     print(index,marks)    
#     index += 1

# age = [89,39,20,29,17]
# for i, num in enumerate(age):
#     if i % 2 == 0:   
#      print(age)

### zip methods - that is the combine in the thwe list and tupls of result in zip    

# name = ["ravi","rishabh","pari","rishu"]
# age = [39,90,20,24]
# result =zip(name,age)
# print(list(result))


# point = [38.5,78.3,90.3,78.2]
# marks = [60,40,80,90,55,89]
# answer = list(zip(point,marks))
# print(answer)


# key = ["name","age","marks","salery","engneering"]
# value = ["rishu","20","456","4000000","softwere"]
# combine = list(zip(key,value))
# print(combine)


###sorted methods - num  ko greater then me convert kar dega 

# numbers = [5, 2, 9, 1, 7]
# print(sorted(numbers))


# num = [9 ,30,12,18,10,59,66,2,6,590,2890,2873,293,000]
# print(sorted(num))

# ages = [789,403,28,578,2,48]
# ages= sorted()



### while loop 

# import random
# realnum = random.randint(0,20)
# # realnum = 34 
# while True:
#     num = int(input("Enter teh number: "))
#     if num > realnum:
#         print("num is > real num ")
#     elif num > realnum:
#         print("num is < realnum ")
#     else :
#         print("number is matched")
#         break


## 3 se multiple hoen wale no. print honge 
# i = 0 
# while i < 21:
#     if i % 3 == 0:
#         print(i)
#     i += 1    
    


## even = square, odd = qube            

# nums = [3, 8, 5, 10, 7, 11, 9, 2]
# i = 0             
# while i < len(nums):
#     if nums[i] % 2 == 0:
#         print(nums[i] * nums[i])
#     else:
#         print(nums[i] * nums[i] * nums[i]) 
#     i += 1


#### function 



#### function contain (def=define)
#1 def function 
# define
# add sub mul dev.
# return 
# def- if elif else combine  





### def

# def message():
#     print("hello rishabh")
#     print("I'm superman")
#     print("my fev. hanuman")
# for i in range(0,10):
#     message()


# def add(a,b):
#     print(a+b)
# add(20,30)
# add(10,20)
# add(30,90)

# def sub(a,b):
#     print(a-b)
# sub(20,10)
# sub(60,40)


### user se input le kr type dena ki kya karna h 
# def multiple(a,b):
#     print(a*b)
# def devide(a,b):
#     print(a/b)  
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)    
# v1 = int(input("v1: "))
# v2 = int(input("v2: "))
# opr  = input("enter the type : ")
# if opr == "+":
#     add(v1,v2)
# elif opr == "-":
#     sub(v1,v2)    
# elif opr == "*":
#     multiple(v1,v2)        
# else:
#     devide(v1,v2)  



## create a fun. to take two fun. and inside a fun. we  should have 
#   3 fun(a,b): if a is >b print(a-b)else (b-a)     
# def func(a,b):
#     if a>b:
#         print(a-b)
#     else:
#         print(b-a)
# func(100,50)
# func(40,80)




### a dict in put the user details and make a function in that of match pw and match user name when print now login elif wroung username and pw ?
# userdetails ={
#     "username":"rishu",
#     "pw":"44444",
#     "selery":"2000000"
# }
# def validate(username, password):
#     if userdetails.get("username") == username and userdetails.get("pw") == password:
#         print("LoggedIn Successfully")
#     elif userdetails.get("username") != username and userdetails.get("pw") != password:
#         print("not match")
#     elif userdetails.get("username") == username and userdetails.get("pw") != password:
#         print("qwerty")
#     else:
#         print("Wrong Username and password")
# validate("rishu", "44444")      # ider se input denge jo bhi lena hoga vo ider 



## make a dict samee upper wale jaise - 
# userdetails = {
#     "rishabh":"5678",
#     "rishu":"12345"
#     }
# def vailedate(username,password):
#     realpassword = userdetails.get(username)
#     if not realpassword or realpassword != password:
#         print("Does not ")
#     else:
#         print("pass")
# vailedate("rishabh","5678")


### ADVANCE FUNCTION 
# def add(a,b):                          ## har baar chnage karne 
#     return a + b
# def multiple(a,b):
#     return a * b
# result = add(12,3)
# result2 = add(result,5)
# result3 = multiple(result2,2)          ## is line se hum kuch bhi add karwa skte hn but uper fun. bnana padega 
# print(result)


###qus - if 18 is smaller than when not allowed in the boting and greater than is allowed of boting ?
# def isAllowed(age):
#     if age > 18:
#         return True 
#     # else:
#     #     return False
#     # OR                   # is dono me se koi bhi kar skte hn else condition se ya return se kisi se bhi 
#     return False
# res = isAllowed(80)
# print(res)



### user se marks ke no lena h or uska avg small h ya big ye dekh ke true false print karwana h 
# def processstudent():
#     name = input("enter the name :")
#     m1 = int(input("m1 : "))
#     m2 = int(input("m2 : "))
#     m3 = int(input("m3 : "))
#     m4 = int(input("m4 : "))
#     m5 = int(input("m5 : "))
#     totle = (m1+m2+m3+m4+m5)
#     average = totle/5
#     if average > 20: # ye return method se else ka rule hi hat jata h or return ke baad koi bhi line nhi chalegi return last h 
#         return True
#     return False
# result = processstudent()
# print(result)



# tem drg selcias huminity ye fun. do argument dega city tem,unit se

# def whether():
#     import requests 
#     import streamlit
#     apiKey = "c8b922f9e4e3eb1bf2a778a976701b67"
#     city = input("Enter Your City Name: ")
#     # tempInCel = 50
#     apiUrl = f"https://api.openweathermap.org/data/2.5/weather?&appid={apiKey}&q={city}"
#     response = requests.get(apiUrl)
#     data = response.json()
#     temp = data.get("main",[]).get("temp",0)
#     humenity = data.get("main",[]).get("humenity",0)
       
#     # result = data.get("main",{}).get("temp" , 0)
#     # print(result-273)  
#     # print(result)      
#     # print(data)    
#     # print(data.get("weather",[{}])[0].get("icon","none"),("main",[{}][].get("humidity","none")))                  #....(to print weather icon no.)
#     print(f"current temeprature in {city} :{temp:.2f}.C")
#     print(f"humenity:{humenity}%")
# whether()


#### all argument 

#### ARGS,KWARGS

#### topic contain
# arguments 
# kay words arguments





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
#  
 
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
# ^NOTE^ - this is the process of closer a closer is chiulde fun are access the parentionfunction
#          jo parentfunction ke arguments ko access kar rha h 
#  make a three func.sum ka addb ,avge % *arg list 
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

# import time


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


# def islogin(func):               ## ye first wale line me func hi likhnge 
#     def wrapper(*args,**kwargs): ## ye sec . me wrapper or *args **kwargs hi likhnge
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

