"""
    A sniffer which listens to localhost tcp connections in hope
    to find posted html form with username and password fields.
"""

import ctypes, os
import urllib.parse

import logging
# Don't print scapy warnings, they are not interesting
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import scapy.all

def unquote_url_data(data):
    """URL data is encoded by default by the browser with a very
       simple substitution encoding called url-encoding. English
       letters are not substituted by characters such as spaces
       are changed. Use this function to decode url-encoded text"""

    return urllib.parse.unquote_plus(data)

def find_and_print(data, pattern, sep='&'):
    if pattern not in data:
        return

    i = data.find(pattern)
    data = data[i:]

    j = data.find(sep)
    if j > 0:
        data = data[:j]

    print(unquote_url_data(data))

def sniff(packet):
    data = packet.original.decode('ascii', 'ignore')
    if 'POST / HTTP/1.1' not in data:
        return

    find_and_print(data, 'username=')
    find_and_print(data, 'password=')

def main():
    scapy.all.sniff(iface='lo0', filter='tcp', prn=sniff)

if __name__ == "__main__":
    try:
        is_root = (os.getuid() == 0)
    except AttributeError:
        # Special treatement for windows
        is_root = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_root:
        print('This program should be run by root')
    else:
        main()
