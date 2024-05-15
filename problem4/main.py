def ubah_huruf(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pattern = ""
    for char in sentence:
        if char.isalpha():
            index = (alphabet.index(char.upper()) + 10) % 26
            encrypted_char = alphabet[index]
            if char.islower():
                pattern += encrypted_char.lower()
            else:
                pattern += encrypted_char
        else:
            pattern += char
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB