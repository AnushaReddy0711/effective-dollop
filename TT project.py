import time
import random
import tkinter as tk
from tkinter import ttk, messagebox

# Sentences categorized by difficulty level
sentences = {
    "Easy": [
        "The cat sits on the mat.",
        "Python is fun to learn.",
        "I love to read books.",
        "Typing fast is useful.",
        "Code and debug often."
    ],
    "Medium": [
        "The quick brown fox jumps over the lazy dog.",
        "A good programmer is always learning new things.",
        "Typing tests improve both speed and accuracy.",
        "Errors are a stepping stone to mastery.",
        "Every journey begins with a single step."
    ],
    "Hard": [
        "Artificial intelligence is revolutionizing the modern world.",
        "Cryptography is essential for securing digital communication.",
        "Debugging complex algorithms requires patience and skill.",
        "Machine learning models analyze vast amounts of data.",
        "Programming challenges help develop logical thinking abilities."
    ]
}

class TypingSpeedTester:
    def __init__(self, root):  # Corrected __init__ method
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=5)
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TCombobox", font=("Arial", 12))

        # UI Elements
        ttk.Label(root, text="Select Difficulty Level:", font=("Arial", 14)).pack(pady=5)

        self.difficulty = ttk.Combobox(root, values=["Easy", "Medium", "Hard"], state="readonly")
        self.difficulty.pack(pady=5)
        self.difficulty.current(0)

        self.start_button = ttk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.sentence_label = ttk.Label(root, text="", font=("Arial", 14), wraplength=500)
        self.sentence_label.pack(pady=10)

        self.text_entry = tk.Text(root, height=3, font=("Arial", 12), state="disabled")
        self.text_entry.pack(pady=10)

        self.submit_button = ttk.Button(root, text="Submit", command=self.calculate_speed, state="disabled")
        self.submit_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

        self.start_time = None
        self.current_sentence = ""

    def start_test(self):
        """Starts the typing test."""
        difficulty = self.difficulty.get()
        self.current_sentence = random.choice(sentences[difficulty])

        self.sentence_label.config(text=self.current_sentence)
        self.text_entry.config(state="normal")
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.focus()

        self.start_time = time.time()
        self.submit_button.config(state="normal")

    def calculate_speed(self):
        """Calculates typing speed and accuracy."""
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        typed_text = self.text_entry.get("1.0", tk.END).strip()
        word_count = len(self.current_sentence.split())
        speed = (word_count / elapsed_time) * 60  # Words per minute (WPM)

        # Accuracy Calculation
        correct_chars = sum(1 for a, b in zip(self.current_sentence, typed_text) if a == b)
        accuracy = (correct_chars / len(self.current_sentence)) * 100 if self.current_sentence else 0

        # Show results
        self.result_label.config(text=f"Speed: {speed:.2f} WPM | Accuracy: {accuracy:.2f}%")
        self.text_entry.config(state="disabled")
        self.submit_button.config(state="disabled")

# Run the GUI
root = tk.Tk()
app = TypingSpeedTester(root)
root.mainloop()
