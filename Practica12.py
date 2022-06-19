import cv2
import numpy as np
import imutils

img = cv2.imread('editada.jpg')

a = [ [ 1, 2, 1 ],
    [ 2, 4, 2 ],
    [ 1, 2, 1 ] ]

kernel = (1)*np.asarray(a)

dst = cv2.filter2D(img, -1, kernel)
cv2.imshow('Convolucion', dst)
cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
