import sys
import copy
import json

class Stack():
    count = 0
    # current = []
    def __init__(self, count = 0, json_data=None, stack=None):
        self.stack = stack
        self.version = []
        self.count = count
        self.json_data = json_data

    # def push(self, item):
    #     self.stack.append(item)
    #     self.save_version()
    #     self.json_data = json.dumps(self.stack, indent=4)

    def push2(self, current, item):
        self.current = current
        if self.current is None:
            self.current = []
            self.current.append(item)
        else:
            self.current.append(item)
        self.save_version()
        self.json_data = json.dumps(self.current, indent=4)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            remove = self.stack.pop()
            self.save_version()
            self.json_data = json.dumps(self.stack, indent=4)
            return remove

    def save_version(self):
        self.version.append(self.current.copy())

    def save_version_to_db(self):
        self.json_data = json.dumps(self.version, indent=4)

    # def print(self):
    #     self.count = 0
    #     for i in self.version:
    #         print(i, self.count, 'version')
    #         self.count += 1

    # def selective_print(self):
    #     print("please choose a version beginning the null and ending len-1")
    #     self.choose = int(input('choose the version: '))
    #     if self.choose >= 0 and self.choose < self.count:
    #         print(self.version[self.choose])
    #         print("what you want to do with this version?")
    #         self.current = list(self.version[self.choose])
    #
    #         self.select = str(input('enter you want to do: ')).lower()
    #
    #         if self.select == 'pop':
    #             self.current.pop()
    #             self.version.append(self.current)
    #             self.count += 1
    #             print(self.current)
    #
    #         elif self.select == 'push':
    #             self.item = int(input("enter: "))
    #             self.current.append(self.item)
    #             self.version.append(self.current)
    #             self.count += 1
    #             print(self.current)
    #     else:
    #         print('error')

    def get_json_data(self):
        return self.json_data

    def get_stack(self):
        return self.stack
