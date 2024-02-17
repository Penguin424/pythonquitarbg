from pdf2image import convert_from_path


images = convert_from_path('JLASH_CATÁLOGO 2023 (7)_compressed.pdf', poppler_path=r'/opt/homebrew/Cellar/poppler/24.01.0/bin/')

x = 0

for image in images:
    image.save(f'./JLASH_CATÁLOGO 2023 (7)_compressed/page{x}.jpg', 'JPEG')
    x += 1
