import re
import requests

mail = "Hallo, bitte senden Sie Ihre Bewerbung an bommelskirchen@digitialisierung.de. Wir freuen uns, von Ihnen zu hören."

matches = re.findall(r'\b[\w.-]+?@\w+?\.\w{2,4}\b', mail)

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