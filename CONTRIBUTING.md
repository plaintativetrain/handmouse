# Contributing to HandMouse

Thank you for your interest in contributing to HandMouse! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the behavior
- Expected behavior vs actual behavior
- Screenshots or videos if applicable
- Your environment (macOS version, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Why this enhancement would be useful
- Any potential implementation ideas

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/AmazingFeature
   ```

2. **Make your changes**:
   - Write clean, readable code
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

3. **Test your changes**:
   - Ensure the app runs without errors
   - Test all gestures work correctly
   - Verify no existing features are broken

4. **Commit your changes**:
   ```bash
   git commit -m "Add some AmazingFeature"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/AmazingFeature
   ```

6. **Open a Pull Request**:
   - Provide a clear description of changes
   - Reference any related issues
   - Include screenshots/videos if UI changes

## 🎨 Code Style

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Add docstrings for functions and classes
- Comment complex algorithms or business logic

## 🧪 Testing Guidelines

Before submitting a PR, please test:
- ✅ Hand tracking works smoothly
- ✅ All gestures (left click, right click, scroll) function properly
- ✅ No performance degradation
- ✅ macOS app builds successfully (if you modified core code)
- ✅ No new warnings or errors in console

## 📝 Documentation

If your PR includes new features or changes existing behavior:
- Update README.md if needed
- Update USER_GUIDE.md for user-facing changes
- Update FEATURES.md for technical features
- Add inline code comments for complex logic

## 🏗️ Development Setup

1. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HandMouse.git
   cd HandMouse
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Make your changes and test**:
   ```bash
   python hand_mouse_control.py
   ```

## 🚀 Areas for Contribution

Here are some areas where contributions would be especially valuable:

### High Priority
- 🪟 Windows compatibility testing and fixes
- 🐧 Linux compatibility testing and fixes
- 📱 Performance optimizations
- 🐛 Bug fixes and stability improvements
- 📖 Documentation improvements
- 🌐 Multi-language support

### Feature Ideas
- 🎮 Custom gesture configuration
- 📊 Performance metrics overlay
- 🎨 Customizable visual themes
- ⌨️ Keyboard shortcuts via gestures
- 🔊 Audio feedback options
- 📹 Recording/playback of gesture sequences
- 🤖 Machine learning for personalized gesture recognition

### Technical Improvements
- ⚡ Reduce CPU usage
- 🎯 Improve gesture detection accuracy
- 🔧 Better error handling
- 📦 Automated testing framework
- 🏗️ Code refactoring for maintainability

## 🔍 Code Review Process

1. A maintainer will review your PR
2. They may request changes or ask questions
3. Make any requested updates
4. Once approved, your PR will be merged!

## 📜 Code of Conduct

### Our Standards

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what's best for the project
- ❌ No harassment or discrimination
- ❌ No trolling or insulting comments

### Our Responsibilities

Project maintainers are responsible for:
- Clarifying standards of acceptable behavior
- Taking appropriate action for unacceptable behavior
- Removing comments, commits, or contributions that violate guidelines

## 🎯 First Time Contributors

New to open source? Here's how to get started:

1. Look for issues labeled `good first issue`
2. Comment on the issue to let others know you're working on it
3. Ask questions if anything is unclear
4. Don't be afraid to make mistakes - we're all learning!

## 📞 Questions?

If you have questions about contributing:
- Open an issue with the `question` label
- Reach out to the maintainers
- Check existing issues and documentation

## 🙏 Thank You!

Every contribution helps make HandMouse better. Whether it's:
- Reporting a bug
- Suggesting a feature
- Writing documentation
- Fixing a typo
- Adding a new feature

Your contribution matters! Thank you for being part of this project.

---

**Happy Contributing! 🎉**
