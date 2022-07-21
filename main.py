import PySimpleGUI as sg
from envia_email import envia_email


# criação da janela
class TelaPython:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Descrição'), sg.Input(key='desc')],
            [sg.Text('Quantidade'), sg.Input(key='quant')],
            [sg.Button('Enviar')]
        ]

        window_get = sg.Window('Enviar Email', layout=layout, finalize=True)
        self.button, self.values = window_get.Read()

    def iniciar(self):
        desc = self.values['desc']
        quant = self.values['quant']
        print(f'Quantidade: {quant}')
        print(f'Descrição: {desc}')
        print(envia_email(desc, quant))


tela = TelaPython()
tela.iniciar()
