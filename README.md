# quantGPT
### QuantGPT: let chatGPT implements and backtest crypto trading strategy

## How to use

- Clone this repo
- Go into it, and run ```pip install -r requirements.txt```
- Run ```streamlit run Home.py```
- Add your openAI API key and create an assistant. You only need to run this step once (as your API key will be stored in .env), and you can see the created assistant on your openAI dashboard.

## How does it work?

The "frontend" dashboard is built with streamlit. The backend uses Binance public API to fetch data. QuantGPT will create a folder "data_cache" to not retrieve the same data multiple times. 
The backtesting is done using backtrader library. 


## Demo 

https://github.com/pierreia/quantGPT/assets/73743089/3640d6d2-bf12-4a04-87ec-9352cc3cd04c

