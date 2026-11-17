# Tarefa 03 - Calculadora com Interface Gráfica
# Disciplina: Introdução à Ciência da Computação
# Aluno: Mariana Werlang - 25204855
# Data: 16/06/2026

import PySimpleGUI as sg

# Define o tema visual da interface
sg.theme('DarkBlue13')

# Layout da calculadora:
# Cada lista representa uma linha da interface
layout = [
    # Display onde será exibida a expressão digitada e os resultados
    [sg.Text('0',
             size=(20, 1),
             font=('Helvetica', 24),
             justification='right',
             key='-DISPLAY-',
             background_color='black',
             text_color='white')],

    # Linha dos parênteses, limpar e divisão
    [sg.Button('(', size=(5, 2)),
     sg.Button(')', size=(5, 2)),
     sg.Button('C', size=(5, 2)),
     sg.Button('÷', size=(5, 2))],

    # Linha dos números 7, 8 e 9
    [sg.Button('7', size=(5, 2)),
     sg.Button('8', size=(5, 2)),
     sg.Button('9', size=(5, 2)),
     sg.Button('×', size=(5, 2))],

    # Linha dos números 4, 5 e 6
    [sg.Button('4', size=(5, 2)),
     sg.Button('5', size=(5, 2)),
     sg.Button('6', size=(5, 2)),
     sg.Button('-', size=(5, 2))],

    # Linha dos números 1, 2 e 3
    [sg.Button('1', size=(5, 2)),
     sg.Button('2', size=(5, 2)),
     sg.Button('3', size=(5, 2)),
     sg.Button('+', size=(5, 2))],

    # Última linha com 0, decimal e igual
    [sg.Button('0', size=(11, 2)),
     sg.Button('.', size=(5, 2)),
     sg.Button('=', size=(5, 2))]
]

# Cria a janela principal da calculadora
window = sg.Window('Calculadora Simples', layout)

# Variável que armazena a expressão digitada pelo usuário
expressao = ""

# Loop principal do programa
# Fica executando até o usuário fechar a janela
while True:

    # Captura o evento (botão clicado) e os valores da interface
    event, values = window.read()

    # Encerra o programa ao fechar a janela
    if event == sg.WIN_CLOSED:
        break

# Fecha a janela ao encerrar o programa
window.close()
