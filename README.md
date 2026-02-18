# AirWriting
🖐️ Virtual Air Drawing System using Computer Vision

A real-time finger drawing application that allows users to draw on a virtual canvas using hand gestures captured through a webcam.

This project uses Computer Vision and Hand Landmark Detection to create a touchless drawing interface.

🚀 Project Overview

The Virtual Air Drawing System detects and tracks hand movements using MediaPipe. By identifying specific finger gestures, the system allows users to:

🎨 Draw in different colors

🧽 Erase drawings

🗑 Clear the canvas

✌ Switch between selection and drawing modes

The entire system works in real time using a webcam.

🧠 Technologies Used

Python

OpenCV – Real-time video processing

MediaPipe – Hand tracking (21 landmark detection)

NumPy – Numerical operations

⚙️ How It Works

Captures live video from webcam

Detects hand landmarks using MediaPipe

Tracks the index fingertip position

Recognizes finger gestures:

✌ Two fingers → Selection Mode

☝ One finger → Drawing Mode

Draws on a virtual canvas using OpenCV

Merges canvas with live webcam feed

🎨 Features

Multiple Color Selection (Blue, Green, Red)

Eraser Mode

Clear Canvas Button

Gesture-Based Mode Switching

Interactive UI Toolbar

Real-Time Performance

📂 Project Structure
air_writing_project/
│
├── main.py
├── requirements.txt
└── README.md

💻 Installation & Setup
1️⃣ Clone the repository

cd air_writing_project

2️⃣ Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt:

pip install opencv-python mediapipe numpy

3️⃣ Run the project
python main.py


Press Q to exit the application.

🎯 Applications

Virtual Whiteboard

Touchless Drawing System

Smart Classroom Tools

Gesture-Based Interfaces

Human-Computer Interaction (HCI) Research
