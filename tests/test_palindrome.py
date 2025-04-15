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

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
        self.assertTrue(is_palindrome("Dammit I'm mad"))
        self.assertTrue(is_palindrome("Borrow or rob?"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("Top spot"))
        self.assertTrue(is_palindrome("God save Eva's dog"))
        self.assertTrue(is_palindrome("No, it is open on one position"))

if __name__ == '__main__':
    unittest.main()