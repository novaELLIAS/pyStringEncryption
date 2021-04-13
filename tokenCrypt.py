# -*- coding: UTF-8 -*-

import utility as util
import random


class TokenEncryptor:
    token = list()
    startPos = 0
    dicEnc = dict()
    dicDec = dict()

    def __init__(self):
        opt = input("Generate or input token? (G/else): ")
        if opt == "G":
            opt = int(input("Len: "))
            TokenEncryptor.token = util.generate_random_str(opt)
            TokenEncryptor.startPos = random.randint(0, 25)
            print("token: ", end="")
            print(TokenEncryptor.token)
            print("startPos: ", end="")
            print(TokenEncryptor.startPos)
        else:
            TokenEncryptor.token = list(input("Please input your token: "))
            TokenEncryptor.startPos = int(input("Please input your startPos: "))
        TokenEncryptor.token = util.remove_same_str(TokenEncryptor.token)
        dicEncTmp = list()
        for i in TokenEncryptor.token:
            dicEncTmp.append(ord(i))
        print(dicEncTmp)
        for i in range(ord("a"), ord("z") + 1):
            if chr(i) not in TokenEncryptor.token:
                dicEncTmp.append(i)
        print(dicEncTmp)
        for i in range(len(dicEncTmp)):
            TokenEncryptor.dicEnc[chr(ord("a") + (i + TokenEncryptor.startPos) % 26)] = chr(dicEncTmp[i])
            TokenEncryptor.dicDec[chr(dicEncTmp[i])] = chr(ord("a") + (i + TokenEncryptor.startPos) % 26)
        print(TokenEncryptor.dicEnc)
        print(TokenEncryptor.dicDec)

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
        for ch in src:
            ret += TokenEncryptor.convertChar(self, ch, isEnc)
        return ret