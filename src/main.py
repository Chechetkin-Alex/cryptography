import os.path
from caesar import Caesar
from vigenere import Vigenere
from vernam import Vernam


def start():
    print("Приветствую, путник!\n"
          "Меня зовут Гарри, и я очень увлекаюсь шифрами.\n"
          "Ты можешь либо перечислить пути к файлам, содержимое которых "
          "ты хотел бы зашифровать/расшифровать, либо оставить ввод пустым, тогда сможешь просто "
          "посмотреть на мои режимы работы:")

    ans = input().split()
    if all(os.path.isfile(path) for path in ans):
        print("Отлично, теперь ты можешь выбрать метод шифрования.")
    else:
        raise FileNotFoundError

    cipher = input("1: Шифр Цезаря\n"
                   "2: Шифр Виженера\n"
                   "3: Шифр Вернама: ")

    if cipher.isnumeric() and 1 <= int(cipher) <= 3:
        cipher = int(cipher)
    else:
        raise ValueError("Expected number from 1 to 3")

    mode = input("\nИ требуется режим.\n"
                 "1: Зашифровать\n"
                 "2: Расшифровать: ")

    if mode.isnumeric() and 1 <= int(mode) <= 2:
        mode = int(mode)
    else:
        raise ValueError("Expected number from 1 to 2")

    if mode == 1:
        encrypt(ans, cipher)
    elif mode == 2:
        decrypt(ans, cipher)

    print("\nБыло приятно познакомиться, приходи снова!")


def encrypt(ans, cipher):
    if len(ans) != 0:
        if cipher == 1:
            shift = input("\nВведи ключ для файлов (число): ")

            if shift.isnumeric():
                shift = int(shift)
            else:
                raise ValueError("Expected number")

            for path in ans:
                with open(path, "r") as original, \
                        open(f"{os.path.splitext(path)[0]}_encrypted", "w") as encrypted:
                    encrypted.write(Caesar(shift).transform(original.read(), 1))

            print("\nДело сделано, не забывай сохранить ключ ;)")

        elif cipher == 2:
            key = input("\nВведи ключ для файлов: ")
            for path in ans:
                with open(path, "r") as original, \
                        open(f"{os.path.splitext(path)[0]}_encrypted", "w") as encrypted:
                    encrypted.write(Vigenere(key).transform(original.read(), 1))

            print("\nДело сделано, не забывай сохранить ключ ;)")

        else:
            for path in ans:
                with open(path, "r") as original, \
                        open(f"{os.path.splitext(path)[0]}_encrypted", "w") as encrypted, \
                        open(f"{os.path.dirname(path)}/key_for_file_{os.path.basename}.txt", "w") as key_file:
                    encrypted_message = Vernam().transform(original.read(), 1)
                    encrypted.write(encrypted_message[0])
                    key_file.write(encrypted_message[1])

            print("\nДело сделано, не забывай сохранить ключ ;)\n"
                  "А ключи ты найдешь в соответствующих файлах.")

    else:
        message = input("\nВведи фразу, которую хочешь зашифровать: ")

        if cipher == 1:
            shift = input("\nВведи ключ (число): ")

            if shift.isnumeric():
                shift = int(shift)
            else:
                raise ValueError("Expected number")

            print(Caesar(shift).transform(message, 1))

        elif cipher == 2:
            key = input("\nВведи ключ: ")

            print(Vigenere(key).transform(message, 1))

        else:
            encrypted_message = Vernam().transform(message, 1)
            print(f"{encrypted_message[0]}\n"
                  f"key = {encrypted_message[1]}")


def decrypt(ans, cipher):
    if len(ans) != 0:
        if cipher == 1:
            shift = input("\nВведи ключ для файлов (число): ")

            if shift.isnumeric():
                shift = int(shift)
            else:
                raise ValueError("Expected number")

            for path in ans:
                with open(path, "r") as original, \
                        open(f"{os.path.splitext(path)[0]}_decrypted", "w") as decrypted:
                    decrypted.write(Caesar(shift).transform(original.read(), 2))

            print("\nВот как я могу!")

        elif cipher == 2:
            key = input("\nВведи ключ для файлов: ")
            for path in ans:
                with open(path, "r") as original, \
                        open(f"{os.path.splitext(path)[0]}_decrypted", "w") as decrypted:
                    decrypted.write(Vigenere(key).transform(original.read(), 2))

            print("\nВот как я могу!")

        else:
            print("\nЕсли я помогал тебе шифровать файлы, то информация про ключики "
                  "должна была остаться в моих файлах. Надеюсь, ты их не удалил))")
            for path in ans:
                with open(path, "r") as original, \
                        open(f"{os.path.splitext(path)[0]}_decrypted", "w") as decrypted, \
                        open(f"{os.path.dirname(path)}/key_for_file_{os.path.basename}.txt", "r") as key_file:
                    working_cipher = Vernam()
                    working_cipher.set_key(key_file.readline())
                    decrypted_message = working_cipher.transform(original.read(), 2)
                    decrypted.write(decrypted_message)

            print("\nВот как я могу!")

    else:
        message = input("\nВведи фразу, которую хочешь расшифровать: ")

        if cipher == 1:
            shift = input("\nВведи ключ (число): ")

            if shift.isnumeric():
                shift = int(shift)
            else:
                raise ValueError("Expected number")

            print(Caesar(shift).transform(message, 2))

        elif cipher == 2:
            key = input("\nВведи ключ: ")

            print(Vigenere(key).transform(message, 2))

        else:
            working_cipher = Vernam()
            working_cipher.set_key(input("\nВведи ключ: "))

            encrypted_message = working_cipher.transform(message, 2)
            print(encrypted_message)


start()
