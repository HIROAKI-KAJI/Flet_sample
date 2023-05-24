import flet as ft

class GreeterControl(ft.UserControl):
    def build(self):
        container = ft.Container(
            content= ft.Row(
            controls = [
            ft.Text(value="Hello"),
            ]
            )
        )
        return container

def main(page):
    
    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.on_keyboard_event = on_keyboard

    page.window_full_screen = True

    page.add(GreeterControl())

if __name__ == "__main__":
    
    ft.app(target=main)


