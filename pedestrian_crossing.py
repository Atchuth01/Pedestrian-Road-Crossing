#Smart Pedestrian Road Crossing

import cv2
import torch
import numpy as np
from collections import deque
from norfair import Tracker, Detection  # Using Norfair instead of SORT

# Load YOLOv5 Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Initialize Norfair tracker
tracker = Tracker(distance_function="euclidean", distance_threshold=30, initialization_delay=2)

# Vehicle classes for detection
vehicle_classes = {2, 3, 5, 7, 1, 8}  # Car, Motorcycle, Bus, Truck, Bicycle, Auto-rickshaw

# Define lane regions (assumed based on frame width)
LANE_DIVISION = [200, 500, 800]  # X-coordinates dividing lanes

ROI_Y_START, ROI_Y_END = 200, 650  # Adjust Region of Interest (ROI)
frame_buffer = deque(maxlen=5)  # Smooth decision-making over 5 frames

video_path = "testVideo.mp4"
cap = cv2.VideoCapture(video_path)
frame_count = 0

# Get screen resolution
screen_width = 1280  # Adjust to your screen resolution
screen_height = 720  # Adjust to your screen resolution

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (screen_width, screen_height))  # Resize to fit screen
    frame_count += 1
    frame_height, frame_width, _ = frame.shape

    # Run YOLO object detection
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()
    detections = [det for det in detections if det[4] > 0.3]  # Confidence threshold

    norfair_detections = []
    lane_counts = [0] * (len(LANE_DIVISION) + 1)

    for x1, y1, x2, y2, conf, cls in detections:
        if int(cls) in vehicle_classes and ROI_Y_START < y2 < ROI_Y_END:
            center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
            norfair_detections.append(Detection(points=np.array([[center_x, center_y]])))

            # Assign lanes
            lane_idx = sum(center_x > x for x in LANE_DIVISION)
            lane_counts[lane_idx] += 1

    # Update tracker
    tracked_objects = tracker.update(detections=norfair_detections)

    # Smooth decision-making
    frame_buffer.append(sum(lane_counts))
    avg_lanes = sum(frame_buffer) / len(frame_buffer)
    decision_text, color = ("CROSS ✅", (0, 255, 0)) if avg_lanes < 5 else ("DO NOT CROSS ❌", (0, 0, 255))

    # Display info
    cv2.putText(frame, f"Frame: {frame_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"Lanes: {lane_counts}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, decision_text, (frame_width // 2 - 100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    cv2.imshow("Pedestrian Crossing System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
