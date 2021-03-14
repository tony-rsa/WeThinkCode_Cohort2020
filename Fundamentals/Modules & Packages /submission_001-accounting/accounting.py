import sys
if len(sys.argv) > 1:
        for each in sys.argv[1:len(sys.argv)]:
            print(each)


import __init__
from user import authentication
from transactions import journal
import banking as reconciliation
# from banking import reconciliation
# from banking.fvb import reconciliation as fvb
# from banking.ubsa import reconciliation as ubsa
# from banking.online import reconciliation as online


if __name__ == "__main__":
    authentication.authenticate_user()
    amount = 100.00
    journal.receive_income(amount)
    journal.pay_expense(amount)
    reconciliation.do_reconciliation()
    # fvb.do_reconciliation()
    # ubsa.do_reconciliation()
    # online.do_reconciliation()

    