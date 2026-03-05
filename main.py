import flet as ft

def main(page: ft.Page):
    page.title = "Ficha de Registro de Participantes"
    page.bgcolor = ft.Colors.RED_900
    page.scroll = "adaptive"
    page.padding = 20
    
    titulo = ft.Text(
        "Registro de Participantes",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700
    )
    
    imagen = ft.Image(
        src="data:image/jpeg;base64,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",
        width=150,
        height=150,
        border_radius=50,
    )
    
    nombre = ft.TextField(
        label="Nombre completo",
        hint_text="Introduzca su nombre completo :3",
    )
    gmail = ft.TextField(
        label="Correo electronico",
        hint_text="Introduzca su correo",
    )
    Tipo_de_curso = ft.Dropdown(
        label="Taller de intereses",
        options=[
            ft.dropdown.Option("Python para principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas")
        ],
        value="Flet Intermedio"
    )
    
    Modalidad = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="pago completo", label="Completo"),
            ft.Radio(value="pago por cuotas", label="Cuotas"),
        ]),
        value="pago completo",
        on_change=lambda e: print(f"Seleccionado: {e.control.value}")

    )
    Modalidad_label = ft.Text("Modalidad:", size=16)
    
    Verificacion = ft.Checkbox(
        label="Acepto términos",
        value=False,
        tristate=False,
        check_color=ft.Colors.WHITE,
        fill_color=ft.Colors.GREEN,
        on_change=lambda e: print(f"Estado: {e.control.value}")
    )
    
    experiencia = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        label="{value} Nivel ",
    )
    experiencia_label = ft.Text("Nivel: ", size=16)
    
    
    resumen_text = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.NORMAL,
        color=ft.Colors.BLACK87
    )
    
    def mostrar_resumen(e):
        if not nombre.value or nombre.value.strip() == "":
            resumen_text.value = ""
        else:
            resumen_text.value = f"""RESUMEN DEL CURSO :3

• Nombre: {nombre.value}
• Gmail: {gmail.value}
• Tipo de curso: {Tipo_de_curso.value}
• Modalidad: {Modalidad.value}
• Experiencia: {int(experiencia.value)} Nivel"""

    page.update()
    
    boton_resumen = ft.ElevatedButton(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE
    )

    page.add(
        ft.Column([
            titulo,
            imagen,
            nombre,
            gmail,
            Tipo_de_curso,
            Modalidad_label,
            Modalidad,
            experiencia_label,
            experiencia,
            Verificacion,
            boton_resumen,
            resumen_text,
        ],
        spacing=15
        )
    )
    
ft.app(target=main)