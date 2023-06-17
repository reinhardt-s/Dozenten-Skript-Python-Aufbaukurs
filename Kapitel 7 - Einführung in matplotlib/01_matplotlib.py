import matplotlib.pyplot as plt

# Daten
labels = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 10, 5]

# Erstellen des Balkendiagramms
plt.bar(labels, values)
# plt.plot(labels, values)

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Beispiel für ein Balkendiagramm')
plt.xlabel('Kategorien')
plt.ylabel('Werte')

# Diagramm anzeigen
plt.savefig('bar.png')
plt.savefig('bar.svg')
plt.show()

