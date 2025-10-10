import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from src.external_api import converting_the_amount_in_rubles

load_dotenv("../.env")

aip_key = os.getenv("AIP_KEY")

headers = {"apikey": f"{aip_key}"}


# Тест когда транзакция указана валюты "USD"
@patch("requests.request")
def test_converting_the_amount_in_rubles_usd(mock_git):
    mock_git.return_value.status_code = 200
    mock_git.return_value.json.return_value = {"result": 6.0}
    assert converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}) == 6.0
    mock_git.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1",
        headers=headers,
        data={},
    )


# Тест когда транзакция указана валюты "EUR"
@patch("requests.request")
def test_converting_the_amount_in_rubles_eur(mock_git):
    mock_git.return_value.status_code = 200
    mock_git.return_value.json.return_value = {"result": 100.0}
    assert converting_the_amount_in_rubles({"operationAmount": {"amount": 10, "currency": {"code": "EUR"}}}) == 100.0
    mock_git.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=10",
        headers=headers,
        data={},
    )


# Тест когда транзакция указана валюты "RUB"
def test_converting_the_amount_in_rubles_rub():
    assert converting_the_amount_in_rubles({"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}) == 100.0


# Тест когда транзакция не содержит данных
def test_converting_the_amount_in_rubles_raise():
    with pytest.raises(ValueError, match="No data available for conversion"):
        converting_the_amount_in_rubles({})


# Тест когда ответ по HTTP запросу выдаёт ошибку 301
def test_converting_the_amount_in_rubles_raise_301():
    mock_get = Mock()
    mock_get.status_code = 301

    with patch("requests.request", return_value=mock_get):
        with pytest.raises(ValueError, match="Moved Permanently"):
            converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})


# Тест когда ответ по HTTP запросу выдаёт ошибку 400
def test_converting_the_amount_in_rubles_raise_400():
    mock_get = Mock()
    mock_get.status_code = 400

    with patch("requests.request", return_value=mock_get):
        with pytest.raises(ValueError, match="Bad Request"):
            converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})


# Тест когда ответ по HTTP запросу выдаёт ошибку 401
def test_converting_the_amount_in_rubles_raise_401():
    mock_get = Mock()
    mock_get.status_code = 401

    with patch("requests.request", return_value=mock_get):
        with pytest.raises(ValueError, match="Unauthorized"):
            converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})


# Тест когда ответ по HTTP запросу выдаёт ошибку 403
def test_converting_the_amount_in_rubles_raise_403():
    mock_get = Mock()
    mock_get.status_code = 403

    with patch("requests.request", return_value=mock_get):
        with pytest.raises(ValueError, match="Forbidden"):
            converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})


# Тест когда ответ по HTTP запросу выдаёт ошибку 404
def test_converting_the_amount_in_rubles_raise_404():
    mock_get = Mock()
    mock_get.status_code = 404

    with patch("requests.request", return_value=mock_get):
        with pytest.raises(ValueError, match="Not Found"):
            converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})


# Тест когда ответ по HTTP запросу выдаёт ошибку 500
def test_converting_the_amount_in_rubles_raise_500():
    mock_get = Mock()
    mock_get.status_code = 500

    with patch("requests.request", return_value=mock_get):
        with pytest.raises(ValueError, match="Internal Server Error"):
            converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})


# Тест когда ответ по HTTP запросу выдаёт ошибку которая не обрабатывается в методе
def test_converting_the_amount_in_rubles_raise_200():
    mock_get = Mock()
    mock_get.status_code != 200

    with patch("requests.request", return_value=mock_get):
        with pytest.raises(ValueError, match="Unknown error contact support"):
            converting_the_amount_in_rubles({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})
