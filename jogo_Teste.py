import tkinter as tk
from tkinter import messagebox
import random

# definindo configuração do jogo
NUM_LINHAS = 4
NUM_COLUNAS = 4
CARTAO_SIZE_W =10
CARTAO_SIZE_H =5
CORES_CARTAO = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta']
COR_FUNDO ="#343a40"
COR_LETRA = '#ffffff'
FONT_STYLE = ('Arial', 12, 'bold')
MAX_TENTATIVAS = 25

# cria umagrade aleatoria de cores para os cartoes
def create_card_grid():
    cores = CORES_CARTAO *2
    random.shuffle(cores)
    grid = []

    for _ in range(NUM_LINHAS):
        linha = []
        for _  in range(NUM_COLUNAS):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

# funcionar com o clique do jogador

def card_clicked(linha, coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor == 'black':
        cartao['bg'] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_match()

# verificar se os dois cartoes revelados são iguais
def check_match():
    carta1, carta2 = cartao_revelado
    if carta1['bg'] == carta2['bg']:
        carta1.after(1000, carta1.destroy)
        carta2.after(1000, carta2.destroy)
        cartao_correspondentes.extend([carta1, carta2])
        check_win()
    else:
        carta1.after(1000, lambda: carta1.config(bg = 'black'))
        carta2.after(1000, lambda: carta2.config(bg = 'black'))
    cartao_revelado.clear()
    update_score()

# Atualizar a pontuação e verificar se o jogador ganhou o jogo
def check_win():
    if len(cartao_correspondentes) == NUM_LINHAS * NUM_COLUNAS:
        messagebox.showinfo('Parabéns!', 'você ganhou o jogo!')
        janela.quit()


# Atualizar a pontuação e verificar se o jogador perdeu o jogo
def update_score():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS))
    if numero_tentativas >= MAX_TENTATIVAS:
        messagebox.showinfo('Fim de jogo', 'Você perdeu o jogo!')


# Criando a interface principal

janela = tk.Tk()
janela.title('Jogo da Memoria')
janela.configure(bg=COR_FUNDO)

# criar grade de cartoes
grid = create_card_grid()
cartoes =[]
cartao_revelado = []
cartao_correspondentes = []
numero_tentativas = 0

# criar grade de cartões
for linha in range(NUM_LINHAS):
    linha_de_cartoes = []
    for col in range(NUM_COLUNAS):
        cartao = tk.Button(janela, command= lambda r=linha, c=col: card_clicked(r, c), width= CARTAO_SIZE_W, height=CARTAO_SIZE_H, bg='black', relief = tk.RAISED, bd=3)
        cartao.grid(row=linha, column=col, padx=5, pady=5)
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)

# personalizando o botão
button_style = {'activebackground': '#f8f9fa', 'font':FONT_STYLE, 'fg':COR_LETRA}
janela.option_add('*Button', button_style)

#label para numero de tentativas
label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS), fg= COR_LETRA, bg= COR_FUNDO, font = FONT_STYLE)
label_tentativas.grid(row = NUM_LINHAS, columnspan= NUM_COLUNAS, padx =10, pady=10)

janela.mainloop()