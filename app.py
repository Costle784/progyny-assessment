"""Crypto Interview Assessment Module."""

import os

from dotenv import find_dotenv, load_dotenv

from crypto_api import crypto_api
from errors import CryptoAPIError

load_dotenv(find_dotenv(raise_error_if_not_found=True))


# You can access the environment variables as such, and any variables from the .env file will be loaded in for you to use.
# os.getenv("DB_HOST")

# Start Here
try:
    print(crypto_api.get_coins())
except CryptoAPIError as e:
    print(e)


try:
    print(crypto_api.get_coin_price_history('bitcoin'))
except CryptoAPIError as e:
    print(e)