import example

def decrypt(key, cipher_text):
    for i in range (0, len(cipher_text)):
        if ord(key[i % len(key)]) <= ord(cipher_text[i]):
            print(chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('A')), end="")
        elif ord(key[i % len(key)]) > ord(cipher_text[i]):
            print(chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('Z') +1), end="")
        # else:
        #     print(chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('A')), end="")

def main():
    # print("Hello World!")
    # print(example.cipher_text)
    cipher_text = example.cipher_text
    cipher_text = cipher_text.replace(" ", "")
    print(cipher_text)

    decrypt("ALICE", cipher_text)

if __name__ == "__main__":
    main()