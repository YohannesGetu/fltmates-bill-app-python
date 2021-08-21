import os
import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount  of the first flatmate1
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount  of the first flatmate2
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open('file://' + os.path.realpath(self.filename))


bill_amount = float(input("Hey user, enter the bill amount: "))
bill_period = input("What is the bill period? E.g. December 2020: ")

flatmate1_name = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {flatmate1_name} stay in the house during the bill period? "))

flatmate2_name = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {flatmate2_name} stay in the house during the bill period? "))

the_bill = Bill(amount=bill_amount, period=bill_period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=days_in_house2)

print(f"{flatmate1_name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2_name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"Report_{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
