import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class WordLikeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WordLike")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill="both")
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        format_menu = tk.Menu(menubar, tearoff=0)
        format_menu.add_command(label="Bold", command=self.make_text_bold)
        format_menu.add_command(label="Italic", command=self.make_text_italic)
        format_menu.add_command(label="Underline", command=self.make_text_underline)
        menubar.add_cascade(label="Format", menu=format_menu)

        self.root.config(menu=menubar)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        if not self.text_area.get(1.0, tk.END).strip():
            messagebox.showwarning("Warning", "Nothing to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_as_file(self):
        if not self.text_area.get(1.0, tk.END).strip():
            messagebox.showwarning("Warning", "Nothing to save.")
            return

        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def make_text_bold(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "bold" in current_tags:
            self.text_area.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("bold", "sel.first", "sel.last")
            self.text_area.tag_config("bold", font=("Arial", 12, "bold"))

    def make_text_italic(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "italic" in current_tags:
            self.text_area.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("italic", "sel.first", "sel.last")
            self.text_area.tag_config("italic", font=("Arial", 12, "italic"))

    def make_text_underline(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "underline" in current_tags:
            self.text_area.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("underline", "sel.first", "sel.last")
            self.text_area.tag_config("underline", underline=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordLikeApp(root)
    root.mainloop()
