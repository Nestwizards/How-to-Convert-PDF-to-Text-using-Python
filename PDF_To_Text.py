
# This module is imported so that we can 
# convert PDF to Text
import PyPDF2

# This will take pdf file as an input
file_obj = open('sample.pdf','rb')

# pdf_reader will create the object file
pdf_reader = PyPDF2.PdfFileReader(file_obj) 

# total_pages will give the number
# of pages pdf has
total_pages = pdf_reader.numPages 
page_obj = pdf_reader.getPage(total_pages-1)

# text will contain all the pdf data
text = page_obj.extractText() # stores info in text

# This will write data into the file
sample = open(r"(Folder Path)/sample.txt","a")
sample.writelines(text)
sample.close()