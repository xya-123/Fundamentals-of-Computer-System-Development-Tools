import re

text = r'{"name": "Alyssa \"P.\" Hacker", "college": "MIT"}'

bad = re.search(r'"name"\s*:\s*"(.*)"', text).group(1)
good = re.search(r'"name"\s*:\s*"((?:\\.|[^"\\])*)"', text).group(1)

print("greedy:", bad)
print("fixed: ", good)