# Sign-Control: Control Your PC with Hand Signs

Sign-Control is a Python-based project that leverages OpenCV for real-time hand sign detection and PyAutoGUI for automating actions on your computer. With this tool, you can control your PC using predefined hand signs, replacing the need for traditional input devices like a mouse and keyboard.

## Features

- **Real-Time Hand Sign Recognition**: Uses your computer's webcam to detect and interpret predefined hand signs.
- **Seamless PC Interaction**: Automates actions such as opening applications, navigating files, or controlling media based on recognized signs.
- **Customizable Gestures**: Define and map your own hand signs to specific actions for a personalized experience.
- **User-Friendly Interface**: Lightweight and easy to set up, making it accessible to everyone.

## Prerequisites

- Python 3.7 or higher
- A webcam-enabled computer

### Required Libraries

Install the following Python libraries before running the project:

- OpenCV: `pip install opencv-python`
- PyAutoGUI: `pip install pyautogui`
- NumPy: `pip install numpy`


## How It Works

1. **Sign Detection**:
   - The webcam captures real-time video input.
   - OpenCV processes the video feed to identify predefined hand signs.

2. **Action Mapping**:
   - Detected signs are mapped to specific actions (e.g., move the mouse, click, type, or open an application).
   - Actions are executed using PyAutoGUI.

3. **Customization**:
   - Modify `config.py` to define your own signs and corresponding actions.

## Limitations

- Works best in well-lit environments.
- Requires consistent hand positioning for accurate detection.

## Future Enhancements

- Add support for dynamic gestures (e.g., swipes or multi-sign sequences).
- Improve accuracy with machine learning models.
- Include a GUI for easier customization.

## Contributions

We welcome contributions! Feel free to submit pull requests, report issues, or suggest new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Acknowledgments

- OpenCV for its powerful image processing capabilities.
- PyAutoGUI for seamless PC automation.

Happy coding! 🚀

