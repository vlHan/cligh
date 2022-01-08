# -*- coding: utf-8 -*-
import sys
import argparse
import requests

from modules import *

__author__ = "vlHan"
__version__ = "1.0"
__license__ = "MIT"


class App:
    @staticmethod
    def _arguments() -> str:
        """Parse arguments to use in the cli function."""
        clear()
        banner()
        parser = argparse.ArgumentParser(
            description=f"CLIGH - Command-line Search tool for GitHub.",
            usage="python3 \tcligh.py -u 'GithubUsername'\n\t\tcligh.py -u 'GithubUsername' -r 'RepositoryName'",
        )
        parser.add_argument(
            "--version", "-v", action="version", version=f"V{__version__}"
        )
        parser.add_argument(
            "-u", "--username", type=str, help="[+] The username GitHub account."
        )
        parser.add_argument(
            "-r",
            "--repository",
            type=str,
            help="[+] The repository from the GitHub user account.",
        )

        args = parser.parse_args()

        if not args.username or not args.username:
            parser.print_help()
            sys.exit(1)

        return args

    @staticmethod
    def main():
        args = App._arguments()

        try:
            if args.username and not args.repository:
                endpoint = f"users/{args.username}"
                return cligh(args.username, args.repository, endpoint).display_user()

            if args.username and args.repository:
                endpoint = f"repos/{args.username}/{args.repository}"
                return cligh(
                    args.username, args.repository, endpoint
                ).display_repository()
            
        except requests.ConnectionError:
            print(
                "Connection Error:",
                end=" " f"{Fore.RED}Could not connect with the GitHub API.{RA}",
            )
        except UserNameNotCorrect:
            print(f"{Fore.RED}The username is not correct.{RA}")


if __name__ == "__main__":
    App.main()
