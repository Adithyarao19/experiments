unit = input("is this temperature is in celsius or faranheit C/F :")
temp= float(input("enter the temp:"))

if unit =="C":
    temp = round((9*temp)/5 + 32 , 1)
    print(f"the temperature in faranhiet is :{temp}F")
elif unit == "F":
    temp = round((temp - 32) *5 / 9,1)
    print(f" the temperature is celsius {temp}C")
else:
    print(f"{unit}is an invalid of measurment")