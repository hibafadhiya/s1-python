text=input("enter a line of text:")
words = text.split()
words_count ={}
for word in words:
    word = word.lower()
    words_count[word] = words_count.get(word , 0) + 1
    for word , count in words_count.items():
        print(f"{word}:{count}" )
