import os
import time

os.system("pip install pyinstaller")

def banner():
    banner1 = """
            ====================
            Py-to-exe by iFanpS
            Inspired by NumeX
            ====================
            """
    print(banner1)
def utama():
    pemilihan = input("With icon or without icon: [wthicon]/[wthouticon] ")
    if pemilihan == "withicon":
        ph1 = input("Put your file.py directory: ")
        phicon = input("Put your icon directory: ")
        os.system(f"pyinstaller -F -i {phicon} {ph1}")
        time.sleep(5)
        print("Your exe is DONE!")
        exit()
    elif pemilihan == "wthouticon":
        ph2 = input("Put your file.py directory: ")
        os.system(f"pyinstaller -F {ph2}")
        print("Your exe is DONE!")
        time.sleep(5)
        exit()
    else:
        print("Something wrong!!")
        input("Click enter to close... ")

if __name__ == "__main__":
    banner()
    time.sleep(1)
    utama()