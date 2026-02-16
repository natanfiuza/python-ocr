# 📸 Conversor de Imagem para Texto (OCR)

Este é um projeto didático *open-source* criado para auxiliar estagiários, estudantes e desenvolvedores iniciantes a entenderem como utilizar bibliotecas de Processamento de Imagem e OCR (*Optical Character Recognition*) em Python.

O script varre um diretório, identifica imagens e gera automaticamente um arquivo `.txt` correspondente com o conteúdo de texto extraído.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído sobre o ombro de gigantes. Utilizamos as seguintes ferramentas:

* **[Python 3.10+](https://www.python.org/):** Linguagem base do projeto.
* **[Pipenv](https://pipenv.pypa.io/en/latest/):** Para gerenciamento moderno de dependências e ambiente virtual.
* **[Pillow (PIL)](https://python-pillow.org/):** Para manipulação e abertura dos arquivos de imagem.
* **[PyTesseract](https://github.com/madmaze/pytesseract):** Wrapper que permite ao Python "conversar" com o motor Tesseract.
* **[Tesseract OCR Engine](https://github.com/tesseract-ocr/tesseract):** O motor de IA (C++) que realiza a leitura dos caracteres.

---

## ⚙️ Pré-requisitos do Sistema (Obrigatório)

Antes de executar o projeto Python, você **precisa** ter o motor de OCR instalado no seu sistema operacional. O Python apenas envia a imagem para ele processar.

### 1. Instalando o Tesseract

#### **No Windows:**

1.  **Download:** Baixe o instalador `.exe` (versão 5.x ou superior) em: [UB-Mannheim Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki).
2.  **Instalação:** Durante a instalação, expanda a seção **"Additional script data"** e marque a opção **"Portuguese"** (para reconhecer acentos e cedilha).
3.  **Configuração de Variáveis (Essencial):**
    Para evitar erros como *"Tesseract not found"* ou *"Error opening data file"*, siga os passos abaixo:

    * Abra o Menu Iniciar e digite **"Editar as variáveis de ambiente do sistema"**.
    * Clique no botão **"Variáveis de Ambiente..."**.
    
    **Passo A: Adicionar ao PATH (Para o comando funcionar)**
    1.  Na lista **"Variáveis do sistema"**, encontre a variável **Path** e clique em **Editar**.
    2.  Clique em **Novo** e cole o caminho da instalação: 
        `C:\Program Files\Tesseract-OCR`
    3.  Dê OK.

    **Passo B: Adicionar TESSDATA_PREFIX (Para o idioma funcionar)**
    1.  Ainda em **"Variáveis do sistema"**, clique no botão **Novo...** (abaixo da lista).
    2.  **Nome da variável:** `TESSDATA_PREFIX`
    3.  **Valor da variável:** `C:\Program Files\Tesseract-OCR\tessdata`
    4.  Dê OK em tudo.

    > **Nota:** Reinicie seu terminal (VS Code, PowerShell ou CMD) para que as alterações tenham efeito.


#### **No Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-por -y
```

#### **No macOS:**

```bash
brew install tesseract
brew install tesseract-lang

```

---

## 🚀 Como Instalar e Rodar o Projeto

Utilizamos o **Pipenv** para garantir que todos trabalhem com as mesmas versões das bibliotecas.

### 1. Clonando o Repositório

```bash
git clone git@github.com:natanfiuza/python-ocr.git
cd python-ocr

```

### 2. Configurando o Ambiente

Se você ainda não tem o Pipenv, instale-o: `pip install pipenv --user`.

Na pasta do projeto, execute:

```bash
pipenv install

```

*Isso criará o ambiente virtual e instalará o `Pillow` e `pytesseract` automaticamente baseados no `Pipfile`.*

### 3. Ativando o Ambiente

Antes de rodar o script, ative o ambiente virtual:

```bash
pipenv shell

```

---

## 💻 Como Usar

Com o terminal dentro do ambiente virtual (`pipenv shell`), use o comando abaixo:

**Opção A: Ler imagens na pasta atual**

```bash
python leitor_ocr.py

```

**Opção B: Ler imagens de uma pasta específica**
Use a flag `-d` (directory) para indicar o caminho:

```bash
python leitor_ocr.py -d "C:/Meus Documentos/Prints"

```

O script gerará um arquivo `.txt` para cada imagem encontrada (ex: `erro_log.png` gera `erro_log.txt`).

---

## 🤝 Como Contribuir

Ficamos muito felizes com o seu interesse em melhorar este material didático! Siga os passos abaixo:

1. Faça um **Fork** deste repositório.
2. Crie uma **Branch** para sua modificação (`git checkout -b feature/melhoria-no-ocr`).
3. **Padrão de Código:**
* Utilize `snake_case` para nomes de variáveis e métodos (ex: `ler_imagem()`).
* Utilize `PascalCase` para nomes de Classes (ex: `ConversorOcr`).
* Comente seu código pensando que um iniciante irá lê-lo.


4. Faça o **Commit** (`git commit -m 'Adiciona suporte a PDFs'`).
5. Envie para o **Push** (`git push origin feature/melhoria-no-ocr`).
6. Abra um **Pull Request** explicando suas alterações.

---

## ✨ Agradecimentos

* A toda a comunidade **Open Source** que mantém o Tesseract e as bibliotecas Python.
* Aos meus alunos e estagiários, que inspiram a criação de conteúdos didáticos e ferramentas que facilitam o dia a dia.

---

## 📩 Contato

Se você tiver dúvidas, sugestões ou quiser trocar uma ideia sobre desenvolvimento e carreira:

**Nataniel Fiuza** 📧 E-mail: [contato@natanfiuza.dev.br](mailto:contato@natanfiuza.dev.br)

