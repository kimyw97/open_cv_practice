###################################################################################
# 미션 2: 
#    - images/person_4.jpg 에서 하단의 공(ROI)을 복사하세요
#    - ROI: img[행 시작:끝, 열 시작:끝]
#    - 복사한 공을 본 이미지의 공 하단으로 복사하여 이미지에 공을 2개로 보이도록 하세요
#    - 주의: 행열의 폭이 일치해야함  
###################################################################################
import cv2
img = cv2.imread('./free_img/person_4.jpg')
x,y,w,h = cv2.selectROI('img',img, False)
copied_img = img[y: y+h, x: x+w]
img[y+ h: y + h +h, x: x + w] = copied_img
cv2.imshow('new',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




