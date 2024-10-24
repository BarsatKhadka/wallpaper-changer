import os
import random
import time
import subprocess
import argparse

def change_wallpaper(wallpaper_folder):
    wallpapers = [f for f in os.listdir(wallpaper_folder) if f.endswith(('.png' , '.jpeg' , '.jpg'))]

    if not wallpapers:
        print(f"No valid image files found in {wallpaper_folder}")

    wallpaper = random.choice(wallpapers)

    wallpaper_path = os.path.join(wallpaper_folder,wallpaper)

    subprocess.run(["gsettings","set","org.cinnamon.desktop.background","picture-uri", f"file://{wallpaper_path}"])

    print(f"Wallpaper changed to: {wallpaper}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wallpaper changer for Linux Mint (Cinnamon and XFCE only)")
    parser.add_argument('--folder', type=str, help='Path to the folder with wallpapers', required=True)
    parser.add_argument('--time', type=int, help='Time interval (in minutes) to change the wallpaper', default=5)
    args = parser.parse_args()


    if not os.path.isdir(args.folder):
        print(f"Error: The folder {args.folder} does not exist.")
        exit(1)

    interval_seconds = args.time * 60

    
    try:
        while True:
            change_wallpaper(args.folder)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("Wallpaper changer stopped.")
        