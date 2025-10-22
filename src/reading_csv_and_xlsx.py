import csv
import logging

import pandas as pd

logging.basicConfig(
    level=logging.ERROR,
    filemode="w",
    filename="logs/reading_csv_xlsx.log",
    format="%(asctime)s - %(funcName)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def from_csv_to_list(file: str) -> list:
    """
    Функция принимает путь к файлу CSV, и выдает список словарей с транзакциями.
    """
    result = []
    try:
        with open(f"data/{file}", "r", encoding="UTF-8", newline="") as f:
            read = csv.DictReader(f, delimiter=";")
            for row in read:
                if row.get("id"):
                    row["id"] = int(row["id"])
                    result.append(row)
    except Exception as ex:
        logger.error(f"{ex}")
        return []
    else:
        return result


def from_xlsx_to_list(file: str) -> list:
    """
    Функция принимает путь к файлу XLSX, и выдает список словарей с транзакциями.
    """
    result = []
    try:
        df = pd.read_excel(f"data/{file}", sheet_name="Лист 1")
        df = df.loc[(df.id.notnull())]
        operations = df.to_dict(orient="records")
        for row in operations:
            row["id"] = int(row["id"])
            row["amount"] = str(float(row["amount"]))
            result.append(row)
    except Exception as ex:
        logger.error(f"{ex}")
        return []
    else:
        return result


# if __name__ == '__main__':
#     path_CSV = 'transactions.csv'
#     path_XLSX = 'transactions_excel.xlsx'
#
#     print(from_xlsx_to_list(path_XLSX))
#     print(from_csv_to_list(path_CSV))
