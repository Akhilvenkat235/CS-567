import unittest
from stringManip import *

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.input_str = "Hello, World! This is a test string with some punctuation. Hello again! Contact me at john.doe@email.com or 123-456-7890."
        self.str_utils = StringUtils(self.input_str)

    def test_reverse(self):
        self.assertEqual(self.str_utils.reverse(), ".0987-654-321 ro moc.liame@eod.nhoj ta em tcatnoC !niaga olleH .noitautcnup emos htiw gnirts tset a si sihT !dlroW ,olleH")

    def test_capitalize_words(self):
        self.assertEqual(self.str_utils.capitalize_words(), "Hello, World! This Is A Test String With Some Punctuation. Hello Again! Contact Me At John.Doe@Email.Com Or 123-456-7890.")

    def test_count_characters(self):
        self.assertEqual(self.str_utils.count_characters(), 121)

    def test_count_words(self):
        self.assertEqual(self.str_utils.count_words(), 18)

    def test_remove_whitespace(self):
        self.assertEqual(self.str_utils.remove_whitespace(), "Hello,World!Thisisateststringwithsomepunctuation.Helloagain!Contactmeatjohn.doe@email.comor123-456-7890.")

    def test_replace_substring(self):
        self.assertEqual(self.str_utils.replace_substring("World", "Python"), "Hello, Python! This is a test string with some punctuation. Hello again! Contact me at john.doe@email.com or 123-456-7890.")

    def test_is_palindrome(self):
        self.assertTrue(self.str_utils.is_palindrome())
        self.assertFalse(StringUtils("notapalindrome").is_palindrome())

    def test_count_occurrences(self):
        self.assertEqual(self.str_utils.count_occurrences("Hello"), 2)
        self.assertEqual(self.str_utils.count_occurrences("Python"), 0)

    def test_to_uppercase(self):
        self.assertEqual(self.str_utils.to_uppercase(), self.input_str.upper())

    def test_to_lowercase(self):
        self.assertEqual(self.str_utils.to_lowercase(), self.input_str.lower())

    def test_split_lines(self):
        lines = ["Hello, World! This is a test string with some punctuation. Hello again! Contact me at john.doe@email.com or 123-456-7890."]
        self.assertEqual(self.str_utils.split_lines(), lines)

    def test_strip_punctuation(self):
        self.assertEqual(self.str_utils.strip_punctuation(), "Hello World This is a test string with some punctuation Hello again Contact me at johndoeemailcom or 1234567890")

    def test_extract_emails(self):
        emails = ["john.doe@email.com"]
        self.assertEqual(self.str_utils.extract_emails(), emails)

    def test_extract_phone_numbers(self):
        phone_numbers = ["123-456-7890"]
        self.assertEqual(self.str_utils.extract_phone_numbers(), phone_numbers)

    def test_reverse_words(self):
        self.assertEqual(self.str_utils.reverse_words(), ".0987-654-321 ro moc.silemod.nhoj ta em tcatnoC olleH .noitautcnup emos htiw gnirts tset a si sihT dlroW ,olleH")

    def test_shuffle_characters(self):
        shuffled_str = self.str_utils.shuffle_characters()
        sorted_input_str = ''.join(sorted(self.input_str))
        self.assertNotEqual(shuffled_str, self.input_str)
        self.assertEqual(sorted(shuffled_str), sorted_input_str)

    def test_title_case(self):
        self.assertEqual(self.str_utils.title_case(), "Hello, World! This Is A Test String With Some Punctuation. Hello Again! Contact Me At John.Doe@Email.Com Or 123-456-7890.")

if __name__ == '__main__':
    unittest.main()
