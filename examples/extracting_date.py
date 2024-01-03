import re

text = "Date: 2023-06-08  08-09-2023"
pattern  = r"\d{4}-\d{2}-\d{2}"

dates = re.findall(pattern,text)

print(dates)