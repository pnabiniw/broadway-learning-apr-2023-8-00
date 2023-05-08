### enumerate() function #####

vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    print(vowel)

for index, value in enumerate(vowels):
    print(index)
    print(value)

for count, value in enumerate(vowels, start=1):
    print(count)
    print(value)
