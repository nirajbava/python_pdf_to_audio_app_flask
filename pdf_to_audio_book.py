from logging import exception
from gtts import gTTS 
import PyPDF2
import random

randomnumber = random.randint(1,1000)



def pdf_to_audio(pdf_file_name, page_to_start, page_to_end):

    book = open(pdf_file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pdftext= ''

    for num in range(page_to_start-1, page_to_end):
        pdftext += pdfReader.getPage(num).extractText()
        print(pdftext)


    myobj = gTTS(text=pdftext, lang='en', slow=True, tld="com")
    filepath = "audio"+str(randomnumber)+".mp3"
    myobj.save("D:\\python_pdf_to_audio_app_flask\\static\\audio\\"+ filepath)

    return filepath

  



