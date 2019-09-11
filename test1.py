import math
import os
import sys

import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
r = requests.get("http://microsoft.com")
print(r.status_code)
print(r.ok)

# name = input("your name? ")
# print("hello,", name)

