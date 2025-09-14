import time

import cv2
import numpy as np
from convolucao import convolucao


#Os Kernels que estão comentados, são somente variações do que foi utilizado

def mostrar_imagens(nome_da_janela, imagem, caminho_da_imagem, kernel):
    tempo_inicial = time.time()

    imagem = cv2.filter2D(imagem, -1, kernel)

    tempo_final = time.time()
    tempo_total = str(tempo_final - tempo_inicial)
    cv2.putText(imagem, tempo_total, (1,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.imshow(nome_da_janela, imagem)
    convolucao(caminho_da_imagem, kernel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_path = 'templo1.jpg'
img = cv2.imread(img_path)

#-------------------------------------------------------------

kernel_emboss = np.array([[-2,-1,0],
                          [-1, 1,1],
                          [ 0, 1,2]])

mostrar_imagens("Kernel emboss", img, img_path, kernel_emboss)


#1
# Não notei diferenca nos resultados mas o tempo da função da convolução que criei é bem mais lento

#-------------------------------------------------------------

#motion blur
motion_blur = np.array([
    [1/5, 0, 0, 0, 0],
    [0, 1/5, 0, 0, 0],
    [0, 0, 1/5, 0, 0],
    [0, 0, 0, 1/5, 0],
    [0, 0, 0, 0, 1/5]
])

#motion_blur = np.array([
#    [1/5, 0, 0],
#    [0, 1/5, 0],
#    [0, 0, 1/5]
#])

mostrar_imagens("Motion_blur", img, img_path, motion_blur)

#-------------------------------------------------------------

#desfoque gaussiano

desfoque_gaussian = np.array([
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16]
])

mostrar_imagens("Desfoque Gaussian", img, img_path, desfoque_gaussian)
#-------------------------------------------------------------

#Emboss diagonal
blur = np.array([
    [1/9, 1/9,  1/9],
    [1/9,  1/9,  1/9],
    [1/9,  1/9,  1/9]
])

mostrar_imagens("Blur", img, img_path, blur)

#-------------------------------------------------------------
#sharpen

#sharpen = np.array([[-2, 0, 0, 0, -2],
#[0, -1, 0, -1, 0],
#[0, 0, 13, 0, 0],
#[0, -1, 0, -1, 0],
#[-2, 0, 0, 0, -2]])

sharpen = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])


mostrar_imagens("Sharpen", img, img_path, sharpen)

#-------------------------------------------------------------
#deteccao de bordas

deteccao_de_bordas = np.array([[-1, -1, -1],
[-1, 8, -1],
[-1, -1, -1]])

mostrar_imagens("deteccao de bordas", img, img_path, deteccao_de_bordas)
