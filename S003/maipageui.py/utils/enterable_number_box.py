from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue


class enterableNumberBox(ft.UserControl):
    def __init__(self, controls: List[Control] | None = None, ref: Ref | None = None, key: str | None = None, width: OptionalNumber = 60, height: OptionalNumber = 60, left: OptionalNumber = None, top: OptionalNumber = None, right: OptionalNumber = None, bottom: OptionalNumber = None, expand: bool | int | None = None, col: ResponsiveNumber | None = None, opacity: OptionalNumber = None, rotate: RotateValue = None, scale: ScaleValue = None, offset: OffsetValue = None, aspect_ratio: OptionalNumber = None, animate_opacity: AnimationValue = None, animate_size: AnimationValue = None, animate_position: AnimationValue = None, animate_rotation: AnimationValue = None, animate_scale: AnimationValue = None, animate_offset: AnimationValue = None, on_animation_end=None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, clip_behavior: ClipBehavior | None = None):
        super().__init__(controls, ref, key, width, height, left, top, right, bottom, expand, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, clip_behavior)
        
        self.width  = width
        self.height = height
        self.borderwidth = 1

        #入力時(カーソルがホバーしたとき)は上にかぶせたキャンバスを無効化するためのbool
        self.inputnow : bool = False

        #テキストフィールド
        self.Textfield = ft.TextField(
            label = '',
            expand=True,
            text_size= int(self.height*0.4),
            text_align = ft.TextAlign.CENTER,
            border=ft.InputBorder.NONE,
            on_change = self.Score_updated,
            )
        #キャンバス
        self.Canvas = ft.canvas.Canvas()
        #コンテナ > テキスト　と キャンバス　をかぶせて保持
        self.maincontrole = ft.Container(

            width  = self.width,
            height = self.height,
            border = ft.border.only(left=ft.border.BorderSide(self.borderwidth),bottom=ft.border.BorderSide(self.borderwidth)),
            on_hover=self.on_hover,

            content= ft.Stack(controls = [self.Textfield ,self.Canvas])
            )
    
    def on_hover(self ,e:ft.ControlEvent):
        self.inputnow = True if e.data == "true" else False
        print(self.inputnow,self.Textfield.value)
        self.maincontrole.update()

    def Score_updated(self,e:ft.ControlEvent):
        self.ScoreIsSpecial()

    def visibleText(self):
        self.Textfield.color = ft.colors.with_opacity(1.0, '#000000')
        self.Textfield.update()
    def invisibleText(self):
        self.Textfield.color = ft.colors.with_opacity(0.1, '#000000')
        self.Textfield.update()

    def ScoreIsSpecial(self):
        if self.Textfield.value == '10':
            self.Canvas.shapes.append(
                ft.canvas.Path(
                    [
                        ft.canvas.Path.MoveTo(self.width-self.borderwidth, self.height),
                        ft.canvas.Path.LineTo(self.width-self.borderwidth, 0),
                        ft.canvas.Path.LineTo(0, self.height),
                    ],
                    paint=ft.Paint(
                        style=ft.PaintingStyle.FILL,
                    ),
                ),

                
            )
            self.invisibleText()
        elif self.Textfield.value == '9':
            self.Canvas.shapes.append(
                ft.canvas.Path(
                    [
                        ft.canvas.Path.MoveTo(0, 0),
                        ft.canvas.Path.LineTo(self.width/2, self.height/2),
                        ft.canvas.Path.LineTo(0, self.height),
                    ],
                    paint=ft.Paint(
                        style=ft.PaintingStyle.FILL,
                    ),
                )
            )
            self.Canvas.shapes.append(
                ft.canvas.Path(
                    [
                        ft.canvas.Path.MoveTo(self.width, 0),
                        ft.canvas.Path.LineTo(self.width/2-self.borderwidth, self.height/2),
                        ft.canvas.Path.LineTo(self.width, self.height),
                    ],
                    paint=ft.Paint(
                        style=ft.PaintingStyle.FILL,
                    ),
                ),
                
            )
            self.invisibleText()
        else:
            self.Canvas.shapes.clear()
            self.visibleText()
        self.Canvas.update()

    def build(self):
        return self.maincontrole

class scoreFlame(ft.UserControl):
    def __init__(self,flamenum : OptionalNumber = 2 ,boxsize = 60, controls: List[Control] | None = None, ref: Ref | None = None, key: str | None = None, left: OptionalNumber = None, top: OptionalNumber = None, right: OptionalNumber = None, bottom: OptionalNumber = None, expand: bool | int | None = None, col: ResponsiveNumber | None = None, opacity: OptionalNumber = None, rotate: RotateValue = None, scale: ScaleValue = None, offset: OffsetValue = None, aspect_ratio: OptionalNumber = None, animate_opacity: AnimationValue = None, animate_size: AnimationValue = None, animate_position: AnimationValue = None, animate_rotation: AnimationValue = None, animate_scale: AnimationValue = None, animate_offset: AnimationValue = None, on_animation_end=None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, clip_behavior: ClipBehavior | None = None):
        super().__init__(controls, ref, key, None, None, left, top, right, bottom, expand, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, clip_behavior)

        
        self.width  = boxsize * (flamenum + 1)

        self.maincontrole = ft.Container(
            border = ft.border.all(1),
            
            content= ft.Column(
                controls=[
                    ft.Row(
                        spacing=0,
                        alignment = ft.MainAxisAlignment.END,
                        controls = [ft.Container(width = boxsize ,height=boxsize)]+[enterableNumberBox(width = boxsize ,height=boxsize) for _ in range(flamenum)]
                        ),
                    ft.Container(
                        alignment=ft.alignment.Alignment(0.6,0.0),
                        content=ft.Text("90",size = 40)
                    )
                ]
            )
        )

    def build(self):
        return self.maincontrole

class scoreBoard(ft.UserControl):
    def __init__(self, controls: List[Control] | None = None, ref: Ref | None = None, key: str | None = None, width: OptionalNumber = None, height: OptionalNumber = None, left: OptionalNumber = None, top: OptionalNumber = None, right: OptionalNumber = None, bottom: OptionalNumber = None, expand: bool | int | None = None, col: ResponsiveNumber | None = None, opacity: OptionalNumber = None, rotate: RotateValue = None, scale: ScaleValue = None, offset: OffsetValue = None, aspect_ratio: OptionalNumber = None, animate_opacity: AnimationValue = None, animate_size: AnimationValue = None, animate_position: AnimationValue = None, animate_rotation: AnimationValue = None, animate_scale: AnimationValue = None, animate_offset: AnimationValue = None, on_animation_end=None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, clip_behavior: ClipBehavior | None = None):
        super().__init__(controls, ref, key, width, height, left, top, right, bottom, expand, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, clip_behavior)

        self.maincontrole = ft.Row(
            spacing=0,
            controls=[scoreFlame() for _ in range(9)]+[scoreFlame(flamenum = 3)]
        )
    
    def build(self):
        return self.maincontrole

def main(page):
    
    page.add(scoreBoard())
    return page

if __name__ == "__main__":
    ft.app(target=main)