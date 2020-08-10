"""
Utils functions.
"""
import re


def is_email(email: str):
    """ Test if str match RFC 5322 standard """
    return bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email))
