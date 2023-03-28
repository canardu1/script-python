import os
from moviepy.editor import VideoFileClip
from datetime import datetime, timedelta
import pandas as pd

folder_path = "/path/to/folder"  # Inserisci il percorso della cartella qui

total_duration = 0
duration_list = []

def calculate_duration(folder_path):
    global total_duration, duration_list
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            calculate_duration(file_path)
        elif filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov"):
            clip = VideoFileClip(file_path)
            duration = clip.duration
            total_duration += duration
            clip.close()
            duration_str = str(timedelta(seconds=int(duration)))
            duration_list.append([filename, duration_str])
            print(f"Titolo: {filename}, Durata: {duration_str}")

start_time = datetime.now()

calculate_duration(folder_path)

end_time = datetime.now()
elapsed_time = end_time - start_time
elapsed_time_seconds = elapsed_time.total_seconds()
total_duration_no_correction = total_duration
total_duration -= elapsed_time_seconds

total_duration_str = str(timedelta(seconds=int(total_duration)))
print(f"\nLa durata totale corretta dei file video nella cartella è di: {total_duration_str}")

total_duration_no_correction_str = str(timedelta(seconds=int(total_duration_no_correction)))
print(f"\nLa durata totale senza correzione dei file video nella cartella è di: {total_duration_no_correction_str}")

df_duration = pd.DataFrame(duration_list, columns=['Titolo', 'Durata'])
df_duration.to_excel("duration.xlsx", index=False)

df_total_duration = pd.DataFrame({'Durata Totale Corretta': [total_duration_str], 'Durata Totale': [total_duration_no_correction_str]})
df_total_duration.to_excel("total_duration.xlsx", index=False)

