# HandMouse 🖐️🖱️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform: macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)](https://www.apple.com/macos/)

Control your Mac's mouse cursor with just your hand and webcam! HandMouse is a gesture-controlled mouse system that uses computer vision and hand tracking to provide an intuitive, touchless computing experience.

## ✨ Features

- **🎯 Intuitive Mouse Control**: Move your cursor by moving your hand (tracks ring finger base for stability)
- **👆 Left Click**: Pinch index finger and thumb together (hold to drag/select text)
- **🖱️ Right Click**: Pinch middle finger and thumb together
- **📜 Smooth Scrolling**: Pinch ring finger and thumb, then move up/down with momentum
- **📊 Real-time Visual Feedback**: See your hand landmarks and gesture detection live
- **⚡ Multi-threaded Performance**: Smooth cursor movement with advanced jitter reduction
- **📏 Adaptive Thresholds**: Works at different distances from camera
- **🎨 Color-coded Finger Tracking**: Easy-to-follow visual indicators

## 🎬 Demo

> Add a demo video or GIF here once you've recorded one!

## 📋 Table of Contents

- [Features](#-features)
- [Download](#-download)
- [Usage Guide](#-usage-guide)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## 📥 Download

HandMouse is available as a standalone macOS application - no Python installation required!

Download the latest release from the [Releases page](https://github.com/YOUR_USERNAME/HandMouse/releases):

1. Download `HandMouseControl.app.zip`
2. Unzip and drag to your Applications folder
3. Launch the app
4. Grant Camera and Accessibility permissions when prompted

**Requirements**:
- macOS 10.13 (High Sierra) or later
- Built-in or USB webcam

## 🎮 Usage Guide

### How It Works

HandMouse tracks your hand movements using your webcam and translates them into mouse actions. The cursor tracking is based on the **ring finger base** (the knuckle where your ring finger meets your palm), which provides stable and precise control.

### Gestures

| Gesture | Action | How To |
|---------|--------|--------|
| **Move Hand** | Control Cursor | The cursor follows your ring finger base position |
| **Index + Thumb Pinch** | Left Click | Pinch your index fingertip to your thumb tip (hold to drag/select) |
| **Middle + Thumb Pinch** | Right Click | Pinch your middle fingertip to your thumb tip |
| **Ring + Thumb Pinch + Move** | Scroll | Pinch ring finger to thumb, then move hand up/down |

### Tips for Best Results

✅ **Keep your hand spread out** - Fingers should be clearly separated and visible

✅ **Face your palm toward the webcam** - Your hand should be clearly visible with all fingers in view

✅ **Use good lighting** - Ensure your hand is well-lit for accurate tracking

✅ **Smooth movements** - Move your hand gradually for better cursor control

✅ **Optimal distance** - Position your hand 1-2 feet from the webcam

✅ **Grant permissions** - Allow Camera and Accessibility access when prompted

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MediaPipe** - Google's hand tracking framework
- **OpenCV** - Computer vision library
- **PyAutoGUI** - Cross-platform GUI automation

## ⚠️ Disclaimer

This is an experimental project for educational and accessibility purposes. It may not be suitable for precision work or production use. Use at your own discretion.

---



