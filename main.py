class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatemate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2):
        pass


the_bill = Bill(amount=120, period="March 2021")
jhon = Flatemate(name="Jhon", days_in_house=20)
marry = Flatemate(name="Marry", days_in_house=25)

print(jhon.pays(bill=the_bill))