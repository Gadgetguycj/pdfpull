#Imports
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import PyPDF2
import os

#SETTINGS
rough_decode = False #Reliable but innaurate results (Reccomend False)

#PARAMETERS - A list of configurable paramaters for cleaning up text
parameters = True #Globally enables or disables parameters
clean_nextline = True #Attempts to catch unnecessary nextlines
clean_compact = True #Makes text more dense and compact

#Cleans up text by applying a series of rulesets
def TEXT_FORMAT(text):
    if(parameters):
        if(clean_nextline):
            text = text.replace("\n\n\n", "\n\n")
        if(clean_compact):
            text = text.replace("\n\n", "\n")
    return text

#Reads from directory and converts a pdf to text
def PDF_TO_TEXT(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    #Read through pages in PDF
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

#Convert the PDF into a text string
def ROUGH_PDF_TO_TEXT(filename):
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    total_pages = pdfReader.numPages
    text=""

    #Iterate over PDF pages
    for i in range(total_pages):
        page_object = pdfReader.getPage(i)
        text += page_object.extractText()

    #Send converted text to be cleaned and formatted
    return TEXT_FORMAT(text)

#Writes to file
def WRITE_TEXTFILE(name, location, text):
    file = open(location+name+".txt","w+", encoding = "utf-8")
    file.write(text)
    file.close()
    print("done.")


#Read files in directory, convert, and send to /converted-pdfs
with os.scandir('pdfs/') as entries:
    for entry in entries:
        print("Converting PDF file: "+entry.name)
        if(not rough_decode):
            text = TEXT_FORMAT(PDF_TO_TEXT("./pdfs/"+entry.name))
        else:
            text = TEXT_FORMAT(ROUGH_PDF_TO_TEXT("./pdfs/"+entry.name))
            
        print("Writing text file: "+entry.name+".txt")
        WRITE_TEXTFILE(entry.name, "./converted-pdfs/", text)