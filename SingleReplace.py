# -*- coding: UTF-8 -*-

import random


class SingleReplaceEncryptor(object):

    dicEnc = dict()
    dicDec = dict()

    def __init__(self):

        oriAlphabet = [chr(i) for i in range(33, 127)]
        encAlphabet = oriAlphabet.copy()
        random.shuffle(encAlphabet)

        self.dicEnc.clear()
        self.dicDec.clear()

        for i in range(len(oriAlphabet)):
            self.dicEnc[oriAlphabet[i]] = encAlphabet[i]
            self.dicDec[encAlphabet[i]] = oriAlphabet[i]

    def printDic(self):
        for key in self.dicEnc.keys():
            print("{} -> {}".format(key, self.dicEnc[key]))

    def convertChar(self, src: str, isEnc: bool) -> str:
        if 33 <= ord(src) < 127:
            if isEnc:
                return self.dicEnc[src]
            else:
                return self.dicDec[src]
        else:
            return str

    def encrypt(self, src: str, isEnc: bool) -> str:
        ret = ''
        for ch in src:
            ret += self.convertChar(ch, isEnc)
        return ret
