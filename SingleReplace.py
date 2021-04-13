# -*- coding: UTF-8 -*-

import random



class SingleReplaceEncryptor(object):

    dicEnc = dict()
    dicDec = dict()

    def __init__(self):

        oriAlphabet = [chr(i) for i in range(33, 127)]
        encAlphabet = oriAlphabet.copy()
        random.shuffle(encAlphabet)

        SingleReplaceEncryptor.dicEnc.clear()
        SingleReplaceEncryptor.dicDec.clear()

        for i in range(94):
            SingleReplaceEncryptor.dicEnc[oriAlphabet[i]] = encAlphabet[i]
            SingleReplaceEncryptor.dicDec[encAlphabet[i]] = oriAlphabet[i]

    def printDic(self):
        #print(SingleReplaceEncryptor.dicEnc)
        for key in SingleReplaceEncryptor.dicEnc.keys():
            print("{} -> {}".format(key, SingleReplaceEncryptor.dicEnc[key]))

    def convertChar(self, src: str, isEnc: bool) -> str:
        ret = ''
        if 33 <= ord(src) < 127:
            if isEnc:
                return SingleReplaceEncryptor.dicEnc[src]
            else:
                return SingleReplaceEncryptor.dicDec[src]
        else:
            return str

    def encrypt(self, src: str, isEnc: bool) -> str:
        ret = ''
        for ch in src:
            ret += SingleReplaceEncryptor.convertChar(self, ch, isEnc)
        return ret