import string


class Vigenere:
    key = ""
    alphabet_size = 26

    def __init__(self, key):
        self.key = key

    def transform_line(self, line, mode):
        """
        mode = 1 -- encrypt
        mode = 2 -- decrypt
        """
        output_line = ""
        count = 0
        for letter in line:
            if letter not in string.ascii_lowercase and letter not in string.ascii_uppercase:
                output_line += letter
            else:
                is_lower = False
                if letter.islower():
                    is_lower = True
                    letter = letter.upper()

                modified_position = ""

                if mode == 1:
                    modified_position = (ord(letter) + ord(self.key[count])) % self.alphabet_size
                elif mode == 2:
                    modified_position = (ord(letter) - ord(
                        self.key[count]) + self.alphabet_size) % self.alphabet_size

                new_letter = chr(modified_position + ord("A"))
                if is_lower:
                    new_letter = new_letter.lower()
                output_line += new_letter

                count = (count + 1) % len(self.key)

        return output_line
