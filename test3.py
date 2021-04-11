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
        headimage = QPixmap('isaac.png')
        self.headimage.setPixmap(headimage)

        self.itemimage = QLabel('ItemImage', self)
        self.itemid = QLabel(self.item.itemid, self)
        self.itemquote = QLabel(self.item.quote, self)
        self.itemdescription = QLabel(self.item.description, self)

        self.searchbutton = QPushButton('Search', self)
        self.searchbutton.clicked.connect(self.search)

        self.searchcontent = QLineEdit('', self)
        self.searchcontent.setFocus()

        vboxleft = QVBoxLayout()
        vboxleft.addStretch(1)
        vboxleft.addWidget(self.headimage)
        vboxleft.addStretch(1)
        vboxleft.addWidget(self.searchcontent)
        vboxleft.addStretch(1)
        vboxleft.addWidget(self.searchbutton)
        vboxleft.addStretch(1)

        vboxright = QVBoxLayout()
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemimage)
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemid)
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemquote)
        vboxright.addStretch(1)
        vboxright.addWidget(self.itemdescription)
        vboxright.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vboxleft)
        hbox.addStretch(1)
        hbox.addLayout(vboxright)
        hbox.addStretch(1)

        self.setLayout(hbox)

    def search(self):
        self.item.search(str(self.searchcontent.text()))
        self.refresh()

    def refresh(self):
        Image.open(requests.get(self.item.imageurl, stream=True).raw).save(
            'temporaryimage.png')
        itemimage = QPixmap('temporaryimage.png')
        self.itemimage.setPixmap(itemimage)
        self.itemid.setText(self.item.itemid)
        self.itemquote.setText(self.item.quote)
        self.itemdescription.setText(self.item.description)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = searchitem()
    ex.show()
    sys.exit(app.exec_())
