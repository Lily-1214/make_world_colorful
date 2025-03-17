import cv2
import numpy as np

# 비디오 캡처 객체 생성 (기본 웹캠: 0)
cap = cv2.VideoCapture(0)

# 비디오 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정 (XVID)
fps = 20.0  # 초당 프레임 설정
frame_size = (int(cap.get(3)), int(cap.get(4)))  # 프레임 크기 가져오기
out = cv2.VideoWriter('recorded_video.avi', fourcc, fps, frame_size)

recording = False  # 녹화 상태 변수
grayscale = False  # 흑백 모드 여부
invert = False  # 색 반전 모드 여부
contrast = 1.0  # 초기 색 대비 값 (1.0 = 기본값)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 프레임을 읽지 못하면 종료

    # 흑백 모드 적용
    if grayscale:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 흑백 변환
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # 저장을 위해 다시 3채널로 변환

    # 색 반전 적용
    if invert:
        frame = cv2.bitwise_not(frame)  # 색 반전

    # 색 대비 조절 (기본 대비: 1.0)
    frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=0)

    # 녹화 중이면 프레임 저장
    if recording:
        out.write(frame)
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)  # 빨간 원 표시 (녹화 중)

    cv2.imshow('Video Recorder', frame)  # 영상 출력

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키 -> 종료
        break
    elif key == 32:  # Space 키 -> 녹화 시작/정지
        recording = not recording  
    elif key == ord('g') or key == ord('G'):  # 'G' 키 -> 흑백 필터 적용/해제
        grayscale = not grayscale
    elif key == ord('c') or key == ord('C'):  # 'C' 키 -> 대비 증가
        contrast = min(contrast + 0.1, 3.0)  # 대비 최대 3.0 제한
    elif key == ord('v') or key == ord('V'):  # 'V' 키 -> 대비 감소
        contrast = max(contrast - 0.1, 0.5)  # 대비 최소 0.5 제한
    elif key == ord('i') or key == ord('I'):  # 'I' 키 -> 색 반전 적용/해제
        invert = not invert

# 정리 및 종료
cap.release()
out.release()
cv2.destroyAllWindows()
