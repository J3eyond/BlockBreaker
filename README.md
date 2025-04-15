# BlockBreaker

**BlockBreaker** is a simple Python script that generates login attempts based on a specified list of passwords to bypass account lockouts during brute-force attacks. The script allows you to control the number of login attempts before a lockout occurs and adds valid credentials when the attempt limit is reached.

## Features

- Reads a list of passwords from a file
- Generates sequential login attempts with valid credentials after each attempt limit
- Configurable number of attempts before lockout
- Writes generated usernames and passwords to output files

## Installation

1. Ensure you have Python 3.6+ installed.
2. Clone the repository or download the script.


## Usage

```
python3 bb.py -h
usage: bb.py [-h] -f PASSWORD_FILE_INPUT -l VALID_LOGIN -p VALID_PASSWORD -u USERNAME_FOR_BRUTE -i INTERVAL [-ou USERNAME_FILE_OUTPUT] [-fp PASSWORD_FILE_OUTPUT]

BlockBreaker - A script for generating login attempts.

options:
  -h, --help            show this help message and exit
  -f PASSWORD_FILE_INPUT, --password_file_input PASSWORD_FILE_INPUT
                        Path to the input password file.
  -l VALID_LOGIN, --valid_login VALID_LOGIN
                        The valid username to be used.
  -p VALID_PASSWORD, --valid_password VALID_PASSWORD
                        The valid password for the valid username.
  -u USERNAME_FOR_BRUTE, --username_for_brute USERNAME_FOR_BRUTE
                        The username to brute force.
  -i INTERVAL, --interval INTERVAL
                        Number of unsuccessful login attempts allowed before blocking.
  -ou USERNAME_FILE_OUTPUT, --username_file_output USERNAME_FILE_OUTPUT
                        Output file for generated usernames.
  -fp PASSWORD_FILE_OUTPUT, --password_file_output PASSWORD_FILE_OUTPUT
                        Output file for generated passwords.

Example: python3 bb.py -f passwords.txt -l admin -p secret123 -u target_user -i 3
```

## Inspiration Lab

Broken brute-force protection, IP block - 
https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block
