def is_palindrome(word):
    cleaned = word.strip().lower()
    return cleaned == cleaned[::-1]

# Example test:
print(is_palindrome("MUM"))    
print(is_palindrome("Hi"))
print(is_palindrome("GOODDAY")) 
print(is_palindrome("BOB")) 