import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread("images\\fruits7.png")
output = img.copy()

# Converte para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Cria a máscara para segmentação
mask = cv2.inRange(hsv, np.array([0,50,50]), np.array([180,255,255]))

# Remove ruídos
kernel = np.ones((5,5), np.uint8)
imagem_mascarada = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
imagem_mascarada = cv2.erode(imagem_mascarada, kernel, iterations=2)

# Detecta componentes conectados
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(imagem_mascarada)

# Loop para cada componente detectado (pulando o fundo, que é label 0)
for i in range(1, num_labels):
    x, y, w, h, area = stats[i]      # bounding box + área
    cx, cy = centroids[i]            # centróide

    # Desenha retângulo verde ao redor do objeto
    cv2.rectangle(output, (x, y), (x+w, y+h), (0,255,0), 2)

    # Desenha círculo vermelho no centróide
    cv2.circle(output, (int(cx), int(cy)), 5, (0,0,255), -1)

    # Escreve o texto acima do objeto
    cv2.putText(output, f"Fruta {i}", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))

cv2.imshow("Deteccao de Frutas", output)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
