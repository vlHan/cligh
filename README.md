# cligh

<p>
   <img alt="Languages" src="https://img.shields.io/badge/Python->=3.0-blue.svg"> 
   <img alt="Repository size" src="https://img.shields.io/github/repo-size/vlHan/cligh">
   <img alt="License" src="https://img.shields.io/github/license/vlHan/cligh.svg">
</p>


cligh is a command-line search tool for GitHub.

This is a project that I developed to learn more about HTTP requests, using the GitHub API :octocat:

## Installation

Clone this repository: `git clone https://github.com/vlHan/cligh` or <a href="https://github.com/vlHan/cligh/archive/refs/heads/main.zip">download zip</a>
- Enter the folder: `cd cligh/` or run out of the diretory.
- Install python3 
  - Linux
    - `sudo apt-get install python3`
    - `chmod +x *`
    - `python3 -m pip install -r requirements.txt`
    - Finished!

  - Windows and Mac
    - [Python 3, download and install](https://www.python.org/downloads/)
    - `python -m pip install -r requirements.txt`
    - Finished!

## Usage
```py
python3 cligh [OPTION]

# usage (out of the diretory): 
python3 cligh -u 'GITHUBUSERNAME'
        cligh -u 'GITHUBUSERNAME' -r 'REPOSITORYNAME'
        cligh -u 'GITHUBUSERNAME' -d 'REPOSITORYNAME' -e 'EXTENSION' -rf 'BRANCH'  

examples: 

# see informations about a profile 
python3 cligh -u 'github'

# see informations about a repository
python3 cligh -u 'github' -r 'github'

# download a .zip repository 
python3 cligh -u 'github' -d 'docs' -e 'zip' -rf 'master'  
```

## Options
```
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit
  -u, --username        The username GitHub account.
  -r, --repository      The repository from the GitHub user account.
  -d, --download        Download the user repository.
  -e, --ext             Repository extension. (zip or tar)
  -rf, --ref            The repository branch.
```


### Example

<img src="./demo/demo.gif">

## License
This project is under [MIT License](LICENSE)

