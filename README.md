# LongBowSpeech

This Python application allows users to execute voice commands to retrieve the current time or date using speech recognition. It utilizes the `speech_recognition` library for capturing audio input and interpreting commands.

## Features

- **Voice Command Recognition**: Users can speak commands to get the current time or date.
- **Colorful Console Output**: Utilizes the `colorama` library for colorful terminal output.
- **Environment Configuration**: Loads environment variables from a `.env` file using `python-dotenv`.

## Requirements

Make sure you have Python installed on your machine. You can create a `requirements.txt` file with the following contents:

```
colorama==0.4.6
dotenv==0.9.9
PyAudio==0.2.14
python-dotenv==1.1.1
pyttsx3==2.98
SpeechRecognition==3.14.3
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xycertbsi/LongBowSpeech.git
   cd LongBowSpeech
   ```

2. Install the required packages:

   on linux:
   ```bash
   pip install -r requirements.txt
   ```
   on windows:
   ```bash
   py -m pip install -r requirements.txt
   ```
   on macos:
   ```bash
   no idea, i not use macos sry :(
   ```

4. Create a `.env` file in the root directory with the following content:

   ```
   command_require=True
   command=Jason
   ListingLang=en
   ```

   Replace `Jason` with the command prefix you want to use (e.g., "Hey Assistant").

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Speak the command "time" to get the current time or "date" to get the current date.

## How It Works

- The application continuously listens for voice input and recognizes speech using Google’s speech recognition service.
- If the recognized command matches the expected commands ("time" or "date"), the corresponding function is executed.
- Color-coded messages are displayed to indicate success, warnings, and errors.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any feature requests or bugs.

## Acknowledgments

- [Colorama](https://pypi.org/project/colorama/) for terminal color output.
- [python-dotenv](https://pypi.org/project/python-dotenv/) for loading environment variables.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for speech recognition capabilities.
