# leap year

def leapyear(year):
    leap = False
    if year % 400 == 0:
        leap= True
    elif year % 100 != 0:
        leap= False
    elif year % 4 == 0:
        leap= True
    return leap


yr = int(input("enter year "))
print(leapyear(yr))