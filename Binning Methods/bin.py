import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import random

# Function to perform equal width binning
def equal_width_binning(data, num_bins):
    min_val = min(data)
    max_val = max(data)
    bin_width = (max_val - min_val) / num_bins
    bins = [(min_val + i * bin_width, min_val + (i + 1) * bin_width) for i in range(num_bins)]
    binned_data = {f"Bin {i+1} ({bins[i][0]:.2f} - {bins[i][1]:.2f})": [] for i in range(num_bins)}

    for d in data:
        for i, bin_range in enumerate(bins):
            if bin_range[0] <= d < bin_range[1]:
                binned_data[f"Bin {i+1} ({bin_range[0]:.2f} - {bin_range[1]:.2f})"].append(d)

    return bins, binned_data

# Function to perform equal depth binning
def equal_depth_binning(data, num_bins):
    sorted_data = sorted(data)
    bin_size = len(data) // num_bins
    bins = [sorted_data[i * bin_size: (i + 1) * bin_size] for i in range(num_bins)]
    bin_ranges = [(min(bin), max(bin)) for bin in bins]
    binned_data = {f"Bin {i+1} ({bin_ranges[i][0]:.2f} - {bin_ranges[i][1]:.2f})": bins[i] for i in range(num_bins)}
    return bin_ranges, binned_data

# Function to generate random data
def generate_random_data():
    num_data_points = 20  # Fixed number of points
    return [random.uniform(1, 100) for _ in range(num_data_points)]

# Function to display the result
def display_result(binning_type, data, num_bins):
    if binning_type == 'Equal Width':
        bins, binned_data = equal_width_binning(data, num_bins)
        result_text.set("Equal Width Binning Steps:\n")
        for i, bin_range in enumerate(bins):
            result_text.set(result_text.get() + f"\nBin {i+1} ({bin_range[0]:.2f} - {bin_range[1]:.2f}) contains {binned_data[f'Bin {i+1} ({bin_range[0]:.2f} - {bin_range[1]:.2f})']}")
    
    elif binning_type == 'Equal Depth':
        bin_ranges, binned_data = equal_depth_binning(data, num_bins)
        result_text.set("Equal Depth Binning Steps:\n")
        for i, bin_range in enumerate(bin_ranges):
            result_text.set(result_text.get() + f"\nBin {i+1} ({bin_range[0]:.2f} - {bin_range[1]:.2f}) contains {binned_data[f'Bin {i+1} ({bin_range[0]:.2f} - {bin_range[1]:.2f})']}")

# Event handler for performing binning
def on_binning():
    binning_type = binning_choice.get()
    data_source = data_choice.get()
    try:
        num_bins = int(num_bins_entry.get())
        if num_bins <= 0:
            raise ValueError("Number of bins should be greater than 0.")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid number of bins: {e}")
        return

    if data_source == 'Enter Data':
        data = list(map(float, data_input.get().split(',')))
    elif data_source == 'Generate Random':
        data = generate_random_data()

    display_result(binning_type, data, num_bins)

# Main window setup
root = tk.Tk()
root.title("Binning Demo")

# Frame for selecting binning method
binning_frame = ttk.LabelFrame(root, text="Select Binning Type", padding="10")
binning_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

binning_choice = ttk.Combobox(binning_frame, values=['Equal Width', 'Equal Depth'], state="readonly")
binning_choice.grid(row=0, column=0, padx=5, pady=5)
binning_choice.set('Equal Width')

# Frame for selecting data source
data_frame = ttk.LabelFrame(root, text="Select Data Source", padding="10")
data_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

data_choice = ttk.Combobox(data_frame, values=['Enter Data', 'Generate Random'], state="readonly")
data_choice.grid(row=0, column=0, padx=5, pady=5)
data_choice.set('Enter Data')

# Frame for entering data
data_input_frame = ttk.LabelFrame(root, text="Enter Data (comma-separated)", padding="10")
data_input_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

data_input = ttk.Entry(data_input_frame, width=40)
data_input.grid(row=0, column=0, padx=5, pady=5)

# Frame for entering number of bins
bins_frame = ttk.LabelFrame(root, text="Number of Bins", padding="10")
bins_frame.grid(row=3, column=0, padx=10, pady=10, sticky="w")

num_bins_entry = ttk.Entry(bins_frame)
num_bins_entry.grid(row=0, column=0, padx=5, pady=5)
num_bins_entry.insert(0, "5")

# Button to perform binning
binning_button = ttk.Button(root, text="Perform Binning", command=on_binning)
binning_button.grid(row=4, column=0, padx=10, pady=10)

# Text widget to show the result
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, anchor="w", justify="left", width=100)
result_label.grid(row=5, column=0, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()
