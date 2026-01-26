# Palindrome Checker Program

text = input("Enter a word: ")

# Convert to lowercase to make comparison case-insensitive
text = text.lower()

# Reverse the string
reversed_text = text[::-1]

if text == reversed_text:
    print("It is a Palindrome ✅")
else:
    print("Not a Palindrome ❌")
