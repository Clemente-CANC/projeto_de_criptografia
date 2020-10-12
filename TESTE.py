import PySimpleGUI as sg

sg.theme("DarkGrey4")
# layout
layout = [
    [sg.Text("Sua chave: "), sg.Input('', size=(60, 5), key='-Cha-')],
    [sg.Text('Digite algo:'), sg.MLine('', key="-Text-"),
     sg.Button("Criptar", border_width=0, size=(10, 3))],
    [sg.Text('Criptado:'),
     sg.MLine(size=(60, 3), disabled=True, key='-Cript-')],
    [sg.HSeparator()],
    [sg.Text("Insira a chave: "),
     sg.Input('', size=(57, 5), key='-Cha2-')],
    [sg.Text("Digite a mensagem criptada: "),
     sg.ML('', size=(43, 1), key='-Text2-')],
    [sg.Text("Descriptada: "),
     sg.MLine(size=(56, 1), disabled=True, key='-Cript2-')],
    [sg.Button('Descriptar', size=(63, 2))]
]

# criando janela
janela = sg.Window("Projeto Cript", font='132 11').layout(layout)


def Criptar(mensagem, chave):
    lista = '''aAbBcCdDeEêfFgGrRsStTuUvVwWxXyYzZ1234
    567890àá~ãõ-=+_éèâ& {([])}\/,.:;'"@hHiIjJ?!kKlLmMnNoOpPqQ'''
    nova = [lista[(lista.index(c) + chave) %
                  (len(lista) - 1)] if c not in '$' else c for c in mensagem]
    nova = ''.join(nova)
    return nova


def Iniciar():
    while True:
        button, values = janela.Read()
        if button == sg.WIN_CLOSED or button == 'Cancel':
            break
        if button == 'Criptar':
            r = Criptar(str(values['-Text-']).replace('\n', '$'),
                        int(values['-Cha-']))
            r = r.replace('$', '\n')
            janela['-Cript-'].Update(r)
        if button == 'Descriptar':
            r = Criptar(str(values['-Text2-']).replace('\n', '$'),
                        -int(values['-Cha2-']))
            r = r.replace('$', '\n')
            janela['-Cript2-'].Update(r)


Iniciar()
