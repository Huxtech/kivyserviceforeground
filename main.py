

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import *
from kivy.utils import platform
from jnius import autoclass


class initialscreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def start_my_service():
        if platform == 'android':
            from jnius import autoclass
            # The package name is found in buildozer.spec (package.domain + package.name)
            # Service name is 'Service' + 'Myservice' (first letter capitalized)
            service = autoclass('org.testapp.testapp.ServiceMyservice')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            service.start(mActivity, "")
     

    def stop_service(self, nm):
        from android import mActivity
        context = mActivity.getApplicationContext()


        SERVICE_NAME = str(context.getPackageName()) + '.Service' + nm

        Service = autoclass(SERVICE_NAME)

        Intent = autoclass('android.content.Intent')
        service_intent = Intent(mActivity, Service)


        mActivity.stopService(service_intent)

class theapp(App):
    def build(self):
        self.screenm = ScreenManager(transition=FadeTransition())

        self.initialscreen = initialscreen()
        screen = Screen(name = 'initialscreen')
        screen.add_widget(self.initialscreen)
        self.screenm.add_widget(screen)
        self.get_permit()
        return self.screenm





    def get_permit(self):
        if platform == 'android':
            from android.permissions import Permission, request_permissions 

            def callback(permissions, results):
                granted_permissions = [perm for perm, res in zip(permissions, results) if res]
                denied_permissions = [perm for perm, res in zip(permissions, results) if not res]

                if denied_permissions:
                    print('Denied permissions:', denied_permissions)

                elif granted_permissions:
                    print('Got all permissions')
                else:
                    print('No permissions were granted or denied')

            requested_permissions = [
                Permission.INTERNET,
                Permission.FOREGROUND_SERVICE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.SYSTEM_ALERT_WINDOW
            ]
            request_permissions(requested_permissions, callback)



if __name__ == "__main__":
    theapp().run()