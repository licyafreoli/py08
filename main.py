import os

def listar_arquivos():
    itens = os.listdir()
    
    print("Arquivos e pastas no diretório atual:")
    for item in itens:
        print(item)

listar_arquivos()