#Import PDF Reader and OS modules
import PyPDF2
import os
#--Parameters--
#Adds dividers and lines to make text more readable
easyparse = False


#Organize String into usable text
def ORGANIZE_TEXT(text):
    #text = text.encode("utf-8")


    
    cleantext = text 
    return cleantext


#Convert the PDF into a text string
def PDF_TO_TEXT(filename):
    print("Converting: "+filename)
    pdfFileObj = open('pdfs/'+filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    total_pages = pdfReader.numPages
    text=""

    for i in range(total_pages):
        page_object = pdfReader.getPage(i)
        text += page_object.extractText()

    return ORGANIZE_TEXT(text)


def WRITE_TEXTFILE(name, location, text):
    #print("Writing "+(location+name))
    file = open("location"+"converted"+".txt","w+", encoding = "utf-8")
    file.write(text);
    file.close()


#Read files in directory, convert, and send to /converted-pdfs
with os.scandir('pdfs/') as entries:
    for entry in entries:
        text = PDF_TO_TEXT(entry.name)
        WRITE_TEXTFILE(entry.name, "./converted-pdfs/", text)





