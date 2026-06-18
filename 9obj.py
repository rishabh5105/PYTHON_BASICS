### dicstinary = collection of key value 
# print []- ye of to of ke liye h mytlb ander se ander tk ki value nilana
# print ()-jo chaiye vo milegi but get se or ek hi print milega
# dict1 = {"name" : "Rishu","ags" : 20, "city" : "bangloare","pin" : 57897}
# print(dict1["name"])

# dict2 = {"name" : "Rishu","ags" : 20, "city" : "bangloare","pin" : 57897, "name":"rishabh"}
# print(dict2["name"])                                           # ye overflow wala op dega       
# print(dict2["Name"])                                             # jo key exist nhi karegi vo error dega
# print(12 / 0)                                                   # ye zero error 

### ye multiple disc ek sath 

# dics5 = {
#         "name" :"pari",
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
#     }

# print(dics5["address"]["home"]["street"])                    ## ye sirf of to of to of  karenge to ander se ander ka hi milega 


#### get  methods - this methods of any thigns take in 
# get methods  dicstionary ki mthd h  =  chenching of methods 
# note-key error ka soltion h  .get

# dics5 = {"name1" : "pari",
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
# # print(dics5.get("street",0))   ## first layar dekhta h  issme nhi h to second layara ka op dega matlab dusra dega 
# print(dics5["address"]["home"]["street"]["landmark"])## ander to ander print kar ke dega
# # print(dics5.get("address").get("area").get("home").get("no").get("street").get("landmark","Not found"))
# # "Not found" isliye likhenge q ki apn jaise address ki speligh glt kar diye to not found print ho jaye 



# details_direc = {"name":"madhav",
#                  "age":"50",
#                  "qualification":{
#                      "college":"jnct",
#                      "work":{
#                          "hometoun":"bhopal"
#                      }
#                  }
# }

# # print(details_direc.get("name").get("work").get("office","not found"))
# #print(details_direc.get("qualification").get("work").get("hometoune","bhopal"))
# print(details_direc["qualification"]["work"]["hometoun"])



# details_direc = {
#     "name":"madhav",
#     "age":"50",
#     "qualification":{
#         "college":"jnct",
#         "work":{
#             "hometoun":"bhopal"
#         }
#     }
# }

# print(details_direc.get("name").get("qualification").get("work"))



# college = {
#     "name":"BIST",
#     "directer":{
#         "name":"Y.K Sharma",
#     },
#     "secondDirector":{
#         "name":"Sk jain",
#     }
# }

# # print(college.get("director",{"secondDirector"}))
# # # print(college.get("director",college.get("secondDirector",{})))
# # print(college.get("directer"))
# print(college["secondDirector"])


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

# print(college.get("director",college.get("secondDiertor",college.get("Hod","name"))))
# # print(college)




### update methods

# details = {
#     "name":"Parii",
#     "age":70
# }
# newdetails = {
#     "name":"parii namdev",
#     "emails":"rishabhnamdev@gmail.com"
# }
# details.update(newdetails)
# print(details)



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


# details_direc = {
#     "name":"madhav",
#     "age":"50",
#     "qualification":{
#         "college":"jnct",
#         "work":{
#             "hometoun":"bhopal"
#         }
#     }
# }

# print(details_direc.get("name").get("qualification").get("work"))
