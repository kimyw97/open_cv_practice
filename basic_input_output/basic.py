import cv2
file_name = './free_img/christmas-tree-2928142_1280.jpg'
rgb_img = cv2.imread(file_name)
print(rgb_img.shape)
print(rgb_img[2])

# 얼굴 및 눈 검출 Haar Cascade 파일 로드
# CascadeClassifier: 객체 감지용 클래스
# Haar, LBP 기반 객체 감지 모델을 사용
# 따라서 사전 학습된 XML 파일이 필요
# 기본 xml들은 cv2에서 가지고 있음
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# 비디오 열때 사용하는 함수, 0 이면 웹캠, 다른 비디오를 열고 싶으면 
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('cam opening is failed')

while 1:
    ret, frame = cap.read()
    if not ret:
        print("Can't read frame")
        break

    # 회색조로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #특정 객체 감지용 메서드
    #인자(순서대로)
    #image: 감지할 이미지
    #scaleFactor: 이미지 크기 조정 비율, 1.1이 10% 축소하며 탐지
    #minNeighbors: 후보 객체 주변에 감지된 객체 수, 기본값 3
    #flags: 특정 플래그 값을 설정해서 감지 동작 제어
    #minSize: 탐지할 객체 최소 크기, 튜플 형태로 지정
    #maxSize: 최대 크기, 튜플 형태로 지정
    #return (x,y,w,h)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # 얼굴에 사각형 그리기
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 얼굴 영역에서 눈 검출
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # 눈에 사각형 그리기
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    cv2.imshow('karios', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('break')
        break
#아래 두 함수는 반드시 필요    
#카메라 객체 해제
cap.release()
#opencv 모든 윈도우 제거
cv2.destroyAllWindows()