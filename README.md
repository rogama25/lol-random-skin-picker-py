# lol-random-skin-picker-py
A script that chooses your League of Legends skin for you

## Installation
### Windows 64-bit
* Go to the [Releases](https://github.com/rogama25/lol-random-skin-picker-py/releases) page and get the latest zip, usually named version-win64.zip
* Uncompress it and run the `main.exe` file.

**Some people told me that this version is sometimes flagged as a virus. Check an explanation below.**

### Other OS/Manual version
* Clone this repository, either using git clone or downloading and uncompressing the zip.
* Install Python 3.7 or newer. This step will depend on your operating system. Tested on Python 3.9.
* Run `pip install -r requirements.txt` (if it fails, run `python -m pip install -r requirements.txt` on Windows or `python3 -m pip install -r requirements.txt` on Mac or Linux)
* You will also need Tk. This is included in the Windows installation, but you may need to install manually on Mac or Linux
* Run `python main.pyw` on Windows or `python3 main.pyw`. On Windows, you just need to double-click the `main.pyw` file. Don't know about Mac or specific Linux distribution.

### Compile it yourself
* Clone this repository.
* Install Python 3.7 or newer.
* Install the requirements.
* Install pyinstaller: `pip install pyinstaller`
* Run `pyinstaller main.spec`
* You will have the `main.exe` file in a new folder called `dist`. To run it, you will have to copy the `icon.png` file in the same folder.

## Usage
When running the program, an icon will be added to the tray. On most OS, you just need to left click the icon after locking in your champion, and it will select a random skin for you. On some OS, you will need to right-click it and click `Randomize`.

To exit the program, just close the League client or right-click the tray icon, and select `Exit`.

## My antivirus is flagging this as a virus!
It seems like PyInstaller, a program that I use to compile my Python scripts to get an .exe file, so it can be run easily [it's getting flagged by some antivirus](https://github.com/pyinstaller/pyinstaller/issues/5490). There isn't much I can do to fix this myself.

If you don't trust me, you can always read the source code, scan it at VirusTotal or other antivirus and then run from source or compile it yourself. I promise it's not that hard.
