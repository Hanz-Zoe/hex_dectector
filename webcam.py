import cv2 as cv

class Webcam:
    def __init__(self):
        self.webcam = cv.VideoCapture(1)

    def __del__(self):
        self.webcam.release()

    def start(self):
        webcam = cv.VideoCapture(0)
        if webcam.isOpened():
            validacao, frame = webcam.read()
            while validacao:
                validacao, frame = webcam.read()
                cv.imshow("Webcam", frame)
                key = cv.waitKey(5)
                if key == 27:
                    break 
        cv.destroyAllWindows()
