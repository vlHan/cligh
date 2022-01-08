# -*- coding: utf-8 -*-

import os 
from colorama import Style, Fore


def banner() -> None:
    try:
        with open("modules/interface/ui.txt", "r") as file:
            print(f"{Fore.RED}{file.read()}{Style.RESET_ALL}")
    except FileNotFoundError:
        with open("cligh/modules/interface/ui.txt", "r") as file:
            print(f"{Fore.RED}{file.read()}{Style.RESET_ALL}")

def clear() -> None:
	"""Clear your terminal"""
	os.system(['clear', 'cls'][os.name == 'nt'])
