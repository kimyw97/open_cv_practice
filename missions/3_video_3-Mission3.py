# OpenCV를 사용하여 웹캠에서 실시간 비디오를 캡처하고, 반전된 화면을 녹화하여 AVI 형식으로 저장

###################################################################################
# 미션 3: 
#    - 웹캠에서 실시간으로 비디오를 캡처하여 'images/capture.avi' 파일로 저장하세요
#    - 저장 조건:
#        - 해상도: 640x480
#        - 프레임 속도: 25 FPS
#        - 코덱: 'DIVX' 사용
#    - 캡처한 영상에 좌우 반전 효과를 적용하세요
#    - 'q' 키를 누르면 프로그램이 종료되도록 구현하세요
###################################################################################
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    file_path = './record.avi'     # 저장할 파일 경로 이름 
    fps = 25.0                     # FPS, 초당 프레임 수
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 인코딩 포맷 문자
    size = (640,840)                        # 프레임 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size)     # VideoWriter 객체 생성
    while True:
        rat, frame = cap.read()
        if rat:
            cv2.imshow('web', frame)
            out.write(frame)                                # 현재 프레임 저장-파일 저장
            if cv2.waitKey(int(1000/fps)) != -1: 
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()