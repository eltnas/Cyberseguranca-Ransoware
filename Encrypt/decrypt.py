from cryptography.fernet import Fernet
import os

def carrega_chave():
    return open("chave.key", "rb").read()

def descriptografa_arquivos(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descritografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descritografados)

def encontra_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave=carrega_chave()
    arquivos=encontra_arquivos("test_files")
    for arquivo in arquivos:
        descriptografa_arquivos(arquivo, chave)
    print("Arquivos restaurados com sucesso!!!")

if __name__=="__main__":
    main()