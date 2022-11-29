import cv2 

imagen = cv2.imread('2.png') 
  
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
 
contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
  
for contorno in contornos:
    epsilon = 0.01*cv2.arcLength(contorno,True)
    approx = cv2.approxPolyDP(contorno,epsilon,True)

    x,y,w,h = cv2.boundingRect(approx)

    if len(approx)==3:
        cv2.putText(imagen,'Triangulo', (x,y-5),1,1,(255,0,0),1)

    if len(approx)==4:
        aspect_ratio = float(w)/h
        if aspect_ratio == 1:
            cv2.putText(imagen,'Cuadrado', (x,y-5),1,1,(255,0,0),1)
        else:
            cv2.putText(imagen,'Rectangulo', (x,y-5),1,1,(255,0,0),1)

    if len(approx)==5:
        cv2.putText(imagen,'Pentagono', (x,y-5),1,1,(255,0,0),1)

    if len(approx)==6:
        cv2.putText(imagen,'Hexagono', (x,y-5),1,1,(255,0,0),1)

    if len(approx)>10:
        cv2.putText(imagen,'Circulo', (x,y-5),1,1,(255,0,0),1)


        
    cv2.drawContours(imagen, [approx], 0, (255,0,0),2)
    cv2.imshow('image',imagen)
    cv2.waitKey(0)
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 