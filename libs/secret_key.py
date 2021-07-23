# coding: utf-8

import string
import random


def make_secret_key(k=42):
    origin_str = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choices(origin_str, k=k))
