import logging


from binance import BinanceClient
from bitmex import BitmexClient

from root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83",
                            "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9",
                            testnet=True, futures=True)
    # binance = BinanceClient("XCOoFTkohJY0epzITt3nUuY7bCEGDQpLVW9Jkt7lgfmuULE0yXNqLzSWkSVm1c4o",
    #                         "ZJ4HSgKyjI2rqEK2UVVQtY5WvMsl2z5myU1xxeUBwGQOwa4daVb0p9l9y3u3R1zL",
    #                         testnet=True, futures=True)


    bitmex = BitmexClient("lUGxv_ROqlMw02UQAiv2C-AN","oXBqscuFlDbMzoTBqfdrk88iZD5MdzACjexvK7ON33v4uEn4", testnet=True)

    root = Root(binance,bitmex)
    root.mainloop()
