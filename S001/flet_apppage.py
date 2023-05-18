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