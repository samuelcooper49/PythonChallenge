#!/usr/bin/env python3

# Solution to challenge 4:

import urllib.request
response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s")
html = response.read()

if __name__ == '__main__':
    import urllib.request
    req = urllib.request.Request("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s")
    response = urllib.request.urlopen(req)
import urllib
import re
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing_rep = "and the next nothing is (\d+)"
nothing = "46059"

while True:
    try:
        source = urllib.urlopen(uri % nothing).read()
        nothing = re.search(nothing_rep, source).group(1)
    except:
        Exception("Something went wrong")

    print(nothing)
    urllib.request(uri)
