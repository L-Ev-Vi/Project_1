from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.reading_csv_and_xlsx import from_csv_to_list, from_xlsx_to_list
from src.utils import from_json_to_list
from src.widget import get_date, mask_account_card


def main() -> None:
    """Функция отвечает за основную логику проекта."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")

    file_number = input("Выберите необходимый пункт меню:\n"
                        "1. Получить информацию о транзакциях из JSON-файла\n"
                        "2. Получить информацию о транзакциях из CSV-файла\n"
                        "3. Получить информацию о транзакциях из XLSX-файла\n"
                        "->")
    if file_number == "1":
        print("Для обработки выбран JSON-файл")
        data = from_json_to_list("operations.json")
    elif file_number == "2":
        print("Для обработки выбран CSV-файл")
        data = from_csv_to_list("transactions.csv")
    elif file_number == "3":
        print("Для обработки выбран XLSX-файл")
        data = from_xlsx_to_list("transactions_excel.xlsx")
    else:
        print("По умолчанию для обработки выбран JSON-файл")
        data = from_json_to_list("operations.json")

    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию\n"
                       "Доступные для фильтровки статусы:\n"
                       "EXECUTED\n"
                       "CANCELED\n"
                       "PENDING\n"
                       "->").upper()
        if status in ["EXECUTED, CANCELED, PENDING"]:
            print(f"Операции отфильтрованы по статусу{status}")
            sorted_data = filter_by_state(data, status)
            break
        else:
            print(f"Статус операции {status} недоступен")

    sort_date = input("Отсортировать операции по дате? Да/Нет\n"
                      "->")
    if sort_date.lower() == "да" or "yes":
        sort_quantity = input("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n"
                              "->")
        if sort_quantity.lower() == "по возрастанию":
            sorted_by_date_data = sort_by_date(sorted_data, False)
        else:
            sorted_by_date_data = sort_by_date(sorted_data)
    else:
        sorted_by_date_data = sorted_data

    ruble_transactions = input("Выводить только рублевые транзакции? Да/Нет\n"
                               "->")
    if ruble_transactions.lower() == "да" or "yes":
        sorted_currency = [operation for operation in sorted_by_date_data if any(
            currency_data == "руб."
            for values in operation.values()
            if type(values) is dict
            for value in values.values()
            if type(value) is dict
            for currency_data in value.values()
        )]
    else:
        sorted_currency = sorted_by_date_data

    sorted_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
                        "->")
    if sorted_word.lower() == "да" or "yes":
        word = input("Введите ключевое слово или описание транзакции\n"
                     "->")
        final_list = process_bank_search(sorted_currency, word)
    else:
        final_list  = sorted_currency

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(final_list)}\n")

    # if len(final_list) == 0:
    #     print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    #
    # else:
    #     result = []
    #     for operation in final_list:
    #         print(f"{get_date(operation["date"])}



if __name__ == '__main__':
    main()
