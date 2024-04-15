from DataFetcher import DataFetcher, get_pairs
import pandas as pd
from datetime import timedelta, datetime
import backtrader as bt

from backtrader_plotly.plotter import BacktraderPlotly
from backtrader_plotly.scheme import PlotScheme

class CryptoStrategyBacktester:
    def __init__(self, pair, frequency, fees):
        self.pair = pair
        self.frequency = frequency
        self.fees = fees
        self.data_fetcher = DataFetcher()


    def fetch_data(self, start_date, end_date):
        # Assuming start_date and end_date are datetime.date objects
        dataframes = []
        current_date = start_date
        while current_date <= end_date:
            df = self.data_fetcher.get_historical_data(self.pair, self.frequency, current_date)
            dataframes.append(df)
            current_date += timedelta(days=1)
        # Concatenate all dataframes
        full_data = pd.concat(dataframes)
        return full_data

    def backtest_strategy(self, strategy, start_date, end_date, optimize = False, params_ranges = None):
        # Fetch data
        data_df = self.fetch_data(start_date, end_date)
        self.market_perf = round((data_df['Close'][-1] - data_df['Close'][0])/data_df['Close'][0],5)
        self.first_price = data_df['Close'][0]
        # Convert the DataFrame to a Backtrader data feed
        data_bt = bt.feeds.PandasData(dataname=data_df, datetime=-1)

        # Initialize Cerebro engine
        cerebro = bt.Cerebro()
        cerebro.adddata(data_bt)  # Add the data feed

        # add analyser
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="trade_analyzer")
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name="drawdown")
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="sharpe_ratio", riskfreerate=0.03)
        cerebro.addanalyzer(bt.analyzers.Returns, _name="returns")

        cerebro.broker.setcash(self.first_price * 2)  # Set initial cash
        cerebro.broker.setcommission(commission=self.fees)
        if optimize:
            cerebro.optstrategy(strategy, **strategy.get_optimisation_ranges())  # Add the strategy class
            runs = cerebro.run()
        else:
            cerebro.addstrategy(strategy)
            runs = [cerebro.run(stdstats=True, writer=True)]


        # Run the strategy

        # Access the analyzers

        best_strat = None
        best_pnl = -1e12
        for run in runs:
            for first_strategy in run:
                trade_stats = first_strategy.analyzers.trade_analyzer.get_analysis()
                drawdown_stats = first_strategy.analyzers.drawdown.get_analysis()
                sharpe_ratio = first_strategy.analyzers.sharpe_ratio.get_analysis()
                returns_stats = first_strategy.analyzers.returns.get_analysis()
                try:
                    if trade_stats.pnl.net.total > best_pnl:
                        best_strat = first_strategy
                        best_pnl = trade_stats.pnl.net.total
                        best_config = (trade_stats, drawdown_stats, sharpe_ratio, returns_stats, best_strat.params.__dict__)
                except:
                    pass
        # Print the results

        #cerebro.plot()
        if optimize:
            print("BEST PNL", best_strat.params.__dict__, best_pnl)
        else:
            scheme = PlotScheme(decimal_places=5, max_legend_text_width=16)
            fig = cerebro.plot(BacktraderPlotly(show=False, scheme=scheme))
        return fig, round(100 * best_pnl/self.first_price,3) , round(self.market_perf * 100,3)








