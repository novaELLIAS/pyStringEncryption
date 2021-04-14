# -*- coding: UTF-8 -*-

import utility as util
import random


class TokenEncryptor:
    token = list()
    startPos = 0
    dicEnc = dict()
    dicDec = dict()

    def __init__(self):
        opt = input("Generate or already have token? (G/else): ")
        if opt == "G":
            opt = int(input("Len: "))
            TokenEncryptor.token = util.generate_random_str(opt)
            TokenEncryptor.startPos = random.randint(0, 25)
            print("token: ", end="")
            print(TokenEncryptor.token)
            print("startPos: ", end="")
            print(TokenEncryptor.startPos)
        else:
            opt = input("Input or read from file? (I/else): ")
            if opt == "I":
                TokenEncryptor.token = list(input("Please input your token: "))
                TokenEncryptor.startPos = int(input("Please input your startPos: "))
            else:
                with open("./src/token.txt", "r") as file:
                    TokenEncryptor.token = list(file.readline())
                    TokenEncryptor.token = TokenEncryptor.token[:-1]
                    print(TokenEncryptor.token)
                    TokenEncryptor.startPos = int(file.readline())
                    print(TokenEncryptor.startPos)
        TokenEncryptor.saveTokenToFile(self)
        TokenEncryptor.token = util.remove_same_str(TokenEncryptor.token)
        dicEncTmp = list()
        for i in TokenEncryptor.token:
            dicEncTmp.append(ord(i))
        for i in range(ord("a"), ord("z") + 1):
            if chr(i) not in TokenEncryptor.token:
                dicEncTmp.append(i)
        for i in range(len(dicEncTmp)):
            TokenEncryptor.dicEnc[chr(ord("a") + (i + TokenEncryptor.startPos) % 26)] = chr(dicEncTmp[i])
            TokenEncryptor.dicDec[chr(dicEncTmp[i])] = chr(ord("a") + (i + TokenEncryptor.startPos) % 26)

    def saveTokenToFile(self):
        with open("./src/token.txt", "w") as file:
            file.write("".join(TokenEncryptor.token))
            file.write("\n")
            file.write(str(TokenEncryptor.startPos))
            file.write("\n")

    def printToken(self):
        print("token: ", end="")
        print(TokenEncryptor.token)
        print("startPos: ", end="")
        print(TokenEncryptor.startPos)

    def convertChar(self, src: str, isEnc: bool) -> str:
        if ord("a") <= ord(src) <= ord("z"):
            if isEnc:
                return TokenEncryptor.dicEnc[src]
            else:
                return TokenEncryptor.dicDec[src]
        else:
            return src

    def encrypt(self, src: str, isEnc: bool) -> str:
        ret = ""
        if src == "":
            src = util.read_str_to_file("./src/text.in")
            print(src)
        for ch in src:
            ret += TokenEncryptor.convertChar(self, ch, isEnc)
        util.write_str_to_file(ret, "./src/text.out")
        return ret