import random
import unicodedata

# Função para remover acentos.
def removerAcentos(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

# Palavras de diculdade fácil.
palavrasFacil = [
    'sol', 'lua', 'flor', 'mar', 'pão', 'gato', 'cão', 'mão', 'frio', 'água',
    'paz', 'luz', 'casa', 'bebê', 'flor', 'beijo', 'doce', 'chuva'
]

# Palavras de dificuldade média.
palavrasMedia = [
    'amigo', 'livro', 'azul', 'tigre', 'canto', 'pedra', 'farol', 'trigo', 'carro', 'música',
    'festa', 'guitarra', 'dança', 'cidade', 'viagem', 'oceano', 'pintura', 'futebol', 'cinema', 'livraria', 'sorriso', 'árvore'
]

# Palavras de dificuldade difícil.
palavrasDificil = [
    'girassol', 'elefante', 'computador', 'morangos', 'telefone', 'camiseta', 'leopardo', 'amarelo', 'hipopótamo', 'paradigma',
    'exoplaneta', 'fuselagem', 'helicóptero', 'microscópio', 'ultrassom', 'hipotenusa', 'arqueologia', 'abstrato', 'paradoxo', 'criptografia'
]

# Palavras de dificuldade extrema.
palavrasExtrema = [
    'xilofone', 'químiossíntese', 'equilíbrio', 'quadrícula', 'magnetômetro', 'pneumático','eletrodoméstico' , 'paleontologia', 'eletromagnetismo', 'paralelepípedo',
    'eletroencefalograma', 'desoxirribonucleico', 'anisotropia', 'paleontólogo', 'eletrocardiograma', 'magnetoforese', 'heterocedasticidade', 'difusividade', 'monocromático', 'piroclástico'
]

# Loop para escolher a dificuldade.
flag = True
while flag:
    print('''Escolha a dificuldade: 
1 - Fácil.
2 - Médio.
3 - Difícil.
4 - Extremo.''')
    dificuldade = input('--> ')
    if dificuldade == '1':
        print('Modo fácil selecionado.')
        vidas = 15
        palavraDois = random.choice(palavrasFacil)
        palavra = removerAcentos(palavraDois)
        flag = False
    elif dificuldade == '2':
        print('Modo médio selecionado.')
        vidas = 10
        palavraDois = random.choice(palavrasMedia)
        palavra = removerAcentos(palavraDois)
        flag = False
    elif dificuldade == '3':
        print('Modo difícil selecionado.')
        vidas = 10
        palavraDois = random.choice(palavrasDificil)
        palavra = removerAcentos(palavraDois)
        flag = False
    elif dificuldade == '4':
        print('Modo extremo selecionado.')
        vidas = 10
        palavraDois = random.choice(palavrasExtrema)
        palavra = removerAcentos(palavraDois)
        flag = False
    else:
        print('\nOpção não encontrada.\n')

# Lógica do jogo em si, contendo alguns parâmetros para evitar certos inputs errados do usuário.
palavraNova = [' ' for i in range(len(palavra))]
letraUtilizadas = []
while vidas > 0: # Loop do jogo. Ele se encerrado quando não restam mais vidas para o player.
    aux = [l for l in palavraNova if l != ' '] 
    if len(aux) < len(palavra): # Teste para ver se ainda restam letras que não foram acertadas.
        palpite = input('\nInsira uma letra: ').lower()
        if palpite.isdigit() or len(palpite) > 1 or len(palpite) == 0 or palpite == ' ': # Teste para verificar se o usuário entrou com algum caractere não permitido.
            print('\nPalpite não permitido.')
        else:
            if palpite not in letraUtilizadas: # Teste para verificar o histórico de palpites do player, para evitar que ele repita palpites.
                if palpite in palavra: # Teste para verificar contém o palpite na palavra.
                    for i in range(len(palavra)): # "Algoritmo" usado para adicionar um acerto na palavra auxiliar.
                        if palavra[i] == palpite:
                            palavraNova[i] = palpite
                    print('\nPalpite certo! :)')
                    print('Palavra: ',end='')
                    for p in palavraNova: # "Algoritmo" usado para mostrar o andamento de acertos.
                        if p == ' ':
                            print('_', end='')
                        else:
                            print(p, end='')
                    print('')
                else:
                    print('\nPalpite errado. :(')
                    vidas -= 1
                letraUtilizadas.append(palpite) # Adiciona o palpite no histórico de palpites.
            else:
                print('\nVocê já testou esta letra.')
                print(f'Letras que já foram testadas: {letraUtilizadas}')
    else:
        print('\nVocê venceu o jogo! :)')
        print('A palavra era: ',palavraDois)
        exit()
print('\nVocê perdeu. :(')
print('A palavra era: ',palavraDois)
input()