import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

def plot_single_run(file_path):
    try:
        data = loadmat(file_path)
        print(f"Variables in {file_path}")
        print (data.keys())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    plot_single_run('/Users/caitlynboynton/Desktop/1051run3.mat')