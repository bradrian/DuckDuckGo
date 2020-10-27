import pytest

from gitremote.presidents import get_presidents


presidents_list = [
    ("Washington", False),
    ("Adams", False),
    ("Jefferson", False),
    ("Madison", False),
    ("Monroe", False),
    ("Jackson", False),
    ("Buren", False),
    ("Harrison", False),
    ("Tyler", False),
    ("Polk", False),
    ("Taylor", False),
    ("Fillmore", False),
    ("Pierce", False),
    ("Buchanan", False),
    ("Lincoln", False),
    ("Johnson", False),
    ("Grant", False),
    ("Hayes", False),
    ("Garfield", False),
    ("Arthur", False),
    ("Cleveland", False),
    ("Harrison", False),
    ("Cleveland", False),
    ("McKinley", False),
    ("Roosevelt", False),
    ("Taft", False),
    ("Wilson", False),
    ("Harding", False),
    ("Coolidge", False),
    ("Hoover", False),
    ("Roosevelt", False),
    ("Truman", False),
    ("Eisenhower", False),
    ("Kennedy", False),
    ("Johnson", False),
    ("Nixon", False),
    ("Ford", False),
    ("Carter", False),
    ("Reagan", False),
    ("Bush", False),
    ("Clinton", False),
    ("Obama", False),
    ("Trump", False)
]

def test_get_presidents():
    original_length = len( presidents_list )
    rsp_data = get_presidents()

    for result in rsp_data:
        for item in ((word[0], word[0] in result["Text"]) for word in presidents_list):
            index = -1
            try:
                index = presidents_list.index((item[0], False))
            except ValueError:
                index = -1

            if item[1] == True and index >= 0:
                presidents_list.pop(index)
                presidents_list.append((item[0], True))

    assert all(word[1] == True for word in presidents_list) and len(presidents_list) == original_length
