from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # In future we can use yolov8s.pt or yolov8m.pt for better accuracy

def detect_objects():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Failed to open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        annotated_frame = results.plot()

        cv2.imshow("YOLOv8 Object Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
