from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ein einfacher Datensatz mit Beispiele für Spam und 'Ham' (nicht-Spam)
data = {
    'mail': [
        'Sie haben eine Million Euro gewonnen',
        'Bitte bestätigen Sie Ihre Kreditkarteninformationen',
        'Haben Sie Zeit für ein Meeting morgen?',
        'Die Projektdokumente sind fertig',
        'Die neuen Produkte sind auf dem Weg',
        'Ein gesperrtes Konto wurde wiederhergestellt',
        'Zur Mittagspause geht es in die Kantine',
    ],
    'spam': [1, 1, 0, 0, 0, 1, 0]
}

# Erstellen Sie ein Bag-of-Words-Modell
# https://en.wikipedia.org/wiki/Bag-of-words_model
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(data['mail'])

# Teilen Sie die Daten in Trainings- und Testsets auf
X_train, X_test, y_train, y_test = train_test_split(features, data['spam'], test_size=0.2)

# Erstellen und trainieren Sie das Modell
model = MultinomialNB()
model.fit(X_train, y_train)

# Machen Sie Vorhersagen auf dem Testset und berechnen Sie die Genauigkeit
predictions = model.predict(X_test)
print('Genauigkeit: ', accuracy_score(y_test, predictions))
# Ausgabe des Klassifikationsberichts
print(classification_report(y_test, predictions))









# Laden Sie die Stoppwörter und den Lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(texts):
    preprocessed_texts = []
    for text in texts:
        # Konvertieren Sie den Text in Kleinbuchstaben
        text = text.lower()

        # Entfernen Sie alle Nicht-Wörter (z.B. Zahlen, Satzzeichen)
        text = re.sub(r'\W', ' ', text)

        # Entfernen Sie alle Einzelzeichen
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)

        # Entfernen Sie einzelne Zeichen vom Anfang
        text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)

        # Ersetzen Sie mehrfache Leerzeichen durch ein einzelnes Leerzeichen
        text = re.sub(r'\s+', ' ', text, flags=re.I)

        # Entfernen Sie Präfix 'b'
        text = re.sub(r'^b\s+', '', text)

        # Lemmatisierung (z.B. "läuft" wird zu "laufen")
        text = text.split()
        text = [lemmatizer.lemmatize(word) for word in text if not word in stop_words]
        text = ' '.join(text)

        # Fügen Sie den vorverarbeiteten Text zur Liste hinzu
        preprocessed_texts.append(text)

    return preprocessed_texts


# Angenommen, Sie haben einen neuen Text, den Sie überprüfen möchten
mails = [
    ["Ihre E-Mail hat eine Million Euro gewonnen! Bitte senden Sie uns Ihre Bankdaten."],
    ["Morgen Meeting um 12! Bitte bestätigen Sie Ihre Teilnahme."],
    ["Hey Peter, die Projektdokumente sind fertig."],
    ["Hi Hans, ich habe neuen Kaffee geholt, komm vorbei!"],
    ["Hallo, ich habe eine Frage zu Ihrem Produkt."],
    ["Bestätigen Sie Ihre Kreditkarteninformationen."],
    ["Ihr Konto wurde gesperrt."],
]

for mail in mails:
    # Text-Vorverarbeitung durchführen
    preprocessed_text = preprocess_text(mail)
    print(preprocessed_text)

    # Vektorisierung
    vectorized_text = vectorizer.transform(preprocessed_text)
    print(vectorized_text)

    # Vorhersage machen
    prediction = model.predict(vectorized_text)

    # Ausgabe der Vorhersage
    if prediction == 1:
        print(f"{mail}: Spam.")
    else:
        print(f"{mail}: Kein Spam.")