import random
import string


class Vernam:
    key = ""
    alphabet_size = 26

    def transform(self, message, mode):
        """
        mode = 1 -- encrypt
        mode = 2 -- decrypt
        """
        output = ""
        count = 0

        if mode == 1:
            self.key = "".join(random.choice(string.ascii_uppercase) for _ in range(len(message)))
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
                    modified_position = (ord(letter) - ord(self.key[count])) % self.alphabet_size
                else:
                    raise ValueError(f"Incorrect {mode=}, should be 1 or 2")

                new_letter = chr(modified_position + ord("A"))
                if is_lower:
                    new_letter = new_letter.lower()
                output += new_letter

                count += 1

        return output
