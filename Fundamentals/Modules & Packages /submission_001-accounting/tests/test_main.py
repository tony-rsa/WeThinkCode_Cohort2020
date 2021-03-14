import unittest
import sys
import subprocess
import importlib
from test_base import captured_output


class MyTestCase(unittest.TestCase):
    def test_step2_module_auth(self):
        import user.authentication
        if 'authentication' in sys.modules or 'user.authentication' in sys.modules:
            self.assertTrue(True, "authentication module loaded")
        else:
            self.fail("authentication module NOT loaded")

    def test_step2_module_auth_output(self):
        with captured_output() as (out, err):
            import user.authentication
            importlib.reload(user.authentication)

        output = out.getvalue().strip()

        self.assertTrue(output.find('[Module] User Authentication loaded.') > -1)

    def test_step3_user_auth(self):
        import user.authentication
        with captured_output() as (out, err):
            user.authentication.authenticate_user()

        output = out.getvalue().strip()
        self.assertEqual('Authenticating User', output)

    def test_step4_module_journal(self):
        import transactions.journal
        if 'journal' in sys.modules or 'transactions.journal' in sys.modules:
            self.assertTrue(True, "journal module loaded")
        else:
            self.fail("journal module NOT loaded")

    def test_step4_module_journal_output(self):
        with captured_output() as (out, err):
            import transactions.journal
            importlib.reload(transactions.journal)

        output = out.getvalue().strip()
        self.assertTrue(output.find('[Module] Journal loaded.') > -1)

    def test_step4_module_journal_use(self):
        import transactions.journal as journal
        with captured_output() as (out, err):
            journal.receive_income(100)
            journal.pay_expense(100)

        output = out.getvalue().strip()
        self.assertEqual('[Journal] Received R100.00\n[Journal] Paid R100.00', output)

    def test_step5_module_banking(self):
        import banking.reconciliation
        if 'banking.reconciliation' in sys.modules:
            self.assertTrue(True, "banking module loaded")
        else:
            self.fail("banking module NOT loaded")

    def test_step5_module_banking_output(self):
        with captured_output() as (out, err):
            import banking.reconciliation
            importlib.reload(banking.reconciliation)

        output = out.getvalue().strip()
        self.assertTrue(output.find('[Module] Reconciliation loaded.') > -1)

    def test_step5_module_banking_recon(self):
        import banking.reconciliation
        with captured_output() as (out, err):
            banking.reconciliation.do_reconciliation()

        output = out.getvalue().strip()
        self.assertEqual('Doing bank reconciliation.', output)

    def test_step5_module_banking_fvb(self):
        import banking.fvb.reconciliation
        if 'banking.fvb.reconciliation' in sys.modules:
            self.assertTrue(True, "banking.fvb module loaded")
        else:
            self.fail("banking.fvb module NOT loaded")

    def test_step5_module_banking_output_fvb(self):
        with captured_output() as (out, err):
            import banking.fvb.reconciliation
            importlib.reload(banking.fvb.reconciliation)

        output = out.getvalue().strip()
        self.assertTrue(output.find('[Module] fvb.Reconciliation loaded.') > -1)

    def test_step5_module_banking_recon_fvb(self):
        import banking.fvb.reconciliation
        with captured_output() as (out, err):
            banking.fvb.reconciliation.do_reconciliation()

        output = out.getvalue().strip()
        self.assertEqual('Doing First Virtual Bank reconciliation.', output)

    def test_step5_module_banking_ubsa(self):
        import banking.ubsa.reconciliation
        if 'banking.ubsa.reconciliation' in sys.modules:
            self.assertTrue(True, "banking.ubsa module loaded")
        else:
            self.fail("banking.ubsa module NOT loaded")

    def test_step5_module_banking_output_ubsa(self):
        with captured_output() as (out, err):
            import banking.ubsa.reconciliation
            importlib.reload(banking.ubsa.reconciliation)

        output = out.getvalue().strip()
        self.assertTrue(output.find('[Module] ubsa.Reconciliation loaded.') > -1)

    def test_step5_module_banking_recon_ubsa(self):
        import banking.ubsa.reconciliation
        with captured_output() as (out, err):
            banking.ubsa.reconciliation.do_reconciliation()

        output = out.getvalue().strip()
        self.assertEqual('Doing Unreal Bank of South Africa reconciliation.', output)

    def test_step6_argv(self):
        out = subprocess.check_output('python3 accounting.py hello world', shell=True)

        output = out.decode("utf-8").strip()
        self.assertTrue(output.find('hello\nworld\n') > -1)

    def test_step7_module_banking_online(self):
        import banking.online.reconciliation
        if 'banking.online.reconciliation' in sys.modules:
            self.assertTrue(True, "banking.online module loaded")
        else:
            self.fail("banking.online module NOT loaded")
        if 'requests' in sys.modules:
            self.assertTrue(True, "requests module loaded")
        else:
            self.fail("requests module NOT loaded")

    def test_step7_module_banking_output_online(self):
        with captured_output() as (out, err):
            import banking.online.reconciliation
            importlib.reload(banking.online.reconciliation)

        output = out.getvalue().strip()
        self.assertTrue(output.find('[Module] online.Reconciliation loaded.') > -1)

    def test_step7_module_banking_recon_online(self):
        import banking.online.reconciliation
        with captured_output() as (out, err):
            banking.online.reconciliation.do_reconciliation()

        output = out.getvalue().strip()
        self.assertEqual('Doing Online Bank reconciliation.\n200', output)

    def test_step9_module_banking_conf(self):
        import banking
        if 'banking.fvb.reconciliation' in sys.modules:
            self.assertTrue(True, "banking.fvb module loaded")
        else:
            self.fail("banking.fvb module NOT loaded")

    def test_step9_app_output(self):
        out = subprocess.check_output('python3 accounting.py', shell=True)

        output = out.decode("utf-8").strip()
        self.assertEqual("""[Package] User package loaded.
[Module] User Authentication loaded.
[Package] Transactions package loaded.
[Module] Journal loaded.
[Package] Banking package loaded.
[Package] Banking.fvb package loaded.
[Module] fvb.Reconciliation loaded.
Authenticating User
[Journal] Received R100.00
[Journal] Paid R100.00
Doing First Virtual Bank reconciliation.""", output)


if __name__ == '__main__':
    unittest.main()
