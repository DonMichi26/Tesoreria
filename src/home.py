import flet as ft
import sys

class MyAplicacion:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Area de Tesoreria - UNCP"
        self.page.bgcolor = ft.colors.WHITE

        button_ancho = 200
        button_alto = 40  
        self.page.window_width = 300
        self.page.window_height = 500

        # Crear el título y la imagen
        titulo = ft.Text("Area de Tesoreria - UNCP", size=24, weight="bold", color=ft.colors.BLACK, italic=True, font_family="Times New Roman")
        imagen = ft.Image(src="uncp.png", width=50, height=50)  

        header = ft.Row(
            controls=[imagen, titulo],
            alignment=ft.MainAxisAlignment.CENTER
        )

        button_style = ft.ButtonStyle(
            text_style=ft.TextStyle(
                color=ft.colors.BLACK,
                font_family="Times New Roman"
            )
        )

        self.btn1 = ft.FilledButton(
            text="Crear reportes de cajas",
            style=button_style,
            width=button_ancho,
            height=button_alto,
            on_click=self.funcion1
        )

        self.btn2 = ft.FilledButton(
            text="Crear cajas de pago",
            style=button_style,
            width=button_ancho,
            height=button_alto,
            on_click=self.funcion2
        )

        self.btn3 = ft.FilledButton(
            text="Busqueda de expedientes",
            style=button_style,
            width=button_ancho,
            height=button_alto,
            on_click=self.funcion3
        )

        self.btn_cerrar = ft.TextButton(
            text="Cerrar Aplicacion",
            on_click=self.cerrar_app,
            icon_color=ft.colors.RED
        )

        fondo = ft.Container(
            content=ft.Column(
                controls=[header, self.btn1, self.btn2, self.btn3, self.btn_cerrar],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            bgcolor=ft.colors.TRANSPARENT,
            expand=True
        )

        contenedor_principal = ft.Container(
            content=fondo,
            expand=True,
            image_src="uncp.png",
            image_opacity=0.5,
            image_fit=ft.ImageFit.COVER
        )

        self.page.add(contenedor_principal)
        self.page.update()

    def funcion1(self, e):
        self.page.add(ft.Text("Botón 1 presionado", color=ft.colors.BLACK))

    def funcion2(self, e):
        self.page.add(ft.Text("Botón 2 presionado", color=ft.colors.BLACK))

    def funcion3(self, e):
        self.page.add(ft.Text("Botón 3 presionado", color=ft.colors.BLACK))

    def cerrar_app(self, e):
        self.page.window_destroy()

def main(page: ft.Page):
    MyAplicacion(page)

ft.app(target=main)