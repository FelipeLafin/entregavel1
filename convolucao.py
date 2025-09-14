import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time


def pixel(matrix_img, kernel):

    # A soma que armazena o valor total final do novo pixel
    # Existe uma soma para cada canal de cor
    soma_vermelho = 0
    soma_verde = 0
    soma_azul = 0

    # Ve tanto a altura quando o comprimento da imagem(é o mesmo tamanho do kernel)
    altura = len(matrix_img)
    comprimento = len(matrix_img[0])

    #Começa a fazer as iterações
    for linha in range(altura):
        for coluna in range(comprimento):
            #Pega o valor do kernel para a iteração atual
            valor_kernel = kernel[linha][coluna]
            #Pega o valor do pixel da imagem, na iteração atual
            # o pixel vai ser uma lista [R,G,B]
            pixel = matrix_img[linha][coluna]

            # Faz o calculo com o kernel para cada pixel
            soma_vermelho += pixel[0] * valor_kernel
            soma_verde += pixel[1] * valor_kernel
            soma_azul += pixel[2] * valor_kernel

    #Retorna o pixel
    #Vai ser no formato de uma lista [R,G,B]
    return [soma_vermelho, soma_verde, soma_azul]

def kernel_has_float(kernel):
    #Função para definir se o kernel tem algum float
    for linha in kernel:
        for numero in linha:
            if isinstance(numero, (float, np.floating)):
                return True
    return False

def convolucao(img_path, kernel):

    # Começa a contar a duração da criação da nova imagem
    tempo_inicial = time.time()
    #utiliza a função para definir se o kernel tem algum float
    kernel_float = kernel_has_float(kernel)

    if kernel_float:
        #converte o array da imagem para um tipo float
        img = np.array(Image.open(img_path).convert('RGB')).astype(np.float32) / 255.0
    else:
        #caso não tenha float, cria a imagem normalmente
        img = np.array(Image.open(img_path).convert('RGB'))

    #Define a altura e comprimento, tanto da imagem quanto do kernel
    altura_image = img.shape[0]
    comprimento_image = img.shape[1]
    altura_kernel = len(kernel)
    comprimento_kernel = len(kernel[0])

    #Começa uma contagem para a iteração
    index_linha = 0
    index_coluna = 0

    #Cria uma lista vazia que irá ser a imagem final, depois da convolução
    matrix_resultante = []
    #Uma lista vazia para cada nova linha da imagem da convolução
    linha = []

    while True:
        #Faz um slice da imagem original, do comprimento e altura do kernel com a posição sendo definida pelo index_linha e index_coluna
        matrix_image_spliced = img[index_linha:altura_kernel + index_linha, index_coluna:comprimento_kernel + index_coluna]
        #Aplica a função de pixel na lista aninhada criada acima, e da o append na linha
        #Agora essa linha tem um novo pixel, recebido como uma lista [R,G.B]
        linha.append(pixel(matrix_image_spliced, kernel))

        index_coluna += 1

        #Caso o comprimento do kernel + o index ultrapasse o comprimento da imagem, quer dizer que todas as colunas
        #da imagem ja foram convolucionadas
        if index_coluna + comprimento_kernel > comprimento_image:
            #Volta o index para a coluna inicial
            index_coluna = 0
            #passa para a linha de baixo
            index_linha += 1
            #Adiciona a nova linha de pixeis a matrix da imagem final
            matrix_resultante.append(linha)
            #Reseta a lista, para a criação de uma nova linha
            linha = []

        #Caso a altura do kernel + index ultrapasse a altura da imagem, quer dizer que todas as linhas foram convolucionada
        #encerrando o loop
        if index_linha + altura_kernel > altura_image:
            break

    #Tempo no qual a criação da nova imagem terminou
    tempo_final = time.time()
    #calculo para o tempo que a imagem demorou para se feita
    tempo_total = str(tempo_final - tempo_inicial)

    if kernel_float:
        #Faz o inverso de quanto alteramos os pixeis para float, trocando seu tipo para inteiros
        matrix_resultante = (np.clip(matrix_resultante, 0, 1) * 255).astype(np.uint8)

    #Demostra qual imagem é para ser demonstrada
    plt.imshow(matrix_resultante)

    #Escreve o tempo na imagem
    plt.text(1, 60, tempo_total, fontfamily= 'sans-serif' ,size= 'large' ,color= 'yellow')

    plt.title('Imagem Convolucionada')
    plt.show()


    return 0
