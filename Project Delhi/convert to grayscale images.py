import os
from PIL import Image

def convert_images_to_grayscale(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    grayscale_img = img.convert('L')  # 'L' mode is for grayscale
                    grayscale_img.save(file_path)  # Overwrite the original image
                    print(f"Converted: {filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

# Example usage:
folder = 'C:/Users/yashs/OneDrive/Desktop/Project Delhi/Icons'  # <-- Change this to your actual folder path
convert_images_to_grayscale(folder)
