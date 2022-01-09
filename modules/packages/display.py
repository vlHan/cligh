# -*- coding: utf-8 -*-
import requests
from colorama import Style, Fore
import sys, os

from modules.packages.exceptions import *

__author__ = "vlHan"
__version__ = "1.1"
__license__ = "MIT"

GITHUB_API_BASE = "https://api.github.com/"
RA = Style.RESET_ALL


class cligh:
    def __init__(self, username: str, repository: str, endopoint: str) -> None:
        """CLI Search tool for GitHub."""
        self.username   = username
        self.repository = repository
        self.endpoint   = endopoint

    def display_user(self) -> None:
        """Display user informations.
        """
        try:
            req = requests.get(GITHUB_API_BASE + self.endpoint)
            response = req.json()
        except requests.ConnectionError:
            raise requests.ConnectionError

        if req.status_code == 200:
            print(f"{Fore.CYAN}User Informations:{RA}\n")
            print(
                f"{Fore.GREEN}[+] Username:{RA} {response['login']}"
                f"\n{Fore.GREEN}[+] ID:{RA} {response['id']}"
                f"\n{Fore.GREEN}[+] Bio:{RA} {response['bio']}"
                f"\n{Fore.GREEN}[+] Location:{RA} {response['location']}"
                f"\n{Fore.GREEN}[+] Company:{RA} {response['company']}"
                f"\n{Fore.GREEN}[+] Web URL:{RA} {response['html_url']}"
                f"\n{Fore.GREEN}[+] Public Repos:{RA} {response['public_repos']}"
                f"\n{Fore.GREEN}[+] Blog/Website:{RA} {response['blog']}"
            )

            print(" ")
            sys.exit(0)

        else:
            raise UserNameNotCorrect

    def display_repository(self) -> None:
        """Display the repositories of the user.
        """
        try:
            req = requests.get(GITHUB_API_BASE + self.endpoint)
            response = req.json()
        except requests.ConnectionError:
            raise requests.ConnectionError

        if req.status_code == 200:
            print(f"{Fore.CYAN}Repository Informations:{RA}\n")
            print(
                f"{Fore.GREEN}[+] Repository:{RA} {response['name']}"
                f"\n{Fore.GREEN}[+] Description:{RA} {response['description']}"
                f"\n{Fore.GREEN}[+] Stars:{RA} {response['stargazers_count']}"
                f"\n{Fore.GREEN}[+] Created at:{RA} {response['created_at']}"
                f"\n{Fore.GREEN}[+] Clone URL:{RA} {response['clone_url']}"
                f"\n{Fore.GREEN}[+] Languages:{RA} {response['language']}\n"
            )
            sys.exit(0)

        else:
            raise RepositoryNotFound

    def download_repository(self, ext) -> None:
        """Download the user repository.
        """
        header = {"Accept": "application/vnd.github.v3+json"}
        try:
            req = requests.get(GITHUB_API_BASE + self.endpoint, headers=header)
        except requests.ConnectionError:
            raise requests.ConnectionError

        if os.path.isfile(f"{self.repository}.zip") or os.path.isfile(f"{self.repository}.tar"):
            print(f"{Fore.RED}The repository is already downloaded.{RA}")
        else:
            if req.status_code == 200:
                print(f'{Fore.GREEN}[+] Owner:{RA} {self.username}')
                print(f'{Fore.GREEN}[+] Diretory:{RA} /cligh/{self.repository}.{ext}')
                print(f'{Fore.GREEN}[+] Display:{RA} {req.content[:10]}')
                print(f'{Fore.GREEN}[+] Size:{RA} {len(req.content)}')
                with open(f"cligh/{self.repository}.{ext}", "wb") as f:
                    f.write(req.content)

                print(f"\n{Fore.GREEN}Downloaded with success.{RA}")

            else:
                raise RepositoryNotFound
