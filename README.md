# Drink Water Reminder

A simple Python desktop reminder application that reminds the user to drink water at a selected time interval.

## Features

- Sends desktop notifications
- Plays a reminder sound
- Allows reminder frequency to be changed by editing the sleep interval
- Shows notification buttons such as **Done** and **Disable Reminder**
- Uses a custom water icon for the notification
- Runs continuously until the user stops or disables the reminder

## Tech Stack

- Python
- asyncio
- desktop-notifier
- playsound
- pathlib

## Project Structure

```text
Drink-water-reminder-python/
├── main.py
├── requirements.txt
├── sound_scifi.wav
├── water.ico
└── README.md
```

## How It Works

The program waits for a selected time interval, plays a reminder sound, and then shows a desktop notification asking the user to drink water.

For testing, the interval is set to `10` seconds.

```python
await asyncio.sleep(10)
```

For real usage, the interval can be changed to `1800` seconds for 30 minutes.

```python
await asyncio.sleep(1800)
```

Or it can be changed to `3600` seconds for 1 hour.

```python
await asyncio.sleep(3600)
```

## Installation

Clone the repository:

```bash
git clone https://github.com/JunaidSyed-dev/Drink-water-reminder-python.git
```

Open the project folder:

```bash
cd Drink-water-reminder-python
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Requirements

The `requirements.txt` file contains:

```txt
desktop-notifier
playsound
```

## Code Note

The project uses `pathlib` to load the icon from the same folder as `main.py`.

```python
icon = Path(__file__).parent / "water.ico"
```

This avoids path errors when the project is moved to another folder or uploaded to GitHub.

## What I Learned

- How to create desktop notifications using Python
- How to use asynchronous programming with `asyncio`
- How to play audio alerts in Python
- How to use relative file paths with `pathlib`
- How to organize and upload a small Python project to GitHub
- How to write a clean README file for a GitHub project

## Author

[Junaid Syed](https://github.com/JunaidSyed-dev)
