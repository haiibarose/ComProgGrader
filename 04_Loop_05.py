word = input()
sentence = input()

# count how many times word appears in sentence
count = 0
i = 0
while (i < len(sentence)):
    if (sentence[i:i+len(word)] == word):
        count += 1
        i += len(word)
    else:
        i += 1
print(count)