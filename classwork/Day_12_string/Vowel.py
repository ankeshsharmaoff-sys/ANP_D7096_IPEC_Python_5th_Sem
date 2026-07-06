# Check if a character is a vowel in a given sentence
sentence = input("Enter a sentence: ")
#initialize  vowel count as 0
vowels = 0
for x in sentence:
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or
        x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        #increment the vowel count by 1
        vowels += 1
print("Number of vowels in the sentence:", vowels)