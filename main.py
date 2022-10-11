from curses.ascii import isalpha
from pydoc import plain
import example

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

frequency = [[0 for i in range(26)]]

def printGuess():
    bestGuess = ""
    for i in range(len(frequency)):
        print(frequency[i])
        max = 0
        for j in range(len(frequency[i])):
            if frequency[i][j] > max:
                max = frequency[i][j]
        bestGuess += ALPHABET[j]
    print("================")
    print(bestGuess)
    print("================")

def decrypt(key, cipher_text):
    plain_text = ""
    for i in range (0, len(cipher_text)):
        if ord(key[i % len(key)]) <= ord(cipher_text[i]):
            # print(chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('A')), end="")
            character = chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('A'))
            # plain_text += chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('A'))
        elif ord(key[i % len(key)]) > ord(cipher_text[i]):
            # print(chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('Z') +1), end="")
            # plain_text += chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('Z') +1)
            character = chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('Z') +1)
        # else:
        #     print(chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('A')), end="")
        if character.isalpha(): plain_text += character
        else: return
    if "THE" in plain_text and "AND" in plain_text and "OF" in plain_text and "TO" in plain_text:
        for letter in range(len(key)):
            if letter >= len(frequency):
                frequency.append([0 for i in range(26)])
            frequency[letter][ord(key[letter]) - ord('A')] += 1
        printGuess()
        # print(plain_text)
        # print(key)

def printAllKLength(set, k):
 
    n = len(set) 
    printAllKLengthRec(set, "", n, k)

# def keyGenerator(set, prefix, n):
#     if n == 0:
#         print(prefix)
#         # return prefix
#     # for i in range(n):
#     for i in range(n):
#         newPrefix = prefix + set[i]
#         keyGenerator(set, newPrefix, n-1)

# def keyGuesser(length):
#     keyGenerator(ALPHABET, "", length)
def printAllKLengthRec(set, prefix, n, k):
     
    # Base case: k is 0,
    # print prefix
    if (k == 0) :
        print(prefix)
        # if prefix == "ALICE":
        #     print("ALICE FOUND")
        #     decrypt(prefix, example.cipher_text.replace(" ", ""))
        #     return
        decrypt(prefix, example.cipher_text.replace(" ", ""))
        return
 
    # One by one add all characters 
    # from set and recursively 
    # call for k equals to k-1
    for i in range(n):
 
        # Next character of input added
        newPrefix = prefix + set[i]
         
        # k is decreased, because 
        # we have added a new character
        printAllKLengthRec(set, newPrefix, n, k - 1)

def main():
    # print("Hello World!")
    # print(example.cipher_text)
    # cipher_text = example.cipher_text
    # cipher_text = cipher_text.replace(" ", "")
    # print(cipher_text)

    # decrypt("ALICE", cipher_text)
    # keyGuesser(3)
    for i in range(5): printAllKLength(ALPHABET, i+1)
    # printAllKLength(ALPHABET, 5)
    decrypt("ALICE", example.cipher_text.replace(" ", ""))
    # bestGuess = ""
    # for i in range(len(frequency)):
    #     print(frequency[i])
    #     max = 0
    #     for j in range(len(frequency[i])):
    #         if frequency[i][j] > max:
    #             max = frequency[i][j]
    #     bestGuess += ALPHABET[j]
    # print(bestGuess)

if __name__ == "__main__":
    main()