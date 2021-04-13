# -*- coding: UTF-8 -*-


class ASCIIoffsetEncryptor:

    offset = 0

    def __init__(self, offset: int):
        ASCIIoffsetEncryptor.offset = offset

    def convertChar(self, src: str, flag: bool) -> str:
        if 33 <= ord(src) <= 126:
            if flag:
                return chr(33 + (ord(src) - 33 + ASCIIoffsetEncryptor.offset) % 94)
            else:
                return chr(33 + (ord(src) - 33 - ASCIIoffsetEncryptor.offset + 94) % 94)
        else:
            return src

    def encrypt(self, src: str, isEnc: bool) -> str:
        ret = ''
        for ch in src:
            ret += ASCIIoffsetEncryptor.convertChar(self, ch, isEnc)
        return ret