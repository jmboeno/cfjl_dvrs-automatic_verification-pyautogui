from datetime import datetime
from fpdf import FPDF
import os

pdf = FPDF(orientation='L', unit='mm', format='A4')
pdf.set_auto_page_break(0)
lista = [x for x in os.listdir('images')]


def createPDF():
    print('Criando o PDF!')
    for i in lista:
        pdf.add_page()
        pdf.set_font('helvetica', 'B', 16)
        pdf.cell(0, 10,  i[:-4], 0, 0, 'C')
        pdf.image('resized_images\\' + i, 10, 30, 275)
    pdf.output("CHECK_DVRS_"+datetime.today().strftime('%Y-%m-%d')+".pdf")
