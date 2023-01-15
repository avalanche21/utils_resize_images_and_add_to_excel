import os
from PIL import Image


def resize_image(image_path, width, height, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    original_image = Image.open(image_path)
    org_width, org_height = original_image.size
    print("Successfully resized file: {} from {}x{} to {}x{} pixels".format(image_path, org_width, org_height, width, height))
    resized_image = original_image.resize((width, height))
    # Extract file name
    file_name = os.path.basename(image_path)
    # Build a new file path
    save_path = os.path.join(save_folder, file_name)
    resized_image.save(save_path)
    return save_path