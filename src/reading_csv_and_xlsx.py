import csv
import logging

import pandas as pd

logging.basicConfig(
    level=logging.ERROR,
    filemode="w",
    filename="logs/reading_csv_xlsx.log",
    encoding="utf-8",
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
                if row["id"].isdigit():
                    dic = {
                        "id": int(row["id"]),
                        "state": row.get("state"),
                        "date": row.get("date"),
                        "operationAmount": {
                            "amount": str(float(row["amount"])),
                            "currency": {"name": row.get("currency_name"), "code": row.get("currency_code")},
                        },
                        "description": row.get("description"),
                        "to": row.get("to"),
                    }
                    if row.get("from"):
                        dic["from"] = row.get("from")
                        result.append(dic)
                    else:
                        result.append(dic)
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
            dic = {
                "id": int(row["id"]),
                "state": row.get("state"),
                "date": row.get("date"),
                "operationAmount": {
                    "amount": str(float(row["amount"])),
                    "currency": {"name": row.get("currency_name"), "code": row.get("currency_code")},
                },
                "description": row.get("description"),
                "to": row.get("to"),
            }
            if type(row.get("from")) == str:
                dic["from"] = row.get("from")
                result.append(dic)
            else:
                result.append(dic)
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
