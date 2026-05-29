# Drink Water Reminder 

import asyncio
from desktop_notifier import DesktopNotifier,Button
import playsound
from pathlib import Path 
notifier  = DesktopNotifier()

async def main() :
    
    while True :    
        
        await asyncio.sleep(10) # the value 10 is for testing only , if U want to set it for every hour then set it to 3600 , because 1 hr = 3600 seconds..
        playsound.playsound(str(Path(__file__).parent / "sound_scifi.wav"))
        await notifier.send(
                            icon = Path(__file__).parent / "water.ico",
                            title = "Reminder",
                            message = "Drink Water...",
                            
                            buttons = [Button(title = "Done",on_pressed = lambda : print("Task Completed Successfully...")),
                                   Button(title = "Disable Reminder",on_pressed = lambda :exit(0))],
                            
                            )



asyncio.run(main())