import pyttsx3
import PyPDF2
book = open('C:\\Users\\pc\\Downloads\\audio.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
for num in range(10,pages):
    speaker = pyttsx3.init()
    speaker.setProperty("rate", 100)
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
