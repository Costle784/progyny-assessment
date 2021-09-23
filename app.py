"""Crypto Interview Assessment Module."""

import os
from typing import Coroutine

from dotenv import find_dotenv, load_dotenv

from crypto_api import crypto_api
from errors import CryptoAPIError

load_dotenv(find_dotenv(raise_error_if_not_found=True))

class CoinTrader:
    def __init__(self):
        pass

    def fetch_top_coins(self):
        try:
            self.top_coins = crypto_api.get_coins(per_page=3)
        except CryptoAPIError as e:
            pass

    def make_trades(self):
        for coin in self.top_coins:
            ten_day_avg = sum([price[1] for price in crypto_api.get_coin_price_history(coin['id'])]) / 10
            if coin['current_price'] < ten_day_avg:
                # TODO - LOG:
                trade_val = crypto_api.submit_order(coin['id'], 1, coin['current_price'])


if __name__ == '__main__':
    coin_trader = CoinTrader()
    coin_trader.fetch_top_coins()
    coin_trader.make_trades()