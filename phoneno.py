import re
import urllib.request

url = "https://www.amazon.co.in"

with urllib.request.urlopen(url) as response:
    html = response.read().decode("utf-8", errors="ignore")

# Find phone numbers (example pattern)
numbers = re.findall(r"\+?\d[\d\s-]{7,}\d", html)

for number in numbers:
    print(number)