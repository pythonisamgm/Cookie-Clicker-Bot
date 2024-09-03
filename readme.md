# Cookie Clicker Automation Bot

This Python script automates interactions in a cookie-clicking game using Selenium and Chrome WebDriver. It clicks the cookie automatically and makes purchases from the game's store based on available currency.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager
- Google Chrome Browser

## Installation

### 1. Install Python and Required Packages

Ensure you have Python 3.x installed. Install the required packages using pip:

```bash
pip install selenium webdriver-manager
```
### 2. WebDriver Installation
#### Windows
#### 1.Install ChromeDriver:
- ChromeDriver is managed automatically by the webdriver-manager package in your script. The webdriver-manager package will handle downloading and setting up ChromeDriver for you.
#### Mac/Linux
#### 1. Install ChromeDriver:
- Similar to Windows, ChromeDriver is managed automatically by the webdriver-manager package. Ensure you have the required permissions to execute the WebDriver.

## Usage
1. Run the Script:

Make sure your environment is set up as described above. You can run the script using:
```bash
python path_to_your_script.py
```
2. Script Functionality:

- click_cookie(): Automatically clicks the cookie every 0.2 seconds for 10 seconds.
- what_to_buy(): Chooses the highest upgrade available from the right column based on the amount of cookies you have.
- The script will run for 5 minutes, clicking the cookie and making purchases according to the strategy defined.

## Note
- Ensure that the game's website URL is correct and the page elements' IDs and classes have not changed. The script relies on these IDs for interaction.
- Adjust the timing and purchase logic if the game mechanics change or if you wish to optimize the bot's performance.
## License
This project is licensed under the MIT License - see the LICENSE file for details.