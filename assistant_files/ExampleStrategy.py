### Example Strategy

import backtrader as bt
from LoggedStrategy import *

# Logged strategy is just a wrapper around bt.Strategy that logs everything

class ExampleStrategy(LoggedStrategy):
    params = (
        ('short_ema_period', 20),
        ('long_ema_period', 250),
    )

    def __init__(self):
        super().__init__()
        self.ema_short = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.short_ema_period)
        self.ema_long = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.long_ema_period)
        self.crossover = bt.indicators.CrossOver(self.ema_short, self.ema_long)

    def next(self):
        if not self.position and self.crossover > 0:
            self.buy()
        elif self.position and self.crossover < 0:
            self.sell()

    @staticmethod
    def get_optimisation_ranges():
        param_ranges = {
            'short_ema_period': range(1, 10, 2),  # Exploring shorter periods for the fast-moving EMA
            'long_ema_period': range(80, 200, 20),  # Longer periods for the slow-moving EMA
        }
        return param_ranges

