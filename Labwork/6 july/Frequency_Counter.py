# WAP to count the frequency of each word in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

# Count frequency of each word
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")
print(frequency)

# Find the most frequent word
max_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        max_word = word

print("\nMost Frequent Word:")
print(max_word, ":", max_count)

# Display words in alphabetical order
print("\nWords in Alphabetical Order:")
sorted_words = sorted(frequency)

for word in sorted_words:
    print(word, ":", frequency[word])





# Output

""""""Enter a sentence: all is well

Word Frequency:
{'all': 1, 'is': 1, 'well': 1}

Most Frequent Word:
all : 1

Words in Alphabetical Order:
all : 1
is : 1
well : 1""""""