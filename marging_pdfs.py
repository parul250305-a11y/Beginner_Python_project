from PyPDF2 import PdfWriter

merge = PdfWriter()

pdfs = []
n = int(input("how many pdf u want to merge \n: "))

for i in  range(0,n):
    name = input(f"enter the mame of the pdfs {i +1} \n: ")
    pdfs.append(name)

for pdf in pdfs :
    merge.append(pdf)

merge.write("merged.pdf")
merge.close() 












































