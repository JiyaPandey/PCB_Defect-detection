"""
Demo script to visualize PCB defect detection on random images
"""
import cv2
import os
import random
from ultralytics import YOLO
import numpy as np

# Configuration
MODEL_PATH = "weights/best.pt"
IMAGE_DIR = "data/images"
OUTPUT_DIR = "results/demo_output"
DEMO_IMG_DIR = "demoimg"

CLASSES = {
    0: "missing_component",
    1: "misaligned_component",
    2: "solder_defect"
}

# Color coding for defects
DEFECT_COLORS = {
    0: (0, 0, 255),      # Red - missing component
    1: (0, 165, 255),    # Orange - misaligned
    2: (0, 255, 255)     # Yellow - solder defect
}

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("🔧 Loading YOLOv8 PCB Inspection Model...")
model = YOLO(MODEL_PATH)
print(f"✅ Model loaded successfully!\n")

# Check if demoimg folder exists and has images
if os.path.exists(DEMO_IMG_DIR):
    demo_images = [f for f in os.listdir(DEMO_IMG_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if len(demo_images) > 0:
        print(f"✨ Using {len(demo_images)} images from demoimg folder")
        selected_images = demo_images
        IMG_DIR = DEMO_IMG_DIR
    else:
        print("⚠️  demoimg folder is empty, using test images instead")
        test_images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if len(test_images) == 0:
            print("No test images found!")
            exit(1)
        num_images = min(10, len(test_images))
        selected_images = random.sample(test_images, num_images)
        IMG_DIR = IMAGE_DIR
else:
    print("📁 demoimg folder not found, using test images instead")
    test_images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if len(test_images) == 0:
        print("No test images found!")
        exit(1)
    num_images = min(10, len(test_images))
    selected_images = random.sample(test_images, num_images)
    IMG_DIR = IMAGE_DIR

num_images = len(selected_images)

print(f"Running PCB inspection on {num_images} images...")
print("Press 'q' to skip to next image or wait 3 seconds for auto-advance\n")

for idx, img_name in enumerate(selected_images, 1):
    img_path = os.path.join(IMG_DIR, img_name)
    
    print(f"[{idx}/{num_images}] Inspecting: {img_name}")
    
    # Read image
    image = cv2.imread(img_path)
    if image is None:
        print(f"  ⚠️  Failed to load image, skipping...")
        continue
    
    h, w, _ = image.shape
    
    # Run inference
    results = model(img_path, conf=0.25, verbose=False)
    
    defect_count = 0
    defects_found = []
    
    # Draw detections
    for r in results:
        boxes = r.boxes
        if boxes is None:
            continue
        
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            
            defect_name = CLASSES.get(cls_id, "unknown")
            color = DEFECT_COLORS.get(cls_id, (255, 255, 255))
            
            # Draw bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            # Draw label with confidence
            label = f"{defect_name} {conf:.2f}"
            label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            
            # Background for text
            cv2.rectangle(image, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), color, -1)
            cv2.putText(image, label, (x1, y1 - 5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
            defect_count += 1
            defects_found.append(defect_name)
    
    # Add status overlay
    status_text = f"Defects: {defect_count}"
    status_color = (0, 0, 255) if defect_count > 0 else (0, 255, 0)
    
    # Status banner at top
    cv2.rectangle(image, (0, 0), (w, 40), (0, 0, 0), -1)
    cv2.putText(image, status_text, (10, 28),
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)
    
    # Image counter
    counter_text = f"Image {idx}/{num_images}"
    cv2.putText(image, counter_text, (w - 150, 28),
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Print detected defects
    if defect_count > 0:
        print(f"  🚨 Found {defect_count} defect(s): {', '.join(defects_found)}")
    else:
        print(f"  ✅ No defects detected - PCB is good!")
    
    # Save output
    output_path = os.path.join(OUTPUT_DIR, f"inspected_{img_name}")
    cv2.imwrite(output_path, image)
    
    # Display image
    cv2.imshow('PCB Quality Inspection Demo', image)
    
    # Wait for 3 seconds or until 'q' is pressed
    key = cv2.waitKey(3000)
    
    if key == ord('q') or key == 27:  # 'q' or ESC to quit
        print("\nDemo stopped by user.")
        break

cv2.destroyAllWindows()
print(f"\n✅ Demo completed!")
print(f"📁 Inspected images saved to: {OUTPUT_DIR}")
