import main

def test_main():
    dmv = main.Queue()
    dmv.push(1)
    dmv.pop()
    assert dmv.cards == []