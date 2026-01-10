# PCB Defect Detection using YOLOv8

An automated PCB (Printed Circuit Board) quality inspection system powered by AI/Deep Learning for detecting manufacturing defects.

## 🎥 Demo Video

> **Add your demo video here:** Replace this text with a link to your demonstration video showing the PCB defect detection in action.

## 🔍 What This Project Does

This is an **automated PCB defect detection system** that uses **AI and Deep Learning (YOLOv8)** to inspect printed circuit boards and identify manufacturing defects in real-time.

The system can detect **3 types of defects**:
- **Missing components** - Components that should be present but are absent
- **Misaligned components** - Parts that are not properly positioned
- **Solder defects** - Issues with solder joints and connections

It provides instant visual feedback with color-coded bounding boxes and confidence scores, making quality control fast and reliable.

## ✨ Features

- **Real-time Detection** - Instant inspection with 30+ FPS
- **High Accuracy** - 99.2% mAP@0.5 performance
- **Interactive Demo** - Visual feedback with color-coded defects
- **Pre-trained Model** - Ready to use out of the box
- **Easy to Use** - Simple command-line interface

## 🚀 How to Run

### Step 1: Install

```bash
# Clone and navigate to the project
git clone https://github.com/JiyaPandey/PCB_Defect-detection.git
cd PCB_Defect-detection

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Run Demo

```bash
python demo.py
```

### Step 3: View Results

Results are automatically saved to `results/demo_output/` with color-coded defects:
- 🔴 Red: Missing components
- 🟠 Orange: Misaligned components  
- 🟡 Yellow: Solder defects

> **Tip:** Press 'q' to skip to the next image during demo

## 📊 Model Performance

- **Accuracy:** 99.2% mAP@0.5
- **Speed:** Real-time (30+ FPS)
- **Training Time:** ~16 minutes on RTX 3050

## 🛠️ Technical Details

- **Model:** YOLOv8n (nano) with transfer learning
- **Framework:** Ultralytics YOLOv8
- **Input Size:** 640x640 pixels
- **Requirements:** Python 3.8+, PyTorch 2.0+, OpenCV

## 📁 Project Structure

```
PCB_Defect-detection/
├── demo.py              # Run the demo
├── pcb_inspect.py       # Inspect single image
├── train.py             # Train model
├── weights/             # Model weights
├── results/             # Output images
└── requirements.txt     # Dependencies
```

## 🔧 Advanced Usage

**Inspect a single image:**
```bash
python pcb_inspect.py
```

**Train from scratch:**
```bash
python train.py
```

**Use custom images:**
```bash
mkdir demoimg
cp your_image.jpg demoimg/
python demo.py
```

## 📄 License & Contributing

This project is open source under the MIT License. Contributions are welcome via Pull Requests!

## 👤 Author

**Jiya Pandey** - [@JiyaPandey](https://github.com/JiyaPandey)

## 🙏 Acknowledgments

Built with YOLOv8 by Ultralytics • Dataset from DeepPCB
