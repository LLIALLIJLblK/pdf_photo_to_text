import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import re
# путь к файлу с PDF
pdf_path = 'path/to/your/pdf/file.pdf'
# папка, куда будут загружены изображения из документа 
output_folder = 'output_images'

# файл, куда будет записан извлеченный текст
output_text_file = 'output.txt'


if os.path.exists(output_text_file):
    with open(output_text_file, 'r', encoding='utf-8') as f:
        extracted_text = f.read().split('\n')
else:

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

   
    images = convert_from_path(pdf_path)

  
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i}.png')
        image.save(image_path, 'PNG')

    
    
    #pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract' 
    #pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


    extracted_text = []
    for i in range(len(images)):
        image_path = os.path.join(output_folder, f'page_{i}.png')
        text = pytesseract.image_to_string(Image.open(image_path), lang='rus')
        extracted_text.append(text)

   
    with open(output_text_file, 'w') as f:
        for text in extracted_text:
            f.write(text + '\n')
    print("файл после обработки тессерактом")



def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)   
    text = text.strip()  
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip() 

    return text


input_file = 'output.txt'

with open(input_file, 'r') as file:
    text = file.read()  


cleaned_text = clean_text(text)
output_file = 'cleaned_output.txt'
with open(output_file, 'w') as file:
    file.write(cleaned_text)

print(f"Очищенный текст сохранен в файл: {output_file}")

