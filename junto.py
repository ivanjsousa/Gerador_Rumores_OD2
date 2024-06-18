import random
import flet as ft

# Dados para o primeiro gerador de rumores
QUANDO = ['na semana passada', 'no último inverno', 'três dias atrás', 'pela manhã', 'depois da meia noite',
          'hoje mais cedo', 'durante o almoço', 'algumas horas atrás', 'durante a tarde', 'no jantar']

QUEM = ['um pirata', 'um aventureiro', 'um homem', 'um nobre', 'um cultista', 'um soldado', 'um sacerdote',
        'uma mulher', 'um criminoso', 'um mago']

ATIVIDADE = ['foi visto com', 'escondida', 'portava', 'recebeu', 'tinha em mãos', 'tentava vender', 'comprou',
             'fugiu com', 'roubou', 'escondeu']

COISA = ['um livro', 'um frasco', 'um monstro', 'um mapa', 'uma armadura', 'um objeto metálico', 'uma espada',
         'uma carta', 'uma túnica', 'um baú']

QUALIDADE = ['novo', 'antigo', 'valioso', 'brilhante', 'falso', 'assassino', 'ameaçador', 'misterioso',
             'roubado', 'terrível']

ONDE = ['próximo a Vanória', 'nas imediações de Arthuria', 'no distrito das Docas de Landora', 'no Charco das Feras',
        'em Kardarin', 'nos arredores de Landora', 'nos Jardins do Caos', 'na Floresta de Pedra', 'oriundo dos Ermos',
        'em Daraksan']

PISTA1 = ['uma bruxa', 'um órfão', 'um monstro', 'um condenado', 'um guarda', 'um cadáver', 'uma mulher', 'um nobre',
          'um cultista', 'uma besta']

PISTA2 = ['um nobre local', 'uma guilda de ladrões', 'um druida que age no local', 'um rico comerciante',
          'um fazendeiro', 'um estalajadeiro', 'a igreja de Theldir', 'um clérigo das imediações',
          'a liga das 7 chaves', 'um guarda do Grifo Branco']

PISTA3 = ['está recrutando um grupo de heróis para investigar', 'paga pela confirmação do rumor',
          'desmente com força este rumor', 'enviou espiões para descobrir tudo sobre isso',
          'tem interesse na história', 'contratou bandidos para se proteger', 'enviou aventureiros para lá',
          'afirma que é mentira', 'investiga com atenção', 'tenta abafar o caso']

# Dados para o segundo gerador de rumores
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


# Funções para gerar rumores
def gerar_rumor_tipo_1():
    rumor = (f" ''Vocês ouviram {random.choice(QUANDO)}, que {random.choice(QUEM)} {random.choice(ATIVIDADE)} "
             f"{random.choice(COISA)} {random.choice(QUALIDADE)} {random.choice(ONDE)} "
             f"e junto havia {random.choice(PISTA1)}. "
             f"Parece que {random.choice(PISTA2)}, {random.choice(PISTA3)}.'' ")
    return rumor


def gerar_rumor_tipo_2():
    rumor = (f" ''A masmorra foi criada por {random.choice(masmorra)} para {random.choice(Para)} um(a) "
             f"{random.choice(Uma)}.'' ")
    return rumor


# Função principal
def main(page: ft.Page):
    page.title = "Gerador de Rumores"
    page.window_width = 500
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    rumor_text = ft.Text(size=20, text_align=ft.TextAlign.JUSTIFY)

    def on_generate_click(event):
        if dropdown.value == "Rumor OD2":
            rumor_text.value = gerar_rumor_tipo_1()
        else:
            rumor_text.value = gerar_rumor_tipo_2()
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


ft.app(target=main)
