# https://de.wikipedia.org/wiki/Liste_der_Pok%C3%A9mon
import re

import requests

mail = "Hallo, bitte senden Sie Ihre Bewerbung an bommelskirchen@digitialisierung.de. Wir freuen uns, von Ihnen zu hören."

matches = re.findall('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', mail)

for entry in matches:
    print(entry)

# r = requests.get(
#     'https://de.wikipedia.org/wiki/Liste_der_Pok%C3%A9mon')
#
# print(r.text)
#
# matches = re.findall(
#     '(?:<tr>\n)(?:<td>)(?:.+)(?:<\/td>\n)(?:<td>)(.+)(?:<\/td>\n)(?:<td>.*<\/td>\n)(?:<td>.*<\/td>\n)'
#     '(?:<td>.*<\/td>\n)(?:<td>.*<\/td>\n)(?:<td>.*<\/td>\n)(?:<td>.*<\/td>\n)(?:<td>)(.+)(?:<\/td>\n)',
#     r.text)
#
# for entry in matches:
#     print(f'{entry[0]}\t{entry[1]}')