"""Crypto API."""

from typing import Dict, List

import requests
from errors import CryptoAPIError

# API Documentation - https://www.coingecko.com/en/api#explore-api

class CryptoAPI:
    BASE_URL = 'https://api.coingecko.com/api/v3'

    def _request(self, path: str,  params: dict = None, method: str = 'GET'):
        url = f"{self.BASE_URL}/{path}"
        if method == 'GET':
            res = requests.get(url, params=params)

        json_resp = res.json()
        if res.ok:
            return json_resp

        raise CryptoAPIError(f"Crypto API return status code: {res.status_code} - {json_resp.get('error')}")

    def get_coins(self) -> List[Dict]:
        """This function will get the top 10 coins at the current time, sorted by market cap in desc order."""
        path = 'coins/markets'
        params = {
            'vs_currency':'usd',
            'order':'market_cap_desc',
            'per_page':10,
            'page':1,
            'sparkline': 'false'
        }
        return self._request(path, params)

    def get_coin_price_history(self, coin_id: str) -> List[List]:
        path = f'coins/{coin_id}/market_chart'
        params = {
            'vs_currency':'usd',
            'days':9,
            'interval':'daily'
        }
        return self._request(path, params).get('prices')

    # utilize this function when submitting an order
    def submit_order(coin_id: str, quantity: int, bid: float):
        """
        Mock function to submit an order to an exchange.
        Assume order went through successfully and the return value is the price the order was filled at.
        """
        return bid

crypto_api = CryptoAPI()