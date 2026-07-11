letters={}



for ch in "abcdefghijklmnmopqrstuvwxyz":
    letters[ch]=0
print(letters)

sentence=input("Enter A Sentence: ").lower()

for ch in sentence:
    if ch in letters:
        letters[ch]=1
pangram =True

for value in letters.values():
    if value==0:
        pangram=False
        break

if pangram:
    print("Its A Pangram")
else:
    print("Not a pangram")
print(letters)