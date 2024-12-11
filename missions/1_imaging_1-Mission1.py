##########################################################################
## 미션 1 
## - 적당한 이미지를 다운받아 3가지 플래그를 적용하고 3개의 창에 띄우시오.
## - 저장한 이미지의 shape 을 출력하세요
## - 회색조 이미지를 저장하세요
## - 키보드 입력이 있을 때까지 대기하도록 하세요
## - 열린 모든 창을 닫으세요.
##########################################################################
import cv2

img_path = './free_img/christmas-tree.jpg'
default_img = cv2.imread(img_path, cv2.IMREAD_COLOR)
gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
unchange_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

dict_img = { 'color': default_img, 'gray': gray_img, 'unchange': unchange_img}

for key in dict_img.keys():
    print(dict_img.get(key).shape)
    cv2.imshow(key, dict_img.get(key))

cv2.waitKey(0)
cv2.destroyAllWindows()
