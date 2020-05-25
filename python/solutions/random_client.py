"""
    Simple web client which posts a password to a web server.
"""

import requests
import argparse

def random(url, password):
    response = requests.post(url, data={'password': password})
    print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('url')
    parser.add_argument('--password', default='2B|!2B')
    args = parser.parse_args()

    random(args.url, args.password)
