'''
编辑器
'''

import sys
from PySide6.QtWidgets import QApplication
from aridity.design.view.mainwindow import MainWindow

def main():
    '''
    
    '''

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()

if __name__ == '__main__':
    main()
