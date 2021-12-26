from PySide6.QtWidgets import QWidget
from .imagecuttingpanel_ui import Ui_ImageCuttingPanel

class ImageCuttingPanel(QWidget):
    '''
    
    '''

    def __init__(self):
        super().__init__()
        self.ui = Ui_ImageCuttingPanel()
        self.ui.setupUi(self)
        