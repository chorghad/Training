from docx import Document
doc_file_path ='test_3.docx'
doc = Document(doc_file_path)
for paragraph in doc.paragraphs:
    print(paragraph.text)