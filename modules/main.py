# -*- coding: utf-8 -*-
import sys
import argparse
import requests
import timeit

from modules import *

__author__ = "vlHan"
__version__ = "1.1"
__license__ = "MIT"


class App:
    def __init__(self) -> None:
        self.init = timeit.default_timer()

    @staticmethod
    def _arguments() -> str:
        """Parse arguments to use in the cli function.
        """
        banner()
        parser = argparse.ArgumentParser(
            description='CLIGH - Command-line Search tool for GitHub.',
            usage="python3 cligh [option] [argument]",
        )
        parser.add_argument(
            "--version", "-v", action="version", version=f"v{__version__}"
        )
        parser.add_argument(
            "-u", "--username", type=str, help="The username GitHub account."
        )
        parser.add_argument(
            "-r",
            "--repository",
            type=str,
            help="The repository from the GitHub user account.",
        )
        parser.add_argument('-d', '--download', type=str, help="Download the user repository.")
        parser.add_argument(
            "-e", "--ext", default='zip', type=str, help="Repository extension. (zip or tar)"
        )
        parser.add_argument(
            "-rf", "--ref", default='main', type=str, help="The repository branch."
        )
        args = parser.parse_args()

        if not args.username:
            parser.print_help()
            sys.exit(1)

        return args

    @staticmethod
    def main() -> None:
        """Main function to run the program
        """
        args = App._arguments()

        try:
            if args.username and not args.repository and not args.download:
                endpoint = f"users/{args.username}"
                return cligh(args.username, args.repository, endpoint).display_user()

            if args.username and args.repository and not args.download:
                endpoint = f"repos/{args.username}/{args.repository}"
                return cligh(args.username, args.repository, endpoint).display_repository()

            if args.username and args.download:
                endpoint = f'repos/{args.username}/{args.download}/{args.ext}ball/{args.ref}'
                return cligh(args.username, args.download, endpoint).download_repository(args.ext)
            
        except requests.ConnectionError:
            print(
                "Connection Error:",
                end=" " f"{Fore.RED}Could not connect with the GitHub API.{RA}",
            )
        except UserNameNotCorrect:
            print(f"{Fore.RED}The username is not correct.{RA}")
        except RepositoryNotFound: 
            print(f"{Fore.RED}Could not found the requested repository.{RA}")

    def run(self):
        """This function use main() and count the time
        """
        banner()
        App.main()
        print(" ")
        print("*"*30)
        print("[+] Thanks for using!")
        end = timeit.default_timer()
        
        print("[+] RUNTIME: %f seconds" % (end - self.init))
        print("*"*30)
