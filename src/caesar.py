import string


class Caesar:
    shift = 0
    alphabet_size = 26

    def __init__(self, shift):
        self.shift = shift % self.alphabet_size

    def transform(self, message, mode):
        """
        mode = 1 -- encrypt
        mode = 2 -- decrypt
        """
        output = ""
        for letter in message:
            if letter not in string.ascii_lowercase and letter not in string.ascii_uppercase:
                output += letter
            else:
                is_lower = False
                if letter.islower():
                    is_lower = True
                    letter = letter.upper()

                if mode == 1:
                    modified_position = (ord(letter) - ord("A") + self.shift) % self.alphabet_size
                elif mode == 2:
                    modified_position = (ord(letter) - ord("A") - self.shift) % self.alphabet_size
                else:
                    raise ValueError(f"Incorrect {mode=}, should be 1 or 2")

                new_letter = chr(modified_position + ord("A"))
                if is_lower:
                    new_letter = new_letter.lower()
                output += new_letter

        return output


def hack_cipher(message):
    letter_frequency = dict()
    message = message.upper()
    for letter in message:
        if letter in string.ascii_uppercase:
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1

    # "E" is the most popular letter in English texts
    return (ord(max(letter_frequency, key=letter_frequency.get)) - ord("E")) % 26
