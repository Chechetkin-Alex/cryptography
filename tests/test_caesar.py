import unittest
from src.caesar import Caesar


class TestCaesar(unittest.TestCase):

    def test_upper_case_encrypt(self):
        cipher = Caesar(12)
        message = "HELLO THERE"
        encrypted_message = "TQXXA FTQDQ"
        result = cipher.transform(message, 1)
        self.assertEqual(encrypted_message, result)

    def test_lower_case_encrypt(self):
        cipher = Caesar(5)
        message = "hello there"
        encrypted_message = "mjqqt ymjwj"
        result = cipher.transform(message, 1)
        self.assertEqual(encrypted_message, result)

    def test_big_shifting(self):
        cipher = Caesar(100500)
        message = "Hello there"
        encrypted_message = "Rovvy drobo"
        result = cipher.transform(message, 1)
        self.assertEqual(encrypted_message, result)

    def test_encrypt_decrypt(self):
        cipher = Caesar(42)
        message = "Hello there"
        encrypted_message = cipher.transform(message, 1)
        result = cipher.transform(encrypted_message, 2)
        self.assertEqual(message, result)

    def test_raises_ValueError(self):
        cipher = Caesar(1)
        message = "Hello there"
        with self.assertRaises(ValueError):
            cipher.transform(message, 3)


if __name__ == "__main__":
    unittest.main()
