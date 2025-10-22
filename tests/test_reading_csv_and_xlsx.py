from unittest.mock import mock_open, patch

import pandas as pd

from src.reading_csv_and_xlsx import from_csv_to_list, from_xlsx_to_list


def test_from_csv_to_list_error():
    assert from_csv_to_list("file.csv") == []


def test_from_xlsx_to_list_error():
    assert from_xlsx_to_list("file.xlsx") == []


@patch("builtins.open")
def test_from_csv_to_list(mock_op, data_csv):
    read_data = data_csv
    mock_open(mock=mock_op, read_data=read_data)
    assert from_csv_to_list("file.csv") == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_op.assert_called_once_with("data/file.csv", "r", encoding="UTF-8", newline="")


@patch("pandas.read_excel")
def test_from_xlsx_to_list(mock_df, data_xlsx):
    mock_df.return_value = pd.DataFrame(data_xlsx)
    assert from_xlsx_to_list("file.xlsx") == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210.0",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_df.assert_called_once_with("data/file.xlsx", sheet_name="Лист 1")
