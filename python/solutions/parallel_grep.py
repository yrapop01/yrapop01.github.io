"""
    Find all lines in all files in a directory tree which contain a pattern.
    Run the search in parallel.
"""

from multiprocessing import Pool
import argparse
import sys
import os
import re

def ls(path):
    for root, _, files in os.walk(path):
        yield from (root + '/' + fl for fl in files)
       
class Grep:
    def __init__(self, rgx, max_string=255):
        self.rgx = rgx
        self.max_string = max_string

    def grep(self, fullname):
        try:
            with open(fullname) as text:
                lines = text.readlines()
            lst = []
            for i, line in enumerate(lines):
                if self.rgx.search(line):
                    lst += [(fullname, i, line[:self.max_string].strip())]
            return lst
        except (UnicodeDecodeError, FileNotFoundError):
            print(fullname, 'is not a text file or does not exist')
            return []

def run_grep(regex_and_file):
    return list(grep(*regex_and_file))

def run_grep_parallel(regex, path):
    pool = Pool()
    files = ls(path)
    rgx = re.compile(regex)
    args = ((rgx, f) for f in files)
    g = Grep(rgx)

    matches = pool.map(g.grep, files)

    # The next statement could be replaced by:
    # matches = sum(matches, [])
    matches = [match for sublist in matches for match in sublist]

    for filename, i, line in matches:
        print('{}:{}\t{}...'.format(filename, i, line))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help='search root path')
    parser.add_argument('regex', help='regex to look up')

    args = parser.parse_args()
    run_grep_parallel(args.regex, args.path)
