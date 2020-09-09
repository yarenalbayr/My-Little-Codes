from cs50 import get_float

while True:
 coins=get_float("Change owed: ")
if coins <= 0:
    print("enter a positive one")
    return 1

coins= round(coins*100)
flag=0  

def coinNum():
    while True :
        if coins>24:
         coins = coins-25
         flag = flag + 1
        else:
              pass
    while True:
        if coins<25 and coins>9:
             coins= coins-10
             flag = flag + 1
        else:
             pass
    while True:
        if coins<10 and coins>4:
             coins= coins-5
             flag = flag + 1
        else:
             pass
    while True:
        if coins<5 and coins>0:
             coins= coins-1
             flag = flag + 1
        else:
             pass
print(flag) 