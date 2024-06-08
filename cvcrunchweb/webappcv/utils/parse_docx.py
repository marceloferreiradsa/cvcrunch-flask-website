import docx
import os
import re
import uuid
import time

file_path = os.path.join('static', 'uploads')
file = os.path.join('static', 'uploads', 'Marcelo_Ferreira_Junior_Psychometrics_Analyst.docx')
new_file = os.path.join('static', 'uploads', 'CV_' + str(uuid.uuid4()) + '_' + str(int(time.time())) + '.txt')

folder = os.getcwd()

def parse_docx(file):
    doc = docx.Document(file)
    new_text = ""
    for p in doc.paragraphs:
        new_text+=p.text.replace('\t', ' ')+' '
        
    new_text = re.sub(' +', ' ', new_text.strip())
    return new_text

text_content = parse_docx(file=file)

with open(new_file, 'w', encoding='utf-8') as file:
        file.write(text_content)
