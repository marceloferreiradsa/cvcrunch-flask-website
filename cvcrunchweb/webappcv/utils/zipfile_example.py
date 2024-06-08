import zipfile
import os
from xml.etree import ElementTree as ET
import uuid
import time

file_path = os.path.join('static', 'uploads')
file = os.path.join('static', 'uploads', 'Marcelo_Ferreira.docx')
new_file = os.path.join('static', 'uploads', 'CV_' + str(uuid.uuid4()) + '_' + str(int(time.time())) + '.txt')

# Path to your .docx file
docx_file = file
# Directory where we'll extract the contents
extract_dir = file_path

# Extract the .docx file
with zipfile.ZipFile(docx_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Path to the extracted 'document.xml' file
document_xml_path = os.path.join(extract_dir, 'word', 'document.xml')

# Parse the 'document.xml' file
tree = ET.parse(document_xml_path)
root = tree.getroot()

# # Define namespaces to search the XML properly
# namespaces = {
#     'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
# }

# # Iterate through the text elements and print out the text
# for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
#     texts = [node.text for node in paragraph.findall('.//w:t', namespaces)]
#     paragraph_text = ''.join(filter(None, texts))  # Join and filter out None values
#     print(paragraph_text)

# # Optionally, clean up by removing the extracted directory
# # Be careful with this if you have important data in the same directory
# # import shutil
# # shutil.rmtree(extract_dir)
