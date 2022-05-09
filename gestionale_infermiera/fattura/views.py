from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

from gestionale_infermiera.settings import PDF_ROOT
from .models import Fattura
from .models import TariffaFatt
# Create your views here.
width, height = A4


class ControllerFattura():
    
    def generatePDF(request, id):
        fattura = Fattura.objects.get(pk=id)
        tariffe=TariffaFatt.objects.all()
        


        #buffer = io.BytesIO()
        c = canvas.Canvas(PDF_ROOT + 'fattura.pdf')
        c.translate(inch/1.75,inch*1.3)
    # define a large font
        c.setFont("Helvetica", 10)
    # choose some colors
        c.setStrokeColorRGB(0,0,0)
        c.setFillColorRGB(0,0,0) # font colour

        #c.drawImage(0.01*inch, 8.7*inch, width=50, height=50)

        intestazione = c.beginText(3.2*inch,9.2*inch)
        intestazione.textLine('Nome Cognome')
        intestazione.textLine('Via NomeVia, 1 - 00000 Macerata (MC)')
        intestazione.textLine('Codice Fiscale: CCCNNN00A00A000A - P.IVA: 12345678910')
        intestazione.textLine('Telefono: +39 3331112211')
        c.drawText(intestazione)

        c.line(0*inch,8.5*inch,7.1*inch,8.5*inch) #(x1,y1,x2,y2)

        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,8.2*inch, 'Destinatario:')
        c.setFont("Helvetica", 10)
        destinatario = c.beginText(1.1*inch,8.2*inch)
        destinatario.textLine(str(fattura.nome))
        destinatario.textLine('Via NomeVia, 1 - 00000 Macerata (MC)')
        destinatario.textLine('Italia')
        destinatario.textLine('P.IVA: 12345678910')
        c.drawText(destinatario)

        c.setFont("Helvetica-Bold", 10)
        dati = c.beginText(4.5*inch,8.2*inch)
        dati.textLine('Fattura:')
        dati.textLine('Tipo di documento: ')
        dati.textLine('Data Fattura: ')
        dati.textLine('Data di scadenza: ')
        c.drawText(dati)

        c.setFont("Helvetica", 10)
        dati1 = c.beginText(6*inch,8.2*inch)
        dati1.textLine('00')
        dati1.textLine('00')
        dati1.textLine('gg/mm/aaaa')
        dati1.textLine('gg/mm/aaaa')
        c.drawText(dati1)

        c.line(0*inch,7.62*inch,7.1*inch,7.62*inch) #(x1,y1,x2,y2)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,7.48*inch, 'Descrizione pagamento:')
        c.drawString(4*inch,7.48*inch, 'Banca d\'appoggio:')
        c.setFont("Helvetica", 10)
        c.drawString(1.7*inch,7.48*inch, 'pagamento')
        c.drawString(5.3*inch+2,7.48*inch, 'banca')
        c.line(0*inch,7.42*inch,7.1*inch,7.42*inch) #(x1,y1,x2,y2)

        c.setFillColorRGB(0,0,0) # font colour
        c.setFont("Helvetica-Bold", 12)
        c.drawString(0.2*inch,7.2*inch,'Descrizione')
        c.line(0*inch,7.15*inch,7.1*inch,7.15*inch)
        #c.drawCentredString(3.8*inch,7.2*inch,'Quantita',mode=None)
        c.drawCentredString(4.5*inch,7.2*inch,'Quantita',mode=None)
        c.drawCentredString(5.2*inch,7.2*inch,'Prezzo',mode=None)
        c.drawCentredString(5.9*inch,7.2*inch,'IVA',mode=None)
        c.drawCentredString(6.6*inch,7.2*inch,'Importo',mode=None)
        

        c.setFillColorRGB(0,0,0) # font colour
        c.setFont("Helvetica", 11)
        row_gap=0.4 # gap between each row
        line_y=6.9 # location of fist Y position 
        total=0
        for tariffa in tariffe:
            if tariffa.fatt.pk == fattura.pk:
                c.drawString(0.2*inch,line_y*inch,str(tariffa.descrizione_prod)) # p Name
                c.drawCentredString(4.5*inch,line_y*inch,str(tariffa.quantita)) # p Qunt 
                c.drawCentredString(5.2*inch,line_y*inch,str(tariffa.prezzo)) # p Price
                c.drawCentredString(5.9*inch,line_y*inch,('0%')) # p IVA
                sub_total=tariffa.prezzo*tariffa.quantita
                c.drawCentredString(6.6*inch,line_y*inch,str(sub_total)) # Sub Total 
                total=round(total+sub_total,2)
                line_y=line_y-row_gap

        c.line(0.01*inch,line_y*inch,7*inch,line_y*inch)# horizontal line total
        row_gap=0.2
        linea_impon=line_y-row_gap
        c.drawRightString(5.2*inch,linea_impon*inch,'Imponibile')
        c.drawRightString(7*inch,linea_impon*inch,str(float(total))) # Total 
        contributi=round(0.04 * total,2)
        linea_contr=linea_impon-row_gap
        c.drawRightString(5.2*inch,linea_contr*inch,'Contributi (INPS) 4%') 
        c.drawRightString(7*inch,linea_contr*inch,str(contributi)) # contributi
        iva=round(0 * total+contributi,2)
        linea_iva=linea_contr-row_gap
        c.drawRightString(5.2*inch,linea_iva*inch,' IVA 0% '+'di ' +str(total+contributi)+ ' (art.10 n.18 DPR 633/1972)') # tax 
        c.drawRightString(7*inch,linea_iva*inch,str(iva)) # iva 
        linea_tot=linea_iva-row_gap
        total_final=round(total+contributi+iva,2)
        c.setFont("Helvetica-Bold", 11)
        c.drawRightString(5.2*inch,linea_tot*inch,'Totale EUR') 
        c.drawRightString(7*inch,linea_tot*inch,str(total_final)) 
        linea_bollo=linea_tot-1.2*row_gap
        c.setFont("Helvetica", 11)
        c.drawRightString(5.2*inch,linea_bollo*inch,'Fattura soggetta a bollo') 
        c.drawRightString(7*inch,linea_bollo*inch,'2.00')
        linea=linea_bollo-0.1
        c.line(3.5*inch,linea*inch,7*inch,linea*inch)
        linea_pag=linea-row_gap
        c.setFont("Helvetica-Bold", 11)
        c.drawRightString(5.2*inch,linea_pag*inch,'Da Pagare: (EUR)') 
        c.drawRightString(7*inch,linea_pag*inch,str(total_final))

        linea_tc=linea_pag-3*row_gap
        c.drawString(0.1*inch,linea_tc*inch,'Termini e Condizioni')
        c.setFont("Helvetica", 11)
        c.drawString(0.1*inch,(linea_tc-row_gap)*inch,'Operazione esente IVA articolo 10, n.18, D.P.R. n.633/1972.')
        c.drawString(0.1*inch,(linea_tc-2*row_gap)*inch,'Imposta di bollo da 2 euro assolta sull\'originale per importi maggiori di 77.47 euro.')
        c.showPage()
        c.save()
        #buffer.seek(0)
        #return FileResponse(buffer, as_attachment=True, filename='fattura'+str(id)+'.pdf')