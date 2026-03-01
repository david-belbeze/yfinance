# -*- coding: utf-8 -*-

import yfinance as yf
from yfinance.config import YfConfig


YfConfig.debug.hide_exceptions = False

ticker_obj = yf.Ticker('BBOX')

prices = ticker_obj.history(period="max", interval="1d", auto_adjust=True)
