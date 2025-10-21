import csv
import logging
import pandas as pd

logging.basicConfig(level=logging.ERROR,
                    filemode="w",
                    filename="logs/reading_csv_xlsx.log",
                    format="%(asctime)s - %(funcName)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def from_csv_to_list(file: str) -> list:
    """
    Функция принимает путь к файлу CSV, и выдает список словарей с транзакциями.
    """
    operations = []
    try:
        with open(f'data/{file}', 'r', encoding='UTF-8', newline='') as f:
            read = csv.DictReader(f, delimiter=';')
            for row in read:
                operations.append(row)
    except Exception as ex:
        logger.error(f"{ex}")
        return []
    else:
        return operations


def from_xlsx_to_list(file: str) -> list:
    """
    Функция принимает путь к файлу XLSX, и выдает список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(f'data/{file}',sheet_name='Лист 1')
        operations = df.to_dict(orient='records')
    except Exception as ex:
        logger.error(f"{ex}")
        return []
    else:
        return operations


if __name__ == '__main__':
    path_CSV = 'transactions.csv'
    path_XLSX = 'transactions_excel.xlsx'

    print(from_xlsx_to_list(path_XLSX))
    # print(from_csv_to_list(path_CSV))

