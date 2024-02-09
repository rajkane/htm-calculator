from src import *
from src.controller.main_controller import MainWindow


def run():
    app = qtw.QApplication(sys.argv)
    app.setApplicationName("Homogeneous Transformation - Calculator")
    app.setWindowIcon(qtg.QIcon(""))
    app.setApplicationVersion("1.0.1")
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
