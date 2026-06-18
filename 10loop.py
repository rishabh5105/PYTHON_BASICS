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
## range jab use karte hn jab [no.,index ] dono print karwana hoga 


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


# color = ["red","white","brawun","blue"]
# for color in color:
#     print(color)
#     for i in color:
#         print(i)

##hw-list ka sum print karwan h but sum ka use nhi karna h 
# list = [40,30,20,80,10]
# a = 0
# for i in range(len(list)):
#     a = a+list[i]   
#     print(a)


# for i in range(10):
#     print(i + 1)



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


# xrtljdtyyguh



























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
    


## even = squ, odd = qub            

# nums = [3, 8, 5, 10, 7, 11, 9, 2]
# i = 0             
# while i < len(nums):
#     if nums[i] % 2 == 0:
#         print(nums[i] * nums[i])
#     else:
#         print(nums[i] * nums[i] * nums[i]) 
#     i += 1


count = 5 
while(count > 0 ):
    print(count)
    count = count -1 

