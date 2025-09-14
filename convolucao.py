import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time


def pixel(matrix_img, kernel):

    soma_vermelho = 0
    soma_verde = 0
    soma_azul = 0

    altura = len(matrix_img)
    comprimento = len(matrix_img[0])

    for linha in range(altura):
        for coluna in range(comprimento):
            valor_kernel = kernel[linha][coluna]
            pixel = matrix_img[linha][coluna]
            soma_vermelho += pixel[0] * valor_kernel
            soma_verde += pixel[1] * valor_kernel
            soma_azul += pixel[2] * valor_kernel
    return [soma_vermelho, soma_verde, soma_azul]

def kernel_has_float(kernel):
    for linha in kernel:
        for numero in linha:
            if isinstance(numero, (float, np.floating)):
                return True
    return False

def convolucao(img_path, kernel):

    tempo_inicial = time.time()

    kernel_float = kernel_has_float(kernel)

    if kernel_float:
        img = np.array(Image.open(img_path).convert('RGB')).astype(np.float32) / 255.0
    else:
        img = np.array(Image.open(img_path).convert('RGB'))

    altura_image = img.shape[0]
    comprimento_image = img.shape[1]
    altura_kernel = len(kernel)
    comprimento_kernel = len(kernel[0])

    index_linha = 0
    index_coluna = 0

    matrix_resultante = []
    linha = []
    while True:

        matrix_image_spliced = img[index_linha:altura_kernel + index_linha, index_coluna:comprimento_kernel + index_coluna]
        linha.append(pixel(matrix_image_spliced, kernel))
        index_coluna += 1

        if index_coluna + comprimento_kernel > comprimento_image:
            index_coluna = 0
            index_linha += 1
            matrix_resultante.append(linha)
            linha = []

        if index_linha + altura_kernel > altura_image:
            break


    tempo_final = time.time()
    tempo_total = str(tempo_final - tempo_inicial)

    if kernel_float:
        matrix_resultante = (np.clip(matrix_resultante, 0, 1) * 255).astype(np.uint8)

    plt.imshow(matrix_resultante)

    plt.text(1, 60, tempo_total, fontfamily= 'sans-serif' ,size= 'large' ,color= 'yellow')

    plt.title('Imagem Convolucionada')
    plt.show()


    return 0

kernel = np.array([
    [-2,-1,0],
    [-1, 1,1],
    [ 0, 1,2]])
convolucao('images\\templo.jpg', kernel)

