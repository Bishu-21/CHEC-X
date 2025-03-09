### **📌 Video Proctoring System**  

🔍 **An advanced AI-powered video proctoring system designed to ensure exam integrity by detecting anomalies such as face liveness, head pose, and background noise analysis.**  

---

## **🛠 Features**  
✅ **Face Liveness Detection** – Prevents spoofing attempts using AI models.  
✅ **Head Pose Estimation** – Monitors user movement for suspicious activity.  
✅ **Audio Analysis** – Detects unauthorized background noise.  
✅ **Real-time Monitoring** – Uses multithreading for smooth performance.  

---

## **📂 Project Structure**  
```
📁 Video_Proctoring
│── 📜 run.py                # Main script to start proctoring
│── 📜 detection.py          # Handles face liveness detection
│── 📜 head_pose.py          # Tracks head movements
│── 📜 audio.py              # Monitors audio activity
│── 📂 models/               # Pre-trained AI models (ONNX/TensorFlow)
│── 📂 utils/                # Helper functions (image processing, logging)
│── 📂 data/                 # Sample test data
│── 📜 requirements.txt      # Dependencies
│── 📜 README.md             # Documentation
```

---

## **📦 Installation**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Bishu-21/CHEC-X.git
cd CHEC-X
```
### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **🚀 Usage**  
### **Run the proctoring system:**  
```bash
python run.py
```
🎥 The system will start **real-time video monitoring**, **head pose detection**, and **audio analysis** simultaneously.  

---

## **🧑‍💻 Tech Stack**  
- **Python** (OpenCV, TensorFlow, ONNX, NumPy, SciPy)  
- **Flask** (for web integration)  
- **Multithreading** (for real-time performance)  
- **Machine Learning** (for face liveness & anomaly detection)  

---

## **🛡 Security Measures**  
✔️ **Encrypted Data Processing**  
✔️ **AI-powered Spoof Detection**  
✔️ **Real-time Alerts for Violations**  

---

## **📜 License**  
MIT License © 2025 Special Chouka  

---

This **README.md** provides a professional and structured overview of your **Video Proctoring System**. Let me know if you need modifications! 🚀💻
