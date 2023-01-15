import os
from image_resize import resize_image
from excel_generator import generate_excel

# Please note that the sub-folder names in "path_to_orig_images_jpg" will be used as excel sheet name
path_to_orig_images_jpg = ".\\original_images_folder"
path_to_resized_images_folder = '.\\resized_images_folder'
path_to_excel_output = '.\\excel_output'
excel_output_file_name = '.\\output_file.xlsx'
new_size = (400, 300)

folders = []
n=1
for folder in os.listdir(path_to_orig_images_jpg):
    if os.path.isdir(os.path.join(path_to_orig_images_jpg, folder)):
        print("folder {}: {} \n".format(n,folder))
        folders.append(folder)
        n+=1

print("folders")

for i in folders:
    # Get the list of all files in original folder
    file_list = os.listdir(os.path.join(path_to_orig_images_jpg ,i))
    # Filter to only the files that have ".jpg" extension
    jpg_files = [file for file in file_list if file.endswith(".jpg")]

    for j in jpg_files:
        try:
            resize_image(image_path =os.path.join(path_to_orig_images_jpg ,i,j)
            , save_folder = os.path.join(path_to_resized_images_folder,i)
            , new_size = new_size
            , fixed_size=False    # Change to True is you don't want to keep original ratio
            )
        except Exception as e:
            print(f"An error occurred while converting the image: {e}")



images_data = {}
for i in folders:
    jpg_files = [file for file in i if file.endswith(".jpg")]
    file_list = os.listdir(os.path.join(path_to_resized_images_folder ,i))
    jpg_files = [file for file in file_list if file.endswith(".jpg")]
    images_data[i] = [os.path.join(path_to_resized_images_folder,i ,j) for j in jpg_files]
print(images_data)
generate_excel(os.path.join(path_to_excel_output,excel_output_file_name), images_data , new_cell_size =new_size)
