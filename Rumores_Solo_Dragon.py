import random
import flet as ft

# Dados
masmorra = ["um Mago Louco", "um Mago Ancestral", "um Clérigo Cego", "um Clérigo Poderoso", "um Clérigo Proscrito",
            "um Guerreiro Poderoso", "um Guerreiro Rico", "um Rei Antigo", "um Rei Poderoso", "um Rei Furioso",
            "um Rei", "uma Sacerdotisa", "um Sábio", "um Demônio", "a Arak-Takna", "um Dragão", "um Orc",
            "um Vampiro", "um Lich", "um Druida", "um Sacerdote", "o próprio Orcus", "um Herói", "um Antigo Vilão",
            "um Comerciante", "um Ladrão ambicioso", "um Ladrão enriquecido", "um Príncipe", "uma Rainha",
            "um Senhor do crime", "um Cultista", "um Bardo", "uma Bruxa", "um Ser Amaldiçoado", "uma Marilith",
            "um Devorador de Cérebro"]

Para = ["proteger", "esconder", "aprisionar", "deter", "impedir", "descobrir", "derrotar", "explorar", "vigiar",
        "atrair", "contratar", "selecionar", "eliminar", "cultuar", "invocar", "restaurar", "enviar", "explodir",
        "criar", "formar", "idolatrar", "conjurar", "afastar", "libertar", "aguardar", "transportar", "seguir",
        "recuperar", "confinar", "invocar", "reviver", "expulsar", "raptar", "definhar", "apagar", "sumir"]

Uma = ["tesouro", "monstro", "espada", "grimório", "Ídolo", "deus", "documento", "demônio", "lich", "joia", "trono",
       "escravo", "vampiro", "profecia", "Líder religioso", "Arak-Takna", "Orcus", "Cthulhu", "ovo de dragão", "portal",
       "rival", "seita", "armadura", "mapa", "goblin", "drider", "criatura", "magia", "elmo", "Guilda", "ettin", "orc",
       "opositor", "confraria", "adaga", "gigante"]


def gerar_rumor():
    rumor = (f" ''A masmorra foi criada por {random.choice(masmorra)} para {random.choice(Para)} um(a) "
             f"{random.choice(Uma)}.'' ")
    return rumor


def main(page: ft.Page):
    page.title = "Gerador de Rumores"
    page.window_width = 400
    page.window_height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    rumor_text = ft.Text(gerar_rumor(), size=20, text_align=ft.TextAlign.JUSTIFY)

    def on_generate_click(event):
        rumor_text.value = gerar_rumor()
        page.update()

    def on_copy_click(event):
        page.set_clipboard(rumor_text.value)

    generate_button = ft.ElevatedButton(text="Gerar Novo Rumor", on_click=on_generate_click)
    copy_button = ft.ElevatedButton(text="Copiar Texto", on_click=on_copy_click)

    page.add(
        ft.Column(
            [
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


ft.app(target=main)
