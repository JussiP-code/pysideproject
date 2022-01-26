import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from quiz_ui import Ui_MainWindow


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.aseta_nappien_tekstit([
			"Eka",
			"Toka",
			"Kolmas",
			"Neljäs",
		])

	def aseta_nappien_tekstit(self, tekstit):
		(t1, t2, t3, t4) = tekstit
		self.ui.button1.setText(t1)
		self.ui.button2.setText(t2)
		self.ui.button3.setText(t3)
		self.ui.button4.setText(t4)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	
	window = MainWindow()
	window.show()

	sys.exit(app.exec())