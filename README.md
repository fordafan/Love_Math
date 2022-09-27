<h1>iLoveMath - Python/ Kivy android app</h1>

Primary school level math app developed in Kivy (Android).
App still in development some bugs may occur.
Simple UI, some design solutions will be added in the nearest future.

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Android build](#build-for-android)
* [Apk installation on physical Android device](#apk-installation-on-physical-android-device)

## General info

App capabilities (mathematical operations training - at primary school level):

* adding/ substraction
* multiplication
* roman numbers exchange to arabic numerals
* percentage estimation (to be implemented)
* Store result in database

App capabilities on Android:

* send sms with final result from Android device phone book
* Store result in database

Android permissions used by the app:

* Read external storage (for database)
* Write external storage (for database)
* Read contacts (sms sending)
* Send sms

## Technologies

Project created with:

* Python 3.8.10
* Kivy 2.1.0
* KivyMD 0.104.2
* sqlite3
* Roman 3.3 (roman nums lib)
* Kvdroid 0.2.9 (Android interaction)
* Plyer 2.0.0 (Android interaction)
* Pyjnius 1.4.1 (Android interaction)
* Buildozer (build for Android)

## Prerequisites

To be run on desktop (see [Setup](#setup)) - just use pip to install requirements.txt in you virtual environment to be set to go.

If You would like to build apk file and use it in Android emulator or physical device you will need:

1. Buildozer (apk build) installed in project root: [Buildozer install homepage](https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android "Install buildozer")
2. Android emulator (will focus on GenyMotion and VSCode IDE)/ or physical device.

GenyMotion from VSCode: [GenyMotion menagement Vscode extension](https://marketplace.visualstudio.com/items?itemName=abehrad.genymotion "VScode extension for Genymotion") <br>
GenyMotion set-up example: [GenyMotion set-up](https://www.geeksforgeeks.org/how-to-set-up-an-emulator-for-vscode/ "Genymotion set-up")

## Setup

### Desktop installation

Highly recommended to establish virtual environment before installation.

Install codebase:

```
$ git clone https://github.com/fordafan/Love_Math.git
$ cd Love_Math
$ pip install -r requirements.txt
```

At this point app can be started by:

```
$ python3 main.py
```


### Build for Android

Buildozer build (based on predefined buildozer.spec - attached to this repo)

```
$ buildozer -v android debug
```

In order to debug/ read logs (ADB) during build/ runtime at emulator

```
adb logcat YOUR_DEVICE_IP > log.txt
```

apk will be produced into bin directory at project root.
apk can be then installed in Android Emulator or physical device.

## apk installation on physical Android device

** To be developed