import re
import urllib.request

sites = "google rediff".split()

print(sites)

for s in sites:
    print("Searching...", s)

    u = urllib.request.urlopen("http://" + s + ".com")
    text = u.read().decode()

    title = re.findall(r"<title>(.*?)</title>", text, re.I)

    if title:
        print(title[0])
    else:
        print("Title not found")