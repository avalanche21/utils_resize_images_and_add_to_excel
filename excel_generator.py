import openpyxl
from openpyxl.drawing.image import Image

def generate_excel(file_path, images_data):
    wb = openpyxl.Workbook()
    wb.remove(wb["Sheet"])
    
    for sheet_name, image_paths in images_data.items():
        ws = wb.create_sheet(title=sheet_name)
        for i, i_path in enumerate(image_paths):
            img = Image(i_path)
            # print("image width = {}, image height = {}".format(img.width,img.height))
            ws.column_dimensions['B'].width = img.height *(1/5.5)
            ws.row_dimensions[2 + i * 2].height = img.height * (3/4)
            ws.add_image(img, 'B{}'.format(2 + i * 2))
            
    wb.save(file_path)