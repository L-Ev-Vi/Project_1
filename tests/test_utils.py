import json
import unittest
from unittest.mock import mock_open, patch

from src.utils import from_json_to_list


# Тест когда указанного файла не существует
def test_from_json_to_list_not_file():
    assert from_json_to_list("file") == []


class TestFrom(unittest.TestCase):

    # Тест когда указанный файл существует
    @patch("builtins.open")
    def test_from_json_to_list_one(self, mock_opens):
        read_data = json.dumps(
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ]
        )

        mock_open(mock=mock_opens, read_data=read_data)
        self.assertEqual(
            from_json_to_list("file.json"),
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        )
        mock_opens.assert_called_once_with("../data/file.json", "r", encoding="UTF-8")

    # Тест когда указанного файла не содержит элемент массив (list)
    @patch("builtins.open")
    def test_from_json_to_list_not_value(self, mock_opens):
        read_data = json.dumps(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        )

        mock_open(mock=mock_opens, read_data=read_data)
        self.assertEqual(from_json_to_list("file.json"), [])
        mock_opens.assert_called_once_with("../data/file.json", "r", encoding="UTF-8")

    # Тест когда указанного файла содержит пустой массив (list)
    @patch("builtins.open")
    def test_from_json_to_list_empty(self, mock_opens):
        read_data = json.dumps([])

        mock_open(mock=mock_opens, read_data=read_data)
        self.assertEqual(from_json_to_list("file.json"), [])
        mock_opens.assert_called_once_with("../data/file.json", "r", encoding="UTF-8")

    # Тест когда не возможно декодировать json-данные
    @patch("builtins.open")
    def test_from_json_to_list_json_decode_error(self, mock_opens):
        read_data = (
            "{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', "
            "'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, "
            "'description': 'Перевод организации', 'from ': 'Счет 75106830613657916952', "
            "'to': 'Счет 11776614605963066702',}"
        )

        mock_open(mock=mock_opens, read_data=read_data)
        self.assertEqual(from_json_to_list("file.json"), [])
        mock_opens.assert_called_once_with("../data/file.json", "r", encoding="UTF-8")
