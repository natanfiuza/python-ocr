import os
import argparse
import platform
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path

class ConversorOcr:
    """Classe responsável por gerenciar a conversão de imagens para texto."""

    def __init__(self, diretorio_alvo):
        self.diretorio_alvo = Path(diretorio_alvo)
        # Extensões comuns de imagem que vamos processar
        self.extensoes_suportadas = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff'}
        # Valida o ambiente logo ao iniciar a classe
        self.validar_ambiente()
    
    def validar_ambiente(self):
        """
        Verifica se as variáveis de ambiente necessárias estão configuradas,
        especialmente para usuários Windows.
        """
        sistema_operacional = platform.system() # Retorna 'Windows', 'Linux' ou 'Darwin' (Mac)

        # No Windows, a variável TESSDATA_PREFIX é crítica
        if sistema_operacional == 'Windows':
            tessdata_prefix = os.environ.get('TESSDATA_PREFIX')
            
            if not tessdata_prefix:
                print("⚠️  AVISO CRÍTICO: Variável de ambiente 'TESSDATA_PREFIX' não encontrada!")
                print("   No Windows, é necessário configurar esta variável apontando para a pasta 'tessdata'.")
                print("   Exemplo: C:\\Program Files\\Tesseract-OCR\\tessdata")
                # Dependendo da rigidez, você pode lançar um erro aqui:
                # raise EnvironmentError("Variável TESSDATA_PREFIX não configurada.")
            else:
                print(f"✅ Ambiente Windows detectado. Tesseract configurado em: {tessdata_prefix}")

    def gerar_configuracao_tesseract(self):
        """
        Gera a string de configuração do Tesseract baseada no SO e nas variáveis de ambiente.
        Retorna a string de configuração dinâmica.
        """
        # Configurações base (psm 6 assume um bloco de texto único, bom para documentos)
        #return "--psm 6"
        return ""

    def processar_arquivos(self):
        """Varre o diretório e inicia a conversão de cada imagem encontrada."""
        if not self.diretorio_alvo.exists():
            print(f"Erro: O diretório '{self.diretorio_alvo}' não existe.")
            return

        arquivos = [f for f in self.diretorio_alvo.iterdir() if f.suffix.lower() in self.extensoes_suportadas]
        
        if not arquivos:
            print("Nenhuma imagem encontrada para processar.")
            return

        print(f"Localizados {len(arquivos)} arquivos. Iniciando OCR...")

        for arquivo_imagem in arquivos:
            self.converter_imagem_para_txt(arquivo_imagem)

    def converter_imagem_para_txt(self, caminho_imagem):
        """Lê a imagem, extrai o texto e salva em um arquivo .txt de mesmo nome."""
        try:
            # Abre a imagem original
            imagem_original = Image.open(caminho_imagem)            
          

            # Configurações extras do Tesseract (PSM)
            # Chamamos o método que constrói a string dinamicamente
            config_dinamica = self.gerar_configuracao_tesseract()

            texto_extraido = pytesseract.image_to_string(
                imagem_original, 
                lang='por', 
                config=config_dinamica
            )

        
            # Define o nome do novo arquivo (ex: foto.png -> foto.txt)
            caminho_txt = caminho_imagem.with_suffix('.txt')

            # Salva o resultado
            with open(caminho_txt, 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write(texto_extraido)

            print(f"Sucesso: {caminho_imagem.name} -> {caminho_txt.name}")

        except Exception as erro:
            print(f"Falha ao processar {caminho_imagem.name}: {erro}")

def main():
    # Configuração dos argumentos de linha de comando (CLI)
    parser = argparse.ArgumentParser(description="Script didático de OCR para estagiários.")
    
    # Opção -d <pasta> ou padrão para o diretório atual (.)
    parser.add_argument(
        "-d", "--diretorio", 
        type=str, 
        default=".", 
        help="Caminho da pasta com as imagens (Padrão: diretório atual)"
    )

    args = parser.parse_args()

    # Instancia a classe e executa o processo
    processador = ConversorOcr(args.diretorio)
    processador.processar_arquivos()

if __name__ == "__main__":
    main()