from src import *
from src.view.htm import Ui_MainWindow
from src.model.htm_model import HomogeneousTransformation


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.htm = HomogeneousTransformation()
        self.__actions()

    def __actions(self):
        self.dsb_x.valueChanged.connect(self.__calcul)
        self.dsb_y.valueChanged.connect(self.__calcul)
        self.dsb_z.valueChanged.connect(self.__calcul)
        self.dial_alpha.valueChanged.connect(self.__calcul)
        self.dial_beta.valueChanged.connect(self.__calcul)
        self.dial_gamma.valueChanged.connect(self.__calcul)
        self.dsb_delta_x.valueChanged.connect(self.__calcul)
        self.dsb_delta_y.valueChanged.connect(self.__calcul)
        self.dsb_delta_z.valueChanged.connect(self.__calcul)

    def __calcul(self):
        self.htm.set_point(
            x=self.dsb_x.value(),
            y=self.dsb_y.value(),
            z=self.dsb_z.value()
        )
        self.htm.set_transform_matrix(
            alpha=self.lcd_alpha.value(),
            beta=self.lcd_beta.value(),
            gamma=self.lcd_gamma.value(),
            x_delta=self.dsb_delta_x.value(),
            y_delta=self.dsb_delta_y.value(),
            z_delta=self.dsb_delta_z.value()
        )
        self.dsb_x_result.setValue(self.htm.get_result()[0])
        self.dsb_y_result.setValue(self.htm.get_result()[1])
        self.dsb_z_result.setValue(self.htm.get_result()[2])


