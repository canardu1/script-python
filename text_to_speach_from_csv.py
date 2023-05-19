import csv
import os
import pyttsx3
from tqdm import tqdm
import time

input_csv_file = 'D:/PYTHON/battute.csv'  # Specifica il percorso del tuo file CSV
output_directory = 'D:/PYTHON/'  # Specifica la directory di output per i file MP3

# Crea la directory di output se non esiste già
os.makedirs(output_directory, exist_ok=True)

# Inizializza il motore text-to-speech di pyttsx3
engine = pyttsx3.init()

# Imposta la velocità desiderata (0.5 = metà della velocità normale)
speed = 160
engine.setProperty('rate', speed)

# Imposta la voce desiderata (utilizza la tua voce preferita)
voices = engine.getProperty('voices')
# Esempio di selezione di una voce femminile in italiano
voice_id = 'italian+f3'
engine.setProperty('voice', voice_id)

# Imposta l'intonazione desiderata (0.5 = metà dell'intonazione normale)
pitch = 0.5
engine.setProperty('pitch', pitch)

# Funzione per inserire pause
def insert_pause(duration):
    time.sleep(duration / 1000)

# Apri il file CSV in modalità di lettura
with open(input_csv_file, 'r') as file:
    reader = csv.reader(file)
    row_count = sum(1 for _ in reader)  # Conta il numero totale di righe nel file CSV
    file.seek(0)  # Torna all'inizio del file per iniziare la lettura

    # Itera sulle righe del file CSV con una barra di avanzamento percentuale celeste
    for index, row in enumerate(tqdm(reader, total=row_count, desc="Conversione in corso", bar_format="{desc}: {percentage:.0f}%|{bar}|")):
        # La battuta si trova nella prima colonna (indice 0)
        battuta = row[0]

        # Crea il nome del file MP3 utilizzando l'indice + 1 (per evitare file 0.mp3)
        file_name = f"{index + 1}.mp3"

        # Crea il percorso completo per il file MP3
        file_path = os.path.join(output_directory, file_name)

        # Utilizza pyttsx3 per generare l'audio della battuta e salvarlo come file MP3
        engine.save_to_file(battuta, file_path)
        engine.runAndWait()

        # Inserisci una pausa di 300 millisecondi tra una battuta e l'altra
        insert_pause(300)

        # Stampa un messaggio per confermare il salvataggio del file MP3
        tqdm.write(f"File MP3 '{file_name}' salvato.")

# Stampa un messaggio al termine dell'elaborazione
print("Conversione delle battute completata.")
