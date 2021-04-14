# -*- coding: UTF-8 -*-

import SingleReplace
import ASCIIoffset
import tokenCrypt


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


def caseToken():
    tk = tokenCrypt.TokenEncryptor()
    while 1:
        opt = input("Option? Show token (S), encrypt (E), return (R), decrypt (else): ")
        if opt == "R":
            return
        elif opt == "S":
            tk.printToken()
        else:
            src = input("Please input string ori: ")
            print(tk.encrypt(src, opt == "E"))


if __name__ == '__main__':
    while 1:
        mode = input("Please select mode. 1 for ASCII offset, 2 for char replace, 3 for token: ")
        if mode == "1":
            caseASCIIoffset()
        elif mode == "2":
            caseSingleReplace()
        elif mode == "3":
            caseToken()