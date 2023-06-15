import cv2 as cv
import numpy as np

# pegando o vídeo
video_path = 'assets/video.mp4'
video = cv.VideoCapture(video_path)

# variáveis globais
r = g = b = 0 

# obtendo x e y quando houver duplo clique do mouse em um pixel específico
def desenhar_cor_na_tela(evento, x, y, flags, param):
    if evento == cv.EVENT_LBUTTONDBLCLK:
        global r, g, b

        # atribuindo o rgb a variáveis
        cor_pixel = frame[y, x]
        b, g, r = frame[y,x]
        
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
cv.namedWindow('video')

# cofigurando função de retorno quando houver clique do mouse
cv.setMouseCallback('video', desenhar_cor_na_tela)
       
while video.isOpened():
    sucesso, frame = video.read()

    if not sucesso:
        break

    # mostrando video
    cv.imshow('video', frame)

    # cofigurando função de retorno quando houver clique do mouse
    cv.setMouseCallback('video', desenhar_cor_na_tela)

    if cv.waitKey(10) & 0xFF == ord(' '):
        # pausando o vídeo
        while True:
            key = cv.waitKey(1)
            if cv.waitKey(1) & 0xFF == ord(' '):
                # resumindo o vídeo
                break

    # parando o loop ao apertar a tecla 'esc'    
    if cv.waitKey(10) & 0xFF == 27:
        break

# liberando os recursos
video.release
cv.destroyAllWindows()