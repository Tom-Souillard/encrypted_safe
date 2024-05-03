import os
import tkinter as tk
from tkinter import filedialog, Listbox, messagebox, simpledialog
from src.encrypted_safe.utils.logging_config import logger

class FileManager:
    def __init__(self, root):
        self.root = root
        self.current_path = None
        self.listbox = Listbox(root)
        self.listbox.pack(fill=tk.BOTH, expand=1)

        # Setup buttons
        tk.Button(root, text="Open Directory", command=self.open_directory).pack()
        tk.Button(root, text="Delete File/Folder", command=self.delete_item).pack()
        tk.Button(root, text="Rename File/Folder", command=self.rename_item).pack()

    def open_directory(self):
        path = filedialog.askdirectory()
        if path:
            self.current_path = path
            self.list_directory()

    def list_directory(self):
        if self.current_path:
            self.listbox.delete(0, tk.END)
            for item in os.listdir(self.current_path):
                self.listbox.insert(tk.END, item)

    def delete_item(self):
        selection = self.listbox.curselection()
        if selection:
            item = self.listbox.get(selection)
            full_path = os.path.join(self.current_path, item)
            try:
                if os.path.isdir(full_path):
                    os.rmdir(full_path)
                else:
                    os.remove(full_path)
                self.list_directory()
                logger.info(f"Action: Deleted {item}")
                messagebox.showinfo("Success", "Item deleted successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "No item selected.")

    def rename_item(self):
        selection = self.listbox.curselection()
        if selection:
            item = self.listbox.get(selection)
            new_name = simpledialog.askstring("Rename", "Enter new name:", initialvalue=item)
            if new_name:
                full_path = os.path.join(self.current_path, item)
                new_path = os.path.join(self.current_path, new_name)
                try:
                    os.rename(full_path, new_path)
                    self.list_directory()
                    messagebox.showinfo("Success", "Item renamed successfully.")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "No item selected.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Manager")
    fm = FileManager(root)
    root.mainloop()
