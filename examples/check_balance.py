from pytrx import Tron
from pytrx.exceptions import AddressNotFound
from pprint import pprint

client = Tron()

def check_balance(address):
    try:
        balance=client.get_account_balance(address)
        return balance
    except AddressNotFound:
        return 'Adress not found..!'


pprint(check_balance('<address>'))
