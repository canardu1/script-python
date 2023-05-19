import csv
import codecs
from nltk.sentiment import SentimentIntensityAnalyzer

# Inizializza l'analizzatore di sentiment di VADER
sid = SentimentIntensityAnalyzer()

# Funzione per calcolare il punteggio di sentiment percentuale
def calculate_sentiment_score(text):
    sentiment_scores = sid.polarity_scores(text)
    sentiment_score = sentiment_scores["compound"]
    sentiment_score = (sentiment_score + 1) / 2  # Converti il range da [-1, 1] a [0, 1]
    sentiment_score = round(sentiment_score * 100)
    sentiment_score = max(1, min(sentiment_score, 100))
    return sentiment_score

# Inizializza una lista per memorizzare i punteggi di sentiment
sentiment_scores = []

# Leggi il file CSV contenente le recensioni
file_path = input("Inserisci il percorso del file CSV: ")
try:
    with codecs.open(file_path, "r", encoding="utf-8", errors="replace") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Salta l'intestazione
        
        # Leggi le recensioni riga per riga
        for row in csv_reader:
            review = row[0].strip()  # Assume che la recensione si trovi nella prima colonna
            
            # Calcola il punteggio di sentiment per la recensione
            sentiment_score = calculate_sentiment_score(review)
            
            # Aggiungi il punteggio di sentiment alla lista
            sentiment_scores.append(sentiment_score)
            
            # Stampa il testo della recensione e il punteggio di sentiment
            print(f"\033[96mRecensione: {review}")
            print(f"Punteggio di sentiment per la recensione: {sentiment_score}%\033[0m")
        
        # Calcola la media dei punteggi di sentiment
        if sentiment_scores:
            average_score = sum(sentiment_scores) / len(sentiment_scores)
            
            # Determina il colore del punteggio di sentiment medio
            if average_score <= 25:
                color = "\033[91m"  # Rosso
            elif average_score <= 50:
                color = "\033[93m"  # Arancione
            else:
                color = "\033[92m"  # Verde
            
            # Stampa la barra di percentuale colorata
            bar_length = 20
            filled_length = int(average_score / 5 * bar_length)
            bar = "=" * filled_length + "-" * (bar_length - filled_length)
            print(f"{color}{bar}\033[0m")
            
            # Stampa il punteggio di sentiment medio totale con lo stesso colore della barra
            print(f"{color}Punteggio di sentiment medio totale: {average_score:.2f}%\033[0m")
        else:
            print("Nessuna recensione trovata nel file CSV.")

except FileNotFoundError:
    print(f"Il file {file_path} non esiste.")
except UnicodeDecodeError:
    print(f"Errore di decodifica del file {file_path}.")
