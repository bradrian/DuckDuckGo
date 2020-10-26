import pytest

from gitremote.presidents import get_presidents


presidents_list = [
    "Washington",
    "Adams",
    "Jefferson",
    "Madison",
    "Monroe",
    "Jackson",
    "Buren",
    "Harrison",
    "Tyler",
    "Polk",
    "Taylor",
    "Fillmore",
    "Pierce",
    "Buchanan",
    "Lincoln",
    "Johnson",
    "Grant",
    "Hayes",
    "Garfield",
    "Arthur",
    "Cleveland",
    "Harrison",
    "Cleveland",
    "McKinley",
    "Roosevelt",
    "Taft",
    "Wilson",
    "Harding",
    "Coolidge",
    "Hoover",
    "Roosevelt",
    "Truman",
    "Eisenhower",
    "Kennedy",
    "Johnson",
    "Nixon",
    "Ford",
    "Carter",
    "Reagan",
    "Bush",
    "Clinton",
    "Obama",
    "Trump",
]

def test_get_presidents():
    rsp_data = get_presidents()

    for result in rsp_data:
        assert any(word in result["Text"] for word in presidents_list), "Could not find a president in " + result["Text"]


