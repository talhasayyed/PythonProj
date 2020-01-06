# find the max score of out(*)players and not out players show there score with name

# library for url
import requests

r = requests.get("http://tattvasdayspa.com/talha/cricket.txt")
s = r.text
# print("actual string is",s)

# crating empty dictionay
d = {}
lines = s.split("\n")
# list of sting splitted by new line
# print(lines)

for line in lines:
    (key,val) = line.split(" |")
    d[(key)] = val
# print(d)
# print(d.keys())
# print(d.values())

# empty dictionary for Out and Not Out players
out = {}
NotOut = {}

for (key,values) in d.items():
    if values[-1]=="*":
        key_value = (key,values)
        out.update({key:values})
    else:
        NotOut.update({key:values})

print("out dictionary")
print(out)
print("------> max of out is ",key,max(out.values()))

print("====================================================")

print("NotOut dictionary")
print(NotOut)
print("------> max of not out is",key,max(NotOut.values()))