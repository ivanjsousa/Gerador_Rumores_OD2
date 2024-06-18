import random
import flet as ft
import dados as d


# Funções para gerar rumores
def gerar_rumor_tipo_1():
    return (f" ''Vocês ouviram {random.choice(d.QUANDO)}, que {random.choice(d.QUEM)} {random.choice(d.ATIVIDADE)} "
            f"{random.choice(d.COISA)} {random.choice(d.QUALIDADE)} {random.choice(d.ONDE)} "
            f"e junto havia {random.choice(d.PISTA1)}. "
            f"Parece que {random.choice(d.PISTA2)}, {random.choice(d.PISTA3)}.'' ")


def gerar_rumor_tipo_2():
    return (f" ''A masmorra foi criada por {random.choice(d.masmorra)} para {random.choice(d.Para)} um(a) "
            f"{random.choice(d.Uma)}.'' ")


# Função principal
def main(page: ft.Page):
    page.title = "Gerador de Rumores"
    page.window_width = 500
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    rumor_text = ft.Text(size=20, text_align=ft.TextAlign.JUSTIFY)

    def on_generate_click(event):
        rumor_text.value = gerar_rumor_tipo_1() if dropdown.value == "Old Dragon 2" else gerar_rumor_tipo_2()
        page.update()

    def on_copy_click(event):
        page.set_clipboard(rumor_text.value)

    dropdown = ft.Dropdown(
        options=[ft.dropdown.Option("Old Dragon 2"), ft.dropdown.Option("Solo Dragon")],
        value="Old Dragon 2",
        width=150
    )

    generate_button = ft.ElevatedButton(text="Gerar Novo Rumor", on_click=on_generate_click)
    copy_button = ft.ElevatedButton(text="Copiar Texto", on_click=on_copy_click)

    page.add(
        ft.Column(
            [
                dropdown,
                ft.Container(height=20),  # Espaçamento entre o dropdown e o texto
                rumor_text,
                ft.Container(height=20),  # Espaçamento entre o texto e os botões
                ft.Row(
                    [
                        generate_button,
                        copy_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10  # Espaçamento entre os botões
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)
