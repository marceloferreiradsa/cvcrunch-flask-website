import os
import uuid
import time

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

def extract_text(pdf_path):
    extracted_text = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                lines = element.get_text().split('\n')
                for line in lines:
                    line = line.strip()
                    if line:  # Skip empty lines
                        extracted_text.append(line)
    return ' '.join(extracted_text)

pdf_path = os.path.join('static', 'uploads', 'Resume_Marcelo_Ferreira.pdf')
text = extract_text(pdf_path)
new_txt = os.path.join('static', 'uploads', 'CV_' + str(uuid.uuid4()) + '_' + str(int(time.time())) + '.txt')

with open(new_txt, 'w', encoding='utf-8') as file:
    file.write(text)