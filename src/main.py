import flet as ft
from home import MyAplicacion

def main(page: ft.Page):

    page.window_width = 300
    page.window_height = 500
    
    MyAplicacion(page)

ft.app(target=main)
