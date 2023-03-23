#!/usr/bin/env python3
'''Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is
separating all fields in the log line (message)
'''


from typing import List
import re
# import logging
# import mysql.connector
# from os import environ


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns a log message obfuscated """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message

# def filter_datum(fields: List[str], redaction: str,
#                  message: str, separator: str) -> str:
#     '''returns obfuscated message'''
#     for x in fields:
#         message = re.sub(f'{x}= .*?{separator}',
#                          f'{x}={redaction}{separator}', message)
#     return message
