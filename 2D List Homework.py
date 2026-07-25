food=[[1,2,3],[4,5,6],[7,8,9]]

big=[]
for a in range(3):
    small=[]
    for b in range(3):
        small.append("🍦")
    big.append(small)
for a in range(0,len(big)):
    for b in range(0,len(big[a])):
        print(big[a][b],end=" ")
    print("\n")