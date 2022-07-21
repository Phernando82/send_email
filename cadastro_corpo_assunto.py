import PySimpleGUI as sg


# criação da janela
class TelaCadastroTexto:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Assunto:'), sg.Input(key='assunto')],
            [sg.Text('Corpo do email:'), sg.Input(key='corpo')],
            [sg.Button('Enviar')]
        ]
        window_get = sg.Window('Cadastrar assunto e corpo do email', layout=layout, finalize=True)
        self.button, self.values = window_get.Read()

    def iniciar(self):
        assunto = self.values['assunto']
        corpo = self.values['corpo']
        print(f'Assunto: {assunto}')
        print(f'Corpo do email: {corpo}')
        with open('dados_email.txt', 'a') as arquivo:
            arquivo.writelines(f'Assunto: {assunto} \nCorpo: {corpo}')


tela_cadastro_texto = TelaCadastroTexto()
tela_cadastro_texto.iniciar()
