import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import st
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
)


def initializeModel(model):
    #model.setTable('student')
    #model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    #model.select()
    #model.setHeaderData(0, QtCore.Qt.Horizontal, "student_id")
    #model.setHeaderData(1, QtCore.Qt.Horizontal, "ticket")
    #model.setHeaderData(2, QtCore.Qt.Horizontal, "fio")
    model.setTable("student")
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.setHeaderData(0, Qt.Horizontal, "student_id")
    model.setHeaderData(1, Qt.Horizontal, "ticket")
    model.setHeaderData(2, Qt.Horizontal, "fio")
    model.setHeaderData(3, Qt.Horizontal, "kurs")
    model.select()
    # Set up the view
   # view = QTableView()
   # view.setModel(model)
   # view.resizeColumnsToContents()


def createView(title, model):
    view =QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


def addrow():
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)


def findrow(i):
    delrow = i.row()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('aq.db3')
    model = QtSql.QSqlTableModel()
    delrow = -1
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    button = QtWidgets.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtWidgets.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())
