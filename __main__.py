from image import image
from PySide2.QtWidgets import *
from form import Ui_MainWindow
import sys
from variables import variables

class main:
    def __init__(self):
        self.im = None
        self.app = QApplication(sys.argv)
        self.Form = QWidget()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Form)
        self.ui.b_open.clicked.connect(self.b_open_clicked)
        self.ui.b_filter.clicked.connect(self.b_filter_clicked)
        self.v = variables()

    def b_open_clicked(self):
        filename = QFileDialog.getOpenFileName(caption="Открыть изображение", filter="Файлы изображений (*.jpg)")
        if filename != ('', ''):
            self.im = image(filename[0])
            self.output_image(self.im, 1)

    def b_filter_clicked(self):
        if (self.im == None):
            QMessageBox.critical(QWidget(), 'Ошибка', "Изображение для обработки не выбрано")
            return
        im2 = self.im.filter(self.v.get_filter_code(name=self.ui.cb_filter.currentText()))

        im2 = self.im.filter("INF")
        im2 = self.im.filter("IVF")
        im2 = self.im.filter("BNF")
        im2 = self.im.filter("BVF")
        im2 = self.im.filter("GNF")
        im2 = self.im.filter("GVF")
        #self.output_image(im2, 2)

    def output_image(self, im, num):
        if (num == 1):
            self.ui.label1.setPixmap(im.to_qpixmap())
        if (num == 2):
            self.ui.label2.setPixmap(im.to_qpixmap())

    def main(self):
        self.Form.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    main = main()
    main.main()




