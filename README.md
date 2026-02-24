# Calculadora desde Flet

Este programa crea una interfaz gráfica sencilla usando la librería Flet en Python. La aplicación muestra un display y botones numéricos organizados en filas y columnas.

# Importacion de librerias
`import flet as ft
`
Se importa la librería Flet y se le asigna el alias ft para escribir menos código.

# Funcion principal 
`def main(page: ft.Page):
`
La función main es el punto central del programa.
El parámetro page representa la ventana principal de la aplicación.
---

# Configuracion de la ventana
`page.title = "Calculadora Estática - TAP"
page.window_width = 280
page.window_height = 450
page.window_resizable = False
page.padding = 15
`
Aquí se configuran las propiedades de la ventana:

- Se define el título.
- Se establece el ancho y alto.
- Se evita que el usuario pueda cambiar el tamaño.
- Se agrega un espacio interno (padding).
---

## Seccin de Display
`texto_display = ft.Text("0", size=20)
`
- Se crea un objeto de texto que mostrará los números.
 Empieza mostrando "0".
---

Luego se define la función que se ejecuta cuando se presiona un botón:
`def boton_click(e):
`
 (e) es el evento que contiene información del botón presionado.
 Si el display tiene "0", se reemplaza por el número presionado.
 Si no, se agrega el nuevo número al final.
 page.update() actualiza la interfaz.

Después se crea el contenedor del display:
` seccion_display = ft.Container(...)
`
El Container:

- Contiene el texto.
- Tiene fondo gris claro.
- Altura fija.
- Borde rojo.
- Centra el contenido.
---

# Seccion de botones numericos
Se crea una columna:

`seccion_numeros = ft.Column(...)
`

Dentro de la columna hay tres Row (filas).
Cada fila contiene tres botones hechos con ft.Container.

Cada botón tiene:
- expand=1 -> ocupa el mismo espacio que los demás.
- height=50 → altura fija.
- bgcolor → color rosa.
- border → borde blanco.
- content=ft.Text("n") → número visible.
- data="n" → valor interno que se envía al hacer clic.
- on_click=boton_click → función que se ejecuta al presionar.
El parámetro spacing=10 agrega espacio entre filas.
---

# Seccion de operaciones
`seccion_operaciones = ft.Row(...)
`
Se crea una fila con tres contenedores verdes.
Actualmente no tienen funcionalidad, solo diseño visual.

# Contruccion final de la interfaz
`page.add(
    ft.Column(
        controls=[ ... ],
        spacing=15
    )
)
`
Aquí se arma toda la estructura final en una columna principal que contiene:

El display

-Texto “Números:”
-Botones numéricos
-Un divisor
-Texto “Operaciones:”
-Botones de operaciones
-El spacing=15 agrega separación entre cada sección.

# Ejecucion del programa
`if __name__ == "__main__":
    ft.app(target=main)
    `

   <img width="1266" height="647" alt="image" src="https://github.com/user-attachments/assets/aeefbc3c-5df2-46b1-9d27-26e2555b14bc" />

    `
- Esta parte indica que cuando el archivo se ejecuta directamente:
- Se inicia la aplicación Flet.
- Se llama a la función main.
- Se abre la ventana.

  # Como ejecutarlo desde Flet

  -Primero dirigirse a la carpeta donde estan guardados los documentos
  <img width="263" height="24" alt="image" src="https://github.com/user-attachments/assets/cc173f0c-b9ad-4b37-a13e-a30e3626a8fe" />
  -Despues seleccionar el archivo
  <img width="262" height="24" alt="image" src="https://github.com/user-attachments/assets/8b8f2af3-9daa-4c77-8b09-dce1f67d7d28" />
  -Dar click derecho en el archivo
  <img width="287" height="56" alt="image" src="https://github.com/user-attachments/assets/0666bba1-a34d-459d-b14e-72c06b583a88" />
  -Seleccionar en **Open git Bash Here** y se abrira el entorno virtual de Git Bash
  <img width="420" height="187" alt="image" src="https://github.com/user-attachments/assets/654aeb75-45ab-45cc-b199-0d608d6ef550" />
  -Una vez abierto el entorno virtual se pondra el comando "Python elnombredelarchivo.py "py" la extension de python para hacer referencia a el archivo
  <img width="354" height="121" alt="image" src="https://github.com/user-attachments/assets/055c9158-b1c5-46af-a7cc-fd8fb26a54b2" />
  -Y asi es como se realiza la ejecucion del programa o el proyecto
  <img width="1258" height="526" alt="image" src="https://github.com/user-attachments/assets/7e347e2a-1285-4468-89a6-7ce4de3cb1e0" />



  



