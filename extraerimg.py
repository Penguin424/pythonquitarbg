import PyPDF2

reader = PyPDF2.PdfReader('doc4.pdf')



for page in reader.pages:
    count = 0
    
    for image in page.images:
        with open(str(count)+image.name, 'wb') as img:
            img.write(image.data)

    count += 1


