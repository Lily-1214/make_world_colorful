# make world colorful

이름은 거창하지만 내용물은 대단하지 않습니다.
화면을 녹화하고, 간단한 필터를 씌울 수 있습니다!



## 녹화 설정값

xvid 코덱을 사용합니다.
fps는 20으로 고정입니다.

```python 
# 비디오 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정 (XVID)
fps = 20.0  # 초당 프레임 설정
frame_size = (int(cap.get(3)), int(cap.get(4)))  # 프레임 크기 가져오기
out = cv2.VideoWriter('recorded_video.avi', fourcc, fps, frame_size)
```



## 기본 기능

Space키를 눌러 녹화를 시작합니다.
Record모드가 활성화되면 화면 좌상단에 빨간 점이 표시됩니다.

<img width="826" alt="Image" src="https://github.com/user-attachments/assets/a910b575-2624-46f8-95b3-9df03a711f23" />

다시 Space키를 눌러 녹화를 종료할 수 있습니다.
Esc키를 눌러 프로그램을 종료하고, 영상이 자동으로 같은 디렉토리에 저장됩니다.



## 필터 기능

```python
grayscale = False  # 흑백 모드 여부
invert = False  # 색 반전 모드 여부
contrast = 1.0  # 초기 색 대비 값 (1.0 = 기본값)
```

필터 모드에 관련된 변수들입니다.

### 흑백 필터

```python
# 흑백 모드 적용
    if grayscale:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 흑백 변환
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # 저장을 위해 다시 3채널로 변환
--------------------------------------------------------------------------------------
    elif key == ord('g') or key == ord('G'):  # 'G' 키 -> 흑백 필터 적용/해제
        grayscale = not grayscale
```

<img width="835" alt="Image" src="https://github.com/user-attachments/assets/d92b3b98-bd75-4c0c-8b43-44fe6ed5755d" />

G키를 눌러 흑백 필터를 on/off할 수 있습니다.

### 색 반전 필터

```python
    # 색 반전 적용
    if invert:
        frame = cv2.bitwise_not(frame)  # 색 반전
--------------------------------------------------------------------------------------
    elif key == ord('i') or key == ord('I'):  # 'I' 키 -> 색 반전 적용/해제
        invert = not invert

```

<img width="835" alt="Image" src="https://github.com/user-attachments/assets/df451adc-bb52-4aec-82cd-54e5ea5804d9" />

I키를 눌러 색 반전 필터를 on/off할 수 있습니다.

### 색 대비 조절 기능

```python
    # 색 대비 조절 (기본 대비: 1.0)
    frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=0)
    elif key == ord('c') or key == ord('C'):  # 'C' 키 -> 대비 증가
        contrast = min(contrast + 0.1, 3.0)  # 대비 최대 3.0 제한
    elif key == ord('v') or key == ord('V'):  # 'V' 키 -> 대비 감소
        contrast = max(contrast - 0.1, 0.5)  # 대비 최소 0.5 제한
```

<img width="833" alt="Image" src="https://github.com/user-attachments/assets/1eaf4fd7-fc85-45eb-8585-958b664f2e89" />

C, V키를 눌러 각각 대비를 증가, 감소 시킬 수 있습니다.



