import streamlit as st
from runLLM import get_strategy, write_strategy
from BacktesterStreamlit import CryptoStrategyBacktester
import pandas as pd
from assistant_files.GeneratedStrategy import GeneratedStrategy

st.title('Backtester: choose your pair and your backtest period')
pair = st.text_input('Choose your pair')
start_date = st.date_input("From date")
end_date = st.date_input("To date")
fee = st.select_slider(label="Fee (%)", options=[0, 0.08, 0.1, 0.2, 0.3])
frequency = st.radio(label="Period", options=["1m", "1h"])


st.write("Choose your strategy params")
params = GeneratedStrategy.get_optimisation_range()
st.write('Adjust a param')
param = st.selectbox("params", options=list(params.keys()))

if param:
    GeneratedStrategy.params.param = st.select_slider(label=param,
                                                      options=GeneratedStrategy.get_optimisation_range()[param])

if st.button('Backtest Strategy'):
    st.write('Getting data from Binance and backtesting...')
    from assistant_files.GeneratedStrategy import GeneratedStrategy

    backtester = CryptoStrategyBacktester(pair, frequency, fee)
    res = backtester.backtest_strategy(GeneratedStrategy, start_date, end_date)
    st.write("Strat PNL (%):", res[1])
    st.write("Hold PNL (%):",res[2])
    st.plotly_chart(res[0][0][0])
    st.dataframe(pd.DataFrame(GeneratedStrategy.logs))