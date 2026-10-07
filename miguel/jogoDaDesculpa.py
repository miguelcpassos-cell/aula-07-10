import random

nome = input('Qual seu nome?')

quem = ['meu cachorro', 'meu primo', 'o wi-fi', ' o professor de matematica', 'meu gato']
açao = ['comeu','apagou', 'escondeu', 'hackeou', 'derrubou café']
alvo = ['meu caderno', 'meu notebook','minha tarefa', 'meu pendrive']

sorteio_quem = random.choice(quem)
sorteio_açao = random.choice(açao)
sorteio_alvo = random.choice(alvo)
print(f'Professor, desculpa! {sorteio_quem.capitalize()}{sorteio_açao}{sorteio_alvo}')
print('Assinado: {nome}')