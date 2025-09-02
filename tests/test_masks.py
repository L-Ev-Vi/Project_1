import pytest

import tests

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('number_card, result', [(1596837868705199, '1596 83** **** 5199'),
                                                 (7158300734726758, '7158 30** **** 6758'),
                                                 (6571529785965, '6571 **** **965'),
                                                 (65715, '***15'),
                                                 (6571552397456239821, '6571 55** **** **** 821')
                                                 ])
def test_get_mask_card_number_positive(number_card, result):
    assert get_mask_card_number(number_card) == result


def test_get_mask_card_number_negative():
    with pytest.raises(TypeError) as info:
        get_mask_card_number('Card')

    assert str(info.value) == "Указан не верный номер карты"


def test_get_mask_card_number_negative_non():
    with pytest.raises(TypeError) as info:
        get_mask_card_number()

    assert str(info.value) == "Указан не верный номер карты"


@pytest.mark.parametrize('account, result', [(64686473678894779589, '**9589'),
                                             (73654108430135874305, '**4305'),
                                             ])
def test_get_mask_account_positive(account, result):
    assert get_mask_account(account) == result


def test_get_mask_account_negative_non():
    with pytest.raises(TypeError) as info:
        get_mask_account()

    assert str(info.value) == "Не верный ввод"
