import tkinter as tk
from tkinter import filedialog, ttk
from ttkthemes import ThemedTk
from bs4 import BeautifulSoup
import os
import pandas as pd

def read_and_parse_html(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return BeautifulSoup(content, 'html.parser')

def extract_lists(soup, class_name):
    elements = []
    for div in soup.find_all(class_=class_name):
        for a in div.find_all('a', href=True):
            elements.append(a.get_text())
    return elements

def compare_lists_and_save_to_excel(file_path):
    base_path = os.path.dirname(file_path)
    followers_1_path = os.path.join(base_path, 'connections/followers_and_following/followers_1.html')
    following_path = os.path.join(base_path, 'connections/followers_and_following/following.html')

    soup_followers_1 = read_and_parse_html(followers_1_path)
    soup_following = read_and_parse_html(following_path)

    list_followers_1 = extract_lists(soup_followers_1, '_a6-p')
    list_following = extract_lists(soup_following, '_a6-p')

    following_not_followers = set(list_following) - set(list_followers_1)

    # Creazione di un DataFrame e salvataggio in un file Excel
    df = pd.DataFrame(following_not_followers, columns=['Following Not Followers'])
    excel_path = os.path.join(base_path, 'following_not_followers.xlsx')
    df.to_excel(excel_path, index=False)

    result.set(f"File Excel generato: {excel_path}")

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Seleziona il file start_here.html", filetypes=[("HTML files", "*.html")])
    if file_path:
        compare_lists_and_save_to_excel(file_path)

# Creazione dell'interfaccia grafica con tema Material Design
root = ThemedTk(theme="equilux")
root.title("Confronto Liste Followers e Following")

result = tk.StringVar()

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

open_button = ttk.Button(frame, text="Apri File start_here.html", command=open_file_dialog)
open_button.pack(fill='x')

result_label = ttk.Label(frame, textvariable=result, justify='left')
result_label.pack(pady=(10, 0))

root.mainloop()
