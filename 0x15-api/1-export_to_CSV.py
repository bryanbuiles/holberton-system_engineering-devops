#!/usr/bin/python3
""" Script using REST API """
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        dicti1 = {'id': sys.argv[1]}
        html1 = requests.get(
            "https://jsonplaceholder.typicode.com/users", params=dicti1)

        dicti2 = {'userId': sys.argv[1]}
        html2 = requests.get(
            "https://jsonplaceholder.typicode.com/todos", params=dicti2)

        username = html1.json()[0].get("username")
        with open(sys.argv[1] + ".csv", mode="w", newline="") as f:
            spamwriter = csv.writer(f, quoting=csv.QUOTE_ALL)
            for i in html2.json():
                spamwriter.writerow([str(sys.argv[1]), str(username),
                                     str(i.get("completed")),
                                     str(i.get("title"))])
