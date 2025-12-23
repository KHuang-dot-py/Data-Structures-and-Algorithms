import re

txt = "randomstuff_more_"

x = re.search("^[^_]+", txt)

print(x.group(0))
