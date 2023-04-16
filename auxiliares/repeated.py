# this file verifyes if the files contains repeated information

import os

folder = os.listdir("../arquivos/")
emails = {}
for file in folder:
    with open(f'../arquivos/{file}', 'r', encoding='UTF-8') as arq:
        linhas = arq.readlines()
        for lin in linhas:
            if "Email :" in lin:
                mail = lin.split(':')[1].strip()
                for x in emails:
                    if mail in emails[x]:
                        print(f"the file {x} and {file} has the same email ({mail})")
                emails[file] = mail
