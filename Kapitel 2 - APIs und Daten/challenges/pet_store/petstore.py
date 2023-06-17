# https://petstore.swagger.io/?_ga=2.24873914.142788932.1686959049-1439266029.1685790459&_gac=1.114894197.1686959049.CjwKCAjwkLCkBhA9EiwAka9QRguBWhlmi7FxPC6LZprucvPyPcKfypBPT7RMsGz3hzHa3LEkPXbAlRoCLu4QAvD_BwE#/
# Schreibe ein Programm, welches die API des Pet Stores nutzt, um die folgenden Aufgaben zu lösen:
# Lese alle verfügbaren Haustiere aus, lade Sie in eine zu erstellende Klasse 'Pet' und gebe sie auf der Konsole aus.
# Finde ein Haustier über dessen ID und gebe es auf der Konsole aus.
# Füge ein neues Haustier dem Pet Store hinzu.

import requests
import json

# Klasse Pet erstellen
class Pet:
    def __init__(self, category, name, photo_urls, tags, status, id=None):
        self.category = category
        self.name = name
        self.photo_urls = photo_urls
        self.tags = tags
        self.status = status
        self.id = id

    def __str__(self):
        return f"Pet(id={self.id}, category={self.category}, name={self.name}, photo_urls={self.photo_urls}, tags={self.tags}, status={self.status})"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_json(json: dict):
        pid = json.get('id', '')
        category = json.get('category', '')
        name = json.get('name', '')
        photo_urls = json.get('photoUrls', '')
        tags = json.get('tags', '')
        status = json.get('status', '')

        return Pet(category, name, photo_urls, tags, status, id=pid)

    def to_json(self):
        return {
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'photoUrls': self.photo_urls,
            'tags': self.tags,
            'status': self.status
        }

# Lese alle verfügbaren Haustiere aus und gebe sie auf der Konsole aus.
response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
print(response.json())
pets = [ Pet.from_json(pet) for pet in response.json()]
for pet in pets:
    print(pet.name)

# Finde ein Haustier über dessen ID und gebe es auf der Konsole aus.
response = requests.get("https://petstore.swagger.io/v2/pet/9223372036854653949")
pet = Pet.from_json(response.json())
print(pet.name, pet.id)

# Füge ein neues Haustier dem Pet Store hinzu.
pet = Pet(category={'name': 'Norwegian'},
          name='Harold', photo_urls=[], tags=[{'name': 'norsk'}], status='available')
response = requests.post("https://petstore.swagger.io/v2/pet", json=pet.to_json())
print(response.json())



