# # #qus1 -HW input lena and list me store karna sum and avg

# age    = int(input("age: "))
# height = int(input("height: "))
# weight = int(input("weight: "))
# salery = int(input("salery: "))
# Dob    = int(input("Dob: "))
# marks  = (age,height,weight,salery,Dob)
# totle = sum(marks)
# average = totle/len(marks)
# print(marks,totle,average)

# ye karna h 
#  #marks.append(input)
#  #add = add.sum(marks)
#  #print(list(add/len(marks)))

# #qus2-CW-maximum value kiski hogi

# m1 = int(input("m1"))
# m2 = int(input("m2"))
# m3 = int(input("m3"))
# print(max(m1,m2,m3))


# ###qus3- ek array me 10 element hn or usse sub. karna h  first 3 and last 3 ko substact karna h 

# arr = [10,20,30,40,50,80,70,10,20,10]
# # print((array[0]+array[1]+array[2])-(array[7]+array[8]+array[9]))
# # print((sum(array[0:1:2]))-(sum(array[7:8:9]))) 
# print((sum(arr[0:3]))-(sum(arr[7:10]))) 


###qus4  - user se 3 input lena 1st  me minimum no.. konsa h 3 me vo print Krna he then unka average True or false print krke btana he
### jo average value he vo minimum value se badi he ya choti isse true ya false print karwana h ye minmum value se choti h ya badi

# m1 = int(input("income: "))
# m2 = int(input("age: "))
# m3 = int(input("weight: "))
# marks = (m1,m2,m3)
# val = min(marks)
# totel = sum(marks)
# average = totel/len(marks)
# print(val,totel,average, val<average or val>average)


###qus5 -  user se input enter your age you have to bot

# age = input("your age : ")
# age  = int(age)
# age > 18 and print("you can vote ")
# age < 18 or print("you can not vote")


###qus6-  input two user name , city / user ke name ,city ki len barabar h to print allow in the city or name ya city barabar nhi h to print you chnage the name 

# name  = input("name : ")
# city  = input("city: ")
# name ==  city and print("to allow in the city ") 
# city != city or print("you change  the name ")


###qus7-  secure h yaa unsecure 
# url  =  input("enter your vailed  web ")
# print(url.find("https")==0)
# url.startswith("https://") == True and print("Secure")
# url.startswith("https://") == False and print("unsecure")


## user se user ka name  nane ki len h yadi vo even h iske charecter h to upper case hona chaiye or nhi h to ;lower hona chaiye 

# name = input("enter your name: ")
# # len(name) % 2 == 0 and print(name.upper())       ## even means sum no/2
# # len(name) % 2 != 0 and print(name.lower())       ## odd means bisum no





# ### user se user ka name name hamesha do word ka hoga name uppper ka hoga or cast lower me hoga 

# name = input("Name: ")
# fName = name.split()[0].upper()
# lName = name.split()[-1].lower()
# print(fName.upper(),lName.lower())



 



##qus1 -1. The Birthday Cake Candles Riya is turning a year older today. Ask her to enter her current age. Print a message saying how many candles will be on her cake next year.

# age = int(input("Enter your current age: "))
# next_age = age + 1
# print("Next year, there will be", next_age, "candles on your cake ") 


# ## qus 2 
# aman = input("hi im rishuu  ")
# print(aman.upper())



## qus 3. Meera signs her diary by writing her name backwards as a secret code. Take her name as input and print the reversed version.

# name = input("Enter your name: ")
# reversed_name = name[::-1]
# print("Reversed name (secret code):", reversed_name)


## qus4 - our mom gives you 5 items to buy: ["milk", "bread", "rice", "oil"]. Print the first item, the last item, and the total number of items on the list.

# list = ["milk","oil","bread","rice","pules"]
# buy1 = list[0]
# buy2 = list[4]
# totel = len(list)
# print(buy1,buy2,totel)

## qus 5 - A student got marks in 5 subjects: [78, 85, 92, 67, 88]. Find and print the highest mark, the lowest mark, the total, and the average.

# marks = [78,85,92,67,88]
# highest_marks = max(marks)
# lower_marks = min(marks)
# totel = sum(marks)
# average =totel/len(marks)
# print(highest_marks,lower_marks,totel,average)

# ## qus 6 - 6. A cricket team has these players: ["Rohit", "Virat", "Shubman", "Hardik"]. The captain wants you to:
# Add "Jadeja" at the end insert "bhumrah" at position 2 and remove "Hardik" because he injured print the final team list .

# player = ["rohit","virat","shubman","hardik"]
# player.insert(4,"jadeja",)
# player.insert(2,"bhumrah")
# player.pop(4)
# print(player)


##qus 7. Take an email address as input from the user. Check if it contains the "@" symbol and the "." symbol. Print "Looks like a valid email" if both are present, otherwise print "Invalid email"

# gmail = input("enter your vailed gmail ")
# print(gmail.find("@")==0)
# gmail.find("@") == True and print("vailed")
# gmail.find("@") != False and print("unvailed")

## qus 8 - 8. Riya is creating a password. Take her password as input and tell her:how many  charecter it has whether its "Too short" (less then 6), or "strong" (10 or more) ? 


# passward = input("Enter your passward: ")
# print(len(passward)<= 6  ,"Too short" , len(passward)>=10 ,"Too strong") 
# # print(len(passward)>=10 ,"Too strong")




# #qus 9- A messy librarian gave you a book title with extra spaces and weird capitalization: "   the great gatsby   ". Clean it up so it prints as "The Great Gatsby"

# Book = "the great gatsby"
# Book = Book.title()
# print(Book)



## qus 10. You're helping a teacher check student essays. Take a sentence as input and tell her how many words are in it. (Hint: split the sentence into a list first.)

# sentance = input("Enter your sentance: ")
# words = sentance.split()
# count = len(words)
# print(words,count)




### all type qus solve hw

# Question 1 â€” "Raju's Grocery Shop"
# Raju runs a small grocery shop in Bhopal. He stores his inventory as a list of dictionaries:
# pythoninventory = [
#     {"item": "Rice", "price": 60, "qty": 10},
#     {"item": "Dal", "price": 120, "qty": 5},
#     {"item": "Sugar", "price": 45, "qty": 0},
#     {"item": "Oil", "price": 180, "qty": 3},
#     {"item": "Atta", "price": 55, "qty": 0},
#     {"item": "Salt", "price": 25, "qty": 8},
# ]
# A customer walks in and gives Raju a shopping list: ["Rice", "Sugar", "Salt", "Paneer"]
# Write a program that loops through the customer's list and for each item prints one of three things:
#  the item name and price if it's available (qty > 0), "Out of stock" if qty is 0, or "Not available in shop"
#  if the item isn't in inventory at all. At the end, print the total bill for only the items that were successfully sold.

# inventory = [
#     {"item": "Rice", "price": 60, "qty": 10},
#     {"item": "Dal", "price": 120, "qty": 5},
#     {"item": "Sugar", "price": 45, "qty": 0},
#     {"item": "Oil", "price": 180, "qty": 3},
#     {"item": "Atta", "price": 55, "qty": 0},
#     {"item": "Salt", "price": 25, "qty": 8},
# ]
# shopping_list = ["Rice", "Sugar", "Salt", "Paneer"]
# total_bill = 0
# for item_name in shopping_list:
#     found = False
#     for item in inventory:
#         if item["item"] == item_name:
#             found = True
#             if item["qty"] > 0:
#                 print(f"{item_name} - ₹{item['price']}")
#                 total_bill += item["price"]
#             else:
#                 print(f"{item_name} - Out of stock")
#             break
#     if not found:
#         print(f"{item_name} - Not available in shop")
# print("\nTotal Bill = ₹", total_bill)







# Question 2 â€” "Gully Cricket Scorecard"
# A group of friends played a gully cricket match. The scores of each player are stored like this:
# pythonteam = {
#     "Aman": [6, 0, 4, 2, 1, 6, 0],
#     "Sahil": [0, 0, 1, 4, 0, 0, 2],
#     "Priya": [4, 4, 6, 6, 2, 1, 4],
#     "Rohan": [1, 1, 0, 0, 0, 1, 0],
#     "Neha": [6, 6, 4, 2, 4, 6, 1],
# }
# Each key is a player name and the value is a list of runs scored per ball. Write a program that 
# calculates total runs for each player, finds who scored the most, counts how many sixes (6s) each player hit,
#  and finally prints the total team score. If a player scored more than 20 runs, print "Star Player" next to their name.

# team = {
#     "Aman": [6, 0, 4, 2, 1, 6, 0],
#     "Sahil": [0, 0, 1, 4, 0, 0, 2],
#     "Priya": [4, 4, 6, 6, 2, 1, 4],
#     "Rohan": [1, 1, 0, 0, 0, 1, 0],
#     "Neha": [6, 6, 4, 2, 4, 6, 1],
# }
# highest_score = 0
# top_scorer = ""
# team_total = 0
# for player, runs in team.items():
#     total_runs = sum(runs)
#     sixes = runs.count(6)
#     team_total += total_runs
#     if total_runs > highest_score:
#         highest_score = total_runs
#         top_scorer = player
#     print(f"{player}: {total_runs} runs, Sixes = {sixes}", end="")
#     if total_runs > 20:
#         print(" Star Player")
#     else:
#         print()
# print("\nTop Scorer:", top_scorer, "-", highest_score)
# print("Total Team Score:", team_total)







# Question 3 â€” "The Hostel Mess Menu Planner"
# A hostel warden has a weekly mess menu stored as a dictionary:
# pythonmenu = {
#     "Monday": {"breakfast": "Poha", "lunch": "Dal Rice", "dinner": "Roti Sabzi"},
#     "Tuesday": {"breakfast": "Idli", "lunch": "Rajma Rice", "dinner": "Paratha"},
#     "Wednesday": {"breakfast": "Upma", "lunch": "Chole Rice", "dinner": "Roti Sabzi"},
#     "Thursday": {"breakfast": "Poha", "lunch": "Dal Rice", "dinner": "Biryani"},
#     "Friday": {"breakfast": "Sandwich", "lunch": "Kadhi Rice", "dinner": "Roti Sabzi"},
# }
# Write a program that asks the user for a day name and a meal type (breakfast/lunch/dinner).
#  If both are valid, print the dish. If the day is wrong, print "Invalid day." If the meal type is wrong,
#  print "Invalid meal type." Also, loop through the entire menu and count how many times "Roti Sabzi" appears 
# in the whole week and print: "Roti Sabzi is served X times this week." Finally, create a list of all unique breakfast items.





# menu = {
#     "Monday": {"breakfast": "Poha", "lunch": "Dal Rice", "dinner": "Roti Sabzi"},
#     "Tuesday": {"breakfast": "Idli", "lunch": "Rajma Rice", "dinner": "Paratha"},
#     "Wednesday": {"breakfast": "Upma", "lunch": "Chole Rice", "dinner": "Roti Sabzi"},
#     "Thursday": {"breakfast": "Poha", "lunch": "Dal Rice", "dinner": "Biryani"},
#     "Friday": {"breakfast": "Sandwich", "lunch": "Kadhi Rice", "dinner": "Roti Sabzi"},
# }
# day = input("Enter day: ")
# meal = input("Enter meal type: ")
# if day not in menu:
#     print("Invalid day.")
# elif meal not in menu[day]:
#     print("Invalid meal type.")
# else:
#     print("Dish:", menu[day][meal])
# count = 0
# for meals in menu.values():
#     for dish in meals.values():
#         if dish == "Roti Sabzi":
#             count += 1
# print(f"Roti Sabzi is served {count} times this week.")
# breakfast_items = []
# for meals in menu.values():
#     breakfast_items.append(meals["breakfast"])
# unique_breakfasts = list(set(breakfast_items))
# print("Unique Breakfast Items:")
# print(unique_breakfasts)



# Question 4 â€” "The Paying Guest Rent Calculator"
# A landlord has 4 tenants. Each tenant's info is stored like this:
# pythontenants = [
#     {"name": "Amit", "rent": 5000, "months_paid": [1, 2, 3, 4, 5]},
#     {"name": "Sonia", "rent": 6000, "months_paid": [1, 2, 4]},
#     {"name": "Karan", "rent": 5500, "months_paid": [1, 2, 3, 4, 5, 6]},
#     {"name": "Divya", "rent": 7000, "months_paid": [1, 3]},
# ]
# The current month is 6. Write a program that loops through each tenant and finds which months
#  they have missed (from month 1 to 6). Calculate the total pending amount for each tenant.
#  If a tenant has paid all months, print "All clear!" next to their name. At the end, print the
#  total pending amount the landlord is yet to collect from everyone.

# tenants = [
#     {"name": "Amit", "rent": 5000, "months_paid": [1, 2, 3, 4, 5]},
#     {"name": "Sonia", "rent": 6000, "months_paid": [1, 2, 4]},
#     {"name": "Karan", "rent": 5500, "months_paid": [1, 2, 3, 4, 5, 6]},
#     {"name": "Divya", "rent": 7000, "months_paid": [1, 3]},
# ]
# current_month = 6k 
# grand_total_pending = 0
# for tenant in tenants:
#     missed_months = []
#     for month in range(1, current_month + 1):
#         if month not in tenant["months_paid"]:
#             missed_months.append(month)
#     pending_amount = len(missed_months) * tenant["rent"]
#     grand_total_pending += pending_amount
#     print("\nName:", tenant["name"])
#     if pending_amount == 0:
#         print("All clear!")
#     else:
#         print("Missed Months:", missed_months)
#         print("Pending Amount: ₹", pending_amount)
# print("\nTotal Pending Amount to Collect = ₹", grand_total_pending)







# Question 5 â€” "The Blog Inspector" (API question)
# A content manager wants to quickly review posts from a blog. Use the JSONPlaceholder API 
# (https://jsonplaceholder.typicode.com/posts) and write a program that fetches all posts using the requests library. 
# Then do the following: 
# filter out only posts where the userId is 1.

# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)
# posts = response.json()
# # Filter posts of userId = 1
# user_posts = []
# for post in posts:
#     if post["userId"] == 1:
#         user_posts.append(post)
# print("Posts by User ID 1\n")
# for post in user_posts:
#     print("Post ID:", post["id"])
#     print("Title:", post["title"])
#     print("Body:", post["body"])
#     print("-" * 50)
# print("\nTotal Posts:", len(user_posts))



# Question — "Zomato Order Processor"
# You're building a mini order system for a food delivery app. Write the following functions:
# pythonmenu = {
#     "Burger": 120,
#     "Pizza": 250,
#     "Pasta": 180,
#     "Fries": 80,
#     "Coke": 40,
# }
# calculate_bill(order_list) — Takes a list of item names, returns the total bill.
#  If an item is not on the menu, skip it and print a warning.
# apply_discount(total, code) — Takes the bill total and a coupon code string. 
# If code is "FIRST50", apply 50% discount (max ₹100 off). 
# If code is "FLAT30", flat ₹30 off. If invalid code, return original total.
# generate_invoice(name, order_list, code) — This function should internally call calculate_bill and apply_discount, 
# then print a formatted invoice showing customer name, items ordered, original total, discount applied, and final amount.
# Test it with: pythongenerate_invoice("Aman", ["Pizza", "Coke", "Coke", "Momos"], "FIRST50")


            