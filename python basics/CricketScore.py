from urllib import request
import requests

r = requests.get("http://tattvasdayspa.com/talha/cricket.txt")
s = r.text
print(type(s))

lines = s.split("|"and"\n")
print(lines)