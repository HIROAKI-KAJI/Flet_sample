from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



class AppFire(ft.UserControl):
    def __init__(self, controls: List[Control] | None = None, ref: Ref | None = None, key: str | None = None, width: OptionalNumber = None, height: OptionalNumber = None, left: OptionalNumber = None, top: OptionalNumber = None, right: OptionalNumber = None, bottom: OptionalNumber = None, expand: bool | int | None = None, col: ResponsiveNumber | None = None, opacity: OptionalNumber = None, rotate: RotateValue = None, scale: ScaleValue = None, offset: OffsetValue = None, aspect_ratio: OptionalNumber = None, animate_opacity: AnimationValue = None, animate_size: AnimationValue = None, animate_position: AnimationValue = None, animate_rotation: AnimationValue = None, animate_scale: AnimationValue = None, animate_offset: AnimationValue = None, on_animation_end=None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, clip_behavior: ClipBehavior | None = None):
        super().__init__(controls, ref, key, width, height, left, top, right, bottom, expand, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, clip_behavior)

        
        
        self.name = ft.TextField(label = "name")
        self.age  = ft.TextField(label = "age")
        self.button = ft.ElevatedButton(
            text="get app data",
            on_click= self.getdata
        )
        self.alldata = ft.Column(
            controls=[
                self.name   ,
                self.age    ,
                self.button ,
            ]
        )
    def getdata(self,*arg):
        #export GOOGLE_APPLICATION_CREDENTIALS="/home/billiards/VScode_workspace/KIMITU/billiard-app-firebase-adminsdk-pv8hs-3fea675bcf.json"

        #cred = credentials.Certificate("/home/billiards/VScode_workspace/KIMITU/billiard-app-firebase-adminsdk-pv8hs-3fea675bcf.json")
        #default_app = firebase_admin.initialize_app(cred, name='other')
        #print(default_app)
        doc_ref = db.collection("users")

        doc = doc_ref.get()
        if doc.exists:
            print(f'Document data: {doc.to_dict()}')
        else:
            print(u'No such document!')


    def did_mount(self):
        self.getdata()
    
    def build(self):
        return self.alldata

def main(page : ft.Page):
    page.update()
    

    appfire = AppFire()

    page.add(appfire)

# Application Default credentials are automatically created.
firebase_admin.initialize_app()
db = firestore.client()

if '__main__' == __name__:
    

    ft.app(target=main)
