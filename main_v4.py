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

    rumor_text = ft.Text(size=20, text_align=ft.TextAlign.JUSTIFY, color="white")

    def on_generate_click(event):
        rumor_text.value = gerar_rumor_tipo_1() if dropdown.value == "Rumor OD2" else gerar_rumor_tipo_2()
        page.update()

    def on_copy_click(event):
        page.set_clipboard(rumor_text.value)

    dropdown = ft.Dropdown(
        options=[ft.dropdown.Option("Rumor OD2"), ft.dropdown.Option("Rumor Solo Dragon")],
        value="Rumor OD2",
        width=170
    )

    generate_button = ft.ElevatedButton(text="Gerar Novo Rumor", on_click=on_generate_click)
    copy_button = ft.ElevatedButton(text="Copiar Texto", on_click=on_copy_click)

    content = ft.Column(
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

    # Adicionando a imagem de fundo
    background_image = ft.Image(
        src="https://olddragon.com.br/vite/assets/home-panel-1-DUG7iSqR.webp",  # Substitua pelo URL da sua imagem
        fit=ft.ImageFit.COVER,
        width=page.window_width,
        height=page.window_height
    )

    page.add(
        ft.Stack(
            [
                background_image,
                ft.Container(
                    content,
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.with_opacity(ft.colors.BLACK, 0.7),  # Transparência para ver a imagem de fundo
                ),
            ],
            expand=True,
        )
    )


ft.app(target=main)
