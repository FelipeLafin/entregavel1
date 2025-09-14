# Ficha Técnica do Projeto

## Integrantes do Grupo
- Felipe Lafin
- Lucas Costa
- Ana Karolina

## Repositório Github
[Link para o repositório](https://github.com/FelipeLafin/entregavel1)  

---

## Aplicações

### **Projeto**
**Elevator Pitch:**

**Detecção de imagens:**

Esse código faz a detecção automática de frutas em uma imagem usando técnicas de visão computacional. Primeiro, ele carrega a imagem e converte para tons de cinza. Depois, aplica uma binarização para separar as frutas do fundo. Para melhorar a qualidade da segmentação, ele usa operações morfológicas: fecha pequenos buracos dentro das frutas e remove ruídos isolados fora delas.
Em seguida, o algoritmo identifica cada objeto na imagem através de componentes conectados, calcula sua área, desenha a caixa delimitadora (bounding box) em verde e marca o centróide em vermelho. No final, temos uma imagem anotada onde cada fruta aparece destacada com seu número e posição, e no terminal vemos quantos objetos foram detectados.

**Convolução:**

Desenvolvemos um código que utiliza a operação matemática de convolução para aplicar diferentes filtros em imagens, como motion blur, sharpen e realce de bordas.
O projeto demonstra, na prática, como funciona a matemática que gera transformações visuais no processamento de imagens.

**Como Rodar:**  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/FelipeLafin/entregavel1.git
   ```  
2. Entre na pasta do projeto:  
   ```bash
   cd entregavel1
   ```  
3. Crie e ative um ambiente virtual:  
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```  
4. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```  
5. Execute a aplicação das 5 frutas:  
   ```bash
   python 5frutas.py
   ```  
6. Execute a aplicação das 7 frutas:  
   ```bash
   python 7frutas.py
   ```
7. Execute a aplicação das convoluções:  
   ```bash
   python main_convolucao.py
   ```  
---

## Observações
- Certifique-se de ter o Python 3.13+ instalado.
- Certifique-se de colocar o caminho correto das imagens caso mude
- É de extrema importancia que siga estes passos para a execução correta do projeto!
