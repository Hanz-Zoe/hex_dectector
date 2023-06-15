import cv2 as cv
import numpy as np

# lendo a imagem
img = cv.imread('assets/baboon.jpg')

# obtendo x e y quando houver duplo clique do mouse em um pixel específico
def desenhar_cor_na_tela(evento, x, y, flags, param):
    if evento == cv.EVENT_LBUTTONDBLCLK:
        # atribuindo o rgb a variáveis
        cor_pixel = img[y, x]
        b, g, r = img[y,x]
        
        # definindo tamanho e cor da imagem na nova janela
        janela_cor_pixel = np.zeros((50, 50, 3), np.uint8)
        janela_cor_pixel[:] = cor_pixel

        # convertendo o rgb para hexadecimal
        cor_hexadecimal = converte_rgb_para_hexadecimal(r, g, b)

        # mostrando nova janela com código hexadecimal e cor do pixel selecionado
        cv.imshow(cor_hexadecimal, janela_cor_pixel)

# função a ser desenvolvida por vinicius
def converte_rgb_para_hexadecimal(r, g, b):
    return 'hexadecimal'


# criando janela para exibição
cv.namedWindow('imagem')

# cofigurando função de retorno quando houver clique do mouse
cv.setMouseCallback('imagem', desenhar_cor_na_tela)
       
while True:
    # mostrando o a imagem na janela        
    cv.imshow('imagem', img)

    # parando o loop ao apertar a tecla 'esc'    
    if cv.waitKey(20) & 0xFF == 27:
        break

# liberando os recursos
cv.destroyAllWindows()