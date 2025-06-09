import tkinter as tk
from tkinter import messagebox

def calculate_soc(voltage):
    min_voltage = 3.0
    max_voltage = 4.2

    if voltage < min_voltage:
        return 0.0
    elif voltage > max_voltage:
        return 100.0
    else:
        return ((voltage - min_voltage) / (max_voltage - min_voltage)) * 100

def on_calculate():
    try:
        voltage = float(entry.get())
        soc = calculate_soc(voltage)
        result_label.config(text=f"Estimated SoC: {soc:.2f}%")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# --- Tkinter UI setup ---
app = tk.Tk()
app.title("Smart BMS - SoC Calculator")

tk.Label(app, text="Enter Voltage (V):").pack(pady=5)
entry = tk.Entry(app)
entry.pack(pady=5)

tk.Button(app, text="Calculate SoC", command=on_calculate).pack(pady=10)
result_label = tk.Label(app, text="")
result_label.pack(pady=5)

app.mainloop()


