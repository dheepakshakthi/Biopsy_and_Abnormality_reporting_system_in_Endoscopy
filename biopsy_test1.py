import torch
from ultralytics import YOLO
import cv2
import time

'''
you can make use of the trained model in yolov11_instruments_without_pipe_results folder.
I have trained the yolov11 model on the kvasir-instrument dataset but it doesnt detect the endoscope pipe and only detects the biopsy instrument.
'''

model = YOLO("path_to_model(.pt)")

cap = cv2.VideoCapture("path_to_video.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)

biopsy_class_id = 0  
frame_num = 0
biopsy_detected = False

# cooldown timer for the detection porgram. if there is a second biopsy, the instrument should not be visible to the camera for the mentioned number of frames
cooldown = 3000 
absence_counter = 0
number_of_biopsy_events = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=0.95, verbose=False)
    detections = results[0].boxes.cls.cpu().numpy()

    if biopsy_class_id in detections:
        if not biopsy_detected:
            timestamp = frame_num / fps
            number_of_biopsy_events += 1
            print(f"biopsy event {number_of_biopsy_events} detected")
            biopsy_detected = True
        absence_counter = 0  
    else:
        if biopsy_detected:
            absence_counter += 1
            if absence_counter >= cooldown:
                biopsy_detected = False  

    frame_num += 1

    cv2.imshow("detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()