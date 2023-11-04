import string


class Vigenere:
    key = ""
    alphabet_size = 26

    def __init__(self, key):
        self.key = key

    def transform(self, message, mode):
        """
        mode = 1 -- encrypt
        mode = 2 -- decrypt
        """
        output = ""
        count = 0
        for letter in message:
            if letter not in string.ascii_lowercase and letter not in string.ascii_uppercase:
                output += letter
            else:
                is_lower = False
                if letter.islower():
                    is_lower = True
                    letter = letter.upper()

                if mode == 1:
                    modified_position = (ord(letter) + ord(self.key[count])) % self.alphabet_size
                elif mode == 2:
                    modified_position = (ord(letter) - ord(
                        self.key[count]) + self.alphabet_size) % self.alphabet_size
                else:
                    raise ValueError(f"Incorrect {mode=}, should be 1 or 2")

                new_letter = chr(modified_position + ord("A"))
                if is_lower:
                    new_letter = new_letter.lower()
                output += new_letter

                count = (count + 1) % len(self.key)

        return output
