import pyttsx3
import PyPDF2
from os import listdir
from os.path import isfile, join

# init speaker
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')[1]  # 0 for english, 1 for french
speaker.setProperty('voice', voices.id)

# test all the voices
# for voice in voices:
#        print(voice, voice.id)
#        speaker.setProperty('voice', voice.id)
#        speaker.say("Hello World!")
#        speaker.runAndWait()
#        speaker.stop()

# init PDF
folderPath = "C:\\Users\\user\\Documents\\PDF\\"  # path of the folder that contains the pdf
filesInFolder = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]  # check folder and adds files to list
pdfFile = folderPath + filesInFolder[1]  # path + file on specific index
print(filesInFolder)

# read pdf
pdf = open(pdfFile, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
nbPages = pdfReader.numPages
startPage = 1
endPage = nbPages  # if you don't want to read all pdf just change the number of endPage

# speak
for pageNumber in range(startPage, endPage):
    currentPage = pdfReader.getPage(pageNumber)
    text = currentPage.extractText()
    print(text)

    speaker.say(text)
    speaker.runAndWait()

