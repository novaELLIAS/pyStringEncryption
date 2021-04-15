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
            self.token = util.generate_random_str(opt)
            self.startPos = random.randint(0, 25)
            print("token: ", end="")
            print(self.token)
            print("startPos: ", end="")
            print(self.startPos)
        else:
            opt = input("Input or read from file? (I/else): ")
            if opt == "I":
                self.token = list(input("Please input your token: "))
                self.startPos = int(input("Please input your startPos: "))
            else:
                with open("./src/token.txt", "r") as file:
                    self.token = list(file.readline())
                    self.token = self.token[:-1]
                    print(self.token)
                    self.startPos = int(file.readline())
                    print(self.startPos)
        self.saveTokenToFile()
        self.token = util.remove_same_str(self.token)
        dicEncTmp = list()
        for i in self.token:
            dicEncTmp.append(ord(i))
        for i in range(ord("a"), ord("z") + 1):
            if chr(i) not in self.token:
                dicEncTmp.append(i)
        for i in range(len(dicEncTmp)):
            self.dicEnc[chr(ord("a") + (i + self.startPos) % 26)] = chr(dicEncTmp[i])
            self.dicDec[chr(dicEncTmp[i])] = chr(ord("a") + (i + self.startPos) % 26)

    def saveTokenToFile(self):
        with open("./src/token.txt", "w") as file:
            file.write("".join(self.token))
            file.write("\n")
            file.write(str(self.startPos))
            file.write("\n")

    def printToken(self):
        print("token: ", end="")
        print(self.token)
        print("startPos: ", end="")
        print(self.startPos)

    def convertChar(self, src: str, isEnc: bool) -> str:
        if ord("a") <= ord(src) <= ord("z"):
            if isEnc:
                return self.dicEnc[src]
            else:
                return self.dicDec[src]
        else:
            return src

    def encrypt(self, src: str, isEnc: bool) -> str:
        ret = ""
        if src == "":
            src = util.read_str_to_file("./src/text.in")
            print(src)
        for ch in src:
            ret += self.convertChar(ch, isEnc)
        util.write_str_to_file(ret, "./src/text.out")
        return ret
