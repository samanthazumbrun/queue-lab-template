import queue

def test_queue():
    dmv = queue.Queue()
    dmv.push(1)
    dmv.pop()
    assert dmv.cards == []