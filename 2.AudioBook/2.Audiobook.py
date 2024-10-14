# This library is used for text-to-speech conversion.
import pyttsx3
# This library is used for reading PDF files.
import PyPDF2

# Open the PDF file .
with open("SQL.pdf", "rb") as book:  # Replace with your PDF file path and read-binary mode ("rb").

    # Creating a PDF Reader Object
    pdf_reader = PyPDF2.PdfReader(book)

    # initializing the Text-to-Speech Engine.
    speaker = pyttsx3.init()

    # Optional: Set properties like speech rate and volume
    #speaker.setProperty("rate", 150)
    #speaker.setProperty("volume", 0.9)


    # Loop through the PDF pages and read the text aloud
    for page in pdf_reader.pages:

        #Extracting Text from the Current Page
        text = page.extract_text()

        if text:  # Check if there's any text to read

            speaker.say(text)
            speaker.runAndWait()


#install this module:
        #pip install pyttsx3
        #pip install PyPDF2
