"""
@author: jay.shah
date: 3/13/25
"""
import re

class Scanner():
    """Scanner class for tokenizing input on the command line"""
    def __init__(self, source):
        self.source = source
        self.token_specification = [ #different token types
            ('NUMBER', r'\d+'),
            ('ASSIGN', r'='),
            ('PLUS', r'\+'),
            ('ID', r'[A-Za-z]+'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.')
        ]
