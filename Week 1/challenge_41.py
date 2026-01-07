# Mapping digits to words
digit_words = ["Zero", "One", "Two", "Three", "Four", "Five", 
               "Six", "Seven", "Eight", "Nine"]

num = int(input("Enter a number: "))

# Convert number to string to iterate over digits
num_str = str(num)

word_list = []
for digit in num_str:
    word_list.append(digit_words[int(digit)])

# Join the words with spaces
result = " ".join(word_list)
print(result)
