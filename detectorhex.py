import numpy as np
import cv2 as cv 
from webcam import Webcam

class Hexdectector :
    Webcam
    if not cv.isOpened(): 
        raise RuntimeError('error openinf VideoCapture')

    (grabbed, frame) = capture.read() 
    snapshot = np.zeros(frame.shape, dtype=np.uint8)
    cv.imshow('snapshot',snapshot)
    
    ColorArray = np.zeros((COLOR_ROWS,COLOR_COLS, 3), dtype=np.uint8)
    cv.imshow('color', ColorArray)