import unittest
from src.caesar import Caesar, hack_cipher


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

    def test_hack_cipher(self):
        message = "Sherlock Holmes.\nFictional detective.\nConsulting detective, Victorian England.\n" \
                  "Keen intellect, observation, deduction, forensic science\nAssisted by Dr. John Watson.\n" \
                  "Solves challenging cases.\nPopular, enduring fictional character.\nAdapted for films, " \
                  "television shows, and other media.\nComplex, flawed character, unique quirks and eccentricities"
        for shift in range(27):
            cipher = Caesar(shift)
            encrypted_message = cipher.transform(message, 1)
            self.assertEqual(hack_cipher(encrypted_message), cipher.shift)


if __name__ == "__main__":
    unittest.main()
