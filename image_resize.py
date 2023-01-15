import os
from PIL import Image


def resize_image(image_path, save_folder, new_size, fixed_size=False,):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    original_image = Image.open(image_path)
    org_width, org_height = original_image.size

    if fixed_size == True:
        resized_image = original_image.resize((new_size[0], new_size[1]), resample=Image.LANCZOS)
        print("Successfully resized file: {} from {}x{} to {}x{} pixels".format(image_path, org_width, org_height, new_size[0], new_size[1]))

    else:
        # check for the original width-height ratio of the image
        original_ratio = org_width / org_height
        # Determine the new aspect ratio of the image
        new_ratio = new_size[0] / new_size[1]
        if original_ratio > new_ratio:
            # Case: Width is the limiting factor
            new_width = new_size[0]
            new_height = int(new_width / original_ratio)
            
        else:
            # Case: Height is the limiting factor
            new_height = new_size[1]
            new_width = int(new_height * original_ratio)
        resized_image = original_image.resize((new_width, new_height), resample=Image.LANCZOS)
        print("Successfully resized file: {} from {}x{} to {}x{} pixels".format(image_path, org_width, org_height, new_width, new_height))

    
    # Extract file name
    file_name = os.path.basename(image_path)
    # Build a new file path
    save_path = os.path.join(save_folder, file_name)
    resized_image.save(save_path)
    return save_path