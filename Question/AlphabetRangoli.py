# Alphabet Rangoli Hackerrank

import string
alpha = string.ascii_lowercase
# a b c d e
# ['e-d-c-b-a-b-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-d-e', 'e-d-e', 'e']
n = 5       # int(input('enter size: '))
L = []
# a b c.... nth
for i in range(n):
    s = "-".join(alpha[i:n])
    # a b c b a
    L.append(s[::-1]+s[1:])

for i in range(n-1,0,-1):
    print(L[i].center(len(L[0]),'-'))

for i in range(n):
    print(L[i].center(len(L[0]),'-'))