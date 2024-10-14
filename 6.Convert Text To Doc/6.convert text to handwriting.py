import pywhatkit as pw

# Define the text to be converted into handwriting
txt = """
PyWhatKit is a Python library with various helpful features. It's easy-to-use and does not require you to do 
any additional setup. Currently, it is one of the most popular libraries for WhatsApp and YouTube automation.
New updates are released frequently with new features and bug fixes.
"""

# Convert text to handwriting and save it as "Demo.png"
pw.text_to_handwriting(txt, "Demo.png", rgb=(0, 0, 255))  # RGB sets text color, here it is blue (0, 0, 255)

print("Handwriting image successfully created and saved as 'Demo.png'")
