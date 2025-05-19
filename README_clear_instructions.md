# 🤖 Maya AI Assistant

**Maya** is a multimodal AI assistant built in Python, combining voice control, face recognition, emotion detection, GPT-based responses, and real-time object detection using YOLOv8 — all in a single intelligent system.

---

## 📌 Features

- 🗣️ Voice-Controlled Interaction (Speech Recognition + TTS)
- 🧠 GPT Integration for Intelligent Q&A
- 🧍 Face Recognition with Personalized Greetings
- 🧏 Emotion Recognition (Visual Mood Detection)
- 🎯 Real-Time Object Detection using YOLOv8
- 📅 Reminders, Memory Module, and Web Search
- 🖼️ GUI Interface using Tkinter

---

## 🛠️ Tech Stack

- `Python`
- `OpenCV`, `face-recognition`
- `SpeechRecognition`, `pyttsx3`
- `OpenAI GPT`, `serpapi`
- `YOLOv8 (ultralytics)`, `torch`
- `Tkinter GUI`
- `Pillow`, `numpy`, `keyboard`, `dotenv`

---

## 🧱 Folder Structure

```
maya_ai_assistant/
├── main.py
├── gui.py
├── tts.py / stt.py
├── command_handler.py
├── object_detection/
├── known_faces/
├── utils/
│   └── __init__.py, helpers...
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 📦 Install Dependencies
Run this from the terminal (ensure you're in the `maya_ai_assistant/` directory):

```bash
pip install -r requirements.txt
```

If needed, install these manually:
```bash
pip install opencv-python face-recognition speechrecognition pyttsx3 openai numpy Pillow torch ultralytics keyboard requests python-dotenv serpapi matplotlib tensorflow scikit-learn dlib pyjokes schedule google-search-results
```

---

### 🛠️ Install Required Tools

- 🔧 **CMake** – [Download here](https://cmake.org/download/)
- 🛠 **Visual Studio C++ Build Tools** – [Install here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
  - ✔ Check: "Desktop development with C++"
  - ✔ Include: Windows 10 SDK and MSVC v142/v143
  - 🔁 Restart your computer after installation

---

## ▶️ How to Run Maya

```bash
cd maya_ai_assistant
python main.py
```

---

## 👤 Face Recognition Setup

- Add your **selfie images** to the `known_faces/` folder.
- The filename should be the name you want Maya to greet you with (e.g., `praveen.jpg` → “Welcome back, Praveen”).

---

## 🔮 Future Enhancements (Planned)

- Multilingual voice support
- Real-time emotion feedback response
- Eye contact detection
- Spotify & calendar integration
- Web GUI version (Flask or React)

---

## 👨‍💻 Author

**Praveen Elayaraja**  
[GitHub](https://github.com/praveen0777)

---

## 📜 License

This project is licensed under the MIT License.
