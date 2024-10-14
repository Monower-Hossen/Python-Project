import pikepdf

# Open the existing PDF
old_pdf = pikepdf.Pdf.open("new_pdf.pdf")

# Rotate each page
for page in old_pdf.pages:
    page.Rotate = 360  # Rotate the page 180 degrees

# Save the modified PDF
old_pdf.save("new.pdf")
old_pdf.close()  # It's a good practice to close the PDF after saving
