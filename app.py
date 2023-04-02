import win32com.client as win32
import os
from time import sleep

def enviaEmail(arquivo):
    outlook = win32.Dispatch('outlook.application')

    email = outlook.CreateItem(0)

    with open(f'arquivos/{arquivo}', 'r', encoding = 'UTF-8') as arq:
        linhas = arq.readlines()
        for i in linhas:
            if "Email :" in i:
                receptor = i
            if "Assunto a ser colocado no email :" in i:
                assunto = i
    
    receptor = receptor.split(':')[1].strip()
    assunto = assunto.split(':')[1].strip()

    with open('curriculum.html', 'r', encoding='UTF-8') as arq:
        conteudo = arq.read()

    email.To = receptor
    email.Subject = assunto
    email. HTMLBody = conteudo

    email.Send()

    print(f'Email enviado com sucesso para {receptor}')
    sleep(30)
    
pasta = os.listdir('arquivos/')

for arquivo in pasta:
    enviaEmail(arquivo)