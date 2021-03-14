print("[Module] Journal loaded.")

def pay_expense(amount):
    """
        function pays an expence
        :returns amount: the amount to pay
    """
    print("[Journal] Paid R{:,.2f}".format(amount))


def receive_income(amount):
    """
        function receives an income
        :returns amount: the amount to recive
    """
    print("[Journal] Received R{:,.2f}".format(amount))