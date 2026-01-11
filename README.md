

Automated PCB quality inspection system using YOLOv8 for detecting manufacturing defects in real-time.

## 🔍 What Does This Detect?

This system identifies three critical PCB manufacturing defects:

- **Missing Components**: Identifies components that are absent from the PCB, ensuring all required parts are present
- **Misaligned Components**: Detects components placed incorrectly or at wrong angles, preventing assembly issues
- **Solder Defects**: Spots issues with solder joints including insufficient solder, bridges, and cold joints

---

## 📹 Demo Video

> [Screencast from 01-10-2026 10:36:56 PM.webm](https://github.com/user-attachments/assets/af88f608-1ead-4769-a7b1-39188afe0f98)# PCB Defect Detection using YOLOv8


## 📊 Results

- **Accuracy:** 99.2% mAP@0.5
- **Training Time:** ~16 minutes on RTX 3050
- **Inference Speed:** Real-time (30+ FPS)

**Visual Output:**
- 🔴 Red boxes: Missing components
- 🟠 Orange boxes: Misaligned components  
- 🟡 Yellow boxes: Solder defects
- Auto-advance every 3 seconds (press 'q' to skip)
- All results saved to `results/demo_output/`

---

## 🚀 Quick Start

**1. Clone and Install**
```bash
git clone https://github.com/JiyaPandey/PCB_Defect-detection.git
cd PCB_Defect-detection
pip install -r requirements.txt
```

**2. Run Inspection**
```bash
python demo.py              # Interactive demo with 10 random images
python pcb_inspect.py       # Inspect a single image
```

**3. Custom Images** (optional)
```bash
mkdir demoimg && cp your_image.jpg demoimg/
python demo.py
```

**4. Train Your Own Model** (optional)
```bash
python train.py             # Customize pcb.yaml for your dataset
```

---

## 📁 Project Structure

```
PCB_Defect-detection/
├── weights/              # Trained YOLOv8 model weights
│   ├── best.pt          # Best model checkpoint
│   └── last.pt          # Last training checkpoint
├── data/                 # PCB images and annotations
│   ├── images/          # PCB images
│   ├── labels/          # YOLO format labels
│   └── classes.txt      # Class names
├── demoimg/              # Custom demo images (optional)
├── results/              # Inspection output
├── demo.py               # Interactive demo script
├── train.py              # Training script
├── pcb_inspect.py        # Single image inspection
├── pcb.yaml              # Dataset configuration
└── requirements.txt      # Python dependencies
```

---

## 🛠️ Technical Specifications

- **Framework:** YOLOv8 (Ultralytics)
- **Base Model:** YOLOv8n (nano) pretrained on COCO
- **Requirements:** Python 3.8+, PyTorch 2.0+, OpenCV
- **Training Config:** 50 epochs, batch size 8, 640x640 images
- **Performance:** Transfer learning achieves excellent results with minimal training data

---

## 🙏 Acknowledgments

- YOLOv8 by Ultralytics
- DeepPCB dataset for training data

---

## 👤 Author

**Jiya Pandey**
- GitHub: [@JiyaPandey](https://github.com/JiyaPandey)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.
