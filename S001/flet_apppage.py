import flet as ft
from typing import TypeVar, Generic, Union, Callable

T = TypeVar('T')

#状態管理クラス。bind()で状態変更時に呼び出したい処理を登録できる。
class State(Generic[T]):
    def __init__(self, value: T):
        self._value = value
        self._observers: list[Callable] = []

    def get(self):
        return self._value #値の参照はここから

    def set(self, new_value: T):
        if self._value != new_value:
            self._value = new_value #新しい値をセット
            for observer in self._observers: observer() #変更時に各observerに通知する

    def bind(self, observer):
        self._observers.append(observer)# 変更時に呼び出す為のリストに登録


text = State('')
text.set('12345')
print(text.get()) # -> 12345

def on_change_handler():
    print(text.get())
text.bind(on_change_handler)

class GreeterControl(ft.UserControl):
    def build(self):
        container = ft.Container(
            content= ft.Row(
            controls = [
            ft.Text(value="Hello"),
            ft.TextField(on_change=lambda e: text.set(e.control.value)),
            ]
            )
        )
        return container
    
def main(page: ft.Page):
    page.title = "MyApp"
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Escape":
            page.window_close()
        if e.key == "F11":
            page.window_full_screen = not page.window_full_screen
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
            
        )

    page.on_keyboard_event = on_keyboard
    def button_clicked(e):
        
        page.window_close()

    b = ft.ElevatedButton("Button with 'click' event", on_click=button_clicked, data=0)
    
    
    page.add(GreeterControl())
    return page
ft.app(target=main)