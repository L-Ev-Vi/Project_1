import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('data, result', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                          ('Счет 73654108430135874305', 'Счет **4305'),
                                          ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                          ('Visa Gold 15684', 'Visa Gold ***84'),
                                          ('MasterCina 6571552397456239821', 'MasterCina 6571 55** **** **** 821')])
def test_mask_account_card_positive(data, result):
    assert mask_account_card(data) == result


def test_mask_account_card_negative():
    with pytest.raises(TypeError) as info:
        mask_account_card()

    assert str(info.value) == "Ошибка ввода"


def test_mask_account_card_negative_name():
    with pytest.raises(AssertionError) as info:
        mask_account_card('7000792289606361')


def test_mask_account_card_negative_number():
    with pytest.raises(AssertionError) as info:
        mask_account_card('Visa Platinum')

    assert str(info.value) == "Не полный ввод данных"


def test_get_date_positive(date_):
    assert get_date(date_) == "11.03.2024"


@pytest.mark.parametrize('date, result', [('2020-11-14 15:43:32.249588', '14.11.2020'),
                                          ('2020-11-14', '14.11.2020'),
                                          ('2020-10-17 09:40:33.614581+02:00', '17.10.2020'),
                                          ('2020.11.14 15:43:32.249588', '14.11.2020'),
                                          ('2020/11/14 15:43:32.249588', '14.11.2020'),
                                          ('Thursday, 17. October 2019 5:10PM', '17.10.2019'),
                                          ('Thu Oct 17 17:10:28 2019', '17.10.2019')
                                          ])
def test_get_date_positive_value(date, result):
    assert get_date(date) == result


def test_get_date_negative():
    with pytest.raises(TypeError) as info:
        get_date(2020 - 11 - 14)

    assert str(info.value) == "Ошибка ввода даты"


def test_get_date_negative_zero():
    with pytest.raises(TypeError) as info:
        get_date()
    assert str(info.value) == "Ошибка ввода даты"
