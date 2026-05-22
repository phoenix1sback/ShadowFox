height=float(input("enter a height :"))
weight=float(input("eneter a weight :"))
BMI=weight/(height)**2
print("BMI is :",BMI)
if(BMI>=30):
    print("obesity")
if ( 25 <=BMI <29):
    print("over weight")
if(18.5 <= BMI <25):
    print("normal weight")
if(BMI<18.5):
    print("underweight")

Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city=input("enter a city name")
if city  in Australia:
    print("city is in australia",city)
elif city  in UAE:
    print("the city is in UAE",city)
elif city  in India:
    print("city is in India",India)
else:
    print("city not found")