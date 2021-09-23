from typing import Dict, List

import requests
from errors import CryptoAPIError

class CryptoAPI:
    """Crypto API."""
    # API Documentation - https://www.coingecko.com/en/api#explore-api

    BASE_URL = 'https://api.coingecko.com/api/v3'

    def _request(self, path: str,  params: dict = None, method: str = 'GET'):
        url = f"{self.BASE_URL}/{path}"
        if method == 'GET':
            res = requests.get(url, params=params)

        json_resp = res.json()
        if res.ok:
            return json_resp

        raise CryptoAPIError(f"Crypto API return status code: {res.status_code} - {json_resp.get('error')}")

    def get_coins(self, currency: str='usd', order: str='market_cap_desc', per_page: int=10, page: int=1) -> List[Dict]:
        """This function will fetch coin market data at the current time given a currency and sort order."""
        path = 'coins/markets'
        params = {
            'vs_currency': currency,
            'order': order,
            'per_page':per_page,
            'page':page,
        }
        return self._request(path, params)

    def get_coin_price_history(self, coin_id: str, currency: str='usd', days: int=9, interval: str='daily') -> List[List]:
        path = f'coins/{coin_id}/market_chart'
        params = {
            'vs_currency':currency,
            'days':days,
            'interval':interval
        }
        return self._request(path, params).get('prices')

    # utilize this function when submitting an order
    def submit_order(self, coin_id: str, quantity: int, bid: float):
        """
        Mock function to submit an order to an exchange.
        Assume order went through successfully and the return value is the price the order was filled at.
        """
        return bid

crypto_api = CryptoAPI()