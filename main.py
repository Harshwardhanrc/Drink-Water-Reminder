import time
from plyer import notification
while True:
    print("Sip some Water Dude!")
    notification.notify(title="Drink Water",
                        message="Sip some Water Dude!",)
    time.sleep(60*60)