# this file verifyes if the files contains repeated information

import os

folder = os.listdir("../arquivos")
emails = {}
for file in folder:
    with open(f'../arquivos/{file}', 'r', encoding='UTF-8') as arq:
        linhas = arq.readlines()
        for lin in linhas:
            if "Email :" in lin:
                mail = lin.split(':')[1].strip()
            if "Assunto a ser colocado no email :" in lin:
                assunto = lin.split(':')[1].strip()
        if assunto == None: assunto = 0
        for x in emails:
            if mail in emails[x][0]:
                print(f"the file {x} and {file} has the same email ({mail})")
                if assunto != 0 and assunto in emails[x][1]:
                    print(f'\tAnd the same subject: "{assunto}"')
               
        emails[file] = [mail,assunto]
print('All files checked')