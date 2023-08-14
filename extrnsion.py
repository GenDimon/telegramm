import requests

class APIExeprion(ValueError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"APIExeprion: {self.message}"



class Parse:
    @staticmethod
    def get_all_val():
        url = f"https://api.exchangerate-api.com/v4/latest/EUR"
        return f'{list(requests.get(url).json()["rates"].keys())}'.strip('[').strip(']').replace("'", '')
    @staticmethod
    def get_prise(base, quote, amount=1):
        if float(amount) < 1:
            return APIExeprion('Число валюты не может быть меньше единицы')
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{base}"
            response = requests.get(url).json()
            data = response["rates"]
        except KeyError:
            return APIExeprion(f'Валюта {base} не найдена')

        try:
            ansver = data[quote]
        except KeyError:
            return APIExeprion(f'Валюта {quote} не найдена')

        return f'{ansver * float(amount)} {quote}'

