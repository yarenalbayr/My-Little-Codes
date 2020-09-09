i=0
list = []
threediv = []
fourdiv = [] 
maxLenghtOfList = 8
while len(list) < maxLenghtOfList:
    nums = int(input("Enter your numbers:  "))
    list.append(nums)
print("Your list is:" )
print(list)
for i in range (maxLenghtOfList) :
    if list[i] % 3 ==0:
        threediv.append(list[i])
    elif list[i] % 4 == 0:
        fourdiv.append(list[i])

print("In your list theese can divided by 3: ", end='' )
print(threediv)
print("In your list theese can divided by 4: " , end='') 
print(fourdiv)
