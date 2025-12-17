import tkinter as tk
import random
import time

class TypingSpeedTest(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Typing Speed Test")
        self.geometry("400x200")

        self.word_label = tk.Label(self, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.input_entry = tk.Entry(self, font=("Arial", 18))
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", self.check_input)

        self.words = ["programming", "python", "typing", "speed", "test", "challenge"]
        self.current_word = ""

        self.start_game()

    def start_game(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.input_entry.delete(0, tk.END)
        self.start_time = time.time()

    def check_input(self, event):
        user_input = self.input_entry.get()
        if user_input == self.current_word:
            elapsed_time = time.time() - self.start_time
            typing_speed = len(self.current_word) / (elapsed_time / 60)
            result_label = tk.Label(self, text=f"Typing Speed: {typing_speed:.2f} WPM", font=("Arial", 18))
            result_label.pack(pady=10)
            self.after(2000, self.reset_game)
        else:
            error_label = tk.Label(self, text="Incorrect, try again!", font=("Arial", 18), fg="red")
            error_label.pack(pady=10)

    def reset_game(self):
        self.input_entry.delete(0, tk.END)
        self.word_label.config(text="")
        self.after(1000, self.start_game)

if __name__ == "__main__":
    app = TypingSpeedTest()
    app.mainloop()
