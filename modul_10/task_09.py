from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return [key for key, value_current in self.data.items() if value == value_current]
        