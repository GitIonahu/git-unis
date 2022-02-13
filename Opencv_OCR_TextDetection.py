import cv2
import numpy as np
import requests
import io
import json

# img = cv2.imread("Resources/screenshot.jpg")
img = cv2.imread("screenshot.jpg")
# print(img.shape)
height,width,_=img.shape
# print(img)

# Cutting image
roi = img[0:height,400:width]
#OCR
url_api = "https://api.ocr.space/parse/image"
_,compressedimage = cv2.imencode(".jpg",roi,[1,90])
file_bytes = io.BytesIO(compressedimage)


result = requests.post(url_api,files = {"screenshot.jpg":file_bytes},
              data={"apikey":"Helloworld"})

result = result.content.decode()
result = json.loads(result)

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)




cv2.imshow('Roi',roi)

cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()