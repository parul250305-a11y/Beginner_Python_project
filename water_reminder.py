import time
from plyer import notification

while True:
    
    notification.notify(
        title="Water Reminder 💧",
        message="You need to drink some water!",
        timeout=10
    )

    print("Notification sent")

    # Wait for 1 hour
    time.sleep(3600)