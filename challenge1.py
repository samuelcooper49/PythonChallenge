#!/usr/bin/env python3

# Solution to Python Challenge Part 1: http://www.pythonchallenge.com/pc/def/map.html

MAP={
    "a" : "c",
    "b" : "d",
    "c" : "e",
    "d" : "f",
    "e" : "g",
    "f" : "h",
    "g" : "i",
    "h" : "j",
    "i" : "k",
    "j" : "l",
    "k" : "m",
    "l" : "n",
    "m" : "o",
    "n" : "p",
    "o" : "q",
    "p" : "r",
    "q" : "s",
    "r" : "t",
    "s" : "u",
    "t" : "v",
    "u" : "w",
    "v" : "x",
    "w" : "y",
    "x" : "z",
    "y" : "a",
    "z" : "b",
}

def decipher(cipher_text):
    """
    decipher input cipher_text using a simple letter exhange mapping
    inputs:
       cipher_text : string, ciphered text
    Outputs:
       str : plain text
    Failure:
       Exception
    """
    plain_text = ""
    for letter in cipher_text:
        if letter in MAP:
            plain_text += MAP[letter]
        else:
            plain_text += letter
    return(plain_text)

if __name__ == "__main__":
    text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
    print(decipher(text))
