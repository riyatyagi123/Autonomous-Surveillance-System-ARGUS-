<div align="center">

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

> **Watch ARGUS in action:**

https://github.com/your-username/argus/assets/your-asset-id/LMC_20250330_125550_Prime_Colour.mp4

> 💡 *If the video doesn't render above, [click here to watch the demo](./LMC_20250330_125550_Prime_Colour.mp4) or place the video file in your repo's `/assets` folder and update the link.*

---

## 📌 Table of Contents

- [Overview](#-overview)
- [The Problem](#-the-problem)
- [Our Solution](#-our-solution)
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Installation & Setup](#-installation--setup)
- [Results & Performance](#-results--performance)
- [Future Scope](#-future-scope)
- [Team](#-team)

---

## 🧠 Overview

**ARGUS** (Autonomous Real-time Guardian Using Surveillance) is an AI-powered intelligent monitoring system built on the intersection of **IoT**, **Computer Vision**, and **Large Language Models**. It continuously captures live video through an ESP32-CAM, processes it with lightweight vision models, and uses the **LLaVA LLM** for deep contextual reasoning — automatically distinguishing between routine activity and genuine threats.

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

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        ARGUS PIPELINE                            │
│                                                                  │
│  [ESP32-CAM]  ──►  [Frame Capture]  ──►  [Vision Model]         │
│                                               │                  │
│                                    ┌──────────▼──────────┐      │
│                                    │  Object / Behavior  │      │
│                                    │  Detection Layer    │      │
│                                    └──────────┬──────────┘      │
│                                               │                  │
│                                    ┌──────────▼──────────┐      │
│                                    │   LLaVA LLM Engine  │      │
│                                    │  (Contextual Reason)│      │
│                                    └──────────┬──────────┘      │
│                                               │                  │
│                              ┌────────────────▼────────────┐    │
│                              │   Decision: Normal / Alert  │    │
│                              └────────────┬────────────────┘    │
│                                           │                      │
│                              [Autonomous Alert System]           │
└──────────────────────────────────────────────────────────────────┘
```

---

## ✨ Key Features

- 🎥 **Live Video Monitoring** — Continuous capture and analysis via ESP32-CAM
- 🤖 **LLM-Powered Reasoning** — LLaVA interprets scene context, not just pixel changes
- 🚶 **Behavior Detection** — Identifies loitering, abnormal movement, and unauthorized presence
- ⚡ **Real-Time Processing** — WebSocket-based low-latency data pipeline
- 🔔 **Autonomous Alerts** — Intelligent notifications with minimal false positives
- 🧩 **Hybrid Architecture** — Edge-side detection + cloud-side reasoning for efficiency
- 🔌 **IoT Native** — Designed for embedded hardware with constrained resources

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Hardware** | ESP32-CAM |
| **Firmware** | Arduino (C++) |
| **Backend** | Python 3.8+ |
| **AI / Vision** | LLaVA (Large Language and Vision Assistant) |
| **Communication** | WebSockets |
| **Computer Vision** | OpenCV, custom behavior models |
| **Alerting** | Custom notification pipeline |

---

## ⚙️ How It Works

### Step 1 — Video Capture
The **ESP32-CAM** module streams live video frames over WebSockets to the Python backend at configurable intervals.

### Step 2 — Lightweight Detection
Incoming frames are analyzed by a **computer vision model** for:
- Human presence detection
- Loitering behavior
- Abnormal or erratic movement patterns

### Step 3 — LLM Contextual Reasoning
When a potential event is flagged, the frame and detection metadata are passed to **LLaVA**. The LLM evaluates the broader scene context — for example, distinguishing a delivery person from an intruder, or a crowd gathering from a fight.

### Step 4 — Decision & Alert
Based on LLaVA's assessment:
- **Normal** → Log and continue monitoring
- **Suspicious** → Trigger an autonomous alert with contextual description

This selective LLM invocation is the key innovation: it preserves **real-time performance** while enabling **deep intelligence**.

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

---

## 🔭 Future Scope

- [ ] Multi-camera support with unified dashboard
- [ ] Integration with smart home/building systems
- [ ] On-device LLM quantization for full edge deployment
- [ ] Mobile app for remote monitoring and alerts
- [ ] Facial recognition with privacy-preserving options
- [ ] Cloud sync and historical incident logging

---

## 👥 Team

| Name | Role |
|------|------|
| *(Add your name)* | AI / ML Engineer |
| *(Add teammate)* | IoT / Hardware Engineer |
| *(Add teammate)* | Backend Developer |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Built with 🧠 intelligence and ⚡ purpose.**

*ARGUS — Because security should understand, not just record.*

</div>
