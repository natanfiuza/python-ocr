import pytesseract
from PIL import Image

# 1. Carregamos a imagem (ex: um print de um erro de código)
caminho_imagem = "pagina_manual.png"
imagem = Image.open(caminho_imagem)

# 2. Chamamos o motor de OCR
# Como você prefere snake_case, vamos nomear a variável assim:
texto_extraido = pytesseract.image_to_string(imagem, lang='por')

print(f"Texto detectado:\n{texto_extraido}")