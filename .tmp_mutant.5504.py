class StringUtils:
break;
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        """Reverse the input string."""
        return self.input_string[::-1]

    def capitalize_words(self):
        """Capitalize the first letter of each word in the input string."""
        words = self.input_string.split()
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)

    def count_characters(self):
        """Count the number of characters in the input string."""
        return len(self.input_string)

    def count_words(self):
        """Count the number of words in the input string."""
        words = self.input_string.split()
        return len(words)

    def remove_whitespace(self):
        """Remove all whitespace (spaces and tabs) from the input string."""
        return ''.join(self.input_string.split())

    def replace_substring(self, old_substring, new_substring):
        """Replace occurrences of old_substring with new_substring in the input string."""
        return self.input_string.replace(old_substring, new_substring)

    def is_palindrome(self):
        """Check if the input string is a palindrome."""
        clean_string = ''.join(self.input_string.split()).lower()
        return clean_string == clean_string[::-1]

    def count_occurrences(self, substring):
        """Count the number of occurrences of a substring in the input string."""
        return self.input_string.count(substring)

    def to_uppercase(self):
        """Convert the input string to uppercase."""
        return self.input_string.upper()

    def to_lowercase(self):
        """Convert the input string to lowercase."""
        return self.input_string.lower()

    def split_lines(self):
        """Split the input string into a list of lines."""
        return self.input_string.splitlines()

    def strip_punctuation(self):
        """Remove all punctuation characters from the input string."""
        import string
        return self.input_string.translate(str.maketrans('', '', string.punctuation))

    def extract_emails(self):
        """Extract and return a list of email addresses from the input string."""
        import re
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.findall(email_pattern, self.input_string)

    def extract_phone_numbers(self):
        """Extract and return a list of phone numbers from the input string."""
        import re
        phone_pattern = r'\b(?:\+\d{1,2}\s?)?(?:\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}\b'
        return re.findall(phone_pattern, self.input_string)

    def reverse_words(self):
        """Reverse the order of words in the input string."""
        words = self.input_string.split()
        return ' '.join(words[::-1])

    def shuffle_characters(self):
        """Shuffle the characters in the input string."""
        import random
        char_list = list(self.input_string)
        random.shuffle(char_list)
        return ''.join(char_list)

    def title_case(self):
        """Convert the input string to title case."""
        return self.input_string.title()

# Example usage:
input_str = "Hello, World! This is a test string with some punctuation. Hello again! Contact me at john.doe@email.com or 123-456-7890."
str_utils = StringUtils(input_str)

print("Original String:", input_str)
print("Reversed String:", str_utils.reverse())
print("Capitalized Words:", str_utils.capitalize_words())
print("Character Count:", str_utils.count_characters())
print("Word Count:", str_utils.count_words())
print("Without Whitespace:", str_utils.remove_whitespace())
print("String Replace:", str_utils.replace_substring("World", "Python"))
print("Is Palindrome:", str_utils.is_palindrome())
print("Count 'Hello' Occurrences:", str_utils.count_occurrences("Hello"))
print("Uppercase:", str_utils.to_uppercase())
print("Lowercase:", str_utils.to_lowercase())
print("Split Lines:", str_utils.split_lines())
print("Strip Punctuation:", str_utils.strip_punctuation())
print("Extracted Emails:", str_utils.extract_emails())
print("Extracted Phone Numbers:", str_utils.extract_phone_numbers())
print("Reverse Words:", str_utils.reverse_words())
print("Shuffle Characters:", str_utils.shuffle_characters())
print("Title Case:", str_utils.title_case())
