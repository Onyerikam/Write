import openai
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image

# Set up OpenAI API key
openai.api_key = "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"

# Set up Tkinter GUI
root = tk.Tk()
root.title("AI Book Writer")

# Set up styles
# Light Mode
style_light = ttk.Style()
style_light.theme_use("clam")
style_light.configure("TLabel", foreground="black", background="white")
style_light.configure("TButton", foreground="white", background="blue")
style_light.map("TButton", foreground=[("pressed", "white"), ("active", "white")], background=[("pressed", "blue"), ("active", "blue")])

# Dark Mode
style_dark = ttk.Style()
style_dark.theme_use("clam")
style_dark.configure("TLabel", foreground="white", background="#1c1c1c")
style_dark.configure("TButton", foreground="white", background="#263d42")
style_dark.map("TButton", foreground=[("pressed", "white"), ("active", "white")], background=[("pressed", "#263d42"), ("active", "#263d42")])

# Default to Light Mode
current_style = style_light

# Function to toggle between light and dark mode
def toggle_style():
    global current_style
    if current_style == style_light:
        current_style = style_dark
    else:
        current_style = style_light
    root.config(bg=current_style.lookup(".", "background"))
    for widget in root.winfo_children():
        widget.configure(style=current_style.lookup(widget.winfo_class(), "style"))

# Set up GUI elements
frame1 = ttk.Frame(root, padding=20, style="TFrame")
frame1.pack(fill="both", expand=True)

search_label = ttk.Label(frame1, text="Search Google for information related to your book:", style="TLabel")
search_label.grid(row=0, column=0, sticky="w")

search_entry = ttk.Entry(frame1, width=40)
search_entry.grid(row=1, column=0, padx=10, pady=10)

def search_google():
    query = search_entry.get()
    if query == "":
        messagebox.showwarning("Warning", "Please enter a search query.")
    else:
        webbrowser.open(f"https://www.google.com/search?q={query}")

search_button = ttk.Button(frame1, text="Search", command=search_google, style="TButton")
search_button.grid(row=1, column=1, padx=10, pady=10)

synonym_label = ttk.Label(frame1, text="Find synonyms and antonyms:", style="TLabel")
synonym_label.grid(row=2, column=0, sticky="w")

synonym_entry = ttk.Entry(frame1, width=40)
synonym_entry.grid(row=3, column=0, padx=10, pady=10)

def find_synonyms():
    word = synonym_entry.get()
    if word == "":
        messagebox.showwarning("Warning", "Please enter a word to find synonyms for.")
    else:
        result = openai.Completion.create(engine="davinci", prompt=f"Find synonyms and antonyms for the word '{word}':", max_tokens=60)
        messagebox.showinfo("Synonyms and Antonyms", result.choices[0].text)

synonym_button = ttk.Button(frame1, text="Find", command=find_synonyms, style="TButton")
synonym_button.grid(row=3, column=1, padx=10, pady=10)

outline_label = ttk.Label(frame1, text="Generate an outline for your book:", style="TLabel")
outline_label.grid(row=4, column=0, sticky="w")

outline_entry = ttk.Entry(frame1, width=40)
outline_entry.grid(row=5, column=0, padx=10, pady=10)

def generate_outline():
    prompt = outline_entry.get()
    if prompt == "":
        messagebox.showwarning("Warning", "Please enter a prompt to generate an outline.")
    else:
       result = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=60)
       messagebox.showinfo("Outline Generated", result.choices[0].text)

outline_button = ttk.Button(frame1, text="Generate", command=generate_outline, style="TButton")
outline_button.grid(row=5, column=1, padx=10, pady=10)

chapter_label = ttk.Label(frame1, text="Generate a chapter for your book:", style="TLabel")
chapter_label.grid(row=6, column=0, sticky="w")

chapter_entry = ttk.Entry(frame1, width=40)
chapter_entry.grid(row=7, column=0, padx=10, pady=10)

def generate_chapter():
    prompt = chapter_entry.get()
    if prompt == "":
       messagebox.showwarning("Warning", "Please enter a prompt to generate a chapter.")
    else:
       result = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=1000)
       messagebox.showinfo("Chapter Generated", result.choices[0].text)

chapter_button = ttk.Button(frame1, text="Generate", command=generate_chapter, style="TButton")
chapter_button.grid(row=7, column=1, padx=10, pady=10)

character_label = ttk.Label(frame1, text="Generate a character for your book:", style="TLabel")
character_label.grid(row=8, column=0, sticky="w")

character_entry = ttk.Entry(frame1, width=40)
character_entry.grid(row=9, column=0, padx=10, pady=10)

def generate_character():
    prompt = character_entry.get()
    if prompt == "":
       messagebox.showwarning("Warning", "Please enter a prompt to generate a character.")
    else:
       result = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=60)
       messagebox.showinfo("Character Generated", result.choices[0].text)

character_button = ttk.Button(frame1, text="Generate", command=generate_character, style="TButton")
character_button.grid(row=9, column=1, padx=10, pady=10)

title_label = ttk.Label(frame1, text="Generate a title for your book:", style="TLabel")
title_label.grid(row=10, column=0, sticky="w")

title_entry = ttk.Entry(frame1, width=40)
title_entry.grid(row=11, column=0, padx=10, pady=10)

def generate_title():
    prompt = title_entry.get()
    if prompt == "":
       messagebox.showwarning("Warning", "Please enter a prompt to generate a title.")
    else:
       result = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=30)
       messagebox.showinfo("Title Generated", result.choices[0].text)

title_button = ttk.Button(frame1, text="Generate", command=generate_title, style="TButton")
title_button.grid(row=11, column=1, padx=10, pady=10)

style_label = ttk.Label(frame1, text="Toggle between light and dark mode:", style="TLabel")
style_label.grid(row=12, column=0, sticky="w")

style_button = ttk.Button(frame1, text="Light Mode", command=toggle_style, style="TButton")
style_button.grid(row=12, column=1, padx=10, pady=10)

root.mainloop() # run the GUI loop
