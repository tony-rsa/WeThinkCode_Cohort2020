print("[Module] online.Reconciliation loaded.")

import requests

def do_reconciliation():
    """
        function dose reconcilation
    """
    print("Doing Online Bank reconciliation.")
    response = requests.get('https://www.wethinkcode.co.za')
    print(response.status_code)
# if you print(response.text) you will see the actual WeThinkCode_ website HTML content
