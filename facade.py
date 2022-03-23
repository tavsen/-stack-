from database import Database
from stack import Stack

class Facade:
    """
    Класс фасада
    """
    def __init__(self):
        """
        Создание объекта базы данных, структуры данных.
        """
        self.DB = Database()
        list = []
        if self.DB.lastVersion() != None:
            #print(self.DB.lastVersion()[0][1:-1].split(','))
            nums = self.DB.lastVersion()[0][1:-1].split(',')
            if nums != '':
                for num in nums:
                    list.append(int(num))

        # print(list)
        self.S = Stack(stack=list)
        self.DB.CreateTable()

    def save(self):
        data = self.S.get_json_data()
        self.DB.Insert_in_Table(data)
        self.S.version.clear()

    def push(self, current, data):
        self.S.push2(current, data)
        self.save()

    def pop(self):
        self.S.pop()
        self.save()

    def push_select(self, data):
        self.S.push_select(data)
        self.save()

    def pop_select(self):
        self.S.pop_select()
        self.save()

    def read(self):
        data = self.S.get_json_data()
        self.DB.ReadTable()

    def get(self):
        version = self.DB.lastVersion()
        # print('vers', version)
        return version

    def get_stack(self):
        return self.S.get_stack()

    def get_id(self):
        list_id = self.DB.id()
        # print('id', list_id)
        return list_id

    def get_lastID(self):
        lastID = self.DB.lastID()
        return lastID

    def get_select(self, id):
        version = self.DB.select(id)
        print('vers_select', version)
        return version

    #def print_versions(self):
    #    self.S.print()

# if __name__ == '__main__':
#    pattern = Facade()
#
#    pattern.push(24)
#    pattern.push(123)
#    pattern.push(321)
#    pattern.push(65)
#    pattern.push(388)
#    pattern.pop()
#    pattern.pop()
#    pattern.push(5)
#
#    pattern.read()
#    pattern.get_select(2)