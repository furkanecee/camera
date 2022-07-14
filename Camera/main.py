import cv2
kamera = cv2.VideoCapture(0)

cv2.namedWindow("Kamera")

sayac = 0

while True:
    ret, frame = kamera.read()
    if not ret:
        print("Ret Hata")
        break  
    cv2.imshow("Kamera",frame)
    
    anahtar = cv2.waitKey(1)
    if anahtar == ord('q'):
        print("Programdan Çıkış Yaptınız")
        break
    
    elif anahtar == ord('p'):
        dosya_adi = 'resim/foto_{}.png'.format(sayac)
        cv2.imwrite(dosya_adi, frame)
        sayac += 1
            
kamera.release()
cv2.destroyAllWindows()
