#!/usr/bin/env python3
import time
import sys
import random

# Detect OS terminal capabilities for raw keypresses
try:
    import tty
    import termios
    HAS_TERMIOS = True
except ImportError:
    HAS_TERMIOS = False

# ANSI Color Codes
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"
RESET = "\033[0m"
BOLD = "\033[1m"
REVERSE = "\033[7m"

def clear():
    print("\033[H\033[2J", end="", flush=True)

def get_keypress():
    """Reads a single keypress without needing Enter (Linux/macOS optimization)."""
    if HAS_TERMIOS:
        fd = sys.stdin.fileno()
        try:
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
        except Exception:
            return sys.stdin.read(1)
    else:
        return input()

def type_mode(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def simulate_boot():
    clear()
    boot_logs = [
        f"[{GREEN}  OK  {RESET}] Reached target Local File Systems.",
        f"[{GREEN}  OK  {RESET}] Started Journal Service.",
        f"[{CYAN} INFO {RESET}] Initializing Taqwa & Iman optimization arrays...",
        f"[{GREEN}  OK  {RESET}] Mounted /mnt/ramadan/fasting_data.",
        f"[{CYAN} INFO {RESET}] Scanning horizon for Crescent Moon... {GREEN}FOUND{RESET}.",
        f"[{GREEN}  OK  {RESET}] Reached target Eid-Ul-Fitr Celebrations."
    ]
    for log in boot_logs:
        print(log)
        time.sleep(random.uniform(0.1, 0.3))
    print("\n" + "="*60 + "\n")

def interactive_mirror_select():
    print(f"{BOLD}:: Select a core blessing mirror repository:{RESET}")
    print(f"  1) {CYAN}mecca-primary-core{RESET}      [Location: Holy Mosque]   (Speed: Divine)")
    print(f"  2) {CYAN}medina-sub-mirror{RESET}      [Location: Al-Nabawi]     (Speed: Blessed)")
    print(f"  3) {CYAN}ummah-global-cdn{RESET}       [Location: Worldwide]     (Speed: Infinite)")
    
    while True:
        choice = input(f"\n{BOLD}Enter selection number (1-3): {RESET}").strip()
        if choice in ['1', '2', '3']:
            mirrors = {
                '1': 'mecca-primary-core.pkg.is',
                '2': 'medina-sub-mirror.pkg.is',
                '3': 'ummah-global-cdn.net'
            }
            print(f"\n{GREEN}[+] Locked onto mirror: {mirrors[choice]}{RESET}")
            time.sleep(0.8)
            return mirrors[choice]
        print(f"{RED}[!] Invalid choice. Try again.{RESET}")

def simulate_pacman(mirror):
    print(f"\n{BOLD}[root@archlinux ~]# pacman -Syu local/eid-mubarak-blessings{RESET}")
    time.sleep(0.5)
    print(f":: Synchronizing package databases via {CYAN}{mirror}{RESET}...")
    time.sleep(1)
    
    print(f"\nTargets (1): {CYAN}eid-mubarak-blessings-2026.05{RESET}\n")
    print(f"Total Download Size:   1432.0 MiB")
    print(f"Net Upgrade Size:      2048.0 MiB")
    
    print(f"\n{BOLD}:: Proceed with installation? [Y/n] {RESET}", end="", flush=True)
    time.sleep(1)
    print("Y")
    
    # Custom interactive progress bar
    bar_width = 40
    for i in range(bar_width + 1):
        percent = int((i / bar_width) * 100)
        filled = "█" * i
        empty = "░" * (bar_width - i)
        sys.stdout.write(f"\r(1/1) Downloading blessings... [{GREEN}{filled}{empty}{RESET}] {percent}%")
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.04))
    print()
    
    print(f"({GREEN}1/1{RESET}) Checking keys & signatures               [{GREEN}██████████████████████{RESET}] 100%")
    print(f"({GREEN}1/1{RESET}) Installing custom packages                [{GREEN}██████████████████████{RESET}] 100%")
    time.sleep(0.5)

def interactive_hacker_decrypt():
    clear()
    print(f"{RED}{REVERSE}       [!] CRITICAL SYSTEM WARNING: PACKAGES BLOCKED [!]       {RESET}\n")
    type_mode(f"{YELLOW}The 'eid-mubarak-blessings' binary is encrypted with high-level joy constraints.{RESET}")
    type_mode(f"{YELLOW}Manual human kinetic keyboard entropy is required to bypass security.{RESET}\n")
    
    print(f"{BOLD}{CYAN}>>> MASH ANY KEYS RAPIDLY TO OVERRIDE FIREWALL AND DECRYPT THE BLESSINGS <<<{RESET}\n")
    
    # Entropy Bar Minigame
    entropy = 0
    bar_width = 50
    chars = "0123456789ABCDEF!@#$%^&*"
    
    while entropy < 100:
        get_keypress() # Wait for a key to be mashed
        entropy += random.randint(4, 8)
        if entropy > 100: entropy = 100
        
        # Matrix garbage stream generation per press
        matrix_stream = "".join(random.choice(chars) for _ in range(35))
        filled_width = int((entropy / 100) * bar_width)
        bar = "█" * filled_width + " " * (bar_width - filled_width)
        
        sys.stdout.write(f"\r{GREEN}SYS-DATA: {matrix_stream} | OVERRIDE: [{CYAN}{bar}{RESET}] {entropy}%")
        sys.stdout.flush()

    print(f"\n\n{GREEN}[SUCCESS] Encryption broken! Executing payload...{RESET}")
    print("\a") # Terminal bell audio ping
    time.sleep(1.5)

def reveal_eid():
    clear()
    arch_logo = [
        "       /\\       ",
        "      /  \\      ",
        "     /\\   \\     ",
        "    /      \\    ",
        "   /   ,,   \\   ",
        "  /   |  |   \\  ",
        " /   .'  '.   \\ ",
        "/___'      '___\\"
    ]
    
    eid_text = [
        "███████╗██╗██████╗     ███╗   ███╗██╗   ██╗██████╗  █████╗ ██████╗  █████╗ ██╗  ██╗",
        "██╔════╝██║██╔══██╗    ████╗ ████║██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝",
        "█████╗  ██║██║  ██║    ██╔████╔██║██║   ██║██████╔╝███████║██████╔╝███████║█████╔╝ ",
        "██╔══╝  ██║██║  ██║    ██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██║██╔═██╗ ",
        "███████╗██║██████╔╝    ██║ ╚═╝ ██║╚██████╔╝██████╔╝██║  ██║██║  ██║██║  ██║██║  ██╗",
        "╚══════╝╚═╝╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝"
    ]
    
    full_display = [""] * 2 + [line.center(90) for line in arch_logo] + [""] * 2 + [line.center(90) for line in eid_text] + [""] * 2
    
    # Quick visual shimmer sequence
    for _ in range(4):
        clear()
        for line in full_display:
            print(f"{YELLOW}{line}{RESET}" if "██" in line else f"{CYAN}{line}{RESET}")
        time.sleep(0.2)
        clear()
        for line in full_display:
            print(f"{WHITE}{line}{RESET}" if "██" in line else f"{CYAN}{line}{RESET}")
        time.sleep(0.2)

if __name__ == "__main__":
    try:
        simulate_boot()
        selected_mirror = interactive_mirror_select()
        simulate_pacman(selected_mirror)
        interactive_hacker_decrypt()
        reveal_eid()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Override routine corrupted by user. Eid Mubarak anyway!{RESET}\n")
