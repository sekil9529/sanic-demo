# coding: utf-8

from __future__ import print_function
from __future__ import unicode_literals

import importlib

try:
    ConfigParser = importlib.import_module('ConfigParser').ConfigParser  # py2
except (ModuleNotFoundError, Exception):
    # ConfigParser = importlib.import_module('configparser').ConfigParser  # py3
    ConfigParser = importlib.import_module('configparser').RawConfigParser  # py3，可匹配特殊字符


class Config(object):
    """配置文件解析"""

    def __init__(self, file, section=None, encoding='utf-8'):
        self._section = section
        self._cnf = ConfigParser()
        self._cnf.read(file, encoding=encoding)

    def format(self):
        if self._section is None:
            return {key: dict(self._cnf.items(key)) for key in self._cnf.sections()}
        else:
            return dict(self._cnf.items(self._section))
