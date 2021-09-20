import pyttsx3
import PyPDF2
import pdfplumber

# speaker = pyttsx3.init()
# speaker.say('hello there')
# speaker.runAndWait()

# book = open("Hustle Harder, Hustle Smarter by Curtis Jackson.pdf", "rb")
file = "Hustle Harder, Hustle Smarter by Curtis Jackson.pdf"
pdfFileObj = open(file, 'rb')
pdfReader =PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages

with pdfplumber.open(file) as pdf:
    for i in range(24, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()


# PDFreader = PyPDF2.PdfFileReader(book)
# pages = PDFreader.numPages
# speaker = pyttsx3.init()
# # print(pages)
#
# for num in range(13, pages):
#     page = PDFreader.getPage(num)
#     text = page.extract_text()
#     # speaker = pyttsx3.init()
#     speaker.say(text)
#     speaker.runAndWait()
#
