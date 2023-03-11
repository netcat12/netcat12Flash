import os
import sys
from termcolor import colored
from tqdm import tqdm
import time

class Netcat12Flash:
    def __init__(self):
        self.iso_path = "/path/to/linux.iso"
        self.usb_device = None

    def unmount_drive(self):
        if self.usb_device:
            os.system(f"umount {self.usb_device}")
            print(colored(f"Unmounted {self.usb_device}.\n", "yellow"))

    def flash_system(self):
        if not self.usb_device:
            print(colored("No USB device specified.\n", "red"))
            return
        
        self.unmount_drive()

        command = f"sudo dd if={self.iso_path} of={self.usb_device} bs=4M status=progress"
        os.system(command)
        print(colored(f"\nFlashing completed on {self.usb_device}.", "yellow"))

    def run(self):
        banner = colored("""
 __      ___________   _____ _   _____ 
 \ \    / /  Netcat12 Flash \ \ / /_ _| \ | ____|
  \ \  / /| |__) \ \ V / | ||  \|  _|  
   \ \/ / |  ___/ > <  | || |\  | |___ 
    \__/  |_|   /_/\_\|___|_| \_|_____|
""", "red")
        print(banner)

        while True:
            self.usb_device = input(colored("Enter the device name of your USB drive: ", "yellow")).strip()
            if not self.usb_device:
                print(colored("Please enter a valid device name.", "red"))
                continue
            break

        for i in tqdm(range(10), desc=colored("Starting the flashing operation", "red")):
            time.sleep(1)

        self.flash_system()

if __name__ == "__main__":
    netcat12_flash = Netcat12Flash()
    netcat12_flash.run()
