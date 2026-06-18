# apikey = as ye identify code 
# urlkey = 

# 200 series = success
# 400 series = client error 
# 500 ki series 

# req = library h      = permisson deta h                 ## inst = pip install requasts krte hn {linux me }
## streamlit = librery h                                  ## ins  = pip install requests streamlit {linux mme karenmge }



# ## CODE1/project****{for finding temperature of any city  all over the world} (from line 11 to 26)
# # ye normal run hoga
# import requests 
# import streamlit
# apiKey = "c8b922f9e4e3eb1bf2a778a976701b67"
# city = input("Enter Your City Name: ")
# tempInCel = 40
# apiUrl = f"https://api.openweathermap.org/data/2.5/weather?&appid={apiKey}&q={city}"
# response = requests.get(apiUrl)
# data = response.json()
# result = data.get("main",{}).get("temp" , 0)
# print(result-273)  
# print(result)      
# print(data)    
# print(data.get("weather",[{}])[0].get("icon","none"))                  #....(to print weather icon no.)
# print(f"current temeprature in {city} is:{tempInCel}.C")




##### CODE2 {ye siidha application m le jayega }
## (this run in commond in termux) python -m streamlit run weather_app.py
import requests
import streamlit
city = streamlit.chat_input("Enter city")
if city:
    apiKey = "c8b922f9e4e3eb1bf2a778a976701b67"
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?&appid={apiKey}&q={city}"
    reasponse = requests.get(apiUrl)
    data = reasponse.json()
    temp = data.get("main", {}).get("temp",0)
    tempInCelsius = temp -273
# print(f"current Temperature in {city} is {tempInCelsius}.c")
streamlit.chat_message("user").marksdown(f"current Temprature in **{city}** is **{tempInCelsius}**")

   


# ### this is the func of code but run in this code 
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