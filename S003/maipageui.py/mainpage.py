import flet as ft


def main(page: ft.Page):

    def create_view(route: str, title: str, next_route1: str, next_route2: str, color: ft.colors):
        return ft.View(route, [
            ft.AppBar(title=ft.Text(title), bgcolor=color),
            ft.TextField(value=title),
            ft.ElevatedButton(
                f"{next_route1} へ移動", on_click=lambda _: page.go(next_route1)),
            ft.ElevatedButton(
                f"{next_route2} を被せる", on_click=lambda _: page.go(next_route2)),
            ft.ElevatedButton(
                f"Root に移動", on_click=lambda _: page.go("/")),
        ])

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        if troute.match("/"):
            page.views.clear()
            page.views.append(
                create_view("/", "Root", "/view1", "/cover/view1", ft.colors.BLUE))
        elif troute.match("/view1"):
            page.views.clear()
            page.views.append(
                create_view("/view1", "View1", "/view2", "/cover/view2", ft.colors.RED))
        elif troute.match("/view2"):
            page.views.clear()
            page.views.append(
                create_view("/view2", "View2", "/view1", "/cover/view1", ft.colors.RED))
        elif troute.match("/cover/view1"):
            page.views.append(
                create_view("/cover/view1", "View1", "/view2", "/cover/view2", ft.colors.GREEN))
        elif troute.match("/cover/view2"):
            page.views.append(
                create_view("/cover/view2", "View2", "/view1", "/cover/view1", ft.colors.YELLOW_800))
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
