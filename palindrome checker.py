def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
print(is_palindrome("madam"))        # Output: True
print(is_palindrome("racecar"))      # Output: True
print(is_palindrome("hello"))        # Output: False
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True