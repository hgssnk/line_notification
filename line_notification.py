#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

def main():
    PATH = "SEND_FILE_PATH"
    ACCESS_TOKEN = "YOUR_LINE_ACCESS_TOKEN"
    REQUEST_URL = "https://notify-api.line.me/api/notify"

    texts = file_reader(PATH)
    line_notification(REQUEST_URL, ACCESS_TOKEN, texts)
    return 0

def file_reader(PATH):
    f = open(PATH, 'r')
    texts = f.read()
    f.close()
    return texts

def line_notification(request, token, texts):
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "message": texts
    }
    requests.post(
        request,
        headers=headers,
        data=data,
    )


if __name__ == '__main__':
    sys.exit(main())