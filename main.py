# -*- coding: UTF-8 -*-

import utility
import SingleReplace
import ASCIIoffset


def caseASCIIoffset():
    offset = int(input("Please input your offset: "))
    ASCIIencryptor = ASCIIoffset.ASCIIoffsetEncryptor(offset)
    while 1:
        opt = input("Option? encrypt (E), return (R), decrypt (else): ")
        if opt == "R":
            return
        src = input("Please input string ori: ")
        print(ASCIIencryptor.encrypt(src, opt == "E"))

def caseSingleReplace():
    srEncryptor = SingleReplace.SingleReplaceEncryptor()
    while 1:
        opt = input("Option? Show dic (S), encrypt (E), return (R), decrypt (else): ")
        if opt == "R":
            return
        elif opt == "S":
            srEncryptor.printDic()
        else:
            src = input("Please input string ori: ")
            print(srEncryptor.encrypt(src, opt == "E"))


if __name__ == '__main__':
    while 1:
        mode = input("Please select mode. 1 for ASCII offset, 2 for char replace: ")
        if mode == "1":
            caseASCIIoffset()
        elif mode == "2":
            caseSingleReplace()