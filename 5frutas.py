import cv2               
import numpy as np       

img = cv2.imread("images/fruits5.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #tons de cinza

_, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV) #converto pra binário (acima de 190 vira preto, abaixo vira branco invertido)

#kernel em formato de cruz para operações morfológicas
kernel = np.array(([0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]), np.uint8)

binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1) #preecho pequenos buracos dentro dos objetos (cv2.MORPH_CLOSE)

binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2) #preecho pequenos buracos fora dos objetos (cv2.MORPH_OPEN) 

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary) #procuro regiões conectadas com o cv2.connectedComponentsWithStats 
# Retorna:
# - num_labels: quantidade de componentes encontrados (inclui o fundo)
# - labels: matriz com o índice do componente para cada pixel
# - stats: informações de cada componente (x, y, largura, altura, área, etc.)
# - centroids: coordenadas (x, y) do centro de massa de cada componente

img_out = img.copy()
count = 0 #contador de objetos detectados
min_area = 1000 #area mínima para considerar um objeto válido (evita detectar ruídos pequenos)

#loop para percorrer todos os componentes detectados (ignorando o fundo, índice 0)
for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]   #area do objeto atual
    if area > min_area:                 #só considera se a área for maior que o mínimo
        count += 1                      #incrementa contador
        x, y, w, h, _ = stats[i]        #pega bounding box do objeto (posição e tamanho)
        cx, cy = map(int, centroids[i]) #converte coordenadas do centróide para inteiros

        #desenha retângulo (bounding box) ao redor do objeto
        cv2.rectangle(img_out, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #desenha círculo vermelho no centro (centróide)
        cv2.circle(img_out, (cx, cy), 4, (0, 0, 255), -1)

        #escreve o nome do objeto acima da caixa
        cv2.putText(img_out, f"Objeto {count}", (x, y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

print("Objetos detectados:", count)

cv2.imshow('Binaria limpa', binary)    
cv2.imshow('Deteccao final', img_out) 
cv2.waitKey(0)                        
cv2.destroyAllWindows()             
