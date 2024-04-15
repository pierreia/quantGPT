
from LoggedStrategy import *
import backtrader as bt

class GeneratedStrategy(LoggedStrategy):
    params = (
        ('fast', 10),  # period for the fast moving average
        ('slow', 30),  # period for the slow moving average
    )

    def __init__(self):
        # Initialize moving averages using simple moving average (SMA)
        self.sma_fast = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.fast)
        self.sma_slow = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.slow)
        self.crossover = bt.indicators.CrossOver(self.sma_fast, self.sma_slow)

    def next(self):
        # Only check for signals if we are not in the market
        if not self.position:
            if self.crossover > 0:
                self.buy()  # fast crosses above slow
            elif self.crossover < 0:
                self.sell()  # fast crosses below slow
        # If already in the market and the trend reverses, close the position
        elif self.crossover < 0 and self.position.size > 0:
            self.close()  # close long position
        elif self.crossover > 0 and self.position.size < 0:
            self.close()  # close short position

    @staticmethod
    def get_optimisation_range():
        # Return a range of parameters to test in optimisation
        return {
            'fast': range(5, 15),  # test fast moving averages from 5 to 14
            'slow': range(20, 40)  # test slow moving averages from 20 to 39
        }
