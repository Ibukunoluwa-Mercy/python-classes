text = input("Enter your text: ")

words = text.split()
word_count = len(words)

character_count = len(text)
characters_no_spaces = len(text.replace(" ", ""))
sentence_count = sum(
    text.count(mark) for mark in [".", "!", "?"]
)

print("\n RESULTS ")
print("Number of words:", word_count)
print("Number of characters:", character_count)
print("Characters without spaces:", characters_no_spaces)
print("Number of sentences:", sentence_count)
