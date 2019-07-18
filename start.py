#Import PDF Reader and OS modules
import PyPDF2
import os
print_out=False
#Organize String into usable text
def ORGANIZE_TEXT(text):
    if(print_out):
        print(text.encode("utf-8"))
    
    text_length = len(text)
    #Remove double next lines
    for i in range(text_length-4):
        #If there are two nextlines (/n) next to eachother, remove
        text.replace("/n/n","/n")
        #if(text[i:(i+1)=="/n" and text[i+2:(i+3)=="/n")

        
        text_length = len(text)

    cleantext = text 
    return cleantext


#Convert the PDF into a text string
def PDF_TO_TEXT(filename):
    print("Converting: "+filename)
    pdfFileObj = open('pdfs/'+filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    total_pages = pdfReader.numPages
    text=""

    #Iterate over PDF pages
    for i in range(total_pages):
        page_object = pdfReader.getPage(i)
        text += page_object.extractText()

    #Send converted text to be cleaned and formatted
    return ORGANIZE_TEXT(text)


def WRITE_TEXTFILE(name, location, text):
    #print("Writing "+(location+name))
    file = open(location+name+".txt","w+", encoding = "utf-8")
    file.write(text);
    file.close()


#Read files in directory, convert, and send to /converted-pdfs
with os.scandir('pdfs/') as entries:
    for entry in entries:
        text = PDF_TO_TEXT(entry.name)
        WRITE_TEXTFILE(entry.name, "./converted-pdfs/", text)





