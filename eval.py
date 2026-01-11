"""
Evaluate YOLOv8 model for PCB defect detection
"""
from ultralytics import YOLO

# Configuration
MODEL_PATH = "weights/best.pt"
DATA_YAML = "pcb.yaml"

print("🔍 Evaluating YOLOv8 PCB Defect Detection Model")
print(f"Model: {MODEL_PATH}")
print(f"Data config: {DATA_YAML}\n")

# Load model
model = YOLO(MODEL_PATH)

# Run validation
metrics = model.val(data=DATA_YAML, split='val')

# Print comprehensive metrics
print("\n" + "="*60)
print("EVALUATION METRICS")
print("="*60)

print("\n📊 Overall Performance:")
print(f"  mAP@0.5:      {metrics.box.map50:.4f} ({metrics.box.map50*100:.2f}%)")
print(f"  mAP@0.5:0.95: {metrics.box.map:.4f} ({metrics.box.map*100:.2f}%)")
print(f"  Precision:    {metrics.box.mp:.4f} ({metrics.box.mp*100:.2f}%)")
print(f"  Recall:       {metrics.box.mr:.4f} ({metrics.box.mr*100:.2f}%)")

# Calculate F1 Score
if (metrics.box.mp + metrics.box.mr) > 0:
    f1_score = 2 * (metrics.box.mp * metrics.box.mr) / (metrics.box.mp + metrics.box.mr)
else:
    f1_score = 0
print(f"  F1 Score:     {f1_score:.4f} ({f1_score*100:.2f}%)")

print("\n📈 Per-Class Metrics:")
class_names = ['missing_component', 'misaligned_component', 'solder_defect']
print(f"\n{'Class':<25} {'Precision':<12} {'Recall':<12} {'mAP@0.5':<12} {'mAP@0.5:0.95'}")
print("-" * 73)

for i, name in enumerate(class_names):
    if hasattr(metrics.box, 'p') and hasattr(metrics.box, 'r') and hasattr(metrics.box, 'ap50') and hasattr(metrics.box, 'ap'):
        precision = metrics.box.p[i] if i < len(metrics.box.p) else 0
        recall = metrics.box.r[i] if i < len(metrics.box.r) else 0
        ap50 = metrics.box.ap50[i] if i < len(metrics.box.ap50) else 0
        ap = metrics.box.ap[i] if i < len(metrics.box.ap) else 0
        
        print(f"{name:<25} {precision*100:>10.2f}%  {recall*100:>10.2f}%  {ap50*100:>10.2f}%  {ap*100:>10.2f}%")

print("\n" + "="*60)
print("✅ Evaluation completed!")
print(f"📁 Results saved to: runs/detect/val")
print("="*60)
