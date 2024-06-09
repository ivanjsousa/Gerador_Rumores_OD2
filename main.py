import random

QUANDO = ['na semana passada', 'no último inverno', 'três dias atrás', 'pela manhã', 'depois da meia noite',
          'hoje mais cedo', 'durante o almoço', 'algumas horas atrás', 'durante a tarde', 'no jantar']

QUEM = ['um pirata', 'um aventureiro', 'um homem', 'um nobre', 'um cultista', 'um soldade', 'um sacerdote',
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
          'afirma que é mentira', 'investiva com atenção', 'tenta abafar o caso']

print(f"Vocês ouviram {random.choice(QUANDO)}, que {random.choice(QUEM)} {random.choice(ATIVIDADE)} "
      f"{random.choice(COISA)} {random.choice(QUALIDADE)} {random.choice(ONDE)} e junto havia {random.choice(PISTA1)}. "
      f"Parece que {random.choice(PISTA2)}, {random.choice(PISTA3)}.")