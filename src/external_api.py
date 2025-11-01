import os

import requests
from dotenv import load_dotenv

load_dotenv("/.env")

aip_key = os.getenv("AIP_KEY")


def converting_the_amount_in_rubles(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях."""
    if len(transaction) == 0:
        raise ValueError("No data available for conversion")

    amount = transaction["operationAmount"].get("amount")
    from_currency = transaction["operationAmount"]["currency"].get("code")
    to = "RUB"
    if from_currency == to:
        return float(amount)

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={amount}"
    payload: dict = {}
    headers = {"apikey": f"{aip_key}"}
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 301:
        raise ValueError("Moved Permanently")
    if response.status_code == 400:
        raise ValueError("Bad Request")
    if response.status_code == 401:
        raise ValueError("Unauthorized")
    if response.status_code == 403:
        raise ValueError("Forbidden")
    if response.status_code == 404:
        raise ValueError("Not Found")
    if response.status_code == 500:
        raise ValueError("Internal Server Error")
    if response.status_code != 200:
        raise ValueError("Unknown error contact support")

    return float(response.json().get("result"))
