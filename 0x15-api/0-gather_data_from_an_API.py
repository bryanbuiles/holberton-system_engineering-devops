#!/usr/bin/python3
""" Script using REST API """
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
        lista = []
        count1 = 0
        count2 = 0
        for i in html2.json():
            count1 += 1
            for k, v in i.items():
                if k == "completed" and v is True:
                    count2 += 1
                    lista.append(i.get("title"))
        name = html1.json()[0].get("name")
        print("Employee {} is done with tasks({}/{}):"
              .format(name, count2, count1))
        for j in lista:
            print("\t ", j)
