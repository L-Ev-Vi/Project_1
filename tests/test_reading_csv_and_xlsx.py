import pytest
import unittest
from unittest.mock import mock_open, patch
from src.reading_csv_and_xlsx import from_csv_to_list, from_xlsx_to_list


class TestFrom(unittest.TestCase):

    @patch('builtins_open')
    def test_from_csv_to_list(self, mock_op, data_csv):
        mock_open(mock=mock_op, read_data=data_csv)
        self.assertEqual(from_csv_to_list('file.csv'),
                         [
                             {'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
                              'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                              'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                             {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
                              'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                              'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}
                         ]
                         )
        mock_op.assert_calleb_once_with(f'data/file.csv', 'r', encoding='UTF-8', newline='')
