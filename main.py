import cv2 as cv

# lendo a imagem
img = cv.imread('assets/baboon.jpg')

# declarando variáveis globais
clicado = False
r = g = b = 0

# obtendo x e y quando houver duplo clique do mouse em um pixel específico
def desenhar_cor_na_tela(evento, x, y, flags, param):
    if evento == cv.EVENT_LBUTTONDBLCLK:
        global r, g, b, clicado
        clicado = True
        b, g, r = img[y,x]
        r, g, b = int(r), int(g), int(b)

# criando janela para exibição
cv.namedWindow('imagem')

# cofigurando função de retorno quando houver clique do mouse
cv.setMouseCallback('imagem', desenhar_cor_na_tela)
       
while True:
    # mostrando o a imagem na janela        
    cv.imshow('imagem', img)

    if clicado:
        # criando o retângulo com a cor clicada pelo mouse
        cv.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        # retornando o código hexadecimal
        texto = 'cor em hexadecimal' 
            
        # colocando o texto na tela
        cv.putText(img, texto, (50,50), 2, 0.8, (255,255,255), 2, cv.LINE_AA)

        clicado = False

    # parando o loop ao apertar a tecla 'esc'    
    if cv.waitKey(20) & 0xFF == 27:
        break

# liberando os recursos
cv.destroyAllWindows()