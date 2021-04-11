# GUI Framework
# duck typing
import abc


class UIControl(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


class TextButton(UIControl):
    def draw(self):
        print("Drawing a textbox")


class CheckBox(UIControl):
    def draw(self):
        print("Drawing a checkbox")


class RadioButton(UIControl):
    def draw(self):
        print("Drawing a radiobutton")


def draw_widgets(widget: UIControl):
    widget.draw()


### Klient

draw_widgets(TextButton())
draw_widgets(CheckBox())
draw_widgets(RadioButton())