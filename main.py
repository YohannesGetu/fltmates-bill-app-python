from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

bill_amount = float(input("Hey user, enter the bill amount: "))
bill_period = input("What is the bill period? E.g. December 2020: ")

flatmate1_name = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {flatmate1_name} stay in the house during the bill period? "))

flatmate2_name = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {flatmate2_name} stay in the house during the bill period? "))

the_bill = Bill(amount=bill_amount, period=bill_period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"Report_{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
