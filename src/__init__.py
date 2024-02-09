try:
    from PyQt5 import QtWidgets as qtw
    from PyQt5 import QtCore as qtc
    from PyQt5 import QtGui as qtg
    import sys
    import os
except ImportError as ie:
    print(ie)
except ImportWarning as iw:
    print(iw)
