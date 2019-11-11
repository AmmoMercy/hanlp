import re

text = "牢/a"

print(re.sub(r'/.+', '', text))
