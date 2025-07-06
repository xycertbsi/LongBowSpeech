# Voice Command Application

This Python application allows users to execute voice commands to retrieve the current time or date using speech recognition. It utilizes the `speech_recognition` library for capturing audio input and interpreting commands.

## Features

- **Voice Command Recognition**: Users can speak commands to get the current time or date.
- **Colorful Console Output**: Utilizes the `colorama` library for colorful terminal output.
- **Environment Configuration**: Loads environment variables from a `.env` file using `python-dotenv`.

## Requirements

Make sure you have Python installed on your machine. You can create a `requirements.txt` file with the following contents:

```
colorama==0.4.4
python-dotenv==0.19.2
SpeechRecognition==3.8.1
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following content:

   ```
   command_require=True
   command=your_command
   ListingLang=en-US
   ```

   Replace `your_command` with the command prefix you want to use (e.g., "Hey Assistant").

## Usage

1. Run the application:

   ```bash
   python your_script.py
   ```

2. Speak the command "time" to get the current time or "date" to get the current date.

## How It Works

- The application continuously listens for voice input and recognizes speech using Google’s speech recognition service.
- If the recognized command matches the expected commands ("time" or "date"), the corresponding function is executed.
- Color-coded messages are displayed to indicate success, warnings, and errors.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any feature requests or bugs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Colorama](https://pypi.org/project/colorama/) for terminal color output.
- [python-dotenv](https://pypi.org/project/python-dotenv/) for loading environment variables.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for speech recognition capabilities.
