# Source - https://stackoverflow.com/a/79836865
# Posted by Fabian Joseph, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-26, License - CC BY-SA 4.0

# ./services/mydownloader.py
print("Entered Service File...")
import time
from jnius import autoclass
from android_notify import Notification


BuildVersion = autoclass("android.os.Build$VERSION")
ServiceInfo = autoclass("android.content.pm.ServiceInfo")
PythonService = autoclass('org.kivy.android.PythonService')


service = PythonService.mService
# foreground_type= ServiceInfo.FOREGROUND_SERVICE_TYPE_DATA_SYNC if BuildVersion.SDK_INT >= 30 else 0
fmt = lambda s: f"{int(s//3600)}h {int((s%3600)//60)}m {int(s%60)}s"


n=Notification(title="Foreground Service Active", message="This service is running in the foreground")
builder=n.fill_args() # not using .send() allowing .startForeground() to send initial notification

service.startForeground(n.id, builder.build())#, foreground_type)

print("Foreground Service is alive. Entering main loop...")
n1 = Notification(title="Running for 0h 0m 0s")
n1.send()
start = time.time()
END_TIME = 6 * 3600
while True:
  elapsed = time.time() - start
  if elapsed >= END_TIME:
    n1.updateTitle(f"Total runtime {fmt(elapsed)}")
    break
  n1.updateTitle(f"Running for {fmt(elapsed)}")
  time.sleep(2)
