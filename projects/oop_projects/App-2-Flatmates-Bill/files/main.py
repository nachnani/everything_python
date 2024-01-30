import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object that contains the Bill Data.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains the Flatmate data.
    """

    def __init__(self, name, days_in_house):
        self.name= name
        self.days_in_house = days_in_house

    def pays_bill(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates a PDF containing the data about the flatmates.
    """


    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("house.png",w=30,h=30)

        # Adding Title
        pdf.set_font(family="Times",size=24,style='B')
        pdf.cell(w=0,h=80,txt='Flatmates Bill',border=1, align="C",ln=1)

        # Adding Label and Value
        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=150,h=40,txt="Period:",border=1)
        pdf.cell(w=150,h=40,txt=bill.period,border=1,ln=1)

        # Name and Amount due for 1st Flatmate
        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=150,h=25,txt=flatmate1.name,border=1)
        pdf.cell(w=150,h=25,txt=str(round(flatmate1.pays_bill(bill,flatmate2),2)),border=1,ln=1)

        # Name and Amount due for 2nd Flatmate
        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=150,h=25,txt=flatmate2.name,border=1)
        pdf.cell(w=150, h=25,txt=str(round(flatmate2.pays_bill(bill, flatmate1),2)),border=1,ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


the_bill = Bill(amount=120, period= "March 2021")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print(john.pays_bill(bill=the_bill, flatmate2 = mary))
print(mary.pays_bill(bill=the_bill, flatmate2 = john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate_pdf(flatmate1=john, flatmate2=mary, bill=the_bill)