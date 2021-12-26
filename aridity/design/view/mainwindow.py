'''

'''

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from .mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    '''
    
    '''

    def __init__(self):
        '''
        
        '''
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(':/edit.ico'))
