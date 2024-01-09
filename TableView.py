import customtkinter as ctk
import tkinter as tk
from typing import List

class TableViewForm:
    """
    A class to create and display a table view form using customtkinter and tkinter.
    """
    def __init__(self, root: tk.Tk, data: List[List[str]]):
        """
        Initialize the TableViewForm.

        :param root: The parent tkinter widget.
        :param data: A 2D list of data to be displayed in the table.
        """
        self.root = root
        self.data = data
        self.num_rows = len(data)
        self.num_cols = len(data[0]) if data else 0
        self.labels = None

    def display(self):
        """
        Display the table form in a new window.
        """
        if not self.labels or len(self.labels) != self.num_cols:
            raise ValueError("Labels are either not set or their count does not match the number of columns.")

        form_window = ctk.CTkToplevel(self.root)
        form_window.title("Data Form")

        for col, label_text in enumerate(self.labels):
            label = ctk.CTkLabel(form_window, text=label_text, text_color='purple1')
            label.grid(row=0, column=col, padx=5, pady=5, sticky="w")

        for row in range(1, self.num_rows + 1):
            for col in range(self.num_cols):
                value = self.data[row - 1][col] if col < len(self.data[row - 1]) else ''
                value_label = ctk.CTkLabel(form_window, text=value)
                value_label.grid(row=row, column=col, padx=5, pady=5, sticky="w")

    def set_labels(self, labels: List[str]):
        """
        Set the column labels for the table.

        :param labels: A list of label strings for the columns.
        """
        if len(labels) != self.num_cols:
            raise ValueError("The number of labels does not match the number of columns.")

        self.labels = labels
