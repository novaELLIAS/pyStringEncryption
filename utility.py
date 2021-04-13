# -*- coding: UTF-8 -*-

import random as random


def generate_random_str(len: int) -> list:
    ret = list()
    for i in range(len):
        ret.append(chr(random.randint(ord('a'), ord('z'))))
    return ret

def remove_same_str(src: list) -> list:
    ret = list()
    for i in src:
        if i not in ret:
            ret.append(i)
    return ret