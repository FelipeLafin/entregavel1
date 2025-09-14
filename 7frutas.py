import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread("images/fruits7.png")
output = img.copy()

# Converte para escala de cinza  usando BGR
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)

# Remove ruídos
kernel = np.ones((5, 5), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)
binary = cv2.erode(binary, kernel, iterations=1)

# Detecta componentes conectados
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

# Loop para cada componente (pulando fundo, label 0)
count = 0
for i in range(1, num_labels):
    x, y, w, h, area = stats[i]
    cx, cy = centroids[i]

    if area > 1000:  # filtra ruídos pequenos
        count += 1
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(output, (int(cx), int(cy)), 5, (0, 0, 255), -1)
        cv2.putText(output, f"Fruta {count}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

cv2.imshow("Deteccao de Frutas", output)
cv2.imshow("Binaria", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()