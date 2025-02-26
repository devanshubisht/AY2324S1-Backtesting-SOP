# This file is used for testing 
# from utils import *
from bt import Backtest, Strategy
import pandas as pd

def main():
    data = {
        'Date': ['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04', '2023-09-05'],
        'Open': [150.0, 151.2, 153.5, 152.8, 152.0],
        'High': [152.3, 153.8, 155.0, 154.2, 153.5],
        'Low': [149.5, 150.7, 152.0, 151.5, 151.2],
        'Close': [151.5, 153.0, 154.5, 153.2, 152.8],
        'Volume': [100000, 120000, 95000, 110000, 105000]
    }

    # 1a) Create a DataFrame
    df = pd.DataFrame(data)

    # 1b) Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index("Date")

    # 2) Strategy Creation
    class CrossOver(Strategy):
        n1 = 10
        n2 = 20
        ema_period = 5
        rsi_period = 5
        upper_bound = 55
        lower_bound = 10
        

        def init(self):
            close = self.data.Close
            # self.sma1 = self.I(SMA, close, self.n1)
            # self.sma2 = self.I(SMA, close, self.n2)

        def next(self):
            pass

        
    # 3) Vanilla backtest
    strategy_params = {
        "ema_period": 14,
        "rsi_period": 14,
        "upper_bound": 14,
        "lower_bound": 14,
    }         

    bt = Backtest(df, strategy=CrossOver, cash=100_000)
    
    strategy_params_limit = {
        "ema_period": [5, 200],
        "rsi_period": [5, 200],
        "upper_bound": [55, 90],
        "lower_bound": [10, 45],
    }
    
    result = bt.optimize(strategy_params_limit=strategy_params_limit)
    bt.runWF(iter=1, strategy_params_limit=strategy_params_limit)
    # bt.run(
    #     ema_period=[5, 200],
    #     rsi_period=[5, 200],
    #     upper_bound=[55, 90],
    #     lower_bound=[10, 45],
    # )
    
if __name__ == "__main__":
    main()