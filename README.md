# Drink Water Reminder

A simple Python desktop reminder application that reminds the user to drink water at a selected time interval.

## Features

- Sends desktop notifications
- Plays a reminder sound
- Allows custom reminder frequency
- Includes notification buttons such as Done and Disable Reminder
- Runs continuously until stopped by the user

## Tech Stack

- Python
- asyncio
- desktop-notifier
- playsound
- pathlib

## Project Structure

```text
drink-water-reminder-python/
├── main.py
├── requirements.txt
├── sound_scifi.wav
├── water.ico
└── README.md
How It Works

The program waits for the selected time interval, plays a sound, and then sends a desktop notification reminding the user to drink water.

For testing, the interval can be set to a small value like 10 seconds. For real usage, it can be changed to 1800 seconds for 30 minutes or 3600 seconds for 1 hour.

Installation
Clone the repository:
git clone https://github.com/JunaidSyed-dev/drink-water-reminder-python.git
Open the project folder:
cd drink-water-reminder-python
Install dependencies:
pip install -r requirements.txt
Run the project:
python main.py
What I Learned
How to create desktop notifications using Python
How to use asynchronous programming with asyncio
How to play audio alerts in Python
How to work with file paths using pathlib
How to structure a small Python utility project
Author

Junaid Syed
