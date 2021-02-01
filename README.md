# lol-random-skin-picker-py
A script that chooses your League of Legends skin for you

## Installation
### Windows 64-bit
* Go to the [Releases](https://github.com/rogama25/lol-random-skin-picker-py/releases) page and get the latest zip, usually named version-win64.zip
* Uncompress it and run the `main.exe` file.

### Other OS/Manual version
* Clone this repository, either using git clone or downloading and uncompressing the zip.
* Install Python 3.7 or newer. This step will depend on your operating system. Tested on Python 3.9.
* Run `pip install -r requirements.txt` (if it fails, run `python -m pip install -r requirements.txt` on Windows or `python3 -m pip install -r requirements.txt` on Mac or Linux)
* You will also need Tk. This is included in the Windows installation, but you may need to install manually on Mac or Linux
* Run `python main.pyw` on Windows or `python3 main.pyw`. On Windows, you just need to double-click the `main.pyw` file. Don't know about Mac or specific Linux distribution.

## Usage
When running the program, an icon will be added to the tray. On most OS, you just need to left click the icon after locking in your champion, and it will select a random skin for you. On some OS, you will need to right-click it and click `Randomize`.
To exit the program, just close the League client or right-click the tray icon, and select `Exit`.
