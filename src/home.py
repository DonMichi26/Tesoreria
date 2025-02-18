import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import flet as ft
import datetime
from models.funtion01 import BankReport  # Importar la clase BankReport

# Clase principal de la aplicación
class MyAplicacion:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Area de Tesoreria - UNCP"  # Título de la ventana
        self.page.bgcolor = ft.colors.WHITE  # Color de fondo de la ventana

        button_ancho = 200  # Ancho de los botones
        button_alto = 40  # Alto de los botones
        self.page.window_width = 300  # Ancho de la ventana
        self.page.window_height = 500  # Alto de la ventana

        # Crear el título y la imagen
        titulo = ft.Text("Area de Tesoreria - UNCP", size=24, weight="bold", color=ft.colors.BLACK, font_family="Courier New")
        imagen = ft.Image(src="uncp.png", width=100, height=100)  # Imagen del logo

        # Encabezado con el título y la imagen
        header = ft.Row(
            controls=[imagen, titulo],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Estilo de los botones
        button_style = ft.ButtonStyle(
            text_style=ft.TextStyle(
                color=ft.colors.BLACK,
                font_family="Courier New"
            )
        )

        # Botón para crear reportes de cajas
        self.btn1 = ft.FilledButton(
            text="Crear reportes de cajas",
            style=button_style,
            width=button_ancho,
            height=button_alto,
            on_click=lambda e: self.page.go("/crear_reportes")
        )

        # Botón para crear cajas de pago
        self.btn2 = ft.FilledButton(
            text="Crear cajas de pago",
            style=button_style,
            width=button_ancho,
            height=button_alto,
            on_click=lambda e: self.page.go("/crear_cajas")
        )

        # Botón para búsqueda de expedientes
        self.btn3 = ft.FilledButton(
            text="Busqueda de expedientes",
            style=button_style,
            width=button_ancho,
            height=button_alto,
            on_click=lambda e: self.page.go("/busqueda_expedientes")
        )

        # Botón para cerrar la aplicación
        self.btn_cerrar = ft.TextButton(
            text="Cerrar Aplicacion",
            on_click=self.cerrar_app,
            icon_color=ft.colors.RED
        )

        # Contenedor principal con todos los controles
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

        # Contenedor principal con imagen de fondo
        contenedor_principal = ft.Container(
            content=fondo,
            expand=True,
            image_src="uncp.png",
            image_opacity=0.5,
            image_fit=ft.ImageFit.COVER
        )

        # Añadir el contenedor principal a la página
        self.page.add(contenedor_principal)
        self.page.update()

    # Función para cerrar la aplicación
    def cerrar_app(self, e):
        sys.exit()  # Cerrar la aplicación

# Función para manejar la vista de creación de reportes de cajas
def crear_reportes(page: ft.Page):
    # Crear un nuevo reporte bancario
    report = BankReport("Bank of Python", "123456789", 1000.00)
    # Añadir algunas transacciones
    report.add_transaction(datetime.date(2023, 10, 1), "Depósito", 500.00)
    report.add_transaction(datetime.date(2023, 10, 2), "Retiro", -200.00)
    # Generar el reporte
    report_text = report.generate_report()

    # Mostrar el reporte en un cuadro de diálogo
    page.dialog = ft.AlertDialog(
        title=ft.Text("Reporte Bancario"),
        content=ft.Text(report_text),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: page.dialog.close())
        ]
    )
    page.dialog.open = True
    page.update()

# Función para manejar la vista de creación de cajas de pago
def crear_cajas(page: ft.Page):
    page.dialog = ft.AlertDialog(
        title=ft.Text("Crear cajas de pago"),
        content=ft.Text("Ventana emergente para crear cajas de pago."),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: page.dialog.close())
        ]
    )
    page.dialog.open = True
    page.update()

# Función para manejar la vista de búsqueda de expedientes
def busqueda_expedientes(page: ft.Page):
    page.dialog = ft.AlertDialog(
        title=ft.Text("Busqueda de expedientes"),
        content=ft.Text("Ventana emergente para búsqueda de expedientes."),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: page.dialog.close())
        ]
    )
    page.dialog.open = True
    page.update()

# Función principal que inicia la aplicación
def main(page: ft.Page):
    # Definir las rutas y las vistas correspondientes
    page.routes = {
        "/": MyAplicacion,
        "/crear_reportes": crear_reportes,
        "/crear_cajas": crear_cajas,
        "/busqueda_expedientes": busqueda_expedientes
    }
    page.go("/")

# Ejecutar la aplicación
ft.app(target=main)