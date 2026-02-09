"""Windowsで動作するシンプルな電卓アプリ。"""

import tkinter as tk


class CalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self) -> None:
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Segoe UI", 22),
            justify="right",
            bd=8,
            relief=tk.GROOVE,
            state="readonly",
            readonlybackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("(", 5, 2), (")", 5, 3),
        ]

        for text, row, col in buttons:
            self._make_button(text, row, col)

        equals_btn = tk.Button(
            self.root,
            text="=",
            font=("Segoe UI", 18, "bold"),
            command=self._calculate,
            bg="#4CAF50",
            fg="white",
            activebackground="#45A049",
        )
        equals_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=8, pady=(0, 8), ipady=12)

        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def _make_button(self, text: str, row: int, col: int) -> None:
        button = tk.Button(
            self.root,
            text=text,
            font=("Segoe UI", 16),
            command=lambda value=text: self._on_button_click(value),
        )
        button.grid(row=row, column=col, sticky="nsew", padx=4, pady=4, ipady=10)

    def _on_button_click(self, value: str) -> None:
        if value == "C":
            self.expression = ""
        elif value == "⌫":
            self.expression = self.expression[:-1]
        else:
            self.expression += value

        self.display_var.set(self.expression or "0")

    def _calculate(self) -> None:
        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_var.set("Error")


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
