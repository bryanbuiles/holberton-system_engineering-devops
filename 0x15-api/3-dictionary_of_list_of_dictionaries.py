#!/usr/bin/python3
""" Script using REST API """
import json
import requests
import sys

if __name__ == "__main__":

    html1 = requests.get(
        "https://jsonplaceholder.typicode.com/users")

    html2 = requests.get(
        "https://jsonplaceholder.typicode.com/todos")

    with open("todo_all_employees.json", mode="w", newline="") as f:
        dictionary = {}

        for j in html1.json():
            lista = []
            for i in html2.json():
                if j.get("id") == i.get("userId"):
                    dictionaryin = {"username": j.get("username"), "task": i.get("title"), "completed": i.get(
                        "completed")}
                    lista.append(dictionaryin)
            dictionary[j.get("id")] = lista
        json.dump(dictionary, f)
