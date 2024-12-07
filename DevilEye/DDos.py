import time
from colorama import Fore

def print_splash_screen():
    print(Fore.LIGHTGREEN_EX + """
      ██████████████████████
      ██████████████████████
      ██████████████████████
    """)

def starting_ddos_attack():
    print(Fore.LIGHTGREEN_EX + "-------------------------------")
    print(Fore.LIGHTYELLOW_EX + "  Initializing DDoS Attack...")
    time.sleep(0.5)
    print(Fore.LIGHTMAGENTA_EX + "    Connecting to Target...\n")
    time.sleep(0.5)
    print(Fore.LIGHTCYAN_EX + "      Synchronizing Data...\n")
    time.sleep(0.5)
    print(Fore.LIGHTRED_EX + "    ██████████████████████")
    print(Fore.LIGHTRED_EX + "    ██████████████████████")
    print(Fore.LIGHTRED_EX + "    ██████████████████████")
    time.sleep(1)
    print(Fore.LIGHTWHITE_EX + "  Attack Initialized. Launching...\n")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + "  Activating Command Sequence...\n")
    time.sleep(0.5)
    print(Fore.LIGHTGREEN_EX + "  Attack in Progress...\n")
    print(Fore.LIGHTYELLOW_EX + "  ██████████████████████")
    print(Fore.LIGHTWHITE_EX + "-------------------------------")
    print(Fore.LIGHTMAGENTA_EX + "  Ctrl + C To Stop Attack")

# Example of the function usage:
print_splash_screen()
starting_ddos_attack()
