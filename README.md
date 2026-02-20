# 🧦 loxiesockie

My dog <b>eats</b> socks. Not chews- he <b>eats</b>!! This has resulted in multiple vet visits, one ER visit, and a household-wide sock paranoia. LoxieSockie is my attempt to solve this with computer vision and begin my first Raspberry Pi project.


## How It Works

A camera feeds frames to a YOLOv8n model running locally on a Raspberry Pi 4. The model detects both "dog" and "sock" in each frame, then a containment ratio algorithm determines whether the sock is inside the dog's bounding box (aka he's eating it). If so, it fires an alert to me and logs the event. All processing happens on-device.

```
Camera → Pi 4 → YOLOv8n (NCNN) → Detection Logic → Push Notification
```
## Hardware

| Component | Details |
|---|---|
| Board | Raspberry Pi 4 Model B / 4GB |
| Camera | Raspberry Pi Camera Module 3 |
| Storage | 32GB microSDHC |
| Cooling | iUniker case with fan + aluminum heatsinks |

## Tech Stack

| Technology | Role | Why This? |
|---|---|---|
| Python | Primary language | Ships with Pi OS; Ultralytics and picamera2 are Python-native |
| YOLOv8n | Object detection model | Nano variant is the smallest/fastest YOLO; fine-tuned on a Roboflow sock dataset since "sock" isn't a default COCO class [TODO: link dataset once i confirm its good] |
| NCNN | Inference runtime | Optimized for ARM CPUs |
| picamera2 | Camera interface | Python wrapper around `libcamera`, which is the low-level driver required by Camera Module 3 |
| OpenCV | Frame processing | Resize frames, draw bounding boxes for debugging, save snapshot images. Installed automatically with Ultralytics |
| Ntfy | Push notifications | Pi sends an HTTP POST, phone buzzes instantly bzzp bzzp |
| SQLite | Local event logging | Felt like it was sufficient for a single device (ideally in a good world) logging a few events per month. Can revisit later. |

## Status

🚧🚧🚧 Pre-development! 
