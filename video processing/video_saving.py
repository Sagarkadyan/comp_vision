import cv2

cam =cv2.VideoCapture(0)
frame_width=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


codex =cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.mp4",codex,20,(frame_width,frame_height))

while True:
    sucess,image=cam.read()

    if not sucess:
        break
    recorder.write(image)
    cv2.imshow("recodring live",image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("quitting...")
        break

cam.release()
recorder.release()
cv2.destroyAllWindows()
