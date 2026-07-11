vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
}
sentence= input("Enter A Sentence ")
for letter in sentence:
    if letter in vowels:
        vowels[letter]=1

pangram=True
for letter in vowels.values():
    if letter==0:
        pangram=False
        break
        
if pangram:
    print("This Sentence Contains Every Vowel")
else:
    print("This Sentence DOESNT Contain Every Vowel")