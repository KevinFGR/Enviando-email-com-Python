#script para achar se alguma informação está dentro de algum arquivo da pasta arquivos
#caso haja alguma vaga que eu queira escluir mas não saiba em que arquivo está

import os

def main():
    char = input("insert sequence of characters you want to find:")
    print('finding ...')
    #try: 
    find(char)
    #except:
        #print('Ops, something went wrong.')

def find(char):
    dir = os.listdir('../arquivos/')
    for file in dir:
        with open(f'../arquivos/{file}', 'r', encoding='UTF-8') as arq:
            if char in arq.read():
                print(f"The content inputted is inside the file {file} \nverificating others files...")
    print('All files checked.')

if __name__ == "__main__":
    while True:
        print("\nPress ctrl+c if you want to exit.")
        try: main()
        except: 
            print("\nclosing program")
            exit()