# ###  string ke methods - str  ye ek function h jo letter ko chota bada any type se karega 
# capatilze 
# title 
# lower
# upper 
# strip
# rstrip
# lsrip
# stratwith
# endswuths
# find
# join



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


## strip:- rstrip and lstrip  left and right 
# email =" parimourya00@gmail.com"
# print(email.rstrip())

# ##strip remove the unnecessary space of the text and lstrip remove left side data and rstrip remove right side of Data 
# email ="parimourya00@gmail.com"
# print(email.lstrip())

# email =" parimourya00@gmail.com "

# email.endswith

# email.startswith    ## true ya false

# email.find

# print(email.endswith)

# url = input("htts://www.hotstar.com/in/sports/cricket/dc-vs-gt/1540065721/video/live/watch#w-DialogWidget")
# print(url.find("https"))


# url = input ("enter your valid website")
# print(url.find("https")==1)


# ### its check whether your website is secure or unsecure

# url = input ("enter your valid website" )  ## web me agr {https} hoga to ye true dega or nhi hoga to false dega 
# print("https" in url)




## str ki methods h ->join (kuch bhi join kar skte hn iska use kar ke )

# msg = ["rishu","how","are","you","?"]
# string = "_".join(msg)
# print(string)

# asd = ["rishabh","is","the","best"]
# string = " + ".join(asd)
# print(string)

# a = ["10","20","70","90"]
# A = " + ".join(a)
# print(A)

### user se name lena h 

# name = input("name: ")
# string  = "".join(name)
# print(string.upper()[0:7],string.lower()[-29:-1])

# fName = name.split()[0].upper()
# lName = name.split()[1:]
# lname = " ".join(lname).lower()


### replace 

# arr = [39,89,44,22,10,39,40,50]
# arr[3] = [100]
# print(arr.replace)


# marks.append
# print(marks,backup)
# ###
# d = [ [1,2]]* 3 


# ##
# lst = []
# print(lst.append(9))


