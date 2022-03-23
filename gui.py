import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from facade import Facade


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi('forms/MainWindow.ui', self)
        self.facade = Facade()
        self.btn_open_add.clicked.connect(lambda: self.add_elem())
        self.btn_delete.clicked.connect(lambda: self.delete_elem_select())
        self.comboBox.addItems(self.facade.get_id())
        self.build()
        self.comboBox.currentIndexChanged.connect(lambda: self.select())

    def select(self):
        id = self.comboBox.currentText()
        self.list = self.facade.get_select(id)
        self.build_select()

    def select_id(self):
        id = self.comboBox.currentText()
        self.current = self.facade.get_select(id)
        return self.current

    def delete_elem(self):
        self.facade.pop()
        self.build_CB()
        self.build()

    def add_elem(self):
        self.ui1 = InsertWidget(self)
        self.ui1.show()

    def build_select(self):
        '''
        когда вызывается, сколько раз вызывается и что должна делать
        что принимает (в данном случае ничего)
        :return: что возвращает (None)
        '''
        self.listWidget.clear()
        strin = '123'
        if type(self.list) == type(strin): # если вернуло строку, а не список, тогда делаем из строки список
            self.list = [self.list]

        if self.list != None:
            self.listWidget.addItems(self.list) # принимает список строк

    def build(self):
        self.list = self.facade.get()
        self.listWidget.clear()
        if self.list != None:
            self.listWidget.addItems(self.list)

    def build_CB(self):
        self.list_id = self.facade.get_id()
        self.comboBox.clear()
        if self.comboBox != None:
            self.comboBox.addItems(self.list_id)


class InsertWidget(QtWidgets.QWidget):
    def __init__(self, link=None):
        self.link = link
        super(InsertWidget, self).__init__()
        self.initUI = self.initUI()

    def initUI(self):
        self.ui1 = uic.loadUi('forms/InsertWidget.ui', self)
        self.btn_add.clicked.connect(self.on_click)

    def on_click(self):
        self.current = self.link.select_id()
        self.data = int(self.lineEdit.text())
        self.link.facade.push(self.current, self.data)
        print("Вы ввели: ", self.data)
        self.label_info.setText(f"Вы ввели: {self.data}")
        self.link.build_CB()
        self.link.build()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())