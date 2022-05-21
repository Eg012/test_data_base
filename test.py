import subprocess


subprocess.run(
    ["notify-send", "-u", "normal", "-t", "3000", "Hello world", "This is the notification body."],
    check=True)