import tkinter as tk

# Colors and Styling
BG_COLOR = "#2c2f33"
BTN_COLOR = "#7289da"
DISPLAY_COLOR = "#23272a"
TEXT_COLOR = "white"
BTN_FONT = ("Helvetica", 16)
DISPLAY_FONT = ("Helvetica", 20)

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Calculator")
        self.root.geometry("350x500")
        self.root.config(bg=BG_COLOR)

        self.expression = ""

        # Display Entry
        self.display = tk.Entry(root, font=DISPLAY_FONT, bg=DISPLAY_COLOR, fg=TEXT_COLOR, bd=0, relief=tk.FLAT, justify="right")
        self.display.pack(fill="both", ipadx=8, ipady=25, pady=(10, 0), padx=10)

        # Button Grid
        btn_frame = tk.Frame(root, bg=BG_COLOR)
        btn_frame.pack(pady=10)

        buttons = [
            ["AC", "(", ")", "%"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for r, row in enumerate(buttons):
            for c, btn_text in enumerate(row):
                btn = tk.Button(
                    btn_frame,
                    text=btn_text,
                    font=BTN_FONT,
                    bg=BTN_COLOR if btn_text != "=" and btn_text != "AC" else ("#43b581" if btn_text == "=" else "#f04747"),
                    fg=TEXT_COLOR,
                    width=6,
                    height=2,
                    command=lambda text=btn_text: self.on_button_click(text)
                )
                btn.grid(row=r, column=c, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "AC":
            self.expression = ""
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
