import os
import pandas as pd

# Definisci il percorso della cartella contenente i file Excel
cartella = r'C:\Users\User\Desktop\excel'

# Crea una lista vuota per memorizzare i DataFrame da ciascun file Excel
elenco_df = []

# Scansiona tutti i file nella cartella
for filename in os.listdir(cartella):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):  # Assicurati che siano file Excel
        percorso_file = os.path.join(cartella, filename)
        df = pd.read_excel(percorso_file)
        elenco_df.append(df)

# Unisci i DataFrame in uno unico
df_completo = pd.concat(elenco_df, ignore_index=True)

# Specifica il percorso e il nome del file Excel in cui desideri salvare il DataFrame combinato
percorso_file_output = r'C:\Users\User\Desktop\excel\output.xlsx'

# Salva il DataFrame in un file Excel
df_completo.to_excel(percorso_file_output, index=False, engine='openpyxl')

print(f"I dati sono stati salvati in {percorso_file_output}")
