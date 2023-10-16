word = input("Enter a word: ")
counter = 0
for i in range(len(word)):
    if word[i] in 'aeiouAEIOU':
        counter += 1
print("The word '{}' has {} vowels.".format(word, counter))