"""
Train YOLOv8 model for PCB defect detection
"""
from ultralytics import YOLO

# Configuration
DATA_YAML = "pcb.yaml"
MODEL = "yolov8n.pt"  # Pretrained YOLOv8 nano model
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 8
PATIENCE = 10

print("🔧 Training YOLOv8 for PCB Quality Inspection")
print(f"Data config: {DATA_YAML}")
print(f"Base model: {MODEL}")
print(f"Epochs: {EPOCHS}")
print(f"Image size: {IMG_SIZE}")
print(f"Batch size: {BATCH_SIZE}\n")

# Load model
model = YOLO(MODEL)

# Train
results = model.train(
    data=DATA_YAML,
    epochs=EPOCHS,
    imgsz=IMG_SIZE,
    batch=BATCH_SIZE,
    patience=PATIENCE,
    save=True,
    project="runs/detect",
    name="train",
    exist_ok=True
)

print("\n✅ Training completed!")
print(f"📁 Best weights saved to: runs/detect/train/weights/best.pt")
