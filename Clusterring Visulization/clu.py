import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to generate and display K-Means clustering
def kmeans_clustering():
    # Generate random data points
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    # Plot the data points and centroids
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

    # Plot the centroids
    centers = kmeans.cluster_centers_
    ax.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5, marker='X')
    
    ax.set_title("K-Means Clustering")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")

    # Display the plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=output_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Main window setup
root = tk.Tk()
root.title("Clustering Visualization")

# Frame for the buttons
button_frame = ttk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Button 1: KMeans Clustering
clustering_button = ttk.Button(button_frame, text="K-Means Clustering", command=kmeans_clustering)
clustering_button.grid(row=0, column=0, padx=5, pady=5)

# Frame for the output area
output_frame = ttk.Frame(root)
output_frame.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
