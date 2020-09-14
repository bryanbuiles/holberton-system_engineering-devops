#!/usr/bin/python3
""" Script using REST API """
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        id = sys.argv[1]
        dicti1 = {'id': sys.argv[1]}
        html1 = requests.get(
            "https://jsonplaceholder.typicode.com/users", params=dicti1)

        dicti2 = {'userId': sys.argv[1]}
        html2 = requests.get(
            "https://jsonplaceholder.typicode.com/todos", params=dicti2)

        username = html1.json()[0].get("username")
        with open(sys.argv[1] + ".json", mode="w", newline="") as f:
            dictionary = {}
            lista = []
            for i in html2.json():
                dictionaryin = {"task": i.get("title"), "completed": i.get(
                    "completed"), "username": username}
                lista.append(dictionaryin)
            dictionary[id] = lista
            json.dump(dictionary, f)
