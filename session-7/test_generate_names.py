import us_names
from generate_names import generate_names


def test_generate_names_1():
    names = generate_names('female', 10)
    assert len(names) == 10
    for name in names:
        assert type(name) == str
        assert ' ' in name
        prename, surname = name.split(' ')
        assert len(prename) >= 1
        assert len(surname) >= 1
        assert prename in us_names.FEMALE_NAMES
        assert surname in us_names.SURNAMES


def test_generate_names_2():
    names = generate_names('male', 5)
    assert len(names) == 5


def test_generate_names_3():
    names = generate_names('schnippschnapp', 8)
    assert len(names) == 0


def test_generate_names_4():
    names = generate_names(-3, 8)
    assert len(names) == 0


# def test_generate_names_5():
#     names = generate_names('male', 123456789123456789123456789123456789123456789123456789123456789123456789123456789)
#     assert len(names) == 123456789123456789123456789123456789123456789123456789123456789123456789123456789
