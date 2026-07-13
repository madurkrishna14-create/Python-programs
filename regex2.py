import re
matcher=re.finditer("[^a-zA-Z0-9]","a7b@k9z")
for match in matcher:
    print(match.start(),"..",match.end())