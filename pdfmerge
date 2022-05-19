from PyPDF2 import PdfFileMerger
import os
# pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf'][:2]
# pdfs = ['pt0.pdf', 'pt1.pdf', 'pt2.pdf', 'pt3.pdf']

path = f'O:\OneDrive\DEUS_ME_DARA_EM_DOBRO\ADMSBC'

files = [os.path.join(path, file)
         for file in os.listdir(path) if file.endswith('pdf')]

files.sort()

input(files)
merger = PdfFileMerger()


# pdfs = [for pdf in pdfs]
pdfs = files

for pdf in pdfs:
    merger.append(pdf)

merger.write(os.path.join(path, "ArquivosJuntos.pdf"))
merger.close()
