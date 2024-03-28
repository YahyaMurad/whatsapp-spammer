# WhatsApp Message Sender

This script allows you to spam messages to a contact on WhatsApp using Selenium.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- Google Chrome browser

## Installation

1. Make sure you have Python installed on your system. If not, you can download and install it from [python.org](https://www.python.org/downloads/).

2. Install the required Python packages using pip:
    ```bash
    pip install selenium
    ```

3. Download the Chrome WebDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your system's PATH.

4. Ensure you have Google Chrome installed on your system. If not, you can download and install it from [here](https://www.google.com/chrome/).

## Usage

1. Clone this repository or download the script (`whatsapp_message_sender.py`) to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:
    ```bash
    python whatsapp_message_sender.py --name [CONTACT_NAME] --word [MESSAGE_WORD] --times [NUM_TIMES]
    ```

    Replace `[CONTACT_NAME]` with the name of the contact you want to send messages to, `[MESSAGE_WORD]` with the word you want to send, and `[NUM_TIMES]` with the number of times you want to send the word.

4. Follow the instructions in the terminal. You may need to scan the QR code using your phone to log in to WhatsApp Web.

5. Once logged in, the script will automatically find the specified contact and start sending the messages.

## Important Notes

- Make sure you have a stable internet connection while running the script.
- The script waits for 20 seconds after opening WhatsApp Web to allow time for scanning the QR code. You can adjust this wait time if needed.
- Avoid running multiple instances of the script simultaneously to prevent conflicts with the WebDriver.
- Use this script responsibly and respect the privacy of others. Automated messaging should only be used for legitimate purposes and in compliance with WhatsApp's terms of service.
