# find the max score of out(*)players and not out players show there score with name
import requests

r = requests.get("http://tattvasdayspa.com/talha/cricket.txt")
s = r.text
print(type(s))

lines = s.split("|"and"\n")
print(lines)