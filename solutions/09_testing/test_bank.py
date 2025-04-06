import pytest

from bookie.bank import Bank

def test_init_bank():
    bank = Bank(100_000)

    assert bank.balance == 100_000
    assert len(bank.players) == 0

def test_bank_new_player():
    bank = Bank(100_000)
    bank.add_player("John", 1000)

    pl1 = bank.find_player("John")

    assert len(bank.players) == 1
    assert pl1.name == "John"
    assert pl1.balance == 1000

@pytest.mark.xfail()    
def test_bank_remove_player():
    bank = Bank(100_000)
    bank.remove_player("John")
