import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("anana"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("kayak"))
        self.assertTrue(is_palindrome("solos"))
        self.assertTrue(is_palindrome("ala"))
        self.assertTrue(is_palindrome("ojo"))
        self.assertTrue(is_palindrome("salas"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("neuquen"))

if __name__ == '__main__':
    unittest.main()