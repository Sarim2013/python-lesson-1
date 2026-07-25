'''#variable stores 1 item and will replace item if item change
name="sarim"
print(name)
#a list stores multiple items together
names=["Tanshi","Sarim"]
print(
names)'''




#2D List
#2D Lists are list that have another list as its item
numbers=[[1,2,3],[4,5,6],[7,8,9]]
print(numbers)
print(numbers[0][1])
print(len(numbers))
print(len(numbers[0]))

#print cool emojis
big=[]
for a in range(5):
    small=[]
    for b in range(4):
        small.append("🍟")
    big.append(small)
print(big)
for a in range(0,len(big)):
    for b in range(0,len(big[a])):
        print(big[a][b],end=" ")
    print("\n")