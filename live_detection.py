# OpenCV (cv2) to handle video processing.
import cv2

# Ultralytics to handle YOLO Object and Face Detection Models
from ultralytics import YOLO

# Loading Object and Face Detection Models
object_model = YOLO('yolov8n.pt')
face_model = YOLO('yolov8n-face.pt')

# Turning On the Webcam
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open webcam.")
    raise SystemExit("Error: Could not open webcam")




# This Loop Will Keep Running until we press 'x' to Exit
while cv2.waitKey(1) != ord('x'):
    ok, frame = camera.read()
    if not ok or frame is None:
        continue

    # Both Models will run in same time, inspecting the exact same frame
    object_results = object_model(frame, verbose=False)
    face_results = face_model(frame, verbose=False)

    # Fusion Trick: Draw faces  boxes on top of objects
    fused_image_results = face_results[0].plot(img=object_results[0].plot())

    cv2.imshow("Press 'x' to exit Face/Object Detection", fused_image_results)


# Cleanup
camera.release() # Release the webcam
cv2.destroyAllWindows() # Close all windows
    
