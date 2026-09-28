a=input("Enter a string")
vowels = 0
consonants = 0
for i in a :
    if i in "aeiouAEIOU":
        vowels+=1
    elif i ==" ":
        continue
    else:
        consonants+=1

print(vowels)
print(consonants)