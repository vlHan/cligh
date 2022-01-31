# -*- coding: utf-8 -*-

import os 
from rich import print

def clear() -> None:
	"""Clear your terminal"""
	os.system(['clear', 'cls'][os.name == 'nt'])


def banner() -> None:
    """Terminal banner"""
    clear()
    try:
        with open("modules/interface/ui.txt", "r") as file:
            print(f"[red]{file.read()}[/]")
    except FileNotFoundError:
        with open("cligh/modules/interface/ui.txt", "r") as file:
            print(f"[red]{file.read()}[/]")
