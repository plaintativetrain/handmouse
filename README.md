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
- [Standalone macOS App](#-standalone-macos-app)
- [Requirements](#-requirements)
- [Installation](#-installation)
  - [From Source](#from-source)
  - [Using the Executable](#using-the-executable)
- [Usage](#-usage)
- [Gestures](#-gestures)
- [Building from Source](#-building-from-source)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## 🎯 Standalone macOS App

This project can be packaged as a standalone macOS application - no Python installation required!

### 📦 Quick Build
```bash
# One command to build, package, and test
./build_and_package.sh
```

Your app will be in `dist/HandMouseControl.app`

### 🚀 Distribution Options
1. **ZIP file**: `HandMouseControl.zip` - Easy sharing
2. **DMG installer**: Professional drag-to-install experience
3. **Direct distribution**: Share the .app bundle
4. **GitHub Releases**: Download pre-built executables from [Releases](https://github.com/YOUR_USERNAME/HandMouse/releases)

See [DISTRIBUTION.md](DISTRIBUTION.md) for complete details.

## 🔧 Requirements

- **Python**: 3.7 or higher
- **Webcam**: Built-in or USB camera
- **Platform**: macOS (tested), Linux and Windows (may require adjustments)
- **Permissions**: Camera and Accessibility access (macOS)

## 📥 Installation

### From Source

1. **Clone the repository**:
```bash
git clone https://github.com/YOUR_USERNAME/HandMouse.git
cd HandMouse
```

2. **Create and activate a virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**:
```bash
pip install -r requirements.txt
```

### Using the Executable

Download the latest release from the [Releases page](https://github.com/YOUR_USERNAME/HandMouse/releases):

1. Download `HandMouseControl.app.zip`
2. Unzip and drag to Applications folder
3. Grant required permissions (see [USER_GUIDE.md](USER_GUIDE.md))
4. Launch and enjoy!

## 🎮 Usage

### Running from Source
```bash
python hand_mouse_control.py
```

**Important for macOS users**: Grant Accessibility permissions:
- Go to `System Preferences` → `Security & Privacy` → `Privacy` → `Accessibility`
- Add Terminal (or your IDE) to allowed apps

## 🖐️ Gestures

| Gesture | Action | Description |
|---------|--------|-------------|
| **Move Hand** | Move Cursor | Move your hand to control cursor position |
| **Index + Thumb Pinch** | Left Click (Hold) | Touch fingertips together and hold to drag |
| **Middle + Thumb Pinch** | Right Click | Quick pinch for context menus |
| **Ring + Thumb Pinch + Move** | Scroll | Pinch and move up/down to scroll with momentum |

### Tips for Best Results
- ✅ Use good lighting
- ✅ Keep hand movements smooth
- ✅ Position yourself clearly in front of camera
- ✅ Practice gestures before important tasks

## 🔨 Building from Source

Want to create the standalone macOS app?

1. **Activate virtual environment**:
```bash
source venv/bin/activate
```

2. **Run the build script**:
```bash
chmod +x build_and_package.sh
./build_and_package.sh
```

3. **Choose your distribution option**:
   - Option 1: Create ZIP
   - Option 2: Create DMG (requires `brew install create-dmg`)
   - Option 3: Just test
   - Option 4: All of the above

See [DISTRIBUTION.md](DISTRIBUTION.md) for advanced packaging options.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MediaPipe** - Google's hand tracking framework
- **OpenCV** - Computer vision library
- **PyAutoGUI** - Cross-platform GUI automation

## 📚 Documentation

- [USER_GUIDE.md](USER_GUIDE.md) - Complete user guide with troubleshooting
- [FEATURES.md](FEATURES.md) - Detailed feature descriptions and technical details
- [DISTRIBUTION.md](DISTRIBUTION.md) - Guide for packaging and distributing
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick reference for gestures

## ⚠️ Disclaimer

This is an experimental project for educational and accessibility purposes. It may not be suitable for precision work or production use. Use at your own discretion.

---


