
import platform
from plyer import notification

if platform.system() in ["Windows", "Darwin", "Linux"]:
    try:
        notification.notify(
            title="Please drink some water",
            message="You need to drink some water"
        )
    except:
        print("🔔 Reminder: Please drink some water!")
else:
    print("🔔 Reminder: Please drink some water!")

