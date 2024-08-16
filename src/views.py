from src.services import normalize_transactions, search_transactions
from src.utils import current_time, greeting, processing_transaction, card_information, fetch_stock_prices, get_currency_rates
from src.reports import get_expenses_by_category
from dotenv import load_dotenv
import os

load_dotenv()
Api_1 = os.getenv("API_KEY_CURRENCY")
Api_2 = os.getenv("api_key_2")


formater = current_time()
greeting_sms = greeting()

symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
Api_2 = "ваш_ключ_здесь"
stock_prices = fetch_stock_prices(symbols, Api_2)

api_key = Api_1
rates = get_currency_rates(api_key)

user_date = "31.12.2021"
category_word = "Супермаркеты"

