# Bromate | Automation & Interaction

This Python-based automation app serves as a keyword-based assistant that performs actions based on user commands and speaks to the user. It offers a range of functionalities including searching on YouTube, Wikipedia, telling jokes, providing weather updates, and even controlling hardware with Arduino.

## Features

- **Voice Interaction:** The assistant listens to user commands and responds with voice feedback.
- **YouTube Search and Play:** Open YouTube and play requested videos or search queries.
- **Wikipedia Search:** Retrieve and read summaries from Wikipedia.
- **Jokes:** Tell random jokes to the user.
- **Weather Updates:** Provide current temperature and weather conditions.
- **App Control:** Open and close various applications on the computer.
- **Hardware Control:** Turn on and off lights connected to an Arduino board.
- **Screenshot Capture:** Capture and save screenshots.

## Prerequisites

- Python 3.x
- PyQt5
- SpeechRecognition
- Pyttsx3
- PyWhatKit
- Wikipedia
- PyJokes
- BeautifulSoup
- Requests
- PyAutoGUI
- Googletrans


## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/keyword-assistant.git
   cd keyword-assistant
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Ensure your Arduino is connected and the COM port is correct in `Light.py`.

## Usage

1. Run the assistant:
   ```sh
   python assistant.py
   ```

2. Use the GUI to start the assistant. You can interact with the assistant by giving voice commands.

## Commands

### General Commands

- **Greeting:**
  - "hello"
  - "hey"

- **Search:**
  - "search [query] on google"
  - "who is [name]"
  - "tell me about [topic]"

- **YouTube:**
  - "open YouTube"
  - "play [song/video] on YouTube"

- **Jokes:**
  - "tell me a joke"
  - "jokes"

- **Weather:**
  - "what's the temperature in [location]"
  - "how is the weather"

- **App Control:**
  - "open [app name]"
  - "close [app name]"

- **Hardware Control:**
  - "turn on [color] light"
  - "turn off [color] light"
  - "turn on all lights"
  - "turn off all lights"

- **Time and Date:**
  - "what time is it"
  - "what's the date today"

- **Screenshots:**
  - "take a screenshot"

### Example Conversation

```
User: Hello
Assistant: Hello Sir, How can I help you?

User: Play Despacito on YouTube
Assistant: Playing Despacito on YouTube.

User: What's the weather like in New York?
Assistant: The temperature is 25°C and the weather is clear.

User: Tell me a joke
Assistant: Here is a joke, Why don’t scientists trust atoms? Because they make up everything!
```

## Web-Based App

A similar web-based app was developed using JavaScript. You can check it out [here](https://bromate.netlify.app/).

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.
