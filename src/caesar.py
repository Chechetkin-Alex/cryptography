import string


class Caesar:
    shift = 0
    alphabet_size = 26

    def __init__(self, shift):
        self.shift = shift % self.alphabet_size

    def encrypt_line(self, text, mode):
        """
        mode = 1 -- encrypt
        mode = 2 -- decrypt
        """
        output_line = ""
        for letter in text:
            if letter not in string.ascii_lowercase and letter not in string.ascii_uppercase:
                output_line += letter
            else:
                start_letter = "A" if letter.isupper() else "a"
                new_position = ""

                if mode == 1:
                    new_position = (ord(letter) - ord(start_letter) + self.shift) % self.alphabet_size
                elif mode == 2:
                    new_position = (ord(letter) - ord(start_letter) - self.shift) % self.alphabet_size

                output_line += chr(new_position + ord(start_letter))
        return output_line


