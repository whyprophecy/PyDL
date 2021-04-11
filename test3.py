from test2 import *
import sys
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel


class searchitem(QWidget):
    def __init__(self):
        super().__init__()
        self.item = item()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Issac Item Searcher')

        self.headimage = QLabel(self)
        Image.open(requests.get('https://static.wikia.nocookie.net/bindingofisaacre_gamepedia/images/e/e5/Character_Isaac_appearance.png/revision/latest/scale-to-width-down/84?cb=20150104210047', stream=True).raw).save(
            'temporaryimage1.png')
        headimage = QPixmap('temporaryimage1.png')
        self.headimage.setPixmap(headimage)

        self.itemimage = QLabel('ItemImage', self)
        self.itemname = QLabel(self.item.name, self)
        self.itemid = QLabel(self.item.itemid, self)
        self.itemquote = QLabel(self.item.quote, self)
        self.itemdescription = QLabel(self.item.description, self)

        self.searchbutton = QPushButton('Search', self)
        self.searchbutton.clicked.connect(self.search)

        self.searchcontent = QLineEdit('', self)
        self.searchcontent.setFocus()

        vboxleft = QVBoxLayout()
        vboxleft.addStretch(2)
        vboxleft.addWidget(self.headimage)
        vboxleft.addStretch(1)
        vboxleft.addWidget(self.searchcontent)
        vboxleft.addStretch(1)
        vboxleft.addWidget(self.searchbutton)
        vboxleft.addStretch(2)

        vboxright = QVBoxLayout()
        vboxright.addStretch(2)
        vboxright.addWidget(self.itemimage)
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemname)
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemid)
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemquote)
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemdescription)
        vboxright.addStretch(2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vboxleft)
        hbox.addStretch(2)
        hbox.addLayout(vboxright)
        hbox.addStretch(1)

        self.setLayout(hbox)

    def search(self):
        self.item.search(str(self.searchcontent.text()))
        self.refresh()

    def refresh(self):
        Image.open(requests.get(self.item.imageurl, stream=True).raw).save(
            'temporaryimage2.png')
        itemimage = QPixmap('temporaryimage2.png')
        self.itemimage.setPixmap(itemimage)
        self.itemname.setText('Name: '+self.item.name)
        self.itemid.setText('ID: '+self.item.itemid)
        self.itemquote.setText('Quote: '+self.item.quote)
        self.itemdescription.setText('Description:\n'+self.item.description)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = searchitem()
    ex.show()
    sys.exit(app.exec_())
