from datetime import datetime, timedelta
import hashlib
from binance.client import Client
from pathlib import Path
import pandas as pd

class DataFetcher:
    def __init__(self):
        self.cache_dir = Path('./data_cache')
        self.cache_dir.mkdir(exist_ok=True)  # Create the cache directory if it doesn't exist
        self.client = Client()  # Initialize the Binance client

    def _get_cache_filename(self, pair, frequency, day):
        """
        Generates a filename for the cache based on pair, frequency, and day.
        """
        # Using a readable format for the filename instead of hashing for easier debugging and access
        formatted_day = day.strftime('%Y-%m-%d')
        filename = f"{pair}_{frequency}_{formatted_day}.parquet"
        return self.cache_dir / filename

    def _is_cached(self, filename):
        """
        Checks if the data for a given filename is cached.
        """
        return filename.exists()

    def _read_cache(self, filename):
        """
        Reads data from cache.
        """
        return pd.read_parquet(filename)

    def _write_cache(self, data, filename):
        """
        Writes data to cache.
        """
        data.to_parquet(filename)

    def get_historical_data(self, pair, frequency, day):
        """
        Fetches historical data for a given pair, frequency, and day.
        If data is not cached, fetches from Binance and saves as CSV.
        """
        day = pd.to_datetime(day)
        filename = self._get_cache_filename(pair, frequency, day)
        if self._is_cached(filename):
            print("Fetching from cache...")
            return self._read_cache(filename)

        print("Fetching from Binance...")
        # Binance requires timestamps in milliseconds for start and end times
        start_str = int(day.timestamp() * 1000)
        end_str = int((day + timedelta(days=1)).timestamp() * 1000)
        klines = self.client.get_historical_klines(pair, frequency, start_str, end_str)

        # Convert the list of klines to a DataFrame
        columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
                   'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                   'Taker buy quote asset volume', 'Ignore']
        data = pd.DataFrame(klines, columns=columns)

        float_columns = [ 'Open', 'High', 'Low', 'Close', 'Volume',
                   'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                   'Taker buy quote asset volume', 'Ignore']

        data[float_columns] = data[float_columns].astype(float)
        # Convert timestamps from milliseconds to readable date format
        data['Open time'] = pd.to_datetime(data['Open time'], unit='ms')
        data['Close time'] = pd.to_datetime(data['Close time'], unit='ms')
        data = data.set_index('Close time')
        #assert len(data) == 86401, f"Data contains only {len(data)} rows"
        self._write_cache(data, filename)
        return data



from binance.client import Client

def get_pairs(base, min_volume, max_volume):
    # Initialize the Binance client
    client = Client()

    # Fetch all tickers
    tickers = client.get_ticker()

    # Fetch exchange information for all symbols
    exchange_info = client.get_exchange_info()
    symbols_info = {item['symbol']: item for item in exchange_info['symbols']}

    # Filter USDT pairs with a 24h volume within specified range and collect their decimal precision
    filtered_pairs = {}
    for ticker in tickers:
        symbol = ticker['symbol']
        if symbol.endswith(base) and min_volume < float(ticker['quoteVolume']) < max_volume:
            try:
                # Extract precision data from exchange info
                precision = symbols_info[symbol]['baseAssetPrecision']
                filtered_pairs[symbol] = precision
            except KeyError:
                # Handle the case where the symbol is not found in the exchange_info
                print(f"Info not found for symbol: {symbol}")

    return filtered_pairs
