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



###  make a dict samee upper wale jaise - 
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