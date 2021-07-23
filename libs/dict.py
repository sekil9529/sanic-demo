# coding: utf-8


class ExtDict(dict):
    """扩展字典"""

    def __setattr__(self, key, value):
        """ Implement self.key = value """
        self[key] = value

    def __getattr__(self, item):
        """ Implement self.key """
        if item not in self:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")
        return self[item]
