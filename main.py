from api import get_currencies_online
from api import get_currency_descriptions

current_rates = get_currencies_online()
currency_descriptions = get_currency_descriptions()


def convert(amount_local, from_ticker_local, to_ticker_local, currencies):
    from_currency = currencies.get(from_ticker_local)
    to_currency = currencies.get(to_ticker_local)
    coefficient = to_currency / from_currency
    return round(amount_local * coefficient, 2)


def input_currency(input_message, currencies):
    ticker = input(f"{input_message}: ").strip()
    currency_local = currencies.get(ticker, None)
    while currency_local is None:
        print(f"Валюты {ticker} нет в нашей базе.")
        ticker = input(f"Попробуйте, пожалуйста, еще раз, для выхода из программы введите EXIT: ").strip()
        currency_local = currencies.get(ticker, None)
        if ticker.lower() == 'exit':
            exit()
    return ticker


def get_currency_description(currency_name):
    return currency_descriptions[currency_name]['name']


print("Привет, это программа Конвертер Валют!")

print("""
Для работы с программой требуется:
- выбрать исходную валюту 
- выбрать в какую валюту следует перевести
- ввести количество исходной валюты

Доступные валюты:
""")

for currency in current_rates:
    print(f'- {currency} - {get_currency_description(currency)}')

from_ticker = input_currency("Введите короткое обозначение исходной валюты", current_rates)
to_ticker = input_currency("Введите короткое обозначение валюты, в которую следует перевести", current_rates)

amount_input = input("Введите количество валюты, например, 10 или 1.25: ")
amount = None
while amount is None:
    try:
        amount = int(amount_input)
    except:
        try:
            amount = float(amount_input.replace(',','.'))
        except:
            amount = None
            amount_input = input(f"Попробуйте, пожалуйста, еще раз, для выхода из программы введите EXIT: ")
            if amount_input.lower() == 'exit':
                exit()

result = convert(amount, from_ticker, to_ticker, current_rates)

print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')
