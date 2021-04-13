# -*- coding: UTF-8 -*-

import SingleReplace


def caseSingleReplace():
    srEncryptor = SingleReplace.SingleReplaceEncryptor()
    while 1:
        opt = input("Option? Show dic (S), encrypt (E), decrypt (else): ")
        if opt == "S":
            srEncryptor.printDic()
        else:
            src = input("Please input string ori: ")
            print(srEncryptor.encrypt(src, opt == "E"))


if __name__ == '__main__':
    caseSingleReplace()
