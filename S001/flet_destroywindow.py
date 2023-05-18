import flet as ft

def main(page: ft.Page):
    page.title = "MyApp"
    def button_clicked(e):
        
        page.window_close()

    b = ft.ElevatedButton("Button with 'click' event", on_click=button_clicked, data=0)
    
    page.window_full_screen = True
    page.add(b)
    return page
ft.app(target=main)