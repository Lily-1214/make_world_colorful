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

