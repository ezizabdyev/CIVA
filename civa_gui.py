# civa_gui.py

import tkinter as tk
from tkinter import messagebox, scrolledtext
from civa_core02 import get_response, speak, listen

# --- GUI Class ---
class CIVAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CIVA - Virtual Assistant")
        self.root.geometry("700x500")
        self.root.configure(bg="#121212")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="white", font=("Segoe UI", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.insert(tk.END, "🤖 CIVA is online. How can I help you?\n\n")
        self.chat_area.configure(state='disabled')

        self.entry = tk.Entry(root, font=("Segoe UI", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
        self.entry.bind("<Return>", self.process_text_input)

        send_btn = tk.Button(root, text="Send", command=self.process_text_input, bg="#00bfa5", fg="white")
        send_btn.pack(side=tk.LEFT, padx=5)

        mic_btn = tk.Button(root, text="🎤", command=self.process_voice_input, bg="#3f51b5", fg="white")
        mic_btn.pack(side=tk.LEFT)

    def append_chat(self, speaker, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"{speaker}: {message}\n\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

    def process_text_input(self, event=None):
        user_input = self.entry.get().strip()
        if user_input:
            self.entry.delete(0, tk.END)
            self.append_chat("🧑‍💻 You", user_input)
            response = get_response(user_input)
            self.append_chat("🤖 CIVA", response)
            speak(response)

    def process_voice_input(self):
        self.append_chat("🎙️", "Listening...")
        user_input = listen()
        if user_input:
            self.append_chat("🧑‍💻 You", user_input)
            response = get_response(user_input)
            self.append_chat("🤖 CIVA", response)
            speak(response)
        else:
            self.append_chat("🤖 CIVA", "Sorry, I couldn't hear you.")

# --- Launch GUI ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CIVAApp(root)
    root.mainloop()
