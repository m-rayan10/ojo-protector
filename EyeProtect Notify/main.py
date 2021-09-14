import time
from plyer import notification 
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Look Away From Screen",
            message = "Its been more then 20 mins u r looking at the screen.\nPlease look away for 20 seconds for the object which is 20 feet away",
            app_icon = "eye.ico",
            timeout=10
        )
        time.sleep(60*20)