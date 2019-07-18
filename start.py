#Import PDF Reader and OS modules
import PyPDF2
import os

#Parameters
parameters=True; #Enable or disable all parameters. Disable for higher performance and lower accuracy.
enter_condense=True; #Removes erroneous nextlines
period_condense=True; #Uses period to determine next line



#Organize String into usable text
def ORGANIZE_TEXT(text):
    text_length = len(text)
    if(print_out):
        print(text.encode("utf-8"))
   
    
    #Remove double next lines
    for i in range(text_length-4):
        #If there are two nextlines (/n) next to eachother, remove the next one
        if text[i:(i+1)]=="\n" and text[i+2:(i+3)]=="\n":
            text = text[:i+1] + text[i+4:]
        #Adjust length for removed characters
        text_length = len(text)


    #Parameters
    if(parameters):
        for i in range(text_length-4):
            if enter_condense and text[i:(i+2)]==" \n":
            text = text[:i+1] + text[i+4:]



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





