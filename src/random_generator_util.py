import os
import sys
import datetime
import json
import random
import argparse

class random_generator_util:

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = """()[]{},;:.-_//?+*#$@%?><"""
    enable_upper, enable_lower, enable_digits, enable_symbols, enable_seed = (
        True,
        True,
        True,
        True,
        True,
    )
    seed = ""

    def generate_random_string(
        self, length: int = 20, amount: int = 10, enable_seed: bool = False
    ):

        generated_pass: str = ""
        generated_password_set = set()
        if len(self.input_string):
            if length >= self.max_length and amount <= self.total_amount:
                generated_pass = self.input_string
            else:
                if length < 10 and length > self.max_length:
                    raise RuntimeError(
                        f"Password length should be equal or less than {self.max_length}, characters."
                    )
                if amount < 2 and amount < self.total_amount:
                    raise RuntimeError(
                        f"Minimum total passwords to be generated is: {self.total_amount}."
                    )
            if self.enable_upper:
                generated_pass += self.uppercase_letters
            if self.enable_lower:
                generated_pass += self.lowercase_letters
            if self.enable_digits:
                generated_pass += self.digits
            if self.enable_symbols:
                generated_pass += self.symbols
            temp_generated_pass = ""
            if self.enable_seed:
                random.seed(self.seed)
            for each in range(self.total_amount):
                temp_generated_pass = "".join(
                    random.sample(generated_pass, self.max_length)
                )
                generated_password_set.add(temp_generated_pass)
            return generated_password_set
        else:
            raise RuntimeError(
                "Input string is still not set. Please check again while creating object of: ",
                __class__.__name__,
            )

    def __init__(
        self,
        input_string="",
        max_length: int = 20,
        total_amount: int = 10,
        sample_seed: str = "",
    ) -> None:
        """Random Generator Utility

        Args:
            input_string (str): Random string to pad new password
            max_length (int, optional): Maximum length of the password. Defaults to 20.
            total_amount (int, optional): Total number of passwords will be generated. Defaults to 10.

        Raises:
            RuntimeError: Incase of exceeding total_amount or max_length to be out of bound.
                        Or incase input_string is blank.
        """
        if len(input_string):
            if self.enable_seed and len(self.seed) == 0 and len(sample_seed):
                self.seed = sample_seed
            else:
                raise RuntimeError("Unable to setup random object with seed enabled.")
            self.input_string = input_string
            self.max_length = max_length
            self.total_amount = total_amount
        else:
            raise RuntimeError(
                "Input string for generating random password can't be blank.\nPlease provide input string, failed to create object of: ",
                __class__.__name__,
            )


def main():
    random_user_input, passwords, random_gen_handle = (
        str(input("Enter your string: ")),
        None,
        None,
    )
    try:
        random_gen_handle = random_generator_util(
            input_string=random_user_input, max_length=30, total_amount=10, sample_seed=str(input("Enter your seed string: "))
        )
        passwords = random_gen_handle.generate_random_string(length=25, amount=3)
    except:
        raise RuntimeError(
            "Unable to generate random passwords. Failed to create random_generator_util object.",
        )
    finally:
        print(passwords)


if __name__ == "__main__":
    main()
