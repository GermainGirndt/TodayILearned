Components -> no semantic value; no style; no html
	* Alls standard -> display: flex


View: div, footer, header, main, aside, section
Text: p, span, strong, h1, h2, h3


** axios with react native: address

ios com emulador local
ios com físico ip máquina
android - emulador: adb reverse tcp:3935 tcp:3935 (redirect localhost -> emulator to computer)
android - emulator (android studio): ip 10.0.2.2
android - emulator (genymotion): ip 10.0.3.2
android + físico - machine ip (settings -> Debbuging -> Debug server and port for device || redirect adb port? )


REMOVING ALL ADB REVERSES
adb reverse --remove-all

REMOVING SPECIFIC ADB REVERSE
adb forward --remove tcp:8081


IP

ip addr show | grep 192


for logging messages in the console:


react-native log-ios        # For iOS
react-native log-android    # For Android



* **error - Unable to load script from assets index.android.bundle**

Add to package.json:
```
"android-linux": "react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res && react-native run-android"

```

* **error - ENOENT: no such file or directory, open 'android/app/src/main/assets/index.android.bundle**

Simply create 'assets' folder in
```
android/app/src/main/assets
```
