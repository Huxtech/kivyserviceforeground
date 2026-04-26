# Source - https://stackoverflow.com/a/79836865
# Posted by Fabian Joseph, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-26, License - CC BY-SA 4.0

# ./p4a/hook.py
from pathlib import Path
from pythonforandroid.toolchain import ToolchainCL

def after_apk_build(toolchain: ToolchainCL):
  manifest_file = Path(toolchain.\_dist.dist_dir) / "src" / "main" / "AndroidManifest.xml"
  text = manifest_file.read_text(encoding="utf-8")

  # Change these three lines to fit your use-case 
  package = "org.testapp.testapp" # Find value in your buildozer.spec "package.domain.package.name"
  service_name="Testservice"
  foreground_type="dataSync"

  target = f'android:name="{package}.Service{service_name.capitalize()}"'

  # Inject foregroundServiceType
  pos = text.find(target)

  if pos != -1:
    end = text.find("/>", pos)
    text = (text[:end] + f'android:foregroundServiceType="{foreground_type}"' + text[end:])
    print("Successfully Added foregroundServiceType to ServiceMydownloader")


  # Write back the final manifest
  manifest_file.write_text(text, encoding="utf-8")
  print("Manifest update completed",text)
