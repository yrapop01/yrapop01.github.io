from multiprocessing import Process, Pipe
import requests
import time
import sys

def url_printer(conn):
    url = conn.recv().strip()
    while url:
        print(requests.get(url).text)
        url = conn.recv().strip()
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=url_printer, args=(child_conn,))
    p.start()
    for line in sys.stdin:
        parent_conn.send(line)
        if not line.strip():
            break
    p.join()
