text = input("Enter a paragraph: ").lower()

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("Word Frequency:")
for word, count in sorted_words:
    print(word, ":", count)

print("\nTop 5 frequent words:")
for word, count in sorted_words[:5]:
    print(word, "-", count)