import unittest
from src.vigenere import Vigenere


class TestCaesar(unittest.TestCase):

    def test_upper_case_encrypt(self):
        cipher = Vigenere("ABACABA")
        message = "HELLO THERE"
        encrypted_message = "HFLNO UHESE"
        result = cipher.transform(message, 1)
        self.assertEqual(encrypted_message, result)

    def test_lower_case_encrypt(self):
        cipher = Vigenere("abaCaba")
        message = "hello there"
        encrypted_message = "nlrnu ankyk"
        result = cipher.transform(message, 1)
        self.assertEqual(encrypted_message, result)

    def test_encrypt_decrypt(self):
        cipher = Vigenere("Password")
        message = "Hello there"
        encrypted_message = cipher.transform(message, 1)
        result = cipher.transform(encrypted_message, 2)
        self.assertEqual(message, result)

    def test_raises_ValueError(self):
        cipher = Vigenere("Rick & Morty")
        message = "Hello there"
        with self.assertRaises(ValueError):
            cipher.transform(message, 3)


if __name__ == "__main__":
    unittest.main()
