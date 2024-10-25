
# Wallpaper Changer for Linux Mint

This Python script allows users to automatically change their desktop wallpaper every specified number of minutes. (The default is 5 minutes) 

It works with Linux Mint (Cinnamon and XFCE).


## Features
* Automatically change wallpapers at a regular interval.
* Supports PNG, JPEG, and JPG formats.
* Lightweight and easy to use.

## Prerequisites
* Python 3.6 or higher
* gsettings (Usually inbuilt in Linux Mint) 

## Installation 
 1 )  Clone this repository:
 ```
 git clone https://github.com/BarsatKhadka/wallpaper-changer.git
```
 2 ) Install required dependencies
 ```
 sudo apt-get install python3
```







## Usage

Run the script with the following command:
```
python3 /home/user_name/wallpaper-changer/wallpaper_changer.py --folder /path/to/your/wallpapers --time 30
```

Replace ```/user_name/``` with your actual username.
Replace ```/path/to/your/wallpapers``` with the folder you have your wallpapers in.

Replace ```30``` with the number of minutes you want the wallpaper to change.

## Notes

This script runs only on Linux Mint. (Cinnamon and XFCE)
## Set up as Start up app

1 ) Make the script executable 

```
chmod +x /path/to/your/script/wallpaper_changer.py
```

Replace ```/path/to/your/script``` with folder you have your wallpapers in.

2 ) Open Startup Applications:

* Go to the Menu and search for Startup Applications.
* Click to open the Startup Applications manager.

3 ) Add Your Script:

* In the Startup Applications window, click the Add button.
* In the pop-up dialog:
* Name: Enter a name like "Wallpaper Changer".
* Command: Enter the full command to run your Python script.
```
python3 /path/to/your/script/wallpaper_changer.py --folder /path/to/your/wallpapers --time 60
```

Replace the paths with your actual script location and desired folder and interval.

4 ) Save

* Click Add to save the entry

5 ) Test

* Restart your system to ensure that the wallpaper changer script runs automatically on login.

## License

This project is licensed under MIT License

