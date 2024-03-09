from docx import Document
doc_file_path ='test_3.docx'
doc = Document(doc_file_path)
new_para='new para text'
doc.add_paragraph(new_para)
doc.save('test_3.docx')