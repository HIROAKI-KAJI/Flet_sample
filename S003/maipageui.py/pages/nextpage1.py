import flet as ft
from typing import Union,TypeVar

T = TypeVar('T')

class npage1(ft.View):
    def __init__(self):
          super().__init__()

    def __call__(self,route : T):

        Control = [
            ft.Column(
                expand = True,
                
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("sample"),
                    ft.Container(
                        width=500,
                        height=500,
                        bgcolor=ft.colors.RED_200,
                        padding = 200,
                        content= ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Text(value=str(0)),
                                    alignment=ft.alignment.center,
                                    width=100,
                                    height=100,
                                    bgcolor=ft.colors.AMBER,
                                    border_radius=ft.border_radius.all(5),
                                )
                            ]
                        )
                    )
                ]
            )
        ]

        return ft.View(route,Control,horizontal_alignment = ft.CrossAxisAlignment.CENTER)



def main(page: ft.Page):

    def create_view(route):
        page1 = npage1()

        return page1(route)
    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        if troute.match("/"):
            page.views.clear()
            page.views.append(
                create_view("/"))
        page.update()

    # ルート変更時のロジック設定
    page.on_route_change = route_change

    def view_pop(handler):
        page.views.pop()  # 1つ前に戻る
        page.go("/back")
        # page.update()
        # update() だと route が変更されない。
        # そうなると1つ戻ってまた進むことができなくなるので go("/back") で回避。不具合？

    # 戻る時のロジック設定
    page.on_view_pop = view_pop

    # Page レイアウト
    page.title = "Navigation and routing"
    # 初期表示
    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)
