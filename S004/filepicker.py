import flet as ft




def main(page):
    
    page.add(ft.Text("file Pick sample"))
    picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(picker)

    page.add(ft.TextButton(text = "getpath",on_click = lambda _ : picker.pick_files()))
    page.add(ft.TextButton(text = "getpath",on_click = lambda _ : picker.get_directory_path()))

def on_dialog_result(e : ft.FilePickerResultEvent):
    print(e.files)
    print(e.path)





    

if __name__ == "__main__":
    
    ft.app(target=main)


