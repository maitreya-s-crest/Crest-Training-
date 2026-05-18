# Owner: Maitreya Sapariya
# Project: Crest Training

import datetime


def log(message: str) -> None:
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")