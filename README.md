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
1. Baixe o instalador `.exe` (versão 5.x ou superior) em: [UB-Mannheim Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki).
2. Durante a instalação, expanda a seção **"Additional script data"** e marque a opção **"Portuguese"** (para reconhecer acentos e cedilha).
3. **⚠️ Importante:** Após instalar, adicione o caminho da pasta de instalação (ex: `C:\Program Files\Tesseract-OCR`) às suas **Variáveis de Ambiente (PATH)** do Windows. Reinicie o terminal após isso.

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
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio

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

