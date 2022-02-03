import requests
from rich import print
import os

from modules.packages.exceptions import *

__author__ = "vlHan"
__version__ = "1.1"
__license__ = "MIT"

GITHUB_API_BASE = "https://api.github.com/"


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

        if "message" in response:
            raise UserNameNotCorrect

        print("[cyan]User Informations:[/]\n")
        print(
            f"[green][+] Username:[/] {response['login']}"
            f"\n[green][+] ID:[/] {response['id']}"
            f"\n[green][+] Bio:[/] {response['bio']}"
            f"\n[green][+] Location:[/] {response['location']}"
            f"\n[green][+] Company:[/] {response['company']}"
            f"\n[green][+] Web URL:[/] {response['html_url']}"
            f"\n[green][+] Public Repos:[/] {response['public_repos']}"
            f"\n[green][+] Blog/Website:[/] {response['blog']}"
        )

    def display_repository(self) -> None:
        """Display the repositories of the user.
        """
        try:
            req = requests.get(GITHUB_API_BASE + self.endpoint)
            response = req.json()
        except requests.ConnectionError:
            raise requests.ConnectionError

        if "message" in response:
            raise RepositoryNotFound
        print("[cyan]Repository Informations:[/]\n")
        print(
            f"[green][+] Repository:[/] {response['name']}"
            f"\n[green][+] Description:[/] {response['description']}"
            f"\n[green][+] Stars:[/] {response['stargazers_count']}"
            f"\n[green][+] Created at:[/] {response['created_at']}"
            f"\n[green][+] Clone URL:[/] {response['clone_url']}"
            f"\n[green][+] Languages:[/] {response['language']}\n"
        )

    def download_repository(self, ext) -> None:
        """Download the user repository.
        """
        header = {"Accept": "application/vnd.github.v3+json"}
        try:
            req = requests.get(GITHUB_API_BASE + self.endpoint, headers=header)
        except requests.ConnectionError:
            raise requests.ConnectionError

        try:
            if os.path.isfile(f"{self.repository}.zip") or os.path.isfile(f"{self.repository}.tar"):
                print("[red]The repository is already downloaded.[/]")
            else:
                if "message" in response:
                    raise RepositoryNotFound

                print(f'[green][+] Owner:[/] {self.username}')
                print(f'[green][+] Diretory:[/] /cligh/{self.repository}.{ext}')
                print(f'[green][+] Display:[/] {req.content[:10]}')
                print(f'[green][+] Size:[/] {len(req.content)}')
                with open(f"cligh/{self.repository}.{ext}", "wb") as f:
                    f.write(req.content)

                print("\n[green]Downloaded with success.[/]")
        
        except FileNotFoundError: 
            if os.path.isfile(f"{self.repository}.zip") or os.path.isfile(f"{self.repository}.tar"):
                print("[red]The repository is already downloaded.[/]")
            else:
                if "message" in response:
                    raise RepositoryNotFound

                print(f'[green][+] Owner:[/] {self.username}')
                print(f'[green][+] Diretory:[/] /cligh/{self.repository}.{ext}')
                print(f'[green][+] Display:[/] {req.content[:10]}')
                print(f'[green][+] Size:[/] {len(req.content)}')
                with open(f"{self.repository}.{ext}", "wb") as f:
                    f.write(req.content)

                print("\n[green]Downloaded with success.[/]")
