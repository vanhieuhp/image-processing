import cv2
import numpy as np

def clahe(image, clip_limit=2.0, grid_size=(8,8)):
    # Convert the image ro grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the size of each grid
    height, width = gray.shape
    grid_height = height // grid_size[0]
    grid_width = width // grid_size[1]

    # Apply CLAHE to each grid
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):

            # Define the region of  interest (ROI) for this grid
            start_row = i * grid_height
            end_row = (i + 1) * grid_height if i < grid_size[0] - 1 else (i + 1) * grid_height