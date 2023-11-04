import unittest
from src.vernam import Vernam


class TestCaesar(unittest.TestCase):

    def test_encrypt_decrypt(self):
        cipher = Vernam()
        message = "Hello there"
        encrypted_message = cipher.transform(message, 1)
        result = cipher.transform(encrypted_message, 2)
        self.assertEqual(message, result)

    def test_raises_ValueError(self):
        cipher = Vernam()
        message = "Hello there"
        with self.assertRaises(ValueError):
            cipher.transform(message, 3)


if __name__ == "__main__":
    unittest.main()
