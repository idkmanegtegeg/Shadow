import discord
from discord.ext import commands
import json
import datetime
import os
import sys
import random
import asyncio
import requests
import tkinter as tk
from tkinter import ttk, messagebox
import platform
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import re
import emoji as emoji_lib  # pip install emoji if not present
from discord.utils import get

def show_disclaimer():
    # Create main window
    root = tk.Tk()
    root.title("Disclaimer")
    root.geometry("700x500")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')  # Center the window

    # Set up custom style using ttk
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure('TButton', font=('Segoe UI', 12), padding=10)
    style.configure('TLabel', font=('Segoe UI', 14, 'bold'), padding=5)
    style.configure('TFrame', background='#2C3E50')
    style.configure('TText', background='#34495E', foreground='white', font=('Segoe UI', 10))

    # Create a frame for the header
    header_frame = ttk.Frame(root, height=50, style='TFrame')
    header_frame.pack(fill="x", side="top", pady=(10, 5))

    header_label = ttk.Label(header_frame, text="Welcome to the Selfbot Setup", style="TLabel")
    header_label.pack(padx=20, pady=10)

    # Create a frame for the disclaimer text
    text_frame = ttk.Frame(root, style="TFrame")
    text_frame.pack(fill="both", padx=20, pady=(0, 10), expand=True)

    disclaimer_text = """IMPORTANT LEGAL DISCLAIMER:

By using this software, you acknowledge and agree to the following terms and conditions:

1. **Educational Use Only**: This software is intended for educational purposes only. It is designed to help users understand selfbot functionality, automation, and related techniques. Any unauthorized use or misuse of this software is strictly prohibited.

2. **No Redistribution**: You are prohibited from redistributing, reverse-engineering, or making this software available for use in any manner other than through this original distribution channel. Violations of this clause may result in legal action.

3. **Responsibility and Liability**: By using this software, you assume full responsibility for any damages or consequences that may arise from its use. The creator of this software is not liable for any damage to data, hardware, or legal implications caused by the use of this tool.

4. **Illegal Activities**: You agree not to use this software to engage in any activities that violate the Terms of Service of any service (including Discord), break any laws, or perform any actions that could harm others, including but not limited to DDoS attacks, spamming, or data theft.

5. **Indemnification**: You agree to indemnify, defend, and hold harmless the creator of this software from any and all legal claims, losses, damages, or expenses (including legal fees) arising out of your use of this software.

6. **No Warranties**: This software is provided "as is" without any warranty of any kind, express or implied. The creator does not guarantee the functionality, reliability, or suitability of the software for any specific purpose.

7. **Termination**: The creator reserves the right to terminate your use of this software at any time if you violate any of the terms and conditions outlined here.

8. **Compliance with Local Laws**: You agree to comply with all applicable laws, rules, and regulations in your jurisdiction regarding the use of this software.

9. **Termination of Rights**: If you violate these terms, all rights granted to you will be terminated immediately without notice, and you must cease using the software.

10. **Change of Terms**: The creator reserves the right to modify these terms and conditions at any time, and it is your responsibility to regularly review them. Your continued use of the software will constitute your acceptance of any such changes.

By clicking "I Agree," you confirm that you have read, understood, and agreed to these terms. If you do not agree with these terms, you must exit the program immediately.
"""

    # Text widget to display disclaimer
    text = tk.Text(text_frame, wrap="word", height=15, font=("Segoe UI", 12), bg="#34495E", fg="white", relief="flat")
    text.insert("1.0", disclaimer_text)
    text.config(state="disabled")
    text.pack(side="left", fill="both", expand=True)

    # Scrollbar for the text area
    scrollbar = ttk.Scrollbar(text_frame, command=text.yview)
    scrollbar.pack(side="right", fill="y")
    text.config(yscrollcommand=scrollbar.set)

    # Create buttons at the bottom
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10, side="bottom", fill="x")

    def on_agree():
        root.destroy()

    def on_decline():
        messagebox.showinfo("Notice", "You must agree to the disclaimer to use this software.")
        root.destroy()
        sys.exit()

    agree_btn = ttk.Button(button_frame, text="I Agree", command=on_agree, state="disabled")
    agree_btn.pack(side="left", padx=30, pady=10)

    decline_btn = ttk.Button(button_frame, text="Decline", command=on_decline)
    decline_btn.pack(side="right", padx=30, pady=10)

    # Function to handle the close event
    def on_close():
        # Ask for confirmation when the user tries to close the window
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            sys.exit()  # Ensure the script stops running when the window is closed

    # Bind the close button (X) to the on_close function
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Enable "I Agree" button when user scrolls to the bottom
    def on_scroll(*args):
        if text.yview()[1] == 1.0:  # Check if the user is at the bottom
            agree_btn.config(state="normal")
        else:
            agree_btn.config(state="disabled")

    text.config(yscrollcommand=lambda f, l: on_scroll(f, l))

    # Start the GUI loop
    root.mainloop()

# Show disclaimer at the start
show_disclaimer()



def clear_console():
    # Check the OS type
    if platform.system() == "Windows":
        os.system('cls')  # Windows command to clear the console
    else:
        os.system('clear')  # macOS/Linux command to clear the console

# Example usage
clear_console()






gradient_chars = '░▒░▒█▓▄▌▀'

def ansi_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def generate_gradient(start_color, end_color, steps):
    return [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (steps - 1),
        ) for i in range(steps)
    ]

def MainColor(text):
    start_color = (0, 0, 139)
    end_color = (0, 255, 255)
    colors = generate_gradient(start_color, end_color, 9)
    colors += list(reversed(colors[:-1]))

    result = []
    lines = text.split('\n')
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in gradient_chars:
                r, g, b = colors[(i + j) % len(colors)]
                result.append(ansi_color(r, g, b) + char + "\033[0m")
            else:
                result.append(char)
        if i < len(lines) - 1:
            result.append('\n')
    return ''.join(result)

def MainColorMenu(text):
    colors = generate_gradient((0, 0, 139), (0, 255, 255), 12)
    result = []
    plain_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789: -,")
    lines = text.split('\n')
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in plain_chars or char.isspace():
                result.append(char)
            else:
                r, g, b = colors[(i + j) % len(colors)]
                result.append(ansi_color(r, g, b) + char + "\033[0m")
        if i < len(lines) - 1:
            result.append('\n')
    return ''.join(result)


def ansi_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

RESET = "\033[0m"

def generate_gradient(start_color, end_color, steps):
    return [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (steps - 1)
        )
        for i in range(steps)
    ]

def gradient_text(text, start_color, end_color):
    steps = len(text)
    gradient = generate_gradient(start_color, end_color, steps)
    return ''.join(ansi_color(r, g, b) + char for (r, g, b), char in zip(gradient, text)) + RESET

# Then call gradient_text in get_banner()



def get_banner():
    local_version = get_local_version()

    # Apply gradient to "Current Version" and "Github link"
    tag_version = gradient_text("Current Version", (0, 0, 139), (255, 255, 255))
    version_val = gradient_text(local_version, (0, 0, 139), (255, 255, 255))
    tag_github = gradient_text("Github link", (0, 0, 139), (255, 255, 255))

    github_link = gradient_text("https://github.com/idkmanegtegeg/Shadow", (0, 0, 139), (255, 255, 255))

    banner = f"""
                                  ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░
                                ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░
                                ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█ 
                                  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█        
                                ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓ 
                                ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  
                                ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░  
                                ░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░  
                                      ░   ░  ░  ░      ░  ░   ░        ░ ░      ░    
                                                            ░                         
    """  
    banner += f"""
               {tag_version} : {version_val}          {tag_github} -> {github_link}
    """  # Applying gradient

    return banner

# Fetch the local version from version.json


# Fetch the local version from version.json
script_dir = os.path.dirname(os.path.abspath(__file__))
version_path = os.path.join(script_dir, "version.json")

def get_local_version():
    """Retrieve the current version from version.json."""
    try:
        with open(version_path, 'r') as file:
            data = json.load(file)
            return data.get("version", "0.0.0")
    except FileNotFoundError:
        return "0.0.0"



# Function to check for updates
def check_for_update():
    """Check for the update by comparing the current version with the remote version."""
    current_version = get_local_version()

    # GitHub URL to raw version information
    url = "https://raw.githubusercontent.com/idkmanegtegeg/update/main/version.json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            remote_version = response.json().get("version", "0.0.0")

            if current_version != remote_version:
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}]     [INFO]        ->        New update available.")
                print(f"Please update from GitHub: https://github.com/idkmanegtegeg/Shadow")
                print("This version is outdated and will not run. Please update from GitHub.")
                sys.exit(1)  # Exit the script
            else:
                print("Selfbot is up to date.")
        else:
            print("Unable to fetch the update.")
            sys.exit(1)
    except Exception as e:
        print(f"Error checking for update: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print(MainColor(get_banner()))
    check_for_update()


# Color codes
RESET = '\033[0m'
GRAY = '\033[90m'
DARK_PURPLE = '\033[38;2;75;0;130m'  # for time brackets

# Load config
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")
with open(config_path, 'r') as f:
    config = json.load(f)

token = config["token"]
prefix = config["prefix"]
debug_mode = config["debugMode"]

# Initialize bot (only one instance)
bot = commands.Bot(command_prefix=prefix, self_bot=True)

# ANSI Gradient Helpers
def ansi_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def generate_gradient(start_color, end_color, steps):
    return [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (steps - 1)
        )
        for i in range(steps)
    ]

def gradient_text(text, start_color, end_color):
    steps = len(text)
    gradient = generate_gradient(start_color, end_color, steps)
    return ''.join(ansi_color(r, g, b) + char for (r, g, b), char in zip(gradient, text)) + RESET

# Timestamp function: dark purple brackets with gray time
def timestamp():
    return f"{DARK_PURPLE}[{GRAY}{datetime.datetime.now().strftime('%H:%M:%S')}{DARK_PURPLE}]{RESET}"

# Logging Functions
def log_success(bot_user):
    label_success = gradient_text("[SUCCESS]", (0, 0, 139), (255, 255, 255)).ljust(17)
    label_info = gradient_text("[INFO]", (0, 0, 139), (255, 255, 255)).ljust(17)
    arrow_success = f"{GRAY}->".rjust(12)
    arrow_info = f"{GRAY}->".rjust(15)
    tag_login = gradient_text("Logged in as", (0, 0, 139), (255, 255, 255))
    user_val = gradient_text(str(bot_user), (0, 0, 139), (255, 255, 255))
    print(f"{timestamp()}     {label_success}{arrow_success}        {tag_login} {user_val}")
    tag_id = gradient_text("User ID:", (0, 0, 139), (255, 255, 255))
    user_id = gradient_text(str(bot_user.id), (0, 0, 139), (255, 255, 255))
    print(f"{timestamp()}     {label_info}{arrow_info}        {tag_id} {user_id}")
    tag_token = gradient_text("Token:", (0, 0, 139), (255, 255, 255))
    token_val = gradient_text(token[:5] + "..." + token[-3:], (0, 0, 139), (255, 255, 255))
    print(f"{timestamp()}     {label_info}{arrow_info}        {tag_token} {token_val}")

def log_invalid_token(token_str):
    label_failed = gradient_text("[FAILED]", (255, 0, 0), (255, 255, 255)).ljust(17)
    arrow_failed = f"{GRAY}->".rjust(8)
    invalid_text = gradient_text("Invalid Token", (255, 0, 0), (255, 255, 255))
    token_display = gradient_text(token_str, (0, 0, 139), (0, 255, 255))
    print(f"{timestamp()}     {label_failed}{arrow_failed}        {invalid_text} {token_display}")

def log_debug(message):
    label_debug = gradient_text("[DEBUG]", (255, 0, 0), (255, 255, 255)).ljust(17)
    arrow_debug = f"{GRAY}->".rjust(14)
    print(f"{timestamp()}     {label_debug}{arrow_debug}        {DARK_PURPLE}{message}{RESET}")

def log_debug_invalid_token(token_str):
    label_debug = gradient_text("[DEBUG]", (255, 0, 0), (255, 255, 255)).ljust(17)
    arrow_debug = f"{GRAY}->".rjust(14)
    invalid_text = gradient_text("Invalid Token", (255, 0, 0), (255, 255, 255))
    token_display = gradient_text(token_str[:len(token_str)-3], (0, 0, 139), (0, 255, 255)) + f"{GRAY}???{RESET}"
    print(f"{timestamp()}     {label_debug}{arrow_debug}        {invalid_text} {token_display}")

def log_command_success(command_name):
    label_success = gradient_text("[SUCCESS]", (0, 0, 139), (255, 255, 255)).ljust(17)
    arrow_success = f"{GRAY}->".rjust(12)
    command_text = gradient_text(command_name, (0, 0, 139), (255, 255, 255))
    print(f"{timestamp()}     {label_success}{arrow_success}        cmd executed {command_text}")

def log_mass_dm_success(message):
    label_success = gradient_text("[SUCCESS]", (0, 0, 139), (255, 255, 255)).ljust(17)
    arrow_success = f"{GRAY}->".rjust(12)
    message_text = gradient_text(message, (0, 0, 139), (255, 255, 255))
    print(f"{timestamp()}     {label_success}{arrow_success}        Mass DM sent: {message_text}")

def log_failed_send(message, reason):
    label_failed = gradient_text("[FAILED]", (255, 0, 0), (255, 255, 255)).ljust(17)
    arrow_failed = f"{GRAY}->".rjust(12)
    failed_text = gradient_text(f"to Send Msg : {message}", (255, 0, 0), (255, 255, 255))
    reason_text = gradient_text(f"[{reason}]", (255, 0, 0), (255, 255, 255))
    print(f"{timestamp()}     {label_failed}{arrow_failed}        {failed_text} {reason_text}")

def log_command_success2(message):
    label_success = gradient_text("[SUCCESS]", (0, 255, 0), (255, 255, 255)).ljust(17)
    arrow = f"{GRAY}->".rjust(12)
    msg = gradient_text(message, (0, 255, 0), (255, 255, 255))
    print(f"{timestamp()}     {label_success}{arrow}        {msg}")

def log_failed_Leaveserver(message, reason):
    label_failed = gradient_text("[FAILED]", (255, 0, 0), (255, 255, 255)).ljust(17)
    arrow_failed = f"{GRAY}->".rjust(12)
    failed_text = gradient_text(f"{message}", (255, 0, 0), (255, 255, 255))
    reason_text = gradient_text(f"[{reason}]", (255, 0, 0), (255, 255, 255))
    print(f"{timestamp()}     {label_failed}{arrow_failed}        {failed_text} {reason_text}")







# Get favorite server IDs from the "FavitoreServer.txt" file
def get_favorite_servers():
    path = os.path.join(os.path.dirname(__file__), "FavitoreServer.txt")
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

# Mass leave servers function
async def mass_leave_servers():
    success_count = 0
    fail_count = 0

    # Load favorite server IDs
    favorite_ids = get_favorite_servers()

    # Iterate through all the servers the bot is in
    for guild in bot.guilds:
        if str(guild.id) in favorite_ids:
            continue  # Skip favorite servers

        try:
            # Try to leave the server
            await guild.leave()
            log_command_success2(f"Left {guild.name} {guild.id}")
            success_count += 1
        except discord.Forbidden:
            log_failed_Leaveserver(f"Leave server {guild.name} {guild.id}", "Missing Permissions")
            fail_count += 1
        except Exception as e:
            log_failed_Leaveserver(f"Leave server {guild.name} {guild.id}", str(e))
            fail_count += 1

    # Final summary
    summary = f"✅ Left: {success_count} | ❌ Failed: {fail_count}"
    print(summary)

# Discord command to trigger mass leave
@bot.command(name="Massleaveservers")
async def mass_leaveservers_command(ctx):
    # Inform the user that the mass leave is starting
    await ctx.send("Started leaving servers (except favorites)...")
    await mass_leave_servers()












chatpack_path = os.path.join(script_dir, "chatpack.txt")

def get_random_words():
    try:
        with open(chatpack_path, 'r') as f:
            chatpack_words = f.read().splitlines() 
        chatpack_words = [word.strip() for word in chatpack_words if word.strip()]
        if chatpack_words:
            return random.choice(chatpack_words)
        else:
            print("Error: No valid words found in the chatpack.txt file.")
            return None
    except FileNotFoundError:
        print(f"Error: {chatpack_path} not found.")
        return None

# Global variable to hold the spamming task for Chatpack command
spamming_task = None

# Global spam_chatpack function; if a Discord context is provided, it sends messages there; otherwise, prints to console.
async def spam_chatpack(ctx=None):
    try:
        while True:
            word = get_random_words()
            if word:
                try:
                    if ctx:
                        await ctx.send(word)
                    else:
                        print(word)
                    log_command_success(f"message sent: {word}")
                    await asyncio.sleep(0.05)  # fast but risky; adjust if needed
                except discord.errors.HTTPException as e:
                    if e.status == 429:
                        retry_after = int(e.response.headers.get("Retry-After", 2))
                        print(f"[Rate Limit] Hit 429, sleeping for {retry_after} seconds...")
                        await asyncio.sleep(retry_after)
                    else:
                        raise  # let other HTTP errors crash it for now
            else:
                await asyncio.sleep(0.2)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"Unexpected error in spam_chatpack: {e}")

# !Chatpack command to spam random words from chatpack.txt in Discord
@bot.command()
async def Chatpack(ctx, *, target: str = None):
    global spamming_task

    if spamming_task is not None and not spamming_task.done():
        await ctx.send("Chatpack spam is already running!")
        return

    if not target:
        await ctx.send("You must enter a target (mention or name)! Example: `!Chatpack @user`")
        return

    mention_text = target.strip()

    # Try to get Member object if in guild
    if ctx.guild:
        try:
            member = await commands.MemberConverter().convert(ctx, target)
            mention_text = member.mention
        except commands.MemberNotFound:
            # Fall back to raw text if not found
            mention_text = target.strip()

    async def spam_chatpack_loop():
        try:
            while True:
                word = get_random_words()
                if word:
                    msg = f"{word} {mention_text}"
                    try:
                        await ctx.send(msg)
                        log_command_success(f"message sent: {msg}")
                        await asyncio.sleep(0.05)
                    except discord.errors.HTTPException as e:
                        if e.status == 429:
                            retry_after = int(e.response.headers.get("Retry-After", 2))
                            print(f"[Rate Limit] Hit 429, sleeping for {retry_after} seconds...")
                            await asyncio.sleep(retry_after)
                        else:
                            raise
                else:
                    await asyncio.sleep(0.2)
        except asyncio.CancelledError:
            pass
        except Exception as e:
            print(f"Unexpected error in spam_chatpack: {e}")

    spamming_task = asyncio.create_task(spam_chatpack_loop())
    log_command_success("!Chatpack started")

# !stop command to stop any ongoing Chatpack spamming
@bot.command()
async def stop(ctx):
    global spamming_task
    if spamming_task is not None and not spamming_task.done():
        spamming_task.cancel()
        await ctx.send("Chatpack spam stopped.")
        log_command_success("!stop")
        spamming_task = None
    else:
        await ctx.send("No Chatpack spam task is running.")






# !massdm command to send a message to every DM channel on Discord (once per channel)
@bot.command()
async def massdm(ctx, *, message: str):
    count = 0
    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel):
            try:
                await channel.send(message)
                count += 1
            except Exception as e:
                print(f"Could not send DM to {channel}: {e}")
    await ctx.send(f"Mass DM sent to {count} channels.")
    log_command_success(f"!massdm {message}")

# Debug Console Task: if debug_mode is on, allow interactive input from the console
async def debug_console():
    global spamming_task  # Declare global at the very beginning of the function
    while True:
        line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
        if not line:
            break
        line = line.strip()

        # Debug: Print the received line
        print(f"Received input: '{line}'")

        # Process debug commands
        if line.startswith("Debug"):
            debug_command = line[len("Debug"):].strip()
            if debug_command.lower() == "invalid token":
                log_debug_invalid_token(token)
            else:
                log_debug(debug_command)

        # Chatpack command
        elif line.lower().startswith("!chatpack"):
            parts = line.split()
            if len(parts) >= 2:
                target_id = parts[1]
                try:
                    channel = bot.get_channel(int(target_id))
                    if channel is None:
                        for dm in bot.private_channels:
                            if isinstance(dm, discord.DMChannel) and str(dm.recipient.id) == target_id:
                                channel = dm
                                break
                    if channel is not None:
                        if spamming_task is not None and not spamming_task.done():
                            print("Chatpack spam is already running (console).")
                        else:
                            spamming_task = asyncio.create_task(spam_chatpack(channel))
                            log_command_success(f"!Chatpack (console) {target_id}")
                    else:
                        print("No channel or DM found for that ID.")
                except Exception as e:
                    print(f"Error processing channel ID: {e}")
            else:
                print("Usage: !Chatpack <channel_id>")

        # Stop chatpack
        elif line.lower().startswith("!stop"):
            if spamming_task is not None and not spamming_task.done():
                spamming_task.cancel()
                print("Chatpack spam stopped (console).")
                log_command_success("!stop (console)")
                spamming_task = None
            else:
                print("No Chatpack spam task is running (console).")

        # Mass DM
        elif line.lower().startswith("!massdm"):
            parts = line.split(" ", 1)
            if len(parts) < 2:
                print("Usage: !massdm <message>")
            else:
                dm_message = parts[1]
                count = 0
                for channel in bot.private_channels:
                    if isinstance(channel, discord.DMChannel):
                        try:
                            await channel.send(dm_message)
                            count += 1
                        except Exception as e:
                            print(f"Could not send DM to {channel}: {e}")
                print(f"Mass DM sent to {count} channels (console).")
                log_command_success(f"!massdm {dm_message} (console)")

        # AutoReact command
        elif line.lower().startswith("!autoreact"):
            parts = line.split()
            if len(parts) == 2:
                emoji = parts[1]
                target_id_input = input("Enter user ID for auto-react (numeric): ").strip()
                if not target_id_input:
                    print("No user ID provided. Command aborted.")
                    continue
                try:
                    target_id = int(target_id_input)
                except ValueError:
                    print("Invalid user ID provided. It must be numeric.")
                    continue
            elif len(parts) >= 3:
                emoji = parts[1]
                try:
                    target_id = int(parts[2])
                except ValueError:
                    print("Invalid user ID provided. It must be numeric.")
                    continue
            else:
                print("Usage: !autoreact <emoji> [user_id]")
                continue

            # Store the auto-react setting
            auto_react_settings[target_id] = emoji

            # Try to fetch the user by ID
            user = bot.get_user(target_id)
            if user:
                log_command_success(f"AutoReact set for {user.name} with {emoji}")
            else:
                log_command_success(f"AutoReact set for user ID {target_id} with {emoji}")

        # Mass Leave Servers (with Favorite Server Skipping)
        elif line.lower().startswith("!massleaveservers"):
            await mass_leave_servers()



        else:
            print("Unrecognized input:", line)








    # Store the auto-react setting
    auto_react_settings[target_id] = emoji
    
    # Try to fetch the user's name from Discord using the bot's cache
    user = bot.get_user(target_id)
    if user is not None:
        log_command_success(f"!autoreact set for {user.name} with {emoji}")
    else:
        log_command_success(f"!autoreact set for user ID {target_id} with {emoji}")

    

@bot.event
async def on_ready():
    log_success(bot.user)
    if debug_mode:
        asyncio.create_task(debug_console())

@bot.command()
async def ping(ctx):
    try:
        await ctx.send("Pong!")
        log_command_success("!ping")
    except Exception as e:
        if debug_mode:
            log_debug(f"Ping command failed: {e}")
            log_invalid_token(token)

# ----- Update Functionality Addition -----
# Import the update module (make sure update.py is in the same folder)



auto_react_settings = {}

@bot.command()
async def autoreact(ctx, emoji: str, user_id: str = None):
    """
    Set auto-react behavior in Discord.
    Usage: !autoreact <emoji> [user_id]
    If no user_id is provided, it defaults to the author.
    """
    if user_id is None:
        target_id = ctx.author.id
    else:
        try:
            target_id = int(user_id)
        except ValueError:
            await ctx.send("Invalid user ID. Please provide a numeric ID.")
            return

    # Check if emoji is in the format of :emoji_name:
    if emoji.startswith(":") and emoji.endswith(":"):
        emoji = emoji[1:-1]  # Strip the colons to get the emoji name
        custom_emoji = get(ctx.guild.emojis, name=emoji)  # Get the custom emoji from the server
        if custom_emoji:
            emoji = str(custom_emoji)  # Convert custom emoji to string
        else:
            # If it's not a custom emoji, we'll use the unicode emoji directly
            pass
    
    auto_react_settings[target_id] = emoji

    user = bot.get_user(target_id)
    username = f"{user.name}#{user.discriminator}" if user else f"ID:{target_id}"

    await ctx.send(f"Auto-react enabled: messages from **{username}** will be reacted with {emoji}.")
    log_command_success(f"AutoReact set to {username} with emoji {emoji}")

@bot.event
async def on_message(message):
    if not message.author.bot:
        emoji = auto_react_settings.get(message.author.id)
        if emoji:
            try:
                await message.add_reaction(emoji)
            except Exception as e:
                print(f"() - Failed to add reaction to message from {message.author}: {e}")
    await bot.process_commands(message)

# Console command handler
async def debug_console():
    global spamming_task
    while True:
        line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
        if not line:
            break
        line = line.strip()

        # Handle !Chatpack command
        if line.lower().startswith("!chatpack"):
            parts = line.split()
            if len(parts) >= 2:
                target_id = parts[1]
                mention_id = parts[2] if len(parts) > 2 else None

                try:
                    channel = bot.get_channel(int(target_id))

                    # Try DM fallback if channel not found
                    if channel is None:
                        for dm in bot.private_channels:
                            if isinstance(dm, discord.DMChannel) and str(dm.recipient.id) == target_id:
                                channel = dm
                                break

                    if channel is not None:
                        if spamming_task is not None and not spamming_task.done():
                            print("Chatpack spam is already running (console).")
                        else:
                            # DM spam
                            if isinstance(channel, discord.DMChannel):
                                spamming_task = asyncio.create_task(spam_chatpack(channel))
                                log_command_success(f"!Chatpack (DM) to {target_id}")
                            # Guild channel spam (mention user if provided)
                            else:
                                if not mention_id:
                                    print("For server channels, you must provide a user ID to mention.")
                                else:
                                    user = bot.get_user(int(mention_id))
                                    mention_text = user.mention if user else f"<@{mention_id}>"

                                    async def chatpack_server_spam():
                                        try:
                                            while True:
                                                word = get_random_words()
                                                if word:
                                                    msg = f"{word} {mention_text}"
                                                    await channel.send(msg)
                                                    log_command_success(f"Sent: {msg}")
                                                    await asyncio.sleep(0.05)
                                                else:
                                                    await asyncio.sleep(0.2)
                                        except asyncio.CancelledError:
                                            pass
                                        except Exception as e:
                                            print(f"Unexpected error in chatpack_server_spam: {e}")

                                    spamming_task = asyncio.create_task(chatpack_server_spam())
                                    log_command_success(f"!Chatpack (guild) to {target_id} mentioning {mention_id}")
                    else:
                        print(f"No channel or DM found for ID: {target_id}")

                except ValueError:
                    print("Error: Invalid target ID format. Please provide numeric IDs.")
                except Exception as e:
                    print(f"Error handling chatpack: {e}")
            else:
                print("Usage:\n  !chatpack <channel_id> <user_id> (for server)\n  !chatpack <user_id> (for DM)")

        # Stop command
        elif line.lower().startswith("!stop"):
            if spamming_task is not None and not spamming_task.done():
                spamming_task.cancel()
                spamming_task = None
                print("Chatpack spam stopped.")
                log_command_success("!stop (console)")
            else:
                print("No Chatpack task is running.")

        # Handle !autoreact command
        elif line.lower().startswith("!autoreact"):
            parts = line.split()

            if len(parts) < 2:
                print("Usage: !autoreact <emoji> [user_id]")
                continue

            emoji = parts[1]
            if len(parts) >= 3:
                try:
                    target_id = int(parts[2])
                except ValueError:
                    print("Invalid user ID. Must be numeric.")
                    continue
            else:
                user_input = input("Enter user ID (leave blank to use selfbot ID): ").strip()
                if user_input == "":
                    target_id = bot.user.id
                else:
                    try:
                        target_id = int(user_input)
                    except ValueError:
                        print("Invalid user ID. Must be numeric.")
                        continue

            if emoji.startswith(":") and emoji.endswith(":"):
                emoji = emoji[1:-1]
                custom_emoji = get(bot.get_guild(message.guild.id).emojis, name=emoji)
                if custom_emoji:
                    emoji = str(custom_emoji)

            auto_react_settings[target_id] = emoji
            user = bot.get_user(target_id)
            username = f"{user.name}#{user.discriminator}" if user else f"ID:{target_id}"
            log_command_success(f"AutoReact set to {username} with emoji {emoji}")

        elif line.lower().startswith("!massleaveservers"):
            await mass_leave_servers()

        else:
            print(f"Unrecognized input: {line}")




@bot.event
async def on_ready():
    log_success(bot.user)
    if debug_mode:
        asyncio.create_task(debug_console())




# Run bot and handle login failure with debug logging if enabled
try:
    bot.run(token, bot=False)
except discord.LoginFailure:
    if debug_mode:
        log_invalid_token(token)


