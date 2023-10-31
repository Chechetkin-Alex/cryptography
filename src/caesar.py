import string


class Caesar:
    shift = 0
    alphabet_size = 26

    def __init__(self, shift):
        self.shift = shift % self.alphabet_size

    def transform_line(self, line, mode):
        """
        mode = 1 -- encrypt
        mode = 2 -- decrypt
        """
        output_line = ""
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
                    modified_position = (ord(letter) - ord("A") + self.shift) % self.alphabet_size
                elif mode == 2:
                    modified_position = (ord(letter) - ord("A") - self.shift) % self.alphabet_size

                new_letter = chr(modified_position + ord("A"))
                if is_lower:
                    new_letter = new_letter.lower()
                output_line += new_letter

        return output_line