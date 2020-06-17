import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Dark')
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(5, 0), key='idade')],
            [sg.Text('Quais provedores de emails são aceitos?')],
            [
             sg.Checkbox('Gmail', key='gmail'),
             sg.Checkbox('Outlook', key='outlook'),
             sg.Checkbox('Yahoo', key='yahoo')
             ],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30, 20))]
        ]

        self.janela = sg.Window('Dados do Usuário').layout(layout)

    def iniciar(self):
        while True:
            self.button, self.valor = self.janela.Read()
            nome = self.valor['nome']
            idade = self.valor['idade']
            aceita_gmail = self.valor['gmail']
            aceita_outlook = self.valor['outlook']
            aceita_yahoo = self.valor['yahoo']
            aceita_cartao= self.valor['aceitaCartao']
            nao_aceita_cartao = self.valor['naoAceitaCartao']
            velocidade_script = self.valor['sliderVelocidade']

            print('Nome:', nome)
            print('Idade:',idade)
            print('Aceita Gmail:',aceita_gmail)
            print('Aceita Outlook:',aceita_outlook)
            print('Aceita Yahoo:',aceita_yahoo)
            print('Aceita Cartão:',aceita_cartao)
            print('Não aceita cartão:',nao_aceita_cartao)
            print('Velocidade Script:', velocidade_script)

tela = TelaPython()
tela.iniciar()
