import tkinter as tk
from tkinter import messagebox
import re

# Common weak passwords list (partial for demonstration)
WEAK_PASSWORDS = {"password", "123456", "qwerty", "abc123", "admin", "letmein", "welcome"}

# Function to check password strength
def check_password_strength():
    password = password_entry.get()
    strength, feedback = evaluate_password(password)
    strength_label.config(text=f"Strength: {strength}", fg=("green" if strength == "Strong" else "red"))
    recommendations_label.config(text=feedback, fg="blue")

# Function to evaluate password
def evaluate_password(password):
    if len(password) < 8:
        return "Weak", "Use at least 8 characters."
    
    if password in WEAK_PASSWORDS:
        return "Weak", "This is a commonly used password. Choose something unique."
    
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    complexity_score = sum([has_upper, has_lower, has_digit, has_special])

    if complexity_score < 3:
        return "Medium", "Use a mix of uppercase, lowercase, numbers, and symbols."
    
    return "Strong", "Good job! Your password is strong."

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
strength_label.pack()

recommendations_label = tk.Label(root, text="", wraplength=350, font=("Arial", 10), fg="blue")
recommendations_label.pack(pady=10)

root.mainloop()
