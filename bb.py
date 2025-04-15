#!/usr/bin/python3


import argparse
import logging
from os import path


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class BlockBreaker:
    def __init__(
        self,
        password_file_input,
        username_file_output="generated_username.txt",
        password_file_output="generated_password.txt",
        valid_login=None,
        valid_password=None,
        username_for_brute=None,
        interval=None,
    ):
        self.password_file_input = password_file_input
        self.username_file_output = username_file_output
        self.password_file_output = password_file_output
        self.valid_login = valid_login
        self.valid_password = valid_password
        self.username_for_brute = username_for_brute
        if interval is None or interval <= 0:
            raise ValueError("The interval must be a positive number.")
        self.interval = interval - 1
        self.passwords = []
        self.usernames = []
        self.passwords_output = []
        self.validate_file_path(self.password_file_input)

    def validate_file_path(self, file_path):
        logging.info(f"Checking if file exists at: {path.abspath(file_path)}")
        if not path.exists(file_path):
            logging.error(f"File '{file_path}' not found.")
            raise FileNotFoundError(f"[-] File '{file_path}' not found.")

    def read_passwords_file(self):
        if path.getsize(self.password_file_input) == 0:
            raise ValueError(f"[ERROR] The file {self.password_file_input} is empty.")
        try:
            with open(self.password_file_input, "r") as f:
                for line in f:
                    password = line.strip()
                    if password:
                        self.passwords.append(password)
        except Exception as e:
            logging.error(
                f"Failed to read file: {self.password_file_input}. Error: {e}"
            )
            raise

    def generate_login_attempts(self):
        for i, password in enumerate(self.passwords):
            if i > 0 and i % self.interval == 0:
                self._append_credentials(self.valid_login, self.valid_password)
            self._append_credentials(self.username_for_brute, password)
        self._append_credentials(self.valid_login, self.valid_password)

    def _append_credentials(self, username, password):
        self.usernames.append(username)
        self.passwords_output.append(password)

    def write_to_file(self, file_name, data):
        try:
            with open(file_name, "w") as f:
                f.write("\n".join(data) + "\n")
        except Exception as e:
            logging.error(f"Failed to write to file: {file_name}. Error: {e}")
            raise

    def generate_files(self):
        self.write_to_file(self.username_file_output, self.usernames)
        self.write_to_file(self.password_file_output, self.passwords_output)
        logging.info(
            f"[+] Files {self.username_file_output} and {self.password_file_output} generated successfully."
        )

    def run(self):
        self.read_passwords_file()
        self.generate_login_attempts()
        self.generate_files()


def main():
    parser = argparse.ArgumentParser(
        description="BlockBreaker - A script for generating login attempts.",
        epilog="Example: python3 bb.py -f passwords.txt -l admin -p secret123 -u target_user -i 3",
    )
    parser.add_argument(
        "-f",
        "--password_file_input",
        help="Path to the input password file.",
        required=True,
    )
    parser.add_argument(
        "-l", "--valid_login", help="The valid username to be used.", required=True
    )
    parser.add_argument(
        "-p",
        "--valid_password",
        help="The valid password for the valid username.",
        required=True,
    )
    parser.add_argument(
        "-u", "--username_for_brute", help="The username to brute force.", required=True
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        help="Number of unsuccessful login attempts allowed before blocking.",
        required=True,
    )
    parser.add_argument(
        "-ou",
        "--username_file_output",
        help="Output file for generated usernames.",
        default="generated_username.txt",
    )
    parser.add_argument(
        "-fp",
        "--password_file_output",
        help="Output file for generated passwords.",
        default="generated_password.txt",
    )

    args = parser.parse_args()

    logging.debug(f"Parsed arguments: {args}")

    try:
        dictionaries_generator = BlockBreaker(
            password_file_input=args.password_file_input,
            username_file_output=args.username_file_output,
            password_file_output=args.password_file_output,
            valid_login=args.valid_login,
            valid_password=args.valid_password,
            username_for_brute=args.username_for_brute,
            interval=args.interval,
        )
        dictionaries_generator.run()
    except (FileNotFoundError, ValueError) as e:
        logging.error(e)


if __name__ == "__main__":
    main()
