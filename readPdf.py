import PyPDF2 as p
import docx 
# import
# # import os
# # import NLP

# # os.chdir('C:\\Users\\shrestha\\Desktop\\sentiment proj')
def pdftoText(f):  
    pdfFile = open(f,'rb')
    reader = p.PdfFileReader(pdfFile)

    text = ''
    for pageNum in range(reader.numPages):
        text = reader.getPage(pageNum).extractText() + text
    return text
# # NLP.extractedText(text)

def doctoText(filename):
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)


