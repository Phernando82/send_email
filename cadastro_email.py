import PySimpleGUI as sg


# criação da janela
class TelaCadastro:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Email'), sg.Input(key='email_dest')],
            [sg.Button('Enviar')]
        ]
        window_get = sg.Window('Cadastrar email', layout=layout, finalize=True)
        self.button, self.values = window_get.Read()

    def iniciar(self):
        email_dest = self.values['email_dest']
        print(f'Email cadastrado: {email_dest}')
        with open('emails.txt', 'a') as arquivo:
            arquivo.writelines(email_dest + ";")


tela_cadastro = TelaCadastro()
tela_cadastro.iniciar()
