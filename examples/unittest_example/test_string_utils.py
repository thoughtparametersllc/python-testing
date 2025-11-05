"""Example unittest tests for string utilities."""
import unittest


def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s):
    """Check if a string is a palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def capitalize_words(s):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in s.split())


class TestStringUtils(unittest.TestCase):
    """Test cases for string utility functions."""

    def test_reverse_string(self):
        """Test string reversal."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

    def test_is_palindrome(self):
        """Test palindrome detection."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))

    def test_capitalize_words(self):
        """Test word capitalization."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python testing"), "Python Testing")
        self.assertEqual(capitalize_words(""), "")

    def test_reverse_string_unicode(self):
        """Test string reversal with unicode."""
        self.assertEqual(reverse_string("hello 🎉"), "🎉 olleh")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases."""

    def test_empty_inputs(self):
        """Test with empty inputs."""
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(capitalize_words(""), "")
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """Test with single character."""
        self.assertEqual(reverse_string("a"), "a")
        self.assertTrue(is_palindrome("a"))


if __name__ == '__main__':
    unittest.main()
