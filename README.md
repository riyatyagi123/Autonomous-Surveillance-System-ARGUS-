<img width="1030" height="848" alt="hardware" src="https://github.com/user-attachments/assets/5e4e3676-290d-43ba-8810-9b92c5b2c99f" /><div align="center">

<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Arduino-ESP32--CAM-teal?style=for-the-badge&logo=arduino" />
<img src="https://img.shields.io/badge/AI-LLaVA%20LLM-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/Protocol-WebSockets-orange?style=for-the-badge" />

# 🔍 ARGUS
### AI + IoT Intelligent Surveillance System

> *"All-seeing, always aware."*
>
> ARGUS is a next-generation surveillance solution that fuses IoT hardware with a Large Language Model (LLaVA) to deliver **real-time, context-aware threat detection** — eliminating the blind spots of traditional security systems.

</div>

---

## 📽️ Demo Video

<!-- Upload your video to the repo under /assets/ folder, then replace the path below -->
<!-- Option 1: GitHub hosted video (drag-drop .mp4 into any Issue to get a hosted URL) -->

<div align="center">

[![ARGUS Demo](https://img.shields.io/badge/▶%20Watch%20Demo-Click%20Here-red?style=for-the-badge)](./LMC_20250330_125550_Prime_Colour.mp4)

> 💡 To embed video on GitHub: Go to any Issue → drag & drop your `.mp4` → copy the generated `https://github.com/...` URL → paste it directly in the README (GitHub auto-renders it).

</div>

---

## 🧠 Overview

**ARGUS** (Autonomous Real-time Guardian Using Surveillance) is an AI-powered intelligent monitoring system built on the intersection of **IoT**, **Computer Vision**, and **Large Language Models**. It continuously captures live video through an ESP32-CAM mounted on a mobile surveillance car, processes frames with lightweight vision models, and uses the **LLaVA LLM** for deep contextual reasoning — automatically distinguishing between routine activity and genuine threats.

Unlike conventional CCTV systems that rely on passive recording and human review, ARGUS **thinks, understands, and acts**.

---

## ❌ The Problem

Traditional surveillance systems suffer from critical limitations:

| Problem | Impact |
|--------|--------|
| 🧍 Manual Monitoring | Operator fatigue leads to missed incidents |
| ⏱️ Delayed Response | Alerts arrive too late for effective intervention |
| 🚨 High False Positives | Wasted resources and alert fatigue |
| 🧩 No Contextual Understanding | Systems flag motion, not meaning |
| 📡 No Real-Time Intelligence | Recordings reviewed after the fact |

---

## ✅ Our Solution

ARGUS addresses each of these pain points through a **hybrid AI pipeline**:

- **Lightweight vision models** handle object and behavior detection on the edge — fast and efficient.
- **LLaVA LLM** is invoked selectively for contextual reasoning — only when an event warrants deeper analysis.
- **WebSocket communication** ensures sub-second latency between the ESP32-CAM and the inference backend.
- **Autonomous alerts** are triggered intelligently, dramatically reducing false positives.
- **Mobile surveillance car** navigates without a predefined path, using human-like thinking to follow targets.

---

## 🏗️ System Architecture

<div align="center">

![ARGUS System Architecture]<img width="1450" height="1383" alt="architecture" src="https://github.com/user-attachments/assets/48211768-6340-434d-8915-08fdad40ab0a" />


</div>

The pipeline operates in 5 stages:

1. **Data Collection** — The surveillance car streams continuous frames via WebSocket, stored locally for processing.
2. **LLM Instructions** — LLaVA sends movement and recording instructions back to the car (follow target, record & stream).
3. **Disturbance Detection** — The system identifies suspicious activity, fights, fire, and smoke.
4. **Custom Instructions** — The monitoring dashboard sends operator-defined rules to the LLM for adaptive behavior.
5. **Live Feed** — Real-time video with GPS location streams to the Surveillance Monitoring Dashboard, accessible by the Safety Department.

---

## 🤖 Hardware

<div align="center">

![ARGUS Surveillance Car]<img width="1030" height="848" alt="hardware" src="https://github.com/user-attachments/assets/a12e34f1-fb39-4dab-89dd-22ec5c31a3f0" />


*The ARGUS surveillance car — ESP32-CAM mounted on a 4WD chassis with Li-ion battery pack, motor driver, and onboard sensors.*

</div>

The mobile unit is built on a **4-wheel drive acrylic chassis** equipped with:
- ESP32-CAM for live video streaming
- Li-ion battery pack for autonomous power
- Motor driver module for directional control
- Onboard sensors for environment awareness
- No predefined path — driven by LLM decision-making

---

## ✨ Key Features

- 🎥 **Live Video Monitoring** — Continuous capture and analysis via ESP32-CAM
- 🤖 **LLM-Powered Reasoning** — LLaVA interprets scene context, not just pixel changes
- 🚗 **Autonomous Mobile Unit** — Surveillance car navigates with human-like thinking
- 🚶 **Behavior Detection** — Identifies loitering, fights, abnormal movement, fire & smoke
- 📍 **GPS Tracking** — Real-time location streamed alongside video feed
- ⚡ **Real-Time Processing** — WebSocket-based low-latency data pipeline
- 🔔 **Autonomous Alerts** — Intelligent notifications with minimal false positives
- 🧩 **Hybrid Architecture** — Edge-side detection + cloud-side reasoning for efficiency
- 📊 **Monitoring Dashboard** — Centralized view for the Safety Department

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Hardware** | ESP32-CAM, 4WD Robot Chassis |
| **Firmware** | Arduino (C++) |
| **Backend** | Python 3.8+ |
| **AI / Vision** | LLaVA (Large Language and Vision Assistant) |
| **Communication** | WebSockets |
| **Computer Vision** | OpenCV, custom behavior models |
| **Alerting** | Custom notification pipeline |

---

## ⚙️ How It Works

### Step 1 — Video Capture
The **ESP32-CAM** on the surveillance car streams live video frames over WebSockets to the Python backend continuously. Frames are stored locally for processing.

### Step 2 — Lightweight Detection
Incoming frames are analyzed by a **computer vision model** for:
- Human presence detection
- Loitering behavior
- Abnormal or erratic movement patterns
- Fire and smoke signatures

### Step 3 — LLM Contextual Reasoning
When a potential event is flagged, the frame and detection metadata are passed to **LLaVA**. The LLM evaluates the broader scene context — distinguishing a delivery person from an intruder, a crowd gathering from a fight, or steam from actual fire.

### Step 4 — Decision & Control
Based on LLaVA's assessment, the system either:
- **Sends instructions to the car** — follow target, continue recording, reposition
- **Triggers an alert** — notifies the Safety Department with live feed + GPS location
- **Logs and continues** — for normal activity

---

## 🚀 Installation & Setup

### Prerequisites

```bash
Python >= 3.8
Arduino IDE (with ESP32 board support)
pip install -r requirements.txt
```

### Clone the Repository

```bash
git clone https://github.com/your-username/argus.git
cd argus
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Flash ESP32-CAM

1. Open `firmware/argus_cam.ino` in Arduino IDE
2. Set your Wi-Fi credentials and server IP in the config section
3. Flash to the ESP32-CAM module

### Configure & Run Backend

```bash
# Copy and edit config
cp config.example.yaml config.yaml

# Start ARGUS
python main.py
```

> ⚠️ **Note:** Ensure LLaVA model weights are downloaded and the model path is set in `config.yaml`.

---

## 📊 Results & Performance

| Metric | Result |
|--------|--------|
| Threat Detection Accuracy | High (LLM-validated) |
| False Positive Rate | Significantly reduced vs traditional systems |
| Alert Latency | Near real-time via WebSockets |
| System Overhead | Low — lightweight model on edge, LLM invoked selectively |
| Mobility | Autonomous navigation, no predefined path |

---

## 🔭 Future Scope

- [ ] Multi-camera support with unified dashboard
- [ ] Integration with smart home/building systems
- [ ] On-device LLM quantization for full edge deployment
- [ ] Mobile app for remote monitoring and alerts
- [ ] Enhanced GPS mapping with incident heat-maps
- [ ] Cloud sync and historical incident logging
