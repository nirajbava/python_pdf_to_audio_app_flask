from gtts import gTTS 
import PyPDF2
import random



def pdf_to_audio(pdf_file_name, page_to_start, page_to_end):
    # read pdf 
    # # pdf_file_name = raw_input("Enter Your File Name (ex: book.pdf) : ")

    book = open(pdf_file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = int(pdfReader.numPages)

    print(pages)

    # get user input
    # page_to_start = int(input('''
    # # Enter Page Number To play From : '''))

    # page_to_end  = int(input('''
    # Enter page Number To End : '''))


    # make file name
    rand = random.randint(1,1000)
    main_namef = 'audio' +str(rand) + ".mp3"
    file_name = 'D:\\python_pdf_to_audio_app_flask\\static\\audio\\' + main_namef

    language = 'en'
    my_text =""

    # set page number to read 
    for num in range(pages):
        page = pdfReader.getPage(num)
        my_text = page.extractText()

        myobj = gTTS(text=my_text, lang=language, slow=False) 
        myobj.save(file_name) 

    return main_namef



pdf_to_audio('D:\\python_pdf_to_audio_app_flask\\static\\pdf\\eng.pdf', 2, 2)