import os
import argparse
import pytesseract
from PIL import Image
from pathlib import Path

class ConversorOcr:
    """Classe responsável por gerenciar a conversão de imagens para texto."""

    def __init__(self, diretorio_alvo):
        self.diretorio_alvo = Path(diretorio_alvo)
        # Extensões comuns de imagem que vamos processar
        self.extensoes_suportadas = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff'}
        
    def preparar_imagem(self, imagem):
        """
        Aplica filtros para melhorar a legibilidade para o OCR.
        Converte para escala de cinza e aumenta o contraste (Binarização simples).
        """
        # 1. Converte para Escala de Cinza (remove cores que atrapalham)
        imagem = imagem.convert('L')

        # 2. Aumenta o contraste drasticamente para separar letras do fundo
        # Isso ajuda a transformar o cinza claro em branco e cinza escuro em preto
        enhancer = ImageEnhance.Contrast(imagem)
        imagem = enhancer.enhance(2)  # Aumenta o contraste em 2x

        # 3. (Opcional) Aumenta a nitidez para "borda" das letras
        imagem = imagem.filter(ImageFilter.SHARPEN)
        
        # 4. Binarização (Threshold) manual para garantir preto e branco puro
        # Tudo que for mais claro que 128 vira branco (255), o resto vira preto (0)
        imagem = imagem.point(lambda x: 0 if x < 140 else 255, '1')

        # Dica Didática: Salve essa imagem temporária para mostrar aos estagiários
        # imagem.save("debug_imagem_processada.png")
        
        return imagem

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
            # 1. Abre a imagem usando a biblioteca Pillow
            imagem_aberta = Image.open(caminho_imagem)

            # 2. Executa o OCR (ajustado para Português)
            texto_extraido = pytesseract.image_to_string(imagem_aberta, lang='por')

            # 3. Define o nome do novo arquivo (ex: foto.png -> foto.txt)
            caminho_txt = caminho_imagem.with_suffix('.txt')

            # 4. Salva o resultado
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