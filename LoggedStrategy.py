
### Logged Strategy
import backtrader as bt

class LoggedStrategy(bt.Strategy):

    logs = []

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.data.datetime.date(0)

        print(f'{dt.isoformat()} {txt}')

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Order has been submitted/accepted - nothing to do
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    f'BUY EXECUTED, Price: {order.executed.price}, Cost: {order.executed.value}, Comm: {order.executed.comm}')
                self.logs.append({"Date": self.data.datetime.date(0), "Side": "BUY", "Price":order.executed.price, "Cost": order.executed.value, "Comm": order.executed.comm})
            elif order.issell():
                self.log(
                    f'SELL EXECUTED, Price: {order.executed.price}, Cost: {order.executed.value}, Comm: {order.executed.comm}')
                self.logs.append({"Date": self.data.datetime.date(0), "Side": "SELL", "Price": order.executed.price,
                                  "Cost": order.executed.value, "Comm": order.executed.comm})
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log(f'OPERATION PROFIT, GROSS {trade.pnl}, NET {trade.pnlcomm}')

    def __next__(self):
        pass

