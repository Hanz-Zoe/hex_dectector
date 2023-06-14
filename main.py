import cv2 as cv

# Reading the image with opencv
img = cv.imread('assets/baboon.jpg')

# declarando variáveis globais
clicked = False
r = g = b = xpos = ypos = 0

# função para obter x, y quando houver clique do mouse
def draw_function(event, x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv.namedWindow('imagem')
cv.setMouseCallback('imagem',draw_function)
       
while(1):        

    cv.imshow("imagem", img)

    if (clicked):
        # cria o retângulo com a cor clicada pelo mouse
        cv.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        # retorna o código hexadecimal
        text = 'cor em hexadecimal' 
            
        # coloca o texto na tela
        cv.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv.LINE_AA)

        clicked = False

    # para o loop ao apertar a tecla 'esc'    
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()