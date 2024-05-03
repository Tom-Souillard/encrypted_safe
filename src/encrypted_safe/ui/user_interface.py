import tkinter as tk
from tkinter import simpledialog, messagebox
from src.encrypted_safe.db.user_crud import create_user, get_user_by_username, update_user, delete_user
from src.encrypted_safe.db.database import SessionLocal, init_db
from src.encrypted_safe.ui.file_manager import FileManager
from src.encrypted_safe.db.auth import login, logout

def create_account():
    with SessionLocal() as db:
        username = simpledialog.askstring("Username", "Enter your username:")
        email = simpledialog.askstring("Email", "Enter your email:")
        password = simpledialog.askstring("Password", "Enter your password:", show='*')
        if username and email and password:
            user = create_user(db, username, email, password)
            messagebox.showinfo("Success", f"User {user.username} created successfully!")

def update_account():
    with SessionLocal() as db:
        user_id = simpledialog.askinteger("User ID", "Enter your user ID:")
        new_password = simpledialog.askstring("New Password", "Enter new password:", show='*')
        user = update_user(db, user_id, new_password)
        if user:
            messagebox.showinfo("Success", "Password updated successfully!")
        else:
            messagebox.showinfo("Failed", "Password update failed!")

def delete_account():
    with SessionLocal() as db:
        user_id = simpledialog.askinteger("User ID", "Enter your user ID:")
        delete_user(db, user_id)
        messagebox.showinfo("Success", "User deleted successfully!")

def prompt_login():
    username = simpledialog.askstring("Login", "Enter your username:")
    password = simpledialog.askstring("Login", "Enter your password:", show='*')
    if login(username, password):
        tk.messagebox.showinfo("Login", "Successfully logged in!")
    else:
        tk.messagebox.showerror("Login", "Failed to log in. Please check your credentials.")

def prompt_logout(username):
    logout(username)
    tk.messagebox.showinfo("Logout", "Successfully logged out!")

def main():
    root = tk.Tk()
    root.title("Encrypted Safe User Management")
    login_button = tk.Button(root, text="Log In", command=prompt_login)
    logout_button = tk.Button(root, text="Log Out", command=lambda: prompt_logout("current_user"))  # Assume "current_user" is tracked somewhere
    login_button.pack()
    logout_button.pack()
    create_account_button = tk.Button(root, text="Create Account", command=create_account)
    update_account_button = tk.Button(root, text="Update Account", command=update_account)
    delete_account_button = tk.Button(root, text="Delete Account", command=delete_account)
    create_account_button.pack()
    update_account_button.pack()
    delete_account_button.pack()

    # Initialize database
    init_db()

    # Optionally start file manager
    fm = FileManager(root)

    root.mainloop()

if __name__ == "__main__":
    main()


# import tkinter as tk
# from tkinter import simpledialog, messagebox
# import sys
# import os
#
# # Ajouter le répertoire racine du projet à sys.path
# project_root = os.path.abspath('../../../')  # Ajustez le chemin selon la structure réelle
# sys.path.append(project_root)
#
# from src.encrypted_safe.db.user_crud import create_user, get_user_by_username, update_user, delete_user
# from src.encrypted_safe.db.database import SessionLocal, init_db
# from src.encrypted_safe.ui.file_manager import FileManager
#
# # Initialisation de la base de données
# init_db()
#
# def create_account():
#     db = SessionLocal()
#     username = simpledialog.askstring("Username", "Enter your username:")
#     email = simpledialog.askstring("Email", "Enter your email:")
#     password = simpledialog.askstring("Password", "Enter your password:", show='*')
#     if username and email and password:
#         user = create_user(db, username, email, password)
#         messagebox.showinfo("Success", f"User {user.username} created successfully!")
#     db.close()
#
# def update_account():
#     db = SessionLocal()
#     user_id = simpledialog.askinteger("User ID", "Enter your user ID:")
#     new_password = simpledialog.askstring("New Password", "Enter new password:", show='*')
#     user = update_user(db, user_id, new_password)
#     if user:
#         messagebox.showinfo("Success", "Password updated successfully!")
#     else:
#         messagebox.showinfo("Failed", "Password update failed!")
#     db.close()
#
# def delete_account():
#     db = SessionLocal()
#     user_id = simpledialog.askinteger("User ID", "Enter your user ID:")
#     delete_user(db, user_id)
#     messagebox.showinfo("Success", "User deleted successfully!")
#     db.close()
#
# root = tk.Tk()
# #root.withdraw()
# create_account_button = tk.Button(root, text="Create Account", command=create_account)
# update_account_button = tk.Button(root, text="Update Account", command=update_account)
# delete_account_button = tk.Button(root, text="Delete Account", command=delete_account)
# create_account_button.pack()
# update_account_button.pack()
# delete_account_button.pack()
# root.mainloop()
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     fm = FileManager(root)
#     root.mainloop()