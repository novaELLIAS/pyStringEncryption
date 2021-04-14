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


def write_str_to_file(src: str, tar: str):
    with open(tar, "w") as file:
        file.write(src)
        file.write("\n")


def read_str_to_file(tar: str) -> str:
    with open(tar, "r") as file:
        return file.read().strip().replace('\n', '').replace('\t', '').replace('\r', '').strip()
