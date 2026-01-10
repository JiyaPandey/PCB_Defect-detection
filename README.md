# PCB Defect Detection using YOLOv8

Automated PCB quality inspection system using YOLOv8 for detecting manufacturing defects.

## 🎯 Features

- **3 Defect Types Detection:**
  - Missing components
  - Misaligned components
  - Solder defects
  
- **Real-time Inspection** with confidence scores
- **Interactive Demo** with visual feedback
- **Pre-trained Model** included for immediate use

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

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/JiyaPandey/PCB_Defect-detection.git
cd PCB_Defect-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Demo

```bash
# Interactive demo (10 random images)
python demo.py

# Or inspect single image
python pcb_inspect.py
```

### 3. Train from Scratch (Optional)

```bash
python train.py
```

## 📊 Model Performance

- **Accuracy:** 99.2% mAP@0.5
- **Training Time:** ~16 minutes on RTX 3050
- **Inference Speed:** Real-time (30+ FPS)

## 🎨 Demo Features

- **Color-coded defects:**
  - 🔴 Red: Missing components
  - 🟠 Orange: Misaligned components
  - 🟡 Yellow: Solder defects
  
- **Auto-advance:** 3 seconds per image (press 'q' to skip)
- **Saved outputs:** All inspected images saved to `results/demo_output/`

## 📸 Custom Demo Images

Place your PCB images in `demoimg/` folder to run demo on specific images:

```bash
mkdir demoimg
cp your_pcb_image.jpg demoimg/
python demo.py
```

## 🛠️ Technical Details

- **Framework:** YOLOv8 (Ultralytics)
- **Base Model:** YOLOv8n (nano) - pretrained on COCO
- **Image Size:** 640x640
- **Batch Size:** 8
- **Training Epochs:** 50 (with early stopping)

## 📝 Requirements

- Python 3.8+
- PyTorch 2.0+
- OpenCV
- Ultralytics YOLO

See `requirements.txt` for complete list.

## 🎓 Training Configuration

Edit `pcb.yaml` to customize:
- Dataset paths
- Number of classes
- Class names

Training parameters in `train.py`:
- Epochs, batch size, image size
- Learning rate, patience, etc.

## 📈 Results

Model achieves excellent performance with minimal training data through transfer learning from COCO-pretrained YOLOv8.

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Jiya Pandey**
- GitHub: [@JiyaPandey](https://github.com/JiyaPandey)

## 🙏 Acknowledgments

- YOLOv8 by Ultralytics
- DeepPCB dataset for training data
