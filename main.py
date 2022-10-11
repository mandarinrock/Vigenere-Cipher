
# cipher_text = "TSMVM MPPCW CZUGX HPECP RFAUE IOBQW PPIMS FXIPC TSQPK SZNUL OPACR DDPKT SLVFW ELTKR GHIZS FNIDF ARMUE NOSKR GDIPH WSGVL EDMCM SMWKP IYOJS TLVFA HPBJI RAQIW HLDGA IYOUX"
cipher_text = "TSMVMMPPCWCZUGXHPECPRFAUEIOBQWPPIMSFXIPCTSQPKSZNULOPACRDDPKTSLVFWELTKRGHIZSFNIDFARMUENOSKRGDIPHWSGVLEDMCMSMWKPIYOJSTLVFAHPBJIRAQIWHLDGAIYOUX"

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frequency = [[0 for i in range(26)]]
savedBest = ""

def getPlainText(cipher_text, key):
    plain_text = ""
    for i in range (0, len(cipher_text)):
        if ord(key[i % len(key)]) <= ord(cipher_text[i]):
            character = chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('A'))
        elif ord(key[i % len(key)]) > ord(cipher_text[i]):
            character = chr(ord(cipher_text[i]) - ord(key[i % len(key)]) + ord('Z') +1)
        if character.isalpha(): plain_text += character
        else: return
    return plain_text

def decrypt(key, cipher_text):
    global savedBest
    plain_text = getPlainText(cipher_text, key)
    if "THE" in plain_text and "AND" in plain_text and "OF" in plain_text and "TO" in plain_text:
        for letter in range(len(key)):
            if letter >= len(frequency):
                frequency.append([0 for i in range(26)])
            frequency[letter][ord(key[letter]) - ord('A')] += 1
        bestGuess = ""
        for i in range(len(frequency)):
            max = 0
            for j in range(len(frequency[i])):
                if frequency[i][j] > max:
                    max = frequency[i][j]
                    bestLetter = j
            bestGuess += ALPHABET[bestLetter]
        if bestGuess != savedBest:
            output = "Key: " + bestGuess + "\nPlain_text: " + getPlainText(cipher_text, bestGuess)
            f = open("guess.txt", "w")
            f.write(output)
            print(output)
            f.close()
            savedBest = bestGuess


def crackKey(combination, length):
    if length == 0:
        decrypt(combination, cipher_text.replace(" ", ""))
        return
    for i in range(len(ALPHABET)): crackKey(combination + ALPHABET[i], length - 1)

def main():
    for i in range(6): crackKey("", i+1)

if __name__ == "__main__":
    main()