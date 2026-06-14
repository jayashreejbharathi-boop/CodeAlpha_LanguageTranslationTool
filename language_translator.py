import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

# Text-to-Speech Engine
engine = pyttsx3.init()

# Supported Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

# Translate Function
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning(
                "Warning",
                "Please enter some text."
            )
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy Function
def copy_text():
    translated = output_text.get("1.0", tk.END)

    root.clipboard_clear()
    root.clipboard_append(translated)

    messagebox.showinfo(
        "Copied",
        "Translated text copied!"
    )

# Speak Function
def speak_text():
    text = output_text.get("1.0", tk.END).strip()

    if text:
        engine.say(text)
        engine.runAndWait()

# Main Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x550")

# Title
title = tk.Label(
    root,
    text="🌐 Language Translation Tool",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Input Label
tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 12)
).pack()

# Input Box
input_text = tk.Text(
    root,
    height=6,
    width=70
)
input_text.pack(pady=5)

# Language Selection
frame = tk.Frame(root)
frame.pack(pady=10)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
source_lang.set("English")
source_lang.grid(row=0, column=0, padx=10)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
target_lang.set("Hindi")
target_lang.grid(row=0, column=1, padx=10)

# Translate Button
translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 12)
)
translate_btn.pack(pady=10)

# Output Label
tk.Label(
    root,
    text="Translated Text:",
    font=("Arial", 12)
).pack()

# Output Box
output_text = tk.Text(
    root,
    height=6,
    width=70
)
output_text.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

copy_btn = tk.Button(
    button_frame,
    text="Copy",
    command=copy_text,
    width=10
)
copy_btn.grid(row=0, column=0, padx=10)

speak_btn = tk.Button(
    button_frame,
    text="Speak",
    command=speak_text,
    width=10
)
speak_btn.grid(row=0, column=1, padx=10)

# Run App
root.mainloop()    