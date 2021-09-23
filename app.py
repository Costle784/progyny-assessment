"""Crypto Interview Assessment Module."""

from crypto_api import crypto_api
from errors import CryptoAPIError

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(raise_error_if_not_found=True))

from daos import crypto_dao

class CoinTrader:
    def __init__(self):
        pass

    def fetch_top_coins(self):
        try:
            self.top_coins = crypto_api.get_coins(per_page=3)
        except CryptoAPIError as e:
            # TODO - LOG:
            pass
        crypto_dao.insert_many([(c['symbol'], c['name'], c['current_price'], c['market_cap_rank']) for c in self.top_coins])

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