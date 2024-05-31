from var6 import get_var6


def test_get_var6_empty():
    lines = []
    actual = get_var6(lines, 'S')
    expected = (0, 0)
    assert actual == expected


def test_get_var6_fare_single_line():
    testline = '1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S'
    actual = get_var6([testline], 'S')
    expected = (7.25, 0)
    assert actual == expected


def test_get_var6_fare_multiple_lines():
    lines = ["1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S",
             "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',female,38,1,0,PC 17599,71.2833,C85,C",
             "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S",
             "4,1,1,'Futrelle, Mrs. Jacques Heath (Lily May Peel)',female,35,1,0,113803,53.1,C123,S"]
    actual = get_var6(lines, 'S')
    expected = (30.5125, 7.25)

    assert actual == expected
