import customtkinter as ctk
import re
from datetime import datetime
from tkinter import messagebox
from oracleDB import *

def create_label_entry(form_window, label_text, row, column=0, pady=5, padx=5):
    """
    Creates a label and an entry widget in the specified form window.

    Args:
        form_window: Parent window where the widgets will be placed.
        label_text (str): Text for the label.
        row (int): Grid row position.
        column (int, optional): Grid column position. Defaults to 0.
        pady (int, optional): Vertical padding. Defaults to 5.
        padx (int, optional): Horizontal padding. Defaults to 5.

    Returns:
        tuple[ctk.CTkLabel, ctk.CTkEntry]: Tuple containing the created label and entry widgets.
    """
    label = ctk.CTkLabel(form_window, text=label_text)
    label.grid(row=row, column=column, padx=padx, pady=pady, sticky='w')

    entry = ctk.CTkEntry(form_window)
    entry.grid(row=row, column=column + 1, padx=padx, pady=pady, sticky='ew')

    return label, entry

def create_form(form_window, fields, dropdowns=None, default_values=None):
    """
    Creates a form in the specified window with labels, entries, and dropdowns for given fields.

    Args:
        form_window: Parent window where the form will be created.
        fields (list): List of field names for labels and entries.
        dropdowns (dict, optional): Dictionary with field names and corresponding dropdown options.
        default_values (dict, optional): Dictionary with field names and their default values.

    Returns:
        dict: Dictionary of created label-entry or label-dropdown pairs.
    """
    widgets = {}
    for row, field in enumerate(fields):
        label = ctk.CTkLabel(form_window, text=field)
        label.grid(row=row, column=0, padx=5, pady=5, sticky="w")

        if dropdowns and field in dropdowns:
            option_menu = ctk.CTkOptionMenu(form_window, values=dropdowns[field])
            option_menu.grid(row=row, column=1, padx=5, pady=5, sticky="w")
            widgets[field] = option_menu
        else:
            entry = ctk.CTkEntry(form_window)
            entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")
            widgets[field] = entry

            if default_values and field in default_values:
                entry.insert(0, default_values[field])

    return widgets

def create_root(title, size=(400, 300), resizable=(False, False)):
    """
    Creates the main application window.

    Args:
        title (str): Window title.
        size (tuple, optional): Window size as (width, height). Defaults to (400, 300).
        resizable (tuple, optional): Tuple specifying resizable properties (width, height). Defaults to (False, False).

    Returns:
        ctk.CTk: The main application window.
    """
    app = ctk.CTk()
    app.title(title)
    app.geometry(f"{size[0]}x{size[1]}")
    app.resizable(*resizable)
    return app

def create_button(app, text, command, row, column, pady, padx=5):
    """
    Creates a button in the specified application window.

    Args:
        app (ctk.CTk): Main application window.
        text (str): Text displayed on the button.
        command: Function to execute on button click.
        row (int): Grid row position.
        column (int): Grid column position.
        pady (int): Vertical padding.
        padx (int, optional): Horizontal padding. Defaults to 5.

    Returns:
        ctk.CTkButton: The created button widget.
    """
    button = ctk.CTkButton(app, text=text, command=command)
    button.grid(row=row, column=column, pady=pady, padx=padx)
    return button

def validate_field(value, field_name, field_type):
    """
    Validates a field based on its type and provided value.

    Args:
        value: The input value to be validated.
        field_name (str): Name of the field for error messages.
        field_type (str): Type of the field (e.g., 'int', 'string').

    Returns:
        bool: True if validation is successful, False otherwise.
    """
    validation_rules = {
        'int': lambda v: v.isdigit(),
        'string': lambda v: isinstance(v, str) and len(v) > 0,
        'email': lambda v: len(v) <= 100 and re.match(r"[^@]+@[^@]+\.[^@]+", v),
        'phone': lambda v: v.isdigit() and len(v) == 10,
        'date': lambda v: bool(datetime.strptime(v, "%Y-%m-%d")),
        'decimal': lambda v: bool(float(v))
    }

    if not validation_rules[field_type](value):
        error_messages = {
            'int': "should be an integer",
            'string': "cannot be empty",
            'email': "is not a valid email",
            'phone': "should be a 10 digit number",
            'date': "is not a valid date (expected format YYYY-MM-DD)",
            'decimal': "should be a decimal number"
        }
        messagebox.showerror("Invalid Input", f"{field_name} {error_messages[field_type]}")
        return False

    return True

def load_SQL_scripts(filepath):
    """
    Reads and splits SQL commands from a file.

    Args:
        filepath (str): Path to the file containing SQL commands.

    Returns:
        list: List of individual SQL commands.
    """
    with open(filepath, "r") as file:
        commands = [cmd.strip() for cmd in file.read().split(';') if cmd.strip()]
    return commands
