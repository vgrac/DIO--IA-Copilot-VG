import pytesseract
import cv2

# Passo 1: ler a imagem
imagem = cv2.imread("Caderno de estudos digital.PNG")

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
else:
    # Caminho para o executável do Tesseract
    caminho = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = caminho

    # Passo 2: pedir pro Tesseract extrair o texto da imagem
    texto = pytesseract.image_to_string(imagem)
    print(texto)
