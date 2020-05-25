"""
    Run divisors.py from another process.
"""

import subprocess
import sys

def main():
    for line in sys.stdin:
        output = subprocess.check_output(['python3', 'divisors.py', line.strip()])
        print(str(output, 'ascii'))

if __name__ == "__main__":
    main()
