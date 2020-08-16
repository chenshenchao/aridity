import glooey
from .label import MyLabel


class MyButton(glooey.Button):
    '''
    开始面板上的按钮。
    '''

    Foreground = MyLabel
    custom_alignment = 'fill'

    class Base(glooey.Background):
        custom_color = '#204a87'

    class Over(glooey.Background):
        custom_color = '#3465a4'

    class Down(glooey.Background):
        custom_color = '#729fcff'

    def __init__(self, text, callback):
        super().__init__(text)
        self.callback = callback

    def on_click(self, widget):
        if callable(self.callback):
            self.callback()
        elif isinstance(self.callback, str):
            print(self.callback)
