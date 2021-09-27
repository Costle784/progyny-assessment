#!/usr/bin/env python3

"""Crypto Interview Assessment Module."""
from loggers import error_log, app_log
from crypto_api import crypto_api
from errors import CryptoAPIError, DatabaseError

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(raise_error_if_not_found=True))

from daos import crypto_dao

class CoinTrader:
    """Fetches top crypto coins, stores the results, and makes trades."""

    def fetch_top_coins(self) -> None:
        try:
            self.top_coins = crypto_api.get_coins(per_page=3)
        except CryptoAPIError as e:
            error_log.exception(f"Error fetching to crypto coins: {e}")
            exit()

        try:
            crypto_dao.insert_many([(c['symbol'], c['name'], c['current_price'], c['market_cap_rank']) for c in self.top_coins])
        except DatabaseError as e:
            error_log.exception(e)


    def make_trades(self) -> None:
        for coin in self.top_coins:
            try:
                ten_day_avg = sum([price[1] for price in crypto_api.get_coin_price_history(coin['id'])]) / 10
            except CryptoAPIError as e:
                error_log.exception(f"Error fetching coin price history for {coin['name']}: {e}")
                continue

            if coin['current_price'] < ten_day_avg:
                trade_val = crypto_api.submit_order(coin['id'], 1, coin['current_price'])
                app_log.info(f"Order Completed: {coin['id']} - price: {trade_val} - quantity: 1")

coin_trader = CoinTrader()
coin_trader.fetch_top_coins()
coin_trader.make_trades()
