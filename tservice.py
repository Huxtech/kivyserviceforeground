from time import sleep
from jnius import autoclass

# Get the Android service instance
PythonService = autoclass('org.kivy.android.PythonService')
mService = PythonService.mService

def set_foreground_notification():
    # We need to build a notification to keep the foreground service alive
    Context = autoclass('android.content.Context')
    Intent = autoclass('android.content.Intent')
    PendingIntent = autoclass('android.app.PendingIntent')
    NotificationBuilder = autoclass('android.app.Notification$Builder')
    
    # Create an intent to open the app if the notification is clicked
    app_context = mService.getApplicationContext()
    notification_intent = Intent(app_context, autoclass('org.kivy.android.PythonActivity'))
    pending_intent = PendingIntent.getActivity(app_context, 0, notification_intent, 0)

    # Build the notification
    # Note: For Android 8.0+, you'd also need a Notification Channel ID
    builder = NotificationBuilder(app_context)
    builder.setContentTitle("Service Running")
    builder.setContentText("Kivy foreground service is active")
    builder.setSmallIcon(app_context.getApplicationInfo().icon)
    builder.setContentIntent(pending_intent)
    
    notification = builder.build()
    
    # 1 is the notification ID (must not be 0)
    mService.startForeground(1, notification)

if __name__ == '__main__':
    set_foreground_notification()
    while True:
        print("Foreground service is working...")
        sleep(2)