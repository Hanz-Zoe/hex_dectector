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

cv.namedWindow('imagem')
cv.setMouseCallback('imagem', desenhar_cor_na_tela)
       
while 1:        
    cv.imshow('imagem', img)

    if clicado:
        # cria o retângulo com a cor clicada pelo mouse
        cv.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        # retorna o código hexadecimal
        texto = 'cor em hexadecimal' 
            
        # coloca o texto na tela
        cv.putText(img, texto, (50,50), 2, 0.8, (255,255,255), 2, cv.LINE_AA)

        clicado = False

    # para o loop ao apertar a tecla 'esc'    
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()