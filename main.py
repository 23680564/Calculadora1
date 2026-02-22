import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Estática - TAP"
    page.window_width = 280
    page.window_height = 450
    page.window_resizable = False
    page.padding = 15

    # --- 1. SECCIÓN DISPLAY (ROJO) ---
    texto_display = ft.Text("0", size=20)

    def boton_click(e):
        if texto_display.value == "0":
            texto_display.value = e.control.data
        else:
            texto_display.value += e.control.data
        page.update()

    seccion_display = ft.Container(
        content=texto_display,
        bgcolor=ft.Colors.BLACK12,
        height=70,
        alignment=ft.alignment.Alignment(0, 0),
        border=ft.border.all(1, ft.Colors.RED)
    )

    # --- 2. SECCIÓN BOTONES NUMÉRICOS (AZUL) ---
    seccion_numeros = ft.Column(
        controls=[

            # Fila 1
            ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("1", color="black"),
                        data="1",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("2", color="black"),
                        data="2",
                        
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("3", color="black"),
                        data="3",
                        on_click=boton_click
                    ),
                ]
            ),

            # Fila 2
            ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("4", color="black"),
                        data="4",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("5", color="black"),
                        data="5",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("6", color="black"),
                        data="6",
                        on_click=boton_click
                    ),
                ]
            ),

            # Fila 3
            ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("7", color="black"),
                        data="7",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("8", color="black"),
                        data="8",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("9", color="black"),
                        data="9",
                        on_click=boton_click
                    ),
                    ft.Row(
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="#00FFFF",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("0", color="black"),
                        data="0",
                        on_click=boton_click
                    )
                    )
                ]
            ),
        ],
        spacing=10
    )

    # --- 3. SECCIÓN OPERACIONES (VERDE) ---
    seccion_operaciones = ft.Row(
        controls=[
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
        ]
    )

    # --- CONSTRUCCIÓN FINAL ---
    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:", size=12),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:", size=12),
                seccion_operaciones
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)