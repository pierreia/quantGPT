         Indicators - Reference - Backtrader    :root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}  \_\_md\_scope=new URL("../..",location),\_\_md\_hash=e=>\[...e\].reduce((e,\_)=>(e<<5)-e+\_.charCodeAt(0),0),\_\_md\_get=(e,\_=localStorage,t=\_\_md\_scope)=>JSON.parse(\_.getItem(t.pathname+"."+e)),\_\_md\_set=(e,\_,t=localStorage,a=\_\_md\_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(\_))}catch(e){}}             (adsbygoogle = window.adsbygoogle || \[\]).push({ google\_ad\_client: "ca-pub-2694577446631179", enable\_page\_level\_ads: true });  html.glightbox-open { overflow: initial; height: 100%; } .gslide-title { margin-top: 0px; user-select: text; } .gslide-desc { color: #666; user-select: text; } .gslide-image img { background: white; } .gscrollbar-fixer { padding-right: 15px; } .gdesc-inner { font-size: 0.75rem; } body\[data-md-color-scheme="slate"\] .gdesc-inner { background: var(--md-default-bg-color);} body\[data-md-color-scheme="slate"\] .gslide-title { color: var(--md-default-fg-color);} body\[data-md-color-scheme="slate"\] .gslide-desc { color: var(--md-default-fg-color);}  

[Skip to content](#indicator-reference)

[![logo](../../images/logo.png)](../.. "Backtrader")

Backtrader

Indicators - Reference

[

DRo

](https://www.linkedin.com/in/daniel-rodriguez-66a6047/ "linkedin")

[

backtrader

](https://github.com/backtrader/backtrader "Go to repository")

[](javascript:void(0) "Share")

Initializing search

*   [Home](../..)
*   [Documentation](../)
*   [Articles](../../blog/)
*   [Recipes/Resources](../../recipes/intro/)

 [![logo](../../images/logo.png)](../.. "Backtrader")Backtrader

[

DRo

](https://www.linkedin.com/in/daniel-rodriguez-66a6047/ "linkedin")

[

backtrader

](https://github.com/backtrader/backtrader "Go to repository")

*    Home
    
    Home
    
    *   [Welcome](../..)
    *   [Features](../../home/features/)
    *   [Hello Algotrading!](../../home/helloalgotrading/)
    *    References
        
        References
        
        *   [Who is using it](../../home/references/who-is-using-it/)
        *   [LinkedIn - Profiles](../../home/references/linkedin/)
        *   [Education - Papers](../../home/references/education/)
        *   [Blogs - Articles](../../home/references/blogs/)
        *   [Videos](../../home/references/videos/)
        *   [Reviews - Mentions](../../home/references/reviews/)
        *   [Job Offers](../../home/references/jobs/)
        *   [Companies](../../home/references/companies/)
        
    
*    Documentation
    
    Documentation
    
    *   [Introduction](../)
    *   [Installation](../installation/)
    *   [Quickstart Guide](../quickstart/quickstart/)
    *    Concepts
        
        Concepts
        
        *   [Platform Concepts](../concepts/)
        *   [Operating the Platform](../operating/)
        
    *    Cerebro
        
        Cerebro
        
        *   [Cerebro](../cerebro/)
        *   [Cerebro - Memory Savings](../memory-savings/memory-savings/)
        *   [Cerebro - Optimization - Improvements](../optimization-improvements/)
        *   [Cerebro - Exceptions](../exceptions/)
        *   [Logging - Writer](../writer/)
        
    *    Data Feeds
        
        Data Feeds
        
        *   [Data Feeds](../datafeed/)
        *   [Data Feeds - Extending](../extending-a-datafeed/)
        *   [Data Feeds - Development - CSV](../datafeed-develop-csv/)
        *   [Data Feeds - Development - General](../datafeed-develop-general/datafeed-develop-general/)
        *   [Data Feeds - Multiple Timeframes](../data-multitimeframe/data-multitimeframe/)
        *   [Data Feeds - Resample](../data-resampling/data-resampling/)
        *   [Data Feeds - Replay](../data-replay/data-replay/)
        *   [Data Feeds - Rollover](../data-rollover/rolling-futures-over/)
        *    Data Feeds - Filters
            
            Data Feeds - Filters
            
            *   [Filters](../filters/)
            *   [Filters - Reference](../filters-reference/)
            
        *   [Data Feeds - Yahoo](../datayahoo/)
        *   [Data Feeds - Panda](../pandas-datafeed/pandas-datafeed/)
        *   [Data Feeds - Reference](../dataautoref/)
        
    *    Strategy
        
        Strategy
        
        *   [Strategy](../strategy/)
        *   [Strategy - Signals](../signal_strategy/signal_strategy/)
        *   [Strategy - Reference](../strategy-reference/)
        
    *    Indicators
        
        Indicators
        
        *   [Indicators - Usage](../induse/)
        *   [Indicators - Development](../inddev/)
        *   [Indicators - Timeframe Mixing](../mixing-timeframes/indicators-mixing-timeframes/)
        *    Indicators - Reference [Indicators - Reference](./)
            
            Table of contents
            
            *   [AccelerationDecelerationOscillator](#accelerationdecelerationoscillator)
            *   [Accum](#accum)
            *   [AdaptiveMovingAverage](#adaptivemovingaverage)
            *   [AdaptiveMovingAverageEnvelope](#adaptivemovingaverageenvelope)
            *   [AdaptiveMovingAverageOscillator](#adaptivemovingaverageoscillator)
            *   [AllN](#alln)
            *   [AnyN](#anyn)
            *   [ApplyN](#applyn)
            *   [AroonDown](#aroondown)
            *   [AroonOscillator](#aroonoscillator)
            *   [AroonUp](#aroonup)
            *   [AroonUpDown](#aroonupdown)
            *   [AroonUpDownOscillator](#aroonupdownoscillator)
            *   [Average](#average)
            *   [AverageDirectionalMovementIndex](#averagedirectionalmovementindex)
            *   [AverageDirectionalMovementIndexRating](#averagedirectionalmovementindexrating)
            *   [AverageTrueRange](#averagetruerange)
            *   [AwesomeOscillator](#awesomeoscillator)
            *   [BaseApplyN](#baseapplyn)
            *   [BollingerBands](#bollingerbands)
            *   [BollingerBandsPct](#bollingerbandspct)
            *   [CointN](#cointn)
            *   [CommodityChannelIndex](#commoditychannelindex)
            *   [CrossDown](#crossdown)
            *   [CrossOver](#crossover)
            *   [CrossUp](#crossup)
            *   [DV2](#dv2)
            *   [DemarkPivotPoint](#demarkpivotpoint)
            *   [DetrendedPriceOscillator](#detrendedpriceoscillator)
            *   [DicksonMovingAverage](#dicksonmovingaverage)
            *   [DicksonMovingAverageEnvelope](#dicksonmovingaverageenvelope)
            *   [DicksonMovingAverageOscillator](#dicksonmovingaverageoscillator)
            *   [DirectionalIndicator](#directionalindicator)
            *   [DirectionalMovement](#directionalmovement)
            *   [DirectionalMovementIndex](#directionalmovementindex)
            *   [DoubleExponentialMovingAverage](#doubleexponentialmovingaverage)
            *   [DoubleExponentialMovingAverageEnvelope](#doubleexponentialmovingaverageenvelope)
            *   [DoubleExponentialMovingAverageOscillator](#doubleexponentialmovingaverageoscillator)
            *   [DownDay](#downday)
            *   [DownDayBool](#downdaybool)
            *   [DownMove](#downmove)
            *   [Envelope](#envelope)
            *   [ExponentialMovingAverage](#exponentialmovingaverage)
            *   [ExponentialMovingAverageEnvelope](#exponentialmovingaverageenvelope)
            *   [ExponentialMovingAverageOscillator](#exponentialmovingaverageoscillator)
            *   [ExponentialSmoothing](#exponentialsmoothing)
            *   [ExponentialSmoothingDynamic](#exponentialsmoothingdynamic)
            *   [FibonacciPivotPoint](#fibonaccipivotpoint)
            *   [FindFirstIndex](#findfirstindex)
            *   [FindFirstIndexHighest](#findfirstindexhighest)
            *   [FindFirstIndexLowest](#findfirstindexlowest)
            *   [FindLastIndex](#findlastindex)
            *   [FindLastIndexHighest](#findlastindexhighest)
            *   [FindLastIndexLowest](#findlastindexlowest)
            *   [Fractal](#fractal)
            *   [HeikinAshi](#heikinashi)
            *   [Highest](#highest)
            *   [HullMovingAverage](#hullmovingaverage)
            *   [HullMovingAverageEnvelope](#hullmovingaverageenvelope)
            *   [HullMovingAverageOscillator](#hullmovingaverageoscillator)
            *   [HurstExponent](#hurstexponent)
            *   [Ichimoku](#ichimoku)
            *   [KnowSureThing](#knowsurething)
            *   [LaguerreFilter](#laguerrefilter)
            *   [LaguerreRSI](#laguerrersi)
            *   [LinePlotterIndicator](#lineplotterindicator)
            *   [Lowest](#lowest)
            *   [MACD](#macd)
            *   [MACDHisto](#macdhisto)
            *   [MeanDeviation](#meandeviation)
            *   [MinusDirectionalIndicator](#minusdirectionalindicator)
            *   [Momentum](#momentum)
            *   [MomentumOscillator](#momentumoscillator)
            *   [MovingAverageBase](#movingaveragebase)
            *   [MovingAverageSimple](#movingaveragesimple)
            *   [MovingAverageSimpleEnvelope](#movingaveragesimpleenvelope)
            *   [MovingAverageSimpleOscillator](#movingaveragesimpleoscillator)
            *   [NonZeroDifference](#nonzerodifference)
            *   [OLS\_BetaN](#ols_betan)
            *   [OLS\_Slope\_InterceptN](#ols_slope_interceptn)
            *   [OLS\_TransformationN](#ols_transformationn)
            *   [OperationN](#operationn)
            *   [Oscillator](#oscillator)
            *   [OscillatorMixIn](#oscillatormixin)
            *   [ParabolicSAR](#parabolicsar)
            *   [PercentChange](#percentchange)
            *   [PercentRank](#percentrank)
            *   [PercentagePriceOscillator](#percentagepriceoscillator)
            *   [PercentagePriceOscillatorShort](#percentagepriceoscillatorshort)
            *   [PeriodN](#periodn)
            *   [PivotPoint](#pivotpoint)
            *   [PlusDirectionalIndicator](#plusdirectionalindicator)
            *   [PrettyGoodOscillator](#prettygoodoscillator)
            *   [PriceOscillator](#priceoscillator)
            *   [RSI\_EMA](#rsi_ema)
            *   [RSI\_SMA](#rsi_sma)
            *   [RSI\_Safe](#rsi_safe)
            *   [RateOfChange](#rateofchange)
            *   [RateOfChange100](#rateofchange100)
            *   [ReduceN](#reducen)
            *   [RelativeMomentumIndex](#relativemomentumindex)
            *   [RelativeStrengthIndex](#relativestrengthindex)
            *   [Signal](#signal)
            *   [SmoothedMovingAverage](#smoothedmovingaverage)
            *   [SmoothedMovingAverageEnvelope](#smoothedmovingaverageenvelope)
            *   [SmoothedMovingAverageOscillator](#smoothedmovingaverageoscillator)
            *   [StandardDeviation](#standarddeviation)
            *   [Stochastic](#stochastic)
            *   [StochasticFast](#stochasticfast)
            *   [StochasticFull](#stochasticfull)
            *   [SumN](#sumn)
            *   [TripleExponentialMovingAverage](#tripleexponentialmovingaverage)
            *   [TripleExponentialMovingAverageEnvelope](#tripleexponentialmovingaverageenvelope)
            *   [TripleExponentialMovingAverageOscillator](#tripleexponentialmovingaverageoscillator)
            *   [Trix](#trix)
            *   [TrixSignal](#trixsignal)
            *   [TrueHigh](#truehigh)
            *   [TrueLow](#truelow)
            *   [TrueRange](#truerange)
            *   [TrueStrengthIndicator](#truestrengthindicator)
            *   [UltimateOscillator](#ultimateoscillator)
            *   [UpDay](#upday)
            *   [UpDayBool](#updaybool)
            *   [UpMove](#upmove)
            *   [Vortex](#vortex)
            *   [WeightedAverage](#weightedaverage)
            *   [WeightedMovingAverage](#weightedmovingaverage)
            *   [WeightedMovingAverageEnvelope](#weightedmovingaverageenvelope)
            *   [WeightedMovingAverageOscillator](#weightedmovingaverageoscillator)
            *   [WilliamsAD](#williamsad)
            *   [WilliamsR](#williamsr)
            *   [ZeroLagExponentialMovingAverage](#zerolagexponentialmovingaverage)
            *   [ZeroLagExponentialMovingAverageEnvelope](#zerolagexponentialmovingaverageenvelope)
            *   [ZeroLagExponentialMovingAverageOscillator](#zerolagexponentialmovingaverageoscillator)
            *   [ZeroLagIndicator](#zerolagindicator)
            *   [ZeroLagIndicatorEnvelope](#zerolagindicatorenvelope)
            *   [ZeroLagIndicatorOscillator](#zerolagindicatoroscillator)
            *   [haDelta](#hadelta)
            
        *   [Indicators - ta-lib](../talib/talib/)
        *   [Indicators - ta-lib - Reference](../talibindautoref/)
        
    *    Orders
        
        Orders
        
        *   [Orders - General](../order/)
        *   [Orders - Creation/Execution](../order-creation-execution/order-creation-execution/)
        *   [Orders - Target Orders](../order_target/order_target/)
        *   [Orders - OCO](../order-creation-execution/oco/oco/)
        *   [Orders - Brackets](../order-creation-execution/bracket/bracket/)
        *   [Orders - Future-Spot Compensation](../order-creation-execution/futurespot/future-vs-spot/)
        *   [Orders - StopTrail](../order-creation-execution/trail/stoptrail/)
        
    *    Broker
        
        Broker
        
        *   [Broker](../broker/)
        *   [Broker - Slippage](../slippage/slippage/)
        *   [Broker - Cheat-On-Open](../cerebro/cheat-on-open/cheat-on-open/)
        *   [Broker - Volume Filling - Fillers](../filler/)
        *   [Position](../position/)
        *   [Trade](../trade/)
        
    *    Commission Schemes
        
        Commission Schemes
        
        *   [Commission Schemes](../commission-schemes/commission-schemes/)
        *   [Commission Schemes - Extending](../extending-commissions/commission-schemes-extended/)
        *   [Commission Schemes - Custom Schemes](../user-defined-commissions/commission-schemes-subclassing/)
        *   [Commission Schemes - Credit Interest](../commission-credit/)
        
    *    Analyzers
        
        Analyzers
        
        *   [Analyzers](../analyzers/analyzers/)
        *   [Analyzers - PyFolio](../analyzers/pyfolio/)
        *   [Analyzers - PyFolio - Integration](../analyzers/pyfolio-integration/pyfolio-integration/)
        *   [Analyzers Reference](../analyzers-reference/)
        
    *    Observers
        
        Observers
        
        *   [Observers - Statistics](../observers-and-statistics/observers-and-statistics/)
        *   [Observers - Benchmarking](../observer-benchmark/benchmarking/)
        *   [Observers - Reference](../observers-reference/)
        
    *    Sizers
        
        Sizers
        
        *   [Sizers](../sizers/sizers/)
        *   [Sizers - Reference](../sizers-reference/)
        
    *    Live Trading
        
        Live Trading
        
        *   [Live Trading - Intro](../live/live/)
        *   [Live Trading - Interactive Brokers](../live/ib/ib/)
        *   [Live Trading - Oanda v1.0](../live/oanda/oanda/)
        *   [Live Trading - Visual Chart](../live/vc/vc/)
        
    *    Plotting
        
        Plotting
        
        *   [Plotting](../plotting/plotting/)
        *   [Plotting - Date Ranges](../plotting/ranges/plotting-date-ranges/)
        *   [Plotting - Same Axis](../plotting/sameaxis/plot-sameaxis/)
        
    *    Datetime
        
        Datetime
        
        *   [Datetime - Management](../timemgmt/)
        *   [Datetime - Timers](../timers/timers/)
        *   [Datetime - Trading Calendars](../tradingcalendar/tradingcalendar/)
        
    *   [Automated Running](../automated-bt-run/automated-bt-run/)
    
*    Articles
    
    Articles
    
    *   [Introduction](../../blog/)
    *   [On Backtesting Performance and Out of Core Memory Execution](../../blog/2019-10-25-on-backtesting-performance-and-out-of-memory/on-backtesting-performance-and-out-of-memory/)
    *   [Cross-Backtesting Pitfalls](../../blog/posts/2019-09-04-donchian-across-platforms/donchian-across-platforms/)
    *   [Fractional Sizes](../../blog/posts/2019-08-29-fractional-sizes/fractional-sizes/)
    *   [Beating The Random Entry](../../blog/2019-08-22-practical-backtesting-replication/practical-replication/)
    *   [Rebalancing - Conservative Formula](../../blog/2019-07-19-rebalancing-conservative/rebalancing-conservative/)
    *   [MFI Generic](../../blog/2019-07-17-mfi-generic/mfi-generic/)
    *   [Canonical vs Non Canonical](../../blog/2019-07-08-canonical-or-not/canonical-or-not/)
    *   [Buy and Hold](../../blog/2019-06-13-buy-and-hold/buy-and-hold/)
    *   [Momentum Strategy](../../blog/2019-05-20-momentum-strategy/momentum-strategy/)
    *    2018
        
        2018
        
        *   [Improving Code](../../blog/posts/2018-04-22-improving-code/improving-code/)
        *   [Dynamic Indicators](../../blog/posts/2018-02-06-dynamic-indicator/dynamic-indicator/)
        *   [Stop-Loss Trading](../../blog/posts/2018-02-01-stop-trading/stop-trading/)
        *   [Recursive Indicators](../../blog/posts/2018-01-27-recursive-indicators/recursive-indicator/)
        
    *    2017
        
        2017
        
        *   [Down Jones 10 Day Streak](../../blog/posts/2017-08-08-dow-10-day-streak/dow-10-day-streak/)
        *   [Order History](../../blog/posts/2017-07-05-order-history/order-history/)
        *   [Renko Bricks](../../blog/posts/2017-06-26-renko-bricks/renko-bricks/)
        *   [Fund Tracking](../../blog/posts/2017-06-19-fund-tracking/fund-tracking/)
        *   [Release 1.9.51.121](../../blog/posts/2017-06-12-release-1.9.51.121/release-1.9.51.121/)
        *   [Strategy Selection - Revisited](../../blog/posts/2017-05-16-stsel-revisited/stsel-revisited/)
        *   [Timers](../../blog/posts/2017-05-03-timers/timers/)
        *   [Cheat-On-Open](../../blog/posts/2017-05-01-cheat-on-open/cheat-on-open/)
        *   [Trading Calendars](../../blog/posts/2017-04-16-trading-calendar/tradingcalendar/)
        *   [Multi-Data Example](../../blog/posts/2017-04-09-multi-example/multi-example/)
        *   [Bracket Orders](../../blog/posts/2017-04-01-bracket/bracket/)
        *   [Trailing Orders](../../blog/posts/2017-03-22-stoptrail/stoptrail/)
        *   [OCO Orders](../../blog/posts/2017-03-19-oco/oco/)
        *   [Plotting on the same Axis](../../blog/posts/2017-03-17-plot-sameaxis/plot-sameaxis/)
        *   [Future vs Spot Compensation](../../blog/posts/2017-03-15-future-vs-spot/future-vs-spot/)
        *   [Plotting Date Ranges](../../blog/posts/2017-03-07-plotting-date-ranges/plotting-date-ranges/)
        *   [Kalman et al.](../../blog/posts/2017-02-14-kalman-et-al/kalman-et-al/)
        *   [PercentRank Reloaded](../../blog/posts/2017-02-05-percentrank-reloaded/percentrank-reloaded/)
        *   [Crossing Over Numbers](../../blog/posts/2017-02-04-crossing-over-numbers/crossing-over-numbers/)
        
    *    2016
        
        2016
        
        *   [BTFD - Reality Bites](../../blog/posts/2016-12-28-btfd-bites/btfd-bites/)
        *   [BTFD - Buy the F...n Dip](../../blog/posts/2016-12-26-btfd/btfd/)
        *   [Gold vs SP500](../../blog/posts/2016-12-13-gold-vs-sp500/gold-vs-sp500/)
        *   [Buy/Sell Arrows](../../blog/posts/2016-12-10-buysellarrows/buysellarrows/)
        *   [Shorting the Cash](../../blog/posts/2016-12-06-shorting-cash/shorting-cash/)
        *   [Python Hidden Powers 3](../../blog/posts/2016-11-25-hidden-powers-3/hidden-powers/)
        *   [Python Hidden Powers 2](../../blog/posts/2016-11-23-hidden-powers-2/hidden-powers/)
        *   [Python Hidden Powers 1](../../blog/posts/2016-11-20-python-hidden-powers/hidden-powers/)
        *   [Strategy Selection](../../blog/posts/2016-10-29-strategy-selection/strategy-selection/)
        *   [Notebook Inline Plotting](../../blog/posts/2016-09-17-notebook-inline/notebook-inline/)
        *   [Data Synchronization](../../blog/posts/2016-09-17-data-synchronization/data-synchronization/)
        *   [Analyzer - VWR](../../blog/posts/2016-09-06-vwr/vwr/)
        *   [Optimization Improvements](../../blog/posts/2016-09-05-optimization-improvements/optimization-improvements/)
        *   [Target Orders](../../blog/posts/2016-09-02-target-orders/target-orders/)
        *   [Futures Roll-over](../../blog/posts/2016-08-31-rolling-over-futures/rolling-futures-over/)
        *   [Credit Interest](../../blog/posts/2016-08-22-credit-interest/credit-interest/)
        *   [Dickson Moving Average](../../blog/posts/2016-08-18-dickson-moving-average/dickson-moving-average/)
        *   [Stock Screening](../../blog/posts/2016-08-15-stock-screening/stock-screening/)
        *   [Signal Strategy](../../blog/posts/2016-08-01-signal-strategy/signal-strategy/)
        *   [MACD Settings](../../blog/posts/2016-07-30-macd-settings/macd-settings/)
        *   [Pinkfish Challenge](../../blog/posts/2016-07-29-pinkfish-challenge/pinkfish-challenge/)
        *   [ta-lib Integration](../../blog/posts/2016-07-26-talib-integration/talib-integration/)
        *   [Sizers - Smart Staking](../../blog/posts/2016-07-23-sizers-smart-staking/sizers-smart-staking/)
        *   [Benchmarking](../../blog/posts/2016-07-22-benchmarking/benchmarking/)
        *   [PyFolio Integration](../../blog/posts/2016-07-17-pyfolio-integration/pyfolio-integration/)
        *   [Volume Filling](../../blog/posts/2016-07-14-volume-filling/volume-filling/)
        *   [Day In Steps](../../blog/posts/2016-07-13-day-in-steps/day-in-steps/)
        *   [Visual Chart Feed](../../blog/posts/2016-07-12-visualchart-feed/visualchart-feed/)
        *   [Ultimate Oscillator](../../blog/posts/2016-06-22-ultimate-oscillator/ultimate-oscillator/)
        *   [Live Data Feeds](../../blog/posts/2016-06-21-livedata-feed/live-data-feed/)
        *   [Memory Savings](../../blog/posts/2016-05-09-memory-savings/memory-savings/)
        *   [Mixing Timeframes](../../blog/posts/2016-05-05-indicators-mixing-timeframes/indicators-mixing-timeframes/)
        *   [PivotPoint Cross-Plotting](../../blog/posts/2016-04-28-pivot-point-cross-plotting/pivotpoint-crossplotting/)
        *   [Sync Different Markets](../../blog/posts/2016-04-19-sync-different-markets/sync-different-markets/)
        *   [Bid/Ask Data to OHLC](../../blog/posts/2016-04-14-bidask-data-to-ohlc/bidask-data-to-ohlc/)
        *   [Escape from OHLC Land](../../blog/posts/2016-03-08-escape-from-ohlc-land/escape-from-ohlc-land/)
        *   [Release 1.2.1.88](../../blog/posts/2016-03-07-release-1.2.1.88/release-1.2.1.88/)
        
    *    2015
        
        2015
        
        *   [Data Filters](../../blog/posts/2015-11-21-data-filters/data-filling-filtering/)
        *   [Subclassing Commission Schemes](../../blog/posts/2015-11-20-commission-schemes-subclassing/commission-schemes-subclassing/)
        *   [Extended Commission Schemes](../../blog/posts/2015-11-05-commission-schemes-extended/commission-schemes-extended/)
        *   [MultiTrades](../../blog/posts/2015-10-05-multitrades/multitrades/)
        *   [Bar Synchronization](../../blog/posts/2015-10-04-bar-synchronization/bar-synchronization/)
        *   [Resample Tick Data](../../blog/posts/2015-09-25-tickdata-resample/resample-tickdata/)
        *   [Plotting on the same Axis](../../blog/posts/2015-09-21-plotting-same-axis/plotting-same-axis/)
        *   [Write It Down](../../blog/posts/2015-09-14-write-it-down/write-it-down/)
        *   [Multiple Data Strategy](../../blog/posts/2015-09-03-multidata-strategy/multidata-strategy/)
        *   [Real World Usage](../../blog/posts/2015-08-27-real-world-usage/real-world-usage/)
        *   [Data Replay](../../blog/posts/2015-08-25-data-replay/data-replay/)
        *   [Data Multi-Timeframe](../../blog/posts/2015-08-24-data-multitimeframe/data-multitimeframe/)
        *   [Data Resampling](../../blog/posts/2015-08-23-data-resampling/data-resampling/)
        *   [Pandas Data Feed](../../blog/posts/2015-08-21-pandas-datafeed/pandas-datafeed/)
        *   [Backtesting with almost no Programming](../../blog/posts/2015-08-16-backtesting-with-almost-no-programming/backtesting-with-almost-no-programming/)
        *   [Observers and Statistics](../../blog/posts/2015-08-12-observers-and-statistics/observers-and-statistics/)
        *   [Data Feed Developmend](../../blog/posts/2015-08-11-datafeed-development/datafeed-development/)
        *   [Order Creation & Execution](../../blog/posts/2015-08-08-order-creation-execution/order-creation-execution/)
        *   [Extending a Data Feed](../../blog/posts/2015-08-07-extending-a-datafeed/extending-a-datafeed/)
        *   [CSV Data Feed Development](../../blog/posts/2015-08-06-csv-data-feed-development/csv-data-feed-development/)
        *   [Generic CSV Data Feed](../../blog/posts/2015-08-04-generic-csv-datafeed/generic-csv-datafeed/)
        *   [Commission Schemes - Updated](../../blog/posts/2015-07-31-commission-schemes-updated/commission-schemes-updated/)
        *   [Commission Schemes](../../blog/posts/2015-07-26-commission-schemes/commission-schemes/)
        *   [Multicore Optimization](../../blog/posts/2015-07-23-multicore-optimization/multicore-optimization/)
        *   [Extending an Indicator](../../blog/posts/2015-07-20-extending-an-indicator/extending-an-indicator/)
        *   [Developing an Indicator](../../blog/posts/2015-07-18-developing-an-indicator/developing-an-indicator/)
        
    
*    Recipes/Resources
    
    Recipes/Resources
    
    *   [Introduction](../../recipes/intro/)
    *    Indicators
        
        Indicators
        
        *   [Introduction](../../recipes/indicators/intro/)
        *   [Absolute Strength Histogram](../../recipes/indicators/ash/ash/)
        *   [Connors RSI](../../recipes/indicators/crsi/crsi/)
        *   [Donchian Channels](../../recipes/indicators/donchian/donchian/)
        *   [Money Flow Indicator](../../recipes/indicators/mfi/mfi/)
        *   [Stochastic (Generic)](../../recipes/indicators/stochastic/stochastic/)
        *   [StochRSI](../../recipes/indicators/stochrsi/stochrsi/)
        
    *    Stores/Brokers/Data Feeds
        
        Stores/Brokers/Data Feeds
        
        *   [Introduction](../../recipes/storesbrokersdata/intro/)
        *   [bt-ccxt-store](../../recipes/storesbrokersdata/bt-ccxt-store/bt-ccxt-store/)
        *   [Metaquotes MQL 5 - API](../../recipes/storesbrokersdata/mql5/mql5/)
        *   [NorgateData](../../recipes/storesbrokersdata/norgatedata/norgatedata/)
        *   [Oanda v20](../../recipes/storesbrokersdata/oandav20/oandav20/)
        *   [TradingView](../../recipes/storesbrokersdata/tradingview/tradingview/)
        
    

Table of contents

*   [AccelerationDecelerationOscillator](#accelerationdecelerationoscillator)
*   [Accum](#accum)
*   [AdaptiveMovingAverage](#adaptivemovingaverage)
*   [AdaptiveMovingAverageEnvelope](#adaptivemovingaverageenvelope)
*   [AdaptiveMovingAverageOscillator](#adaptivemovingaverageoscillator)
*   [AllN](#alln)
*   [AnyN](#anyn)
*   [ApplyN](#applyn)
*   [AroonDown](#aroondown)
*   [AroonOscillator](#aroonoscillator)
*   [AroonUp](#aroonup)
*   [AroonUpDown](#aroonupdown)
*   [AroonUpDownOscillator](#aroonupdownoscillator)
*   [Average](#average)
*   [AverageDirectionalMovementIndex](#averagedirectionalmovementindex)
*   [AverageDirectionalMovementIndexRating](#averagedirectionalmovementindexrating)
*   [AverageTrueRange](#averagetruerange)
*   [AwesomeOscillator](#awesomeoscillator)
*   [BaseApplyN](#baseapplyn)
*   [BollingerBands](#bollingerbands)
*   [BollingerBandsPct](#bollingerbandspct)
*   [CointN](#cointn)
*   [CommodityChannelIndex](#commoditychannelindex)
*   [CrossDown](#crossdown)
*   [CrossOver](#crossover)
*   [CrossUp](#crossup)
*   [DV2](#dv2)
*   [DemarkPivotPoint](#demarkpivotpoint)
*   [DetrendedPriceOscillator](#detrendedpriceoscillator)
*   [DicksonMovingAverage](#dicksonmovingaverage)
*   [DicksonMovingAverageEnvelope](#dicksonmovingaverageenvelope)
*   [DicksonMovingAverageOscillator](#dicksonmovingaverageoscillator)
*   [DirectionalIndicator](#directionalindicator)
*   [DirectionalMovement](#directionalmovement)
*   [DirectionalMovementIndex](#directionalmovementindex)
*   [DoubleExponentialMovingAverage](#doubleexponentialmovingaverage)
*   [DoubleExponentialMovingAverageEnvelope](#doubleexponentialmovingaverageenvelope)
*   [DoubleExponentialMovingAverageOscillator](#doubleexponentialmovingaverageoscillator)
*   [DownDay](#downday)
*   [DownDayBool](#downdaybool)
*   [DownMove](#downmove)
*   [Envelope](#envelope)
*   [ExponentialMovingAverage](#exponentialmovingaverage)
*   [ExponentialMovingAverageEnvelope](#exponentialmovingaverageenvelope)
*   [ExponentialMovingAverageOscillator](#exponentialmovingaverageoscillator)
*   [ExponentialSmoothing](#exponentialsmoothing)
*   [ExponentialSmoothingDynamic](#exponentialsmoothingdynamic)
*   [FibonacciPivotPoint](#fibonaccipivotpoint)
*   [FindFirstIndex](#findfirstindex)
*   [FindFirstIndexHighest](#findfirstindexhighest)
*   [FindFirstIndexLowest](#findfirstindexlowest)
*   [FindLastIndex](#findlastindex)
*   [FindLastIndexHighest](#findlastindexhighest)
*   [FindLastIndexLowest](#findlastindexlowest)
*   [Fractal](#fractal)
*   [HeikinAshi](#heikinashi)
*   [Highest](#highest)
*   [HullMovingAverage](#hullmovingaverage)
*   [HullMovingAverageEnvelope](#hullmovingaverageenvelope)
*   [HullMovingAverageOscillator](#hullmovingaverageoscillator)
*   [HurstExponent](#hurstexponent)
*   [Ichimoku](#ichimoku)
*   [KnowSureThing](#knowsurething)
*   [LaguerreFilter](#laguerrefilter)
*   [LaguerreRSI](#laguerrersi)
*   [LinePlotterIndicator](#lineplotterindicator)
*   [Lowest](#lowest)
*   [MACD](#macd)
*   [MACDHisto](#macdhisto)
*   [MeanDeviation](#meandeviation)
*   [MinusDirectionalIndicator](#minusdirectionalindicator)
*   [Momentum](#momentum)
*   [MomentumOscillator](#momentumoscillator)
*   [MovingAverageBase](#movingaveragebase)
*   [MovingAverageSimple](#movingaveragesimple)
*   [MovingAverageSimpleEnvelope](#movingaveragesimpleenvelope)
*   [MovingAverageSimpleOscillator](#movingaveragesimpleoscillator)
*   [NonZeroDifference](#nonzerodifference)
*   [OLS\_BetaN](#ols_betan)
*   [OLS\_Slope\_InterceptN](#ols_slope_interceptn)
*   [OLS\_TransformationN](#ols_transformationn)
*   [OperationN](#operationn)
*   [Oscillator](#oscillator)
*   [OscillatorMixIn](#oscillatormixin)
*   [ParabolicSAR](#parabolicsar)
*   [PercentChange](#percentchange)
*   [PercentRank](#percentrank)
*   [PercentagePriceOscillator](#percentagepriceoscillator)
*   [PercentagePriceOscillatorShort](#percentagepriceoscillatorshort)
*   [PeriodN](#periodn)
*   [PivotPoint](#pivotpoint)
*   [PlusDirectionalIndicator](#plusdirectionalindicator)
*   [PrettyGoodOscillator](#prettygoodoscillator)
*   [PriceOscillator](#priceoscillator)
*   [RSI\_EMA](#rsi_ema)
*   [RSI\_SMA](#rsi_sma)
*   [RSI\_Safe](#rsi_safe)
*   [RateOfChange](#rateofchange)
*   [RateOfChange100](#rateofchange100)
*   [ReduceN](#reducen)
*   [RelativeMomentumIndex](#relativemomentumindex)
*   [RelativeStrengthIndex](#relativestrengthindex)
*   [Signal](#signal)
*   [SmoothedMovingAverage](#smoothedmovingaverage)
*   [SmoothedMovingAverageEnvelope](#smoothedmovingaverageenvelope)
*   [SmoothedMovingAverageOscillator](#smoothedmovingaverageoscillator)
*   [StandardDeviation](#standarddeviation)
*   [Stochastic](#stochastic)
*   [StochasticFast](#stochasticfast)
*   [StochasticFull](#stochasticfull)
*   [SumN](#sumn)
*   [TripleExponentialMovingAverage](#tripleexponentialmovingaverage)
*   [TripleExponentialMovingAverageEnvelope](#tripleexponentialmovingaverageenvelope)
*   [TripleExponentialMovingAverageOscillator](#tripleexponentialmovingaverageoscillator)
*   [Trix](#trix)
*   [TrixSignal](#trixsignal)
*   [TrueHigh](#truehigh)
*   [TrueLow](#truelow)
*   [TrueRange](#truerange)
*   [TrueStrengthIndicator](#truestrengthindicator)
*   [UltimateOscillator](#ultimateoscillator)
*   [UpDay](#upday)
*   [UpDayBool](#updaybool)
*   [UpMove](#upmove)
*   [Vortex](#vortex)
*   [WeightedAverage](#weightedaverage)
*   [WeightedMovingAverage](#weightedmovingaverage)
*   [WeightedMovingAverageEnvelope](#weightedmovingaverageenvelope)
*   [WeightedMovingAverageOscillator](#weightedmovingaverageoscillator)
*   [WilliamsAD](#williamsad)
*   [WilliamsR](#williamsr)
*   [ZeroLagExponentialMovingAverage](#zerolagexponentialmovingaverage)
*   [ZeroLagExponentialMovingAverageEnvelope](#zerolagexponentialmovingaverageenvelope)
*   [ZeroLagExponentialMovingAverageOscillator](#zerolagexponentialmovingaverageoscillator)
*   [ZeroLagIndicator](#zerolagindicator)
*   [ZeroLagIndicatorEnvelope](#zerolagindicatorenvelope)
*   [ZeroLagIndicatorOscillator](#zerolagindicatoroscillator)
*   [haDelta](#hadelta)

Indicator Reference
===================

### AccelerationDecelerationOscillator

Alias:

`* AccDeOsc`

Acceleration/Deceleration Technical Indicator (AC) measures acceleration and deceleration of the current driving force. This indicator will change direction before any changes in the driving force, which, it its turn, will change its direction before the price.

Formula:

`* AcdDecOsc = AwesomeOscillator - SMA(AwesomeOscillator, period)`

See:

`* [https://www.metatrader5.com/en/terminal/help/indicators/bw_indicators/ao](https://www.metatrader5.com/en/terminal/help/indicators/bw_indicators/ao)  * [https://www.ifcmarkets.com/en/ntx-indicators/ntx-indicators-accelerator-decelerator-oscillator](https://www.ifcmarkets.com/en/ntx-indicators/ntx-indicators-accelerator-decelerator-oscillator)`

Lines:

`* accde`

Params:

`* period (5)  * movav (SMA)`

PlotInfo:

`* plot (True)  * plotmaster (None)  * legendloc (None)  * subplot (True)  * plotname ()  * plotskip (False)  * plotabove (False)  * plotlinelabels (False)  * plotlinevalues (True)  * plotvaluetags (True)`

*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   accde:
    *   \_method (bar)
    *   alpha (0.5)
    *   width (1.0)

### Accum

Alias:

*   CumSum, CumulativeSum

Cummulative sum of the data values

Formula:

*   accum += data

Lines:

*   accum

Params:

*   seed (0.0)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   accum:

### AdaptiveMovingAverage

Alias:

*   KAMA, MovingAverageAdaptive

Defined by Perry Kaufman in his book “Smarter Trading”.

It is A Moving Average with a continuously scaled smoothing factor by taking into account market direction and volatility. The smoothing factor is calculated from 2 ExponetialMovingAverage smoothing factors, a fast one and slow one.

If the market trends the value will tend to the fast ema smoothing period. If the market doesn’t trend it will move towards the slow EMA smoothing period.

It is a subclass of SmoothingMovingAverage, overriding once to account for the live nature of the smoothing factor

Formula:

*   direction = close - close\_period
    
*   volatility = sumN(abs(close - close\_n), period)
    
*   effiency\_ratio = abs(direction / volatility)
    
*   fast = 2 / (fast\_period + 1)
    
*   slow = 2 / (slow\_period + 1)
    
*   smfactor = squared(efficienty\_ratio \* (fast - slow) + slow)
    
*   smfactor1 = 1.0 - smfactor
    
*   The initial seed value is a SimpleMovingAverage
    

See also:

*   [http://fxcodebase.com/wiki/index.php/Kaufman’s\_Adaptive\_Moving\_Average\_(KAMA](http://fxcodebase.com/wiki/index.php/Kaufman's_Adaptive_Moving_Average_(KAMA))
    
*   [http://www.metatrader5.com/en/terminal/help/analytics/indicators/trend\_indicators/ama](http://www.metatrader5.com/en/terminal/help/analytics/indicators/trend_indicators/ama)
    
*   [http://help.cqg.com/cqgic/default.htm#!Documents/adaptivemovingaverag2.htm](http://help.cqg.com/cqgic/default.htm#!Documents/adaptivemovingaverag2.htm)
    

Lines:

*   kama

Params:

*   period (30)
    
*   fast (2)
    
*   slow (30)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   kama:

### AdaptiveMovingAverageEnvelope

Alias:

*   KAMAEnvelope, MovingAverageAdaptiveEnvelope

AdaptiveMovingAverage and envelope bands separated “perc” from it

Formula:

*   kama (from AdaptiveMovingAverage)
    
*   top = kama \* (1 + perc)
    
*   bot = kama \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   kama
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   fast (2)
    
*   slow (30)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   kama:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### AdaptiveMovingAverageOscillator

Alias:

*   AdaptiveMovingAverageOsc, KAMAOscillator, KAMAOsc, MovingAverageAdaptiveOscillator, MovingAverageAdaptiveOsc

Oscillation of a AdaptiveMovingAverage around its data

Lines:

*   kama

Params:

*   period (30)
    
*   fast (2)
    
*   slow (30)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   kama:
    
*   \_0:
    
    *   \_name (osc)

### AllN

Has a value of `True` (stored as `1.0` in the lines) if _all_ of the values in the `period` evaluates to non-zero (ie: `True`)

Uses the built-in `all` for the calculation

Formula:

*   alln = all(data, period)

Lines:

*   alln

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   alln:

### AnyN

Has a value of `True` (stored as `1.0` in the lines) if _any_ of the values in the `period` evaluates to non-zero (ie: `True`)

Uses the built-in `any` for the calculation

Formula:

*   anyn = any(data, period)

Lines:

*   anyn

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   anyn:

### ApplyN

Calculates `func` for a given period

Formula:

*   line = func(data, period)

Lines:

*   apply

Params:

*   period (1)
    
*   func (None)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   apply:

### AroonDown

This is the AroonDown from the indicator AroonUpDown developed by Tushar Chande in 1995.

Formula:

*   down = 100 \* (period - distance to lowest low) / period

Note:

`The lines oscillate between 0 and 100. That means that the “distance” to the last highest or lowest must go from 0 to period so that the formula can yield 0 and 100.  Hence the lookback period is period + 1, because the current bar is also taken into account. And therefore this indicator needs an effective lookback period of period + 1.`

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:aroon](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:aroon)

Lines:

*   aroondown

Params:

*   period (14)
    
*   upperband (70)
    
*   lowerband (30)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[0, 100\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   aroondown:

### AroonOscillator

Alias:

*   AroonOsc

It is a variation of the AroonUpDown indicator which shows the current difference between the AroonUp and AroonDown value, trying to present a visualization which indicates which is stronger (greater than 0 -> AroonUp and less than 0 -> AroonDown)

Formula:

*   aroonosc = aroonup - aroondown

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:aroon](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:aroon)

Lines:

*   aroonosc

Params:

*   period (14)
    
*   upperband (70)
    
*   lowerband (30)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[0, 100\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   aroonosc:

### AroonUp

This is the AroonUp from the indicator AroonUpDown developed by Tushar Chande in 1995.

Formula:

*   up = 100 \* (period - distance to highest high) / period

Note:

`The lines oscillate between 0 and 100. That means that the “distance” to the last highest or lowest must go from 0 to period so that the formula can yield 0 and 100.  Hence the lookback period is period + 1, because the current bar is also taken into account. And therefore this indicator needs an effective lookback period of period + 1.`

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:aroon](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:aroon)

Lines:

*   aroonup

Params:

*   period (14)
    
*   upperband (70)
    
*   lowerband (30)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[0, 100\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   aroonup:

### AroonUpDown

Alias:

*   AroonIndicator

Developed by Tushar Chande in 1995.

It tries to determine if a trend exists or not by calculating how far away within a given period the last highs/lows are (AroonUp/AroonDown)

Formula:

*   up = 100 \* (period - distance to highest high) / period
    
*   down = 100 \* (period - distance to lowest low) / period
    

Note:

`The lines oscillate between 0 and 100. That means that the “distance” to the last highest or lowest must go from 0 to period so that the formula can yield 0 and 100.  Hence the lookback period is period + 1, because the current bar is also taken into account. And therefore this indicator needs an effective lookback period of period + 1.`

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:aroon](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:aroon)

Lines:

*   aroonup
    
*   aroondown
    

Params:

*   period (14)
    
*   upperband (70)
    
*   lowerband (30)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[0, 100\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   aroonup:
    
*   aroondown:
    

### AroonUpDownOscillator

Alias:

*   AroonUpDownOsc

Presents together the indicators AroonUpDown and AroonOsc

Formula:

`(None, uses the aforementioned indicators)`

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:aroon](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:aroon)

Lines:

*   aroonup
    
*   aroondown
    
*   aroonosc
    

Params:

*   period (14)
    
*   upperband (70)
    
*   lowerband (30)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[0, 100\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   aroonup:
    
*   aroondown:
    
*   aroonosc:
    

### Average

Alias:

*   ArithmeticMean, Mean

Averages a given data arithmetically over a period

Formula:

*   av = data(period) / period

See also:

*   [https://en.wikipedia.org/wiki/Arithmetic\_mean](https://en.wikipedia.org/wiki/Arithmetic_mean)

Lines:

*   av

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   av:

### AverageDirectionalMovementIndex

Alias:

*   ADX

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

Intended to measure trend strength

This indicator only shows ADX:

*   Use PlusDirectionalIndicator (PlusDI) to get +DI
    
*   Use MinusDirectionalIndicator (MinusDI) to get -DI
    
*   Use Directional Indicator (DI) to get +DI, -DI
    
*   Use AverageDirectionalIndexRating (ADXR) to get ADX, ADXR
    
*   Use DirectionalMovementIndex (DMI) to get ADX, +DI, -DI
    
*   Use DirectionalMovement (DM) to get ADX, ADXR, +DI, -DI
    

Formula:

*   upmove = high - high(-1)
    
*   downmove = low(-1) - low
    
*   +dm = upmove if upmove > downmove and upmove > 0 else 0
    
*   \-dm = downmove if downmove > upmove and downmove > 0 else 0
    
*   +di = 100 \* MovingAverage(+dm, period) / atr(period)
    
*   \-di = 100 \* MovingAverage(-dm, period) / atr(period)
    
*   dx = 100 \* abs(+di - -di) / (+di + -di)
    
*   adx = MovingAverage(dx, period)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   adx

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   plusDI:
    
    *   \_name (+DI)
*   minusDI:
    
    *   \_name (-DI)
*   adx:
    
    *   \_name (ADX)

### AverageDirectionalMovementIndexRating

Alias:

*   ADXR

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

Intended to measure trend strength.

ADXR is the average of ADX with a value period bars ago

This indicator shows the ADX and ADXR:

*   Use PlusDirectionalIndicator (PlusDI) to get +DI
    
*   Use MinusDirectionalIndicator (MinusDI) to get -DI
    
*   Use Directional Indicator (DI) to get +DI, -DI
    
*   Use AverageDirectionalIndex (ADX) to get ADX
    
*   Use DirectionalMovementIndex (DMI) to get ADX, +DI, -DI
    
*   Use DirectionalMovement (DM) to get ADX, ADXR, +DI, -DI
    

Formula:

*   upmove = high - high(-1)
    
*   downmove = low(-1) - low
    
*   +dm = upmove if upmove > downmove and upmove > 0 else 0
    
*   \-dm = downmove if downmove > upmove and downmove > 0 else 0
    
*   +di = 100 \* MovingAverage(+dm, period) / atr(period)
    
*   \-di = 100 \* MovingAverage(-dm, period) / atr(period)
    
*   dx = 100 \* abs(+di - -di) / (+di + -di)
    
*   adx = MovingAverage(dx, period)
    
*   adxr = (adx + adx(-period)) / 2
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   adx
    
*   adxr
    

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   plusDI:
    
    *   \_name (+DI)
*   minusDI:
    
    *   \_name (-DI)
*   adx:
    
    *   \_name (ADX)
*   adxr:
    
    *   \_name (ADXR)

### AverageTrueRange

Alias:

*   ATR

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

The idea is to take the close into account to calculate the range if it yields a larger range than the daily range (High - Low)

Formula:

*   SmoothedMovingAverage(TrueRange, period)

See:

*   [http://en.wikipedia.org/wiki/Average\_true\_range](https://en.wikipedia.org/wiki/Average_true_range)

Lines:

*   atr

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   atr:

### AwesomeOscillator

Alias:

*   AwesomeOsc, AO

Awesome Oscillator (AO) is a momentum indicator reflecting the precise changes in the market driving force which helps to identify the trend’s strength up to the points of formation and reversal.

Formula:

*   median price = (high + low) / 2
    
*   AO = SMA(median price, 5)- SMA(median price, 34)
    

See:

*   [https://www.metatrader5.com/en/terminal/help/indicators/bw\_indicators/awesome](https://www.metatrader5.com/en/terminal/help/indicators/bw_indicators/awesome)
    
*   [https://www.ifcmarkets.com/en/ntx-indicators/awesome-oscillator](https://www.ifcmarkets.com/en/ntx-indicators/awesome-oscillator)
    

Lines:

*   ao

Params:

*   fast (5)
    
*   slow (34)
    
*   movav (SMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ao:
    *   \_method (bar)
    *   alpha (0.5)
    *   width (1.0)

### BaseApplyN

Base class for ApplyN and others which may take a `func` as a parameter but want to define the lines in the indicator.

Calculates `func` for a given period where func is given as a parameter, aka named argument or `kwarg`

Formula:

*   lines\[0\] = func(data, period)

Any extra lines defined beyond the first (index 0) are not calculated

Params:

*   period (1)
    
*   func (None)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

### BollingerBands

Alias:

*   BBands

Defined by John Bollinger in the 80s. It measures volatility by defining upper and lower bands at distance x standard deviations

Formula:

*   midband = SimpleMovingAverage(close, period)
    
*   topband = midband + devfactor \* StandardDeviation(data, period)
    
*   botband = midband - devfactor \* StandardDeviation(data, period)
    

See:

*   [http://en.wikipedia.org/wiki/Bollinger\_Bands](https://en.wikipedia.org/wiki/Bollinger_Bands)

Lines:

*   mid
    
*   top
    
*   bot
    

Params:

*   period (20)
    
*   devfactor (2.0)
    
*   movav (MovingAverageSimple)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   mid:
    
    *   ls (–)
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### BollingerBandsPct

Extends the Bollinger Bands with a Percentage line

Lines:

*   mid
    
*   top
    
*   bot
    
*   pctb
    

Params:

*   period (20)
    
*   devfactor (2.0)
    
*   movav (MovingAverageSimple)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   mid:
    
    *   ls (–)
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)
*   pctb:
    
    *   \_name (%B)

### CointN

Calculates the score (coint\_t) and pvalue for a given `period` for the data feeds

Uses `pandas` and `statsmodels` (for `coint`)

Lines:

*   score
    
*   pvalue
    

Params:

*   period (10)
    
*   regression ©
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   score:
    
*   pvalue:
    

### CommodityChannelIndex

Alias:

*   CCI

Introduced by Donald Lambert in 1980 to measure variations of the “typical price” (see below) from its mean to identify extremes and reversals

Formula:

*   tp = typical\_price = (high + low + close) / 3
    
*   tpmean = MovingAverage(tp, period)
    
*   deviation = tp - tpmean
    
*   meandev = MeanDeviation(tp)
    
*   cci = deviation / (meandeviation \* factor)
    

See:

*   [https://en.wikipedia.org/wiki/Commodity\_channel\_index](https://en.wikipedia.org/wiki/Commodity_channel_index)

Lines:

*   cci

Params:

*   period (20)
    
*   factor (0.015)
    
*   movav (MovingAverageSimple)
    
*   upperband (100.0)
    
*   lowerband (-100.0)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   cci:

### CrossDown

This indicator gives a signal if the 1st provided data crosses over the 2nd indicator upwards

It does need to look into the current time index (0) and the previous time index (-1) of both the 1st and 2nd data

Formula:

*   diff = data - data1
    
*   downcross = last\_non\_zero\_diff > 0 and data0(0) < data1(0)
    

Lines:

*   cross

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[0.0, 1.0\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   cross:

### CrossOver

This indicator gives a signal if the provided datas (2) cross up or down.

*   1.0 if the 1st data crosses the 2nd data upwards
    
*   \-1.0 if the 1st data crosses the 2nd data downwards
    

It does need to look into the current time index (0) and the previous time index (-1) of both the 1t and 2nd data

Formula:

*   diff = data - data1
    
*   upcross = last\_non\_zero\_diff < 0 and data0(0) > data1(0)
    
*   downcross = last\_non\_zero\_diff > 0 and data0(0) < data1(0)
    
*   crossover = upcross - downcross
    

Lines:

*   crossover

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[-1.0, 1.0\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   crossover:

### CrossUp

This indicator gives a signal if the 1st provided data crosses over the 2nd indicator upwards

It does need to look into the current time index (0) and the previous time index (-1) of both the 1st and 2nd data

Formula:

*   diff = data - data1
    
*   upcross = last\_non\_zero\_diff < 0 and data0(0) > data1(0)
    

Lines:

*   cross

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.05)
    
*   plotyhlines (\[0.0, 1.0\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   cross:

### DV2

RSI(2) alternative Developed by David Varadi of [http://cssanalytics.wordpress.com/](http://cssanalytics.wordpress.com/)

This seems to be the _Bounded_ version.

See also:

*   [http://web.archive.org/web/20131216100741/http://quantingdutchman.wordpress.com/2010/08/06/dv2-indicator-for-amibroker/](http://web.archive.org/web/20131216100741/http://quantingdutchman.wordpress.com/2010/08/06/dv2-indicator-for-amibroker/)

Lines:

*   dv2

Params:

*   period (252)
    
*   maperiod (2)
    
*   \_movav (SMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   dv2:

### DemarkPivotPoint

Defines a level of significance by taking into account the average of price bar components of the past period of a larger timeframe. For example when operating with days, the values are taking from the already “past” month fixed prices.

Example of using this indicator:

data = btfeeds.ADataFeed(dataname=x, timeframe=bt.TimeFrame.Days) cerebro.adddata(data) cerebro.resampledata(data, timeframe=bt.TimeFrame.Months)

In the `__init__` method of the strategy:

pivotindicator = btind.DemarkPivotPoiont(self.data1) # the resampled data

The indicator will try to automatically plot to the non-resampled data. To disable this behavior use the following during construction:

*   \_autoplot=False

Note:

The example shows _days_ and _months_, but any combination of timeframes can be used. See the literature for recommended combinations

Formula:

*   if close < open x = high + (2 x low) + close
    
*   if close > open x = (2 x high) + low + close
    
*   if Close == open x = high + low + (2 x close)
    
*   p = x / 4
    
*   support1 = x / 2 - high
    
*   resistance1 = x / 2 - low
    

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:pivot\_points](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:pivot_points)

Lines:

*   p
    
*   s1
    
*   r1
    

Params:

*   open (False)
    
*   close (False)
    
*   \_autoplot (True)
    
*   level1 (0.382)
    
*   level2 (0.618)
    
*   level3 (1.0)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   p:
    
*   s1:
    
*   r1:
    

### DetrendedPriceOscillator

Alias:

*   DPO

Defined by Joe DiNapoli in his book _“Trading with DiNapoli levels”_

It measures the price variations against a Moving Average (the trend) and therefore removes the “trend” factor from the price.

Formula:

*   movav = MovingAverage(close, period)
    
*   dpo = close - movav(shifted period / 2 + 1)
    

See:

*   [http://en.wikipedia.org/wiki/Detrended\_price\_oscillator](https://en.wikipedia.org/wiki/Detrended_price_oscillator)

Lines:

*   dpo

Params:

*   period (20)
    
*   movav (MovingAverageSimple)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   dpo:

### DicksonMovingAverage

Alias:

*   DMA, DicksonMA

By Nathan Dickson

The _Dickson Moving Average_ combines the `ZeroLagIndicator` (aka _ErrorCorrecting_ or _EC_) by _Ehlers_, and the `HullMovingAverage` to try to deliver a result close to that of the _Jurik_ Moving Averages

Formula:

*   ec = ZeroLagIndicator(period, gainlimit)
    
*   hma = HullMovingAverage(hperiod)
    
*   dma = (ec + hma) / 2
    
*   The default moving average for the _ZeroLagIndicator_ is EMA, but can be changed with the parameter `_movav`
    
    \-_NOTE_\*: the passed moving average must calculate alpha (and 1 - alpha) and make them available as attributes `alpha` and `alpha1`
    
*   The 2nd moving averag can be changed from _Hull_ to anything else with the param _\_hma_
    

See also:

*   [https://www.reddit.com/r/algotrading/comments/4xj3vh/dickson\_moving\_average](https://www.reddit.com/r/algotrading/comments/4xj3vh/dickson_moving_average)

Lines:

*   dma

Params:

*   period (30)
    
*   gainlimit (50)
    
*   hperiod (7)
    
*   \_movav (EMA)
    
*   \_hma (HMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   dma:

### DicksonMovingAverageEnvelope

Alias:

*   DMAEnvelope, DicksonMAEnvelope

DicksonMovingAverage and envelope bands separated “perc” from it

Formula:

*   dma (from DicksonMovingAverage)
    
*   top = dma \* (1 + perc)
    
*   bot = dma \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   dma
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   gainlimit (50)
    
*   hperiod (7)
    
*   \_movav (EMA)
    
*   \_hma (HMA)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   dma:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### DicksonMovingAverageOscillator

Alias:

*   DicksonMovingAverageOsc, DMAOscillator, DMAOsc, DicksonMAOscillator, DicksonMAOsc

Oscillation of a DicksonMovingAverage around its data

Lines:

*   dma

Params:

*   period (30)
    
*   gainlimit (50)
    
*   hperiod (7)
    
*   \_movav (EMA)
    
*   \_hma (HMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   dma:
    
*   \_0:
    
    *   \_name (osc)

### DirectionalIndicator

Alias:

*   DI

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

Intended to measure trend strength

This indicator shows +DI, -DI:

*   Use PlusDirectionalIndicator (PlusDI) to get +DI
    
*   Use MinusDirectionalIndicator (MinusDI) to get -DI
    
*   Use AverageDirectionalIndex (ADX) to get ADX
    
*   Use AverageDirectionalIndexRating (ADXR) to get ADX, ADXR
    
*   Use DirectionalMovementIndex (DMI) to get ADX, +DI, -DI
    
*   Use DirectionalMovement (DM) to get ADX, ADXR, +DI, -DI
    

Formula:

*   upmove = high - high(-1)
    
*   downmove = low(-1) - low
    
*   +dm = upmove if upmove > downmove and upmove > 0 else 0
    
*   \-dm = downmove if downmove > upmove and downmove > 0 else 0
    
*   +di = 100 \* MovingAverage(+dm, period) / atr(period)
    
*   \-di = 100 \* MovingAverage(-dm, period) / atr(period)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   plusDI
    
*   minusDI
    

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   plusDI:
    
*   minusDI:
    

### DirectionalMovement

Alias:

*   DM

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

Intended to measure trend strength

This indicator shows ADX, ADXR, +DI, -DI.

*   Use PlusDirectionalIndicator (PlusDI) to get +DI
    
*   Use MinusDirectionalIndicator (MinusDI) to get -DI
    
*   Use Directional Indicator (DI) to get +DI, -DI
    
*   Use AverageDirectionalIndex (ADX) to get ADX
    
*   Use AverageDirectionalIndexRating (ADXR) to get ADX, ADXR
    
*   Use DirectionalMovementIndex (DMI) to get ADX, +DI, -DI
    

Formula:

*   upmove = high - high(-1)
    
*   downmove = low(-1) - low
    
*   +dm = upmove if upmove > downmove and upmove > 0 else 0
    
*   \-dm = downmove if downmove > upmove and downmove > 0 else 0
    
*   +di = 100 \* MovingAverage(+dm, period) / atr(period)
    
*   \-di = 100 \* MovingAverage(-dm, period) / atr(period)
    
*   dx = 100 \* abs(+di - -di) / (+di + -di)
    
*   adx = MovingAverage(dx, period)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   adx
    
*   adxr
    
*   plusDI
    
*   minusDI
    

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   plusDI:
    
*   minusDI:
    
*   adx:
    
    *   \_name (ADX)
*   adxr:
    
    *   \_name (ADXR)

### DirectionalMovementIndex

Alias:

*   DMI

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

Intended to measure trend strength

This indicator shows the ADX, +DI, -DI:

*   Use PlusDirectionalIndicator (PlusDI) to get +DI
    
*   Use MinusDirectionalIndicator (MinusDI) to get -DI
    
*   Use Directional Indicator (DI) to get +DI, -DI
    
*   Use AverageDirectionalIndex (ADX) to get ADX
    
*   Use AverageDirectionalIndexRating (ADXRating) to get ADX, ADXR
    
*   Use DirectionalMovement (DM) to get ADX, ADXR, +DI, -DI
    

Formula:

*   upmove = high - high(-1)
    
*   downmove = low(-1) - low
    
*   +dm = upmove if upmove > downmove and upmove > 0 else 0
    
*   \-dm = downmove if downmove > upmove and downmove > 0 else 0
    
*   +di = 100 \* MovingAverage(+dm, period) / atr(period)
    
*   \-di = 100 \* MovingAverage(-dm, period) / atr(period)
    
*   dx = 100 \* abs(+di - -di) / (+di + -di)
    
*   adx = MovingAverage(dx, period)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   adx
    
*   plusDI
    
*   minusDI
    

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   plusDI:
    
*   minusDI:
    
*   adx:
    
    *   \_name (ADX)

### DoubleExponentialMovingAverage

Alias:

*   DEMA, MovingAverageDoubleExponential

DEMA was first time introduced in 1994, in the article “Smoothing Data with Faster Moving Averages” by Patrick G. Mulloy in “Technical Analysis of Stocks & Commodities” magazine.

It attempts to reduce the inherent lag associated to Moving Averages

Formula:

*   dema = (2.0 - ema(data, period) - ema(ema(data, period), period)

See:

`(None)`

Lines:

*   dema

Params:

*   period (30)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   dema:

### DoubleExponentialMovingAverageEnvelope

Alias:

*   DEMAEnvelope, MovingAverageDoubleExponentialEnvelope

DoubleExponentialMovingAverage and envelope bands separated “perc” from it

Formula:

*   dema (from DoubleExponentialMovingAverage)
    
*   top = dema \* (1 + perc)
    
*   bot = dema \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   dema
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   \_movav (EMA)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   dema:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### DoubleExponentialMovingAverageOscillator

Alias:

*   DoubleExponentialMovingAverageOsc, DEMAOscillator, DEMAOsc, MovingAverageDoubleExponentialOscillator, MovingAverageDoubleExponentialOsc

Oscillation of a DoubleExponentialMovingAverage around its data

Lines:

*   dema

Params:

*   period (30)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   dema:
    
*   \_0:
    
    *   \_name (osc)

### DownDay

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ for the RSI

Records days which have been “down”, i.e.: the close price has been lower than the day before.

Formula:

*   downday = max(close\_prev - close, 0)

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Lines:

*   downday

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   downday:

### DownDayBool

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ for the RSI

Records days which have been “down”, i.e.: the close price has been lower than the day before.

Note:

*   This version returns a bool rather than the difference

Formula:

*   downday = close\_prev > close

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Lines:

*   downday

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   downday:

### DownMove

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ as part of the Directional Move System to calculate Directional Indicators.

Positive if the given data has moved lower than the previous day

Formula:

*   downmove = data(-1) - data

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   downmove

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   downmove:

### Envelope

It creates envelopes bands separated from the source data by a given percentage

Formula:

*   src = datasource
    
*   top = src \* (1 + perc)
    
*   bot = src \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   src
    
*   top
    
*   bot
    

Params:

*   perc (2.5)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   src:
    
    *   \_plotskip (True)
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### ExponentialMovingAverage

Alias:

*   EMA, MovingAverageExponential

A Moving Average that smoothes data exponentially over time.

It is a subclass of SmoothingMovingAverage.

*   self.smfactor -> 2 / (1 + period)
    
*   self.smfactor1 -> 1 - self.smfactor
    

Formula:

*   movav = prev \* (1.0 - smoothfactor) + newdata \* smoothfactor

See also:

*   [http://en.wikipedia.org/wiki/Moving\_average#Exponential\_moving\_average](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average)

Lines:

*   ema

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ema:

### ExponentialMovingAverageEnvelope

Alias:

*   EMAEnvelope, MovingAverageExponentialEnvelope

ExponentialMovingAverage and envelope bands separated “perc” from it

Formula:

*   ema (from ExponentialMovingAverage)
    
*   top = ema \* (1 + perc)
    
*   bot = ema \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   ema
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ema:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### ExponentialMovingAverageOscillator

Alias:

*   ExponentialMovingAverageOsc, EMAOscillator, EMAOsc, MovingAverageExponentialOscillator, MovingAverageExponentialOsc

Oscillation of a ExponentialMovingAverage around its data

Lines:

*   ema

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ema:
    
*   \_0:
    
    *   \_name (osc)

### ExponentialSmoothing

Alias:

*   ExpSmoothing

Averages a given data over a period using exponential smoothing

A regular ArithmeticMean (Average) is used as the seed value considering the first period values of data

Formula:

*   av = prev \* (1 - alpha) + data \* alpha

See also:

*   [https://en.wikipedia.org/wiki/Exponential\_smoothing](https://en.wikipedia.org/wiki/Exponential_smoothing)

Lines:

*   av

Params:

*   period (1)
    
*   alpha (None)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   av:

### ExponentialSmoothingDynamic

Alias:

*   ExpSmoothingDynamic

Averages a given data over a period using exponential smoothing

A regular ArithmeticMean (Average) is used as the seed value considering the first period values of data

Note:

*   alpha is an array of values which can be calculated dynamically

Formula:

*   av = prev \* (1 - alpha) + data \* alpha

See also:

*   [https://en.wikipedia.org/wiki/Exponential\_smoothing](https://en.wikipedia.org/wiki/Exponential_smoothing)

Lines:

*   av

Params:

*   period (1)
    
*   alpha (None)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   av:

### FibonacciPivotPoint

Defines a level of significance by taking into account the average of price bar components of the past period of a larger timeframe. For example when operating with days, the values are taking from the already “past” month fixed prices.

Fibonacci levels (configurable) are used to define the support/resistance levels

Example of using this indicator:

data = btfeeds.ADataFeed(dataname=x, timeframe=bt.TimeFrame.Days) cerebro.adddata(data) cerebro.resampledata(data, timeframe=bt.TimeFrame.Months)

In the `__init__` method of the strategy:

pivotindicator = btind.FibonacciPivotPoiont(self.data1) # the resampled data

The indicator will try to automatically plo to the non-resampled data. To disable this behavior use the following during construction:

*   \_autoplot=False

Note:

The example shows _days_ and _months_, but any combination of timeframes can be used. See the literature for recommended combinations

Formula:

*   pivot = (h + l + c) / 3 # variants duplicate close or add open
    
*   support1 = p - level1 \* (high - low) # level1 0.382
    
*   support2 = p - level2 \* (high - low) # level2 0.618
    
*   support3 = p - level3 \* (high - low) # level3 1.000
    
*   resistance1 = p + level1 \* (high - low) # level1 0.382
    
*   resistance2 = p + level2 \* (high - low) # level2 0.618
    
*   resistance3 = p + level3 \* (high - low) # level3 1.000
    

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:pivot\_points](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:pivot_points)

Lines:

*   p
    
*   s1
    
*   s2
    
*   s3
    
*   r1
    
*   r2
    
*   r3
    

Params:

*   open (False)
    
*   close (False)
    
*   \_autoplot (True)
    
*   level1 (0.382)
    
*   level2 (0.618)
    
*   level3 (1.0)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   p:
    
*   s1:
    
*   s2:
    
*   s3:
    
*   r1:
    
*   r2:
    
*   r3:
    

### FindFirstIndex

Returns the index of the last data that satisfies equality with the condition generated by the parameter \_evalfunc

Note:

`Returned indexes look backwards. 0 is the current index and 1 is the previous bar.`

Formula:

*   index = first for which data\[index\] == \_evalfunc(data)

Lines:

*   index

Params:

*   period (1)
    
*   \_evalfunc (None)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   index:

### FindFirstIndexHighest

Returns the index of the first data that is the highest in the period

Note:

`Returned indexes look backwards. 0 is the current index and 1 is the previous bar.`

Formula:

*   index = index of first data which is the highest

Lines:

*   index

Params:

*   period (1)
    
*   \_evalfunc ()
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   index:

### FindFirstIndexLowest

Returns the index of the first data that is the lowest in the period

Note:

`Returned indexes look backwards. 0 is the current index and 1 is the previous bar.`

Formula:

*   index = index of first data which is the lowest

Lines:

*   index

Params:

*   period (1)
    
*   \_evalfunc ()
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   index:

### FindLastIndex

Returns the index of the last data that satisfies equality with the condition generated by the parameter \_evalfunc

Note:

`Returned indexes look backwards. 0 is the current index and 1 is the previous bar.`

Formula:

*   index = last for which data\[index\] == \_evalfunc(data)

Lines:

*   index

Params:

*   period (1)
    
*   \_evalfunc (None)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   index:

### FindLastIndexHighest

Returns the index of the last data that is the highest in the period

Note:

`Returned indexes look backwards. 0 is the current index and 1 is the previous bar.`

Formula:

*   index = index of last data which is the highest

Lines:

*   index

Params:

*   period (1)
    
*   \_evalfunc ()
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   index:

### FindLastIndexLowest

Returns the index of the last data that is the lowest in the period

Note:

`Returned indexes look backwards. 0 is the current index and 1 is the previous bar.`

Formula:

*   index = index of last data which is the lowest

Lines:

*   index

Params:

*   period (1)
    
*   \_evalfunc ()
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   index:

### Fractal

References:

`[Ref 1] [http://www.investopedia.com/articles/trading/06/fractals.asp](http://www.investopedia.com/articles/trading/06/fractals.asp)`

Lines:

*   fractal\_bearish
    
*   fractal\_bullish
    

Params:

*   period (5)
    
*   bardist (0.015)
    
*   shift\_to\_potential\_fractal (2)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   fractal\_bearish:
    
    *   marker (^)
    *   markersize (4.0)
    *   color (lightblue)
    *   fillstyle (full)
    *   ls ()
*   fractal\_bullish:
    
    *   marker (v)
    *   markersize (4.0)
    *   color (lightblue)
    *   fillstyle (full)
    *   ls ()

### HeikinAshi

Heikin Ashi candlesticks in the forms of lines

Formula:

`ha_open = (ha_open(-1) + ha_close(-1)) / 2 ha_high = max(hi, ha_open, ha_close) ha_low = min(lo, ha_open, ha_close) ha_close = (open + high + low + close) / 4`

See also:

`[https://en.wikipedia.org/wiki/Candlestick_chart#Heikin_Ashi_candlesticks](https://en.wikipedia.org/wiki/Candlestick_chart#Heikin_Ashi_candlesticks) [http://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:heikin_ashi](http://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:heikin_ashi)`

Lines:

*   ha\_open
    
*   ha\_high
    
*   ha\_low
    
*   ha\_close
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ha\_open:
    
*   ha\_high:
    
*   ha\_low:
    
*   ha\_close:
    

### Highest

Alias:

*   MaxN

Calculates the highest value for the data in a given period

Uses the built-in `max` for the calculation

Formula:

*   highest = max(data, period)

Lines:

*   highest

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   highest:

### HullMovingAverage

Alias:

*   HMA, HullMA

By Alan Hull

The Hull Moving Average solves the age old dilemma of making a moving average more responsive to current price activity whilst maintaining curve smoothness. In fact the HMA almost eliminates lag altogether and manages to improve smoothing at the same time.

Formula:

*   hma = wma(2 \* wma(data, period // 2) - wma(data, period), sqrt(period))

See also:

*   [http://alanhull.com/hull-moving-average](http://alanhull.com/hull-moving-average)

Note:

*   Please note that the final minimum period is not the period passed with the parameter `period`. A final moving average on moving average is done in which the period is the _square root_ of the original.
    
    In the default case of `30` the final minimum period before the moving average produces a non-NAN value is `34`
    

Lines:

*   hma

Params:

*   period (30)
    
*   \_movav (WMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   hma:

### HullMovingAverageEnvelope

Alias:

*   HMAEnvelope, HullMAEnvelope

HullMovingAverage and envelope bands separated “perc” from it

Formula:

*   hma (from HullMovingAverage)
    
*   top = hma \* (1 + perc)
    
*   bot = hma \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   hma
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   \_movav (WMA)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   hma:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### HullMovingAverageOscillator

Alias:

*   HullMovingAverageOsc, HMAOscillator, HMAOsc, HullMAOscillator, HullMAOsc

Oscillation of a HullMovingAverage around its data

Lines:

*   hma

Params:

*   period (30)
    
*   \_movav (WMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   hma:
    
*   \_0:
    
    *   \_name (osc)

### HurstExponent

Alias:

`- Hurst  References:  - [https://www.quantopian.com/posts/hurst-exponent](https://www.quantopian.com/posts/hurst-exponent)  - [https://www.quantopian.com/posts/some-code-from-ernie-chans-new-book-implemented-in-python](https://www.quantopian.com/posts/some-code-from-ernie-chans-new-book-implemented-in-python)`

Interpretation of the results

`1. Geometric random walk (H=0.5)  1. Mean-reverting series (H<0.5)  1. Trending Series (H>0.5)`

Important notes:

*   The default period is `40`, but experimentation by users has shown that it would be advisable to have at least 2000 samples (i.e.: a period of at least 2000) to have stable values.
    
*   The lag\_start and lag\_end values will default to be `2` and `self.p.period / 2` unless the parameters are specified.
    
    Experimentation by users has also shown that values of around `10` and `500` produce good results
    

The original values (40, 2, self.p.period / 2) are kept for backwards compatibility

Lines:

*   hurst

Params:

*   period (40)
    
*   lag\_start (None)
    
*   lag\_end (None)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   hurst:

### Ichimoku

Developed and published in his book in 1969 by journalist Goichi Hosoda

Formula:

*   tenkan\_sen = (Highest(High, tenkan) + Lowest(Low, tenkan)) / 2.0
    
*   kijun\_sen = (Highest(High, kijun) + Lowest(Low, kijun)) / 2.0
    
    The next 2 are pushed 26 bars into the future
    
*   senkou\_span\_a = (tenkan\_sen + kijun\_sen) / 2.0
    
*   senkou\_span\_b = ((Highest(High, senkou) + Lowest(Low, senkou)) / 2.0
    
    This is pushed 26 bars into the past
    
*   chikou = close
    

The cloud (Kumo) is formed by the area between the senkou\_spans

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:ichimoku\_cloud](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ichimoku_cloud)

Lines:

*   tenkan\_sen
    
*   kijun\_sen
    
*   senkou\_span\_a
    
*   senkou\_span\_b
    
*   chikou\_span
    

Params:

*   tenkan (9)
    
*   kijun (26)
    
*   senkou (52)
    
*   senkou\_lead (26)
    
*   chikou (26)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   senkou\_span\_a:
    
    *   \_fill\_gt ((‘senkou\_span\_b’, ‘g’))
    *   \_fill\_lt ((‘senkou\_span\_b’, ‘r’))
*   tenkan\_sen:
    
*   kijun\_sen:
    
*   senkou\_span\_b:
    
*   chikou\_span:
    

### KnowSureThing

Alias:

*   KST

It is a “summed” momentum indicator. Developed by Martin Pring and published in 1992 in Stocks & Commodities.

Formula:

*   rcma1 = MovAv(roc100(rp1), period)
    
*   rcma2 = MovAv(roc100(rp2), period)
    
*   rcma3 = MovAv(roc100(rp3), period)
    
*   rcma4 = MovAv(roc100(rp4), period)
    
*   kst = 1.0 \* rcma1 + 2.0 \* rcma2 + 3.0 \* rcma3 + 4.0 \* rcma4
    
*   signal = MovAv(kst, speriod)
    

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:know\_sure\_thing\_kst](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:know_sure_thing_kst)

Params

*   `rma1`, `rma2`, `rma3`, `rma4`: for the MovingAverages on ROCs
    
*   `rp1`, `rp2`, `rp3`, `rp4`: for the ROCs
    
*   `rsig`: for the MovingAverage for the signal line
    
*   `rfactors`: list of factors to apply to the different MovAv(ROCs)
    
*   `_movav` and `_movavs`, allows to change the Moving Average type applied for the calculation of kst and signal
    

Lines:

*   kst
    
*   signal
    

Params:

*   rp1 (10)
    
*   rp2 (15)
    
*   rp3 (20)
    
*   rp4 (30)
    
*   rma1 (10)
    
*   rma2 (10)
    
*   rma3 (10)
    
*   rma4 (10)
    
*   rsignal (9)
    
*   rfactors (\[1.0, 2.0, 3.0, 4.0\])
    
*   \_rmovav (SMA)
    
*   \_smovav (SMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   kst:
    
*   signal:
    

### LaguerreFilter

Alias:

*   LAGF

Defined by John F. Ehlers in Cybernetic Analysis for Stock and Futures, 2004, published by Wiley. ISBN: 978-0-471-46307-8

`gamma` is meant to have values between `0.2` and `0.8`, with the best balance found theoretically at the default of `0.5`

Lines:

*   lfilter

Params:

*   period (1)
    
*   gamma (0.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   lfilter:

### LaguerreRSI

Alias:

*   LRSI

Defined by John F. Ehlers in Cybernetic Analysis for Stock and Futures, 2004, published by Wiley. ISBN: 978-0-471-46307-8

The Laguerre RSI tries to implements a better RSI by providing a sort of _Time Warp without Time Travel_ using a Laguerre filter. This provides for faster reactions to price changes

`gamma` is meant to have values between `0.2` and `0.8`, with the best balance found theoretically at the default of `0.5`

Lines:

*   lrsi

Params:

*   period (6)
    
*   gamma (0.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.15)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[0.0, 0.2, 0.5, 0.8, 1.0\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   lrsi:

### LinePlotterIndicator

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

### Lowest

Alias:

*   MinN

Calculates the lowest value for the data in a given period

Uses the built-in `min` for the calculation

Formula:

*   lowest = min(data, period)

Lines:

*   lowest

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   lowest:

### MACD

Moving Average Convergence Divergence. Defined by Gerald Appel in the 70s.

It measures the distance of a short and a long term moving average to try to identify the trend.

A second lagging moving average over the convergence-divergence should provide a “signal” upon being crossed by the macd

Formula:

*   macd = ema(data, me1\_period) - ema(data, me2\_period)
    
*   signal = ema(macd, signal\_period)
    

See:

*   [http://en.wikipedia.org/wiki/MACD](https://en.wikipedia.org/wiki/MACD)

Lines:

*   macd
    
*   signal
    

Params:

*   period\_me1 (12)
    
*   period\_me2 (26)
    
*   period\_signal (9)
    
*   movav (ExponentialMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   signal:
    
    *   ls (–)
*   macd:
    

### MACDHisto

Alias:

*   MACDHistogram

Subclass of MACD which adds a “histogram” of the difference between the macd and signal lines

Formula:

*   histo = macd - signal

See:

*   [http://en.wikipedia.org/wiki/MACD](https://en.wikipedia.org/wiki/MACD)

Lines:

*   macd
    
*   signal
    
*   histo
    

Params:

*   period\_me1 (12)
    
*   period\_me2 (26)
    
*   period\_signal (9)
    
*   movav (ExponentialMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   signal:
    
    *   ls (–)
*   macd:
    
*   histo:
    
    *   \_method (bar)
    *   alpha (0.5)
    *   width (1.0)

### MeanDeviation

Alias:

*   MeanDev

MeanDeviation (alias MeanDev)

Calculates the Mean Deviation of the passed data for a given period

Note:

*   If 2 datas are provided as parameters, the 2nd is considered to be the mean of the first

Formula:

*   mean = MovingAverage(data, period) (or provided mean)
    
*   absdeviation = abs(data - mean)
    
*   meandev = MovingAverage(absdeviation, period)
    

See:

*   [https://en.wikipedia.org/wiki/Average\_absolute\_deviation](https://en.wikipedia.org/wiki/Average_absolute_deviation)

Lines:

*   meandev

Params:

*   period (20)
    
*   movav (MovingAverageSimple)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   meandev:

### MinusDirectionalIndicator

Alias:

*   MinusDI

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

Intended to measure trend strength

This indicator shows -DI:

*   Use PlusDirectionalIndicator (PlusDI) to get +DI
    
*   Use Directional Indicator (DI) to get +DI, -DI
    
*   Use AverageDirectionalIndex (ADX) to get ADX
    
*   Use AverageDirectionalIndexRating (ADXR) to get ADX, ADXR
    
*   Use DirectionalMovementIndex (DMI) to get ADX, +DI, -DI
    
*   Use DirectionalMovement (DM) to get ADX, ADXR, +DI, -DI
    

Formula:

*   upmove = high - high(-1)
    
*   downmove = low(-1) - low
    
*   \-dm = downmove if downmove > upmove and downmove > 0 else 0
    
*   \-di = 100 \* MovingAverage(-dm, period) / atr(period)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   minusDI

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname (-DirectionalIndicator)
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   plusDI:
    
    *   \_name (+DI)
*   minusDI:
    

### Momentum

Measures the change in price by calculating the difference between the current price and the price from a given period ago

Formula:

*   momentum = data - data\_period

See:

*   [http://en.wikipedia.org/wiki/Momentum\_(technical\_analysis](https://en.wikipedia.org/wiki/Momentum_(technical_analysis))

Lines:

*   momentum

Params:

*   period (12)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   momentum:

### MomentumOscillator

Alias:

*   MomentumOsc

Measures the ratio of change in prices over a period

Formula:

*   mosc = 100 \* (data / data\_period)

See:

*   [http://ta.mql4.com/indicators/oscillators/momentum](http://ta.mql4.com/indicators/oscillators/momentum)

Lines:

*   momosc

Params:

*   period (12)
    
*   band (100.0)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   momosc:

### MovingAverageBase

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

### MovingAverageSimple

Alias:

*   SMA, SimpleMovingAverage

Non-weighted average of the last n periods

Formula:

*   movav = Sum(data, period) / period

See also:

*   [http://en.wikipedia.org/wiki/Moving\_average#Simple\_moving\_average](https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average)

Lines:

*   sma

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   sma:

### MovingAverageSimpleEnvelope

Alias:

*   SMAEnvelope, SimpleMovingAverageEnvelope

MovingAverageSimple and envelope bands separated “perc” from it

Formula:

*   sma (from MovingAverageSimple)
    
*   top = sma \* (1 + perc)
    
*   bot = sma \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   sma
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   sma:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### MovingAverageSimpleOscillator

Alias:

*   MovingAverageSimpleOsc, SMAOscillator, SMAOsc, SimpleMovingAverageOscillator, SimpleMovingAverageOsc

Oscillation of a MovingAverageSimple around its data

Lines:

*   sma

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   sma:
    
*   \_0:
    
    *   \_name (osc)

### NonZeroDifference

Alias:

*   NZD

Keeps track of the difference between two data inputs skipping, memorizing the last non zero value if the current difference is zero

Formula:

*   diff = data - data1
    
*   nzd = diff if diff else diff(-1)
    

Lines:

*   nzd

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   nzd:

### OLS\_BetaN

Calculates a regression of data1 on data0 using `pandas.ols`

Uses `pandas`

Lines:

*   beta

Params:

*   period (10)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   beta:

### OLS\_Slope\_InterceptN

Calculates a linear regression using `statsmodel.OLS` (Ordinary least squares) of data1 on data0

Uses `pandas` and `statsmodels`

Use `prepend_constant` to influence the paramter `prepend` of sm.add\_constant

Lines:

*   slope
    
*   intercept
    

Params:

*   period (10)
    
*   prepend\_constant (True)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   slope:
    
*   intercept:
    

### OLS\_TransformationN

Calculates the `zscore` for data0 and data1. Although it doesn’t directly uses any external package it relies on `OLS_SlopeInterceptN` which uses `pandas` and `statsmodels`

Lines:

*   spread
    
*   spread\_mean
    
*   spread\_std
    
*   zscore
    

Params:

*   period (10)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   spread:
    
*   spread\_mean:
    
*   spread\_std:
    
*   zscore:
    

### OperationN

Calculates “func” for a given period

Serves as a base for classes that work with a period and can express the logic in a callable object

Note:

`Base classes must provide a “func” attribute which is a callable`

Formula:

*   line = func(data, period)

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

### Oscillator

Oscillation of a given data around another data

Datas:

`This indicator can accept 1 or 2 datas for the calculation.`

*   If 1 data is provided, it must be a complex “Lines” object (indicator) which also has “datas”. Example: A moving average
    
    The calculated oscillation will be that of the Moving Average (in the example) around the data that was used for the average calculation
    
*   If 2 datas are provided the calculated oscillation will be that of the 2nd data around the 1st data
    

Formula:

*   1 data -> osc = data.data - data
    
*   2 datas -> osc = data0 - data1
    

Lines:

*   osc

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   \_0:
    
    *   \_name (osc)
*   osc:
    

### OscillatorMixIn

MixIn class to create a subclass with another indicator. The main line of that indicator will be substracted from the other base class main line creating an oscillator

The usage is:

*   Class XXXOscillator(XXX, OscillatorMixIn)

Formula:

*   XXX calculates lines\[0\]
    
*   osc = self.data - XXX.lines\[0\]
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   \_0:
    *   \_name (osc)

### ParabolicSAR

Alias:

*   PSAR

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ for the RSI

SAR stands for _Stop and Reverse_ and the indicator was meant as a signal for entry (and reverse)

How to select the 1st signal is left unspecified in the book and the increase/decrease of bars

See:

*   [https://en.wikipedia.org/wiki/Parabolic\_SAR](https://en.wikipedia.org/wiki/Parabolic_SAR)
    
*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:parabolic\_sar](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:parabolic_sar)
    

Lines:

*   psar

Params:

*   period (2)
    
*   af (0.02)
    
*   afmax (0.2)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   psar:
    *   marker (.)
    *   markersize (4.0)
    *   color (black)
    *   fillstyle (full)
    *   ls ()

### PercentChange

Alias:

*   PctChange

Measures the perccentage change of the current value with respect to that of period bars ago

Lines:

*   pctchange

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   pctchange:
    *   \_name (%change)

### PercentRank

Alias:

*   PctRank

Measures the percent rank of the current value with respect to that of period bars ago

Lines:

*   pctrank

Params:

*   period (50)
    
*   func ( at 0x000001F1E4478B70>)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   pctrank:

### PercentagePriceOscillator

Alias:

*   PPO, PercPriceOsc

Shows the difference between a short and long exponential moving averages expressed in percentage. The MACD does the same but expressed in absolute points.

Expressing the difference in percentage allows to compare the indicator at different points in time when the underlying value has significatnly different values.

Formula:

*   po = 100 \* (ema(short) - ema(long)) / ema(long)

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:price\_oscillators\_ppo](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:price_oscillators_ppo)

Lines:

*   ppo
    
*   signal
    
*   histo
    

Params:

*   period1 (12)
    
*   period2 (26)
    
*   \_movav (ExponentialMovingAverage)
    
*   period\_signal (9)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   histo:
    
    *   \_method (bar)
    *   alpha (0.5)
    *   width (1.0)
*   ppo:
    
*   signal:
    

### PercentagePriceOscillatorShort

Alias:

*   PPOShort, PercPriceOscShort

Shows the difference between a short and long exponential moving averages expressed in percentage. The MACD does the same but expressed in absolute points.

Expressing the difference in percentage allows to compare the indicator at different points in time when the underlying value has significatnly different values.

Most on-line literature shows the percentage calculation having the long exponential moving average as the denominator. Some sources like MetaStock use the short one.

Formula:

*   po = 100 \* (ema(short) - ema(long)) / ema(short)

See:

*   [http://www.metastock.com/Customer/Resources/TAAZ/?c=3&p=94](http://www.metastock.com/Customer/Resources/TAAZ/?c=3&p=94)

Lines:

*   ppo
    
*   signal
    
*   histo
    

Params:

*   period1 (12)
    
*   period2 (26)
    
*   \_movav (ExponentialMovingAverage)
    
*   period\_signal (9)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   histo:
    
    *   \_method (bar)
    *   alpha (0.5)
    *   width (1.0)
*   ppo:
    
*   signal:
    

### PeriodN

Base class for indicators which take a period (**init** has to be called either via super or explicitly)

This class has no defined lines

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

### PivotPoint

Defines a level of significance by taking into account the average of price bar components of the past period of a larger timeframe. For example when operating with days, the values are taking from the already “past” month fixed prices.

Example of using this indicator:

data = btfeeds.ADataFeed(dataname=x, timeframe=bt.TimeFrame.Days) cerebro.adddata(data) cerebro.resampledata(data, timeframe=bt.TimeFrame.Months)

In the `__init__` method of the strategy:

pivotindicator = btind.PivotPoiont(self.data1) # the resampled data

The indicator will try to automatically plo to the non-resampled data. To disable this behavior use the following during construction:

*   \_autoplot=False

Note:

The example shows _days_ and _months_, but any combination of timeframes can be used. See the literature for recommended combinations

Formula:

*   pivot = (h + l + c) / 3 # variants duplicate close or add open
    
*   support1 = 2.0 \* pivot - high
    
*   support2 = pivot - (high - low)
    
*   resistance1 = 2.0 \* pivot - low
    
*   resistance2 = pivot + (high - low)
    

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:pivot\_points](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:pivot_points)
    
*   [https://en.wikipedia.org/wiki/Pivot\_point\_(technical\_analysis](https://en.wikipedia.org/wiki/Pivot_point_(technical_analysis))
    

Lines:

*   p
    
*   s1
    
*   s2
    
*   r1
    
*   r2
    

Params:

*   open (False)
    
*   close (False)
    
*   \_autoplot (True)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   p:
    
*   s1:
    
*   s2:
    
*   r1:
    
*   r2:
    

### PlusDirectionalIndicator

Alias:

*   PlusDI

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

Intended to measure trend strength

This indicator shows +DI:

*   Use MinusDirectionalIndicator (MinusDI) to get -DI
    
*   Use Directional Indicator (DI) to get +DI, -DI
    
*   Use AverageDirectionalIndex (ADX) to get ADX
    
*   Use AverageDirectionalIndexRating (ADXR) to get ADX, ADXR
    
*   Use DirectionalMovementIndex (DMI) to get ADX, +DI, -DI
    
*   Use DirectionalMovement (DM) to get ADX, ADXR, +DI, -DI
    

Formula:

*   upmove = high - high(-1)
    
*   downmove = low(-1) - low
    
*   +dm = upmove if upmove > downmove and upmove > 0 else 0
    
*   +di = 100 \* MovingAverage(+dm, period) / atr(period)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   plusDI

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname (+DirectionalIndicator)
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   plusDI:
    
*   minusDI:
    
    *   \_name (-DI)

### PrettyGoodOscillator

Alias:

*   PGO, PrettyGoodOsc

The “Pretty Good Oscillator” (PGO) by Mark Johnson measures the distance of the current close from its simple moving average of period Average), expressed in terms of an average true range (see Average True Range) over a similar period.

So for instance a PGO value of +2.5 would mean the current close is 2.5 average days’ range above the SMA.

Johnson’s approach was to use it as a breakout system for longer term trades. If the PGO rises above 3.0 then go long, or below -3.0 then go short, and in both cases exit on returning to zero (which is a close back at the SMA).

Formula:

*   pgo = (data.close - sma(data, period)) / atr(data, period)

See also:

*   [http://user42.tuxfamily.org/chart/manual/Pretty-Good-Oscillator.html](http://user42.tuxfamily.org/chart/manual/Pretty-Good-Oscillator.html)

Lines:

*   pgo

Params:

*   period (14)
    
*   \_movav (MovingAverageSimple)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   pgo:

### PriceOscillator

Alias:

*   PriceOsc, AbsolutePriceOscillator, APO, AbsPriceOsc

Shows the difference between a short and long exponential moving averages expressed in points.

Formula:

*   po = ema(short) - ema(long)

See:

*   [http://www.metastock.com/Customer/Resources/TAAZ/?c=3&p=94](http://www.metastock.com/Customer/Resources/TAAZ/?c=3&p=94)

Lines:

*   po

Params:

*   period1 (12)
    
*   period2 (26)
    
*   \_movav (ExponentialMovingAverage)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   po:

### RSI\_EMA

Uses an ExponentialMovingAverage as described in Wikipedia

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Lines:

*   rsi

Params:

*   period (14)
    
*   movav (ExponentialMovingAverage)
    
*   upperband (70.0)
    
*   lowerband (30.0)
    
*   safediv (False)
    
*   safehigh (100.0)
    
*   safelow (50.0)
    
*   lookback (1)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   rsi:

### RSI\_SMA

Alias:

*   RSI\_Cutler

Uses a SimpleMovingAverage as described in Wikipedia and other soures

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Lines:

*   rsi

Params:

*   period (14)
    
*   movav (MovingAverageSimple)
    
*   upperband (70.0)
    
*   lowerband (30.0)
    
*   safediv (False)
    
*   safehigh (100.0)
    
*   safelow (50.0)
    
*   lookback (1)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   rsi:

### RSI\_Safe

Subclass of RSI which changes parameers `safediv` to `True` as the default value

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Lines:

*   rsi

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    
*   upperband (70.0)
    
*   lowerband (30.0)
    
*   safediv (True)
    
*   safehigh (100.0)
    
*   safelow (50.0)
    
*   lookback (1)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   rsi:

### RateOfChange

Alias:

*   ROC

Measures the ratio of change in prices over a period

Formula:

*   roc = (data - data\_period) / data\_period

See:

*   [http://en.wikipedia.org/wiki/Momentum\_(technical\_analysis](https://en.wikipedia.org/wiki/Momentum_(technical_analysis))

Lines:

*   roc

Params:

*   period (12)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   roc:

### RateOfChange100

Alias:

*   ROC100

Measures the ratio of change in prices over a period with base 100

This is for example how ROC is defined in stockcharts

Formula:

*   roc = 100 \* (data - data\_period) / data\_period

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:rate\_of\_change\_roc\_and\_momentum](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:rate_of_change_roc_and_momentum)

Lines:

*   roc100

Params:

*   period (12)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   roc100:

### ReduceN

Calculates the Reduced value of the `period` data points applying `function`

Uses the built-in `reduce` for the calculation plus the `func` that subclassess define

Formula:

*   reduced = reduce(function(data, period)), initializer=initializer)

Notes:

*   In order to mimic the python `reduce`, this indicator takes a `function` non-named argument as the 1st argument, unlike other Indicators which take only named arguments

Lines:

*   reduced

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   reduced:

### RelativeMomentumIndex

Alias:

*   RMI

Description: The Relative Momentum Index was developed by Roger Altman and was introduced in his article in the February, 1993 issue of Technical Analysis of Stocks & Commodities magazine.

While your typical RSI counts up and down days from close to close, the Relative Momentum Index counts up and down days from the close relative to a close x number of days ago. The result is an RSI that is a bit smoother.

Usage: Use in the same way you would any other RSI . There are overbought and oversold zones, and can also be used for divergence and trend analysis.

See:

*   [https://www.marketvolume.com/technicalanalysis/relativemomentumindex.asp](https://www.marketvolume.com/technicalanalysis/relativemomentumindex.asp)
    
*   [https://www.tradingview.com/script/UCm7fIvk-FREE-INDICATOR-Relative-Momentum-Index-RMI/](https://www.tradingview.com/script/UCm7fIvk-FREE-INDICATOR-Relative-Momentum-Index-RMI/)
    
*   [https://www.prorealcode.com/prorealtime-indicators/relative-momentum-index-rmi/](https://www.prorealcode.com/prorealtime-indicators/relative-momentum-index-rmi/)
    

Lines:

*   rsi

Params:

*   period (20)
    
*   movav (SmoothedMovingAverage)
    
*   upperband (70.0)
    
*   lowerband (30.0)
    
*   safediv (False)
    
*   safehigh (100.0)
    
*   safelow (50.0)
    
*   lookback (5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   rsi:
    *   \_name (rmi)

### RelativeStrengthIndex

Alias:

*   RSI, RSI\_SMMA, RSI\_Wilder

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_.

It measures momentum by calculating the ration of higher closes and lower closes after having been smoothed by an average, normalizing the result between 0 and 100

Formula:

*   up = upday(data)
    
*   down = downday(data)
    
*   maup = movingaverage(up, period)
    
*   madown = movingaverage(down, period)
    
*   rs = maup / madown
    
*   rsi = 100 - 100 / (1 + rs)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Notes:

*   `safediv` (default: False) If this parameter is True the division rs = maup / madown will be checked for the special cases in which a `0 / 0` or `x / 0` division will happen
    
*   `safehigh` (default: 100.0) will be used as RSI value for the `x / 0` case
    
*   `safelow` (default: 50.0) will be used as RSI value for the `0 / 0` case
    

Lines:

*   rsi

Params:

*   period (14)
    
*   movav (SmoothedMovingAverage)
    
*   upperband (70.0)
    
*   lowerband (30.0)
    
*   safediv (False)
    
*   safehigh (100.0)
    
*   safelow (50.0)
    
*   lookback (1)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   rsi:

### Signal

Lines:

*   signal

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   signal:

### SmoothedMovingAverage

Alias:

*   SMMA, WilderMA, MovingAverageSmoothed, MovingAverageWilder, ModifiedMovingAverage

Smoothing Moving Average used by Wilder in his 1978 book New Concepts in Technical Trading

Defined in his book originally as:

*   new\_value = (old\_value \* (period - 1) + new\_data) / period

Can be expressed as a SmoothingMovingAverage with the following factors:

*   self.smfactor -> 1.0 / period
    
*   self.smfactor1 -> 1.0 - self.smfactor
    

Formula:

*   movav = prev \* (1.0 - smoothfactor) + newdata \* smoothfactor

See also:

*   [http://en.wikipedia.org/wiki/Moving\_average#Modified\_moving\_average](https://en.wikipedia.org/wiki/Moving_average#Modified_moving_average)

Lines:

*   smma

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   smma:

### SmoothedMovingAverageEnvelope

Alias:

*   SMMAEnvelope, WilderMAEnvelope, MovingAverageSmoothedEnvelope, MovingAverageWilderEnvelope, ModifiedMovingAverageEnvelope

SmoothedMovingAverage and envelope bands separated “perc” from it

Formula:

*   smma (from SmoothedMovingAverage)
    
*   top = smma \* (1 + perc)
    
*   bot = smma \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   smma
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   smma:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### SmoothedMovingAverageOscillator

Alias:

*   SmoothedMovingAverageOsc, SMMAOscillator, SMMAOsc, WilderMAOscillator, WilderMAOsc, MovingAverageSmoothedOscillator, MovingAverageSmoothedOsc, MovingAverageWilderOscillator, MovingAverageWilderOsc, ModifiedMovingAverageOscillator, ModifiedMovingAverageOsc

Oscillation of a SmoothedMovingAverage around its data

Lines:

*   smma

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   smma:
    
*   \_0:
    
    *   \_name (osc)

### StandardDeviation

Alias:

*   StdDev

Calculates the standard deviation of the passed data for a given period

Note:

*   If 2 datas are provided as parameters, the 2nd is considered to be the mean of the first
    
*   `safepow` (default: False) If this parameter is True, the standard deviation will be calculated as pow(abs(meansq - sqmean), 0.5) to safe guard for possible negative results of `meansq - sqmean` caused by the floating point representation.
    

Formula:

*   meansquared = SimpleMovingAverage(pow(data, 2), period)
    
*   squaredmean = pow(SimpleMovingAverage(data, period), 2)
    
*   stddev = pow(meansquared - squaredmean, 0.5) # square root
    

See:

*   [http://en.wikipedia.org/wiki/Standard\_deviation](https://en.wikipedia.org/wiki/Standard_deviation)

Lines:

*   stddev

Params:

*   period (20)
    
*   movav (MovingAverageSimple)
    
*   safepow (True)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   stddev:

### Stochastic

Alias:

*   StochasticSlow

The regular (or slow version) adds an additional moving average layer and thus:

*   The percD line of the StochasticFast becomes the percK line
    
*   percD becomes a moving average of period\_dslow of the original percD
    

Formula:

*   k = k
    
*   d = d
    
*   d = MovingAverage(d, period\_dslow)
    

See:

*   [http://en.wikipedia.org/wiki/Stochastic\_oscillator](https://en.wikipedia.org/wiki/Stochastic_oscillator)

Lines:

*   percK
    
*   percD
    

Params:

*   period (14)
    
*   period\_dfast (3)
    
*   movav (MovingAverageSimple)
    
*   upperband (80.0)
    
*   lowerband (20.0)
    
*   safediv (False)
    
*   safezero (0.0)
    
*   period\_dslow (3)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   percD:
    
    *   \_name (%D)
    *   ls (–)
*   percK:
    
    *   \_name (%K)

### StochasticFast

By Dr. George Lane in the 50s. It compares a closing price to the price range and tries to show convergence if the closing prices are close to the extremes

*   It will go up if closing prices are close to the highs
    
*   It will roughly go down if closing prices are close to the lows
    

It shows divergence if the extremes keep on growing but closing prices do not in the same manner (distance to the extremes grow)

Formula:

*   hh = highest(data.high, period)
    
*   ll = lowest(data.low, period)
    
*   knum = data.close - ll
    
*   kden = hh - ll
    
*   k = 100 \* (knum / kden)
    
*   d = MovingAverage(k, period\_dfast)
    

See:

*   [http://en.wikipedia.org/wiki/Stochastic\_oscillator](https://en.wikipedia.org/wiki/Stochastic_oscillator)

Lines:

*   percK
    
*   percD
    

Params:

*   period (14)
    
*   period\_dfast (3)
    
*   movav (MovingAverageSimple)
    
*   upperband (80.0)
    
*   lowerband (20.0)
    
*   safediv (False)
    
*   safezero (0.0)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   percD:
    
    *   \_name (%D)
    *   ls (–)
*   percK:
    
    *   \_name (%K)

### StochasticFull

This version displays the 3 possible lines:

*   percK
    
*   percD
    
*   percSlow
    

Formula:

*   k = d
    
*   d = MovingAverage(k, period\_dslow)
    
*   dslow =
    

See:

*   [http://en.wikipedia.org/wiki/Stochastic\_oscillator](https://en.wikipedia.org/wiki/Stochastic_oscillator)

Lines:

*   percK
    
*   percD
    
*   percDSlow
    

Params:

*   period (14)
    
*   period\_dfast (3)
    
*   movav (MovingAverageSimple)
    
*   upperband (80.0)
    
*   lowerband (20.0)
    
*   safediv (False)
    
*   safezero (0.0)
    
*   period\_dslow (3)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   percD:
    
    *   \_name (%D)
    *   ls (–)
*   percK:
    
    *   \_name (%K)
*   percDSlow:
    
    *   \_name (%DSlow)

### SumN

Calculates the Sum of the data values over a given period

Uses `math.fsum` for the calculation rather than the built-in `sum` to avoid precision errors

Formula:

*   sumn = sum(data, period)

Lines:

*   sumn

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   sumn:

### TripleExponentialMovingAverage

Alias:

*   TEMA, MovingAverageTripleExponential

TEMA was first time introduced in 1994, in the article “Smoothing Data with Faster Moving Averages” by Patrick G. Mulloy in “Technical Analysis of Stocks & Commodities” magazine.

It attempts to reduce the inherent lag associated to Moving Averages

Formula:

*   ema1 = ema(data, period)
    
*   ema2 = ema(ema1, period)
    
*   ema3 = ema(ema2, period)
    
*   tema = 3 \* ema1 - 3 \* ema2 + ema3
    

See:

`(None)`

Lines:

*   tema

Params:

*   period (30)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   tema:

### TripleExponentialMovingAverageEnvelope

Alias:

*   TEMAEnvelope, MovingAverageTripleExponentialEnvelope

TripleExponentialMovingAverage and envelope bands separated “perc” from it

Formula:

*   tema (from TripleExponentialMovingAverage)
    
*   top = tema \* (1 + perc)
    
*   bot = tema \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   tema
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   \_movav (EMA)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   tema:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### TripleExponentialMovingAverageOscillator

Alias:

*   TripleExponentialMovingAverageOsc, TEMAOscillator, TEMAOsc, MovingAverageTripleExponentialOscillator, MovingAverageTripleExponentialOsc

Oscillation of a TripleExponentialMovingAverage around its data

Lines:

*   tema

Params:

*   period (30)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   tema:
    
*   \_0:
    
    *   \_name (osc)

### Trix

Alias:

*   TRIX

Defined by Jack Hutson in the 80s and shows the Rate of Change (%) or slope of a triple exponentially smoothed moving average

Formula:

*   ema1 = EMA(data, period)
    
*   ema2 = EMA(ema1, period)
    
*   ema3 = EMA(ema2, period)
    
*   trix = 100 \* (ema3 - ema3(-1)) / ema3(-1)
    
    The final formula can be simplified to: 100 \* (ema3 / ema3(-1) - 1)
    

The moving average used is the one originally defined by Wilder, the SmoothedMovingAverage

See:

*   [https://en.wikipedia.org/wiki/Trix\_(technical\_analysis](https://en.wikipedia.org/wiki/Trix_(technical_analysis))
    
*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:trix](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:trix)
    

Lines:

*   trix

Params:

*   period (15)
    
*   \_rocperiod (1)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   trix:

### TrixSignal

Extension of Trix with a signal line (ala MACD)

Formula:

*   trix = Trix(data, period)
    
*   signal = EMA(trix, sigperiod)
    

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:trix](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:trix)

Lines:

*   trix
    
*   signal
    

Params:

*   period (15)
    
*   \_rocperiod (1)
    
*   \_movav (EMA)
    
*   sigperiod (9)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[0.0\])
    
*   plotforce (False)
    

PlotLines:

*   trix:
    
*   signal:
    

### TrueHigh

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ for the ATR

Records the “true high” which is the maximum of today’s high and yesterday’s close

Formula:

*   truehigh = max(high, close\_prev)

See:

*   [http://en.wikipedia.org/wiki/Average\_true\_range](https://en.wikipedia.org/wiki/Average_true_range)

Lines:

*   truehigh

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   truehigh:

### TrueLow

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ for the ATR

Records the “true low” which is the minimum of today’s low and yesterday’s close

Formula:

*   truelow = min(low, close\_prev)

See:

*   [http://en.wikipedia.org/wiki/Average\_true\_range](https://en.wikipedia.org/wiki/Average_true_range)

Lines:

*   truelow

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   truelow:

### TrueRange

Alias:

*   TR

Defined by J. Welles Wilder, Jr. in 1978 in his book New Concepts in Technical Trading Systems.

Formula:

*   max(high - low, abs(high - prev\_close), abs(prev\_close - low)
    
    which can be simplified to
    
*   max(high, prev\_close) - min(low, prev\_close)
    

See:

*   [http://en.wikipedia.org/wiki/Average\_true\_range](https://en.wikipedia.org/wiki/Average_true_range)

The idea is to take the previous close into account to calculate the range if it yields a larger range than the daily range (High - Low)

Lines:

*   tr

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   tr:

### TrueStrengthIndicator

Alias:

*   TSI

The True Strength Indicators was first introduced in Stocks & Commodities Magazine by its author William Blau. It measures momentum with a double exponential (default) of the prices.

It shows divergence if the extremes keep on growign but closing prices do not in the same manner (distance to the extremes grow)

Formula:

*   price\_change = close - close(pchange periods ago)
    
*   sm1\_simple = EMA(price\_close\_change, period1)
    
*   sm1\_double = EMA(sm1\_simple, period2)
    
*   sm2\_simple = EMA(abs(price\_close\_change), period1)
    
*   sm2\_double = EMA(sm2\_simple, period2)
    
*   tsi = 100.0 \* sm1\_double / sm2\_double
    

See:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:true\_strength\_index](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:true_strength_index)

Params

*   `period1`: the period for the 1st smoothing
    
*   `period2`: the period for the 2nd smoothing
    
*   `pchange`: the lookback period for the price change
    
*   `_movav`: the moving average to apply for the smoothing
    

Lines:

*   tsi

Params:

*   period1 (25)
    
*   period2 (13)
    
*   pchange (1)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   tsi:

### UltimateOscillator

Formula:

`# Buying Pressure = Close - TrueLow BP = Close - Minimum(Low or Prior Close)  # TrueRange = TrueHigh - TrueLow TR = Maximum(High or Prior Close)  -  Minimum(Low or Prior Close)  Average7 = (7-period BP Sum) / (7-period TR Sum) Average14 = (14-period BP Sum) / (14-period TR Sum) Average28 = (28-period BP Sum) / (28-period TR Sum)  UO = 100 x [(4 x Average7)+(2 x Average14)+Average28]/(4+2+1)`

See:

*   [https://en.wikipedia.org/wiki/Ultimate\_oscillator](https://en.wikipedia.org/wiki/Ultimate_oscillator)
    
*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:ultimate\_oscillator](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ultimate_oscillator)
    

Lines:

*   uo

Params:

*   p1 (7)
    
*   p2 (14)
    
*   p3 (28)
    
*   upperband (70.0)
    
*   lowerband (30.0)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   uo:

### UpDay

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ for the RSI

Records days which have been “up”, i.e.: the close price has been higher than the day before.

Formula:

*   upday = max(close - close\_prev, 0)

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Lines:

*   upday

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   upday:

### UpDayBool

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ for the RSI

Records days which have been “up”, i.e.: the close price has been higher than the day before.

Note:

*   This version returns a bool rather than the difference

Formula:

*   upday = close > close\_prev

See:

*   [http://en.wikipedia.org/wiki/Relative\_strength\_index](https://en.wikipedia.org/wiki/Relative_strength_index)

Lines:

*   upday

Params:

*   period (1)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   upday:

### UpMove

Defined by J. Welles Wilder, Jr. in 1978 in his book _“New Concepts in Technical Trading Systems”_ as part of the Directional Move System to calculate Directional Indicators.

Positive if the given data has moved higher than the previous day

Formula:

*   upmove = data - data(-1)

See:

*   [https://en.wikipedia.org/wiki/Average\_directional\_movement\_index](https://en.wikipedia.org/wiki/Average_directional_movement_index)

Lines:

*   upmove

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   upmove:

### Vortex

See:

*   [http://www.vortexindicator.com/VFX\_VORTEX.PDF](http://www.vortexindicator.com/VFX_VORTEX.PDF)

Lines:

*   vi\_plus
    
*   vi\_minus
    

Params:

*   period (14)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   vi\_plus:
    
    *   \_name (+VI)
*   vi\_minus:
    
    *   \_name (-VI)

### WeightedAverage

Alias:

*   AverageWeighted

Calculates the weighted average of the given data over a period

The default weights (if none are provided) are linear to assigne more weight to the most recent data

The result will be multiplied by a given “coef”

Formula:

*   av = coef \* sum(mul(data, period), weights)

See:

*   [https://en.wikipedia.org/wiki/Weighted\_arithmetic\_mean](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)

Lines:

*   av

Params:

*   period (1)
    
*   coef (1.0)
    
*   weights (())
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   av:

### WeightedMovingAverage

Alias:

*   WMA, MovingAverageWeighted

A Moving Average which gives an arithmetic weighting to values with the newest having the more weight

Formula:

*   weights = range(1, period + 1)
    
*   coef = 2 / (period \* (period + 1))
    
*   movav = coef \* Sum(weight\[i\] \* data\[period - i\] for i in range(period))
    

See also:

*   [http://en.wikipedia.org/wiki/Moving\_average#Weighted\_moving\_average](https://en.wikipedia.org/wiki/Moving_average#Weighted_moving_average)

Lines:

*   wma

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   wma:

### WeightedMovingAverageEnvelope

Alias:

*   WMAEnvelope, MovingAverageWeightedEnvelope

WeightedMovingAverage and envelope bands separated “perc” from it

Formula:

*   wma (from WeightedMovingAverage)
    
*   top = wma \* (1 + perc)
    
*   bot = wma \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   wma
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   wma:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### WeightedMovingAverageOscillator

Alias:

*   WeightedMovingAverageOsc, WMAOscillator, WMAOsc, MovingAverageWeightedOscillator, MovingAverageWeightedOsc

Oscillation of a WeightedMovingAverage around its data

Lines:

*   wma

Params:

*   period (30)

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   wma:
    
*   \_0:
    
    *   \_name (osc)

### WilliamsAD

By Larry Williams. It does cumulatively measure if the price is accumulating (upwards) or distributing (downwards) by using the concept of UpDays and DownDays.

Prices can go upwards but do so in a fashion that no longer shows accumulation because updays and downdays are canceling out each other, creating a divergence.

See: - [http://www.metastock.com/Customer/Resources/TAAZ/?p=125](http://www.metastock.com/Customer/Resources/TAAZ/?p=125) - [http://ta.mql4.com/indicators/trends/williams\_accumulation\_distribution](http://ta.mql4.com/indicators/trends/williams_accumulation_distribution)

Lines:

*   ad

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ad:

### WilliamsR

Developed by Larry Williams to show the relation of closing prices to the highest-lowest range of a given period.

Known as Williams %R (but % is not allowed in Python identifiers)

Formula:

*   num = highest\_period - close
    
*   den = highestg\_period - lowest\_period
    
*   percR = (num / den) \* -100.0
    

See:

*   [http://en.wikipedia.org/wiki/Williams\_%25R](https://en.wikipedia.org/wiki/Williams_%25R)

Lines:

*   percR

Params:

*   period (14)
    
*   upperband (-20.0)
    
*   lowerband (-80.0)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname (Williams R%)
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   percR:
    
    *   \_name (R%)

### ZeroLagExponentialMovingAverage

Alias:

*   ZLEMA, ZeroLagEma

The zero-lag exponential moving average (ZLEMA) is a variation of the EMA which adds a momentum term aiming to reduce lag in the average so as to track current prices more closely.

Formula:

*   lag = (period - 1) / 2
    
*   zlema = ema(2 \* data - data(-lag))
    

See also:

*   [http://user42.tuxfamily.org/chart/manual/Zero\_002dLag-Exponential-Moving-Average.html](http://user42.tuxfamily.org/chart/manual/Zero_002dLag-Exponential-Moving-Average.html)

Lines:

*   zlema

Params:

*   period (30)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   zlema:

### ZeroLagExponentialMovingAverageEnvelope

Alias:

*   ZLEMAEnvelope, ZeroLagEmaEnvelope

ZeroLagExponentialMovingAverage and envelope bands separated “perc” from it

Formula:

*   zlema (from ZeroLagExponentialMovingAverage)
    
*   top = zlema \* (1 + perc)
    
*   bot = zlema \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   zlema
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   \_movav (EMA)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   zlema:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### ZeroLagExponentialMovingAverageOscillator

Alias:

*   ZeroLagExponentialMovingAverageOsc, ZLEMAOscillator, ZLEMAOsc, ZeroLagEmaOscillator, ZeroLagEmaOsc

Oscillation of a ZeroLagExponentialMovingAverage around its data

Lines:

*   zlema

Params:

*   period (30)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   zlema:
    
*   \_0:
    
    *   \_name (osc)

### ZeroLagIndicator

Alias:

*   ZLIndicator, ZLInd, EC, ErrorCorrecting

By John Ehlers and Ric Way

The zero-lag indicator (ZLIndicator) is a variation of the EMA which modifies the EMA by trying to minimize the error (distance price - error correction) and thus reduce the lag

Formula:

*   EMA(data, period)
    
*   For each iteration calculate a best-error-correction of the ema (see the paper and/or the code) iterating over `-bestgain` -> `+bestgain` for the error correction factor (both incl.)
    
*   The default moving average is EMA, but can be changed with the parameter `_movav`
    
    **NOTE**: the passed moving average must calculate alpha (and 1 - alpha) and make them available as attributes `alpha` and `alpha1` in the instance
    

See also:

*   [http://www.mesasoftware.com/papers/ZeroLag.pdf](http://www.mesasoftware.com/papers/ZeroLag.pdf)

Lines:

*   ec

Params:

*   period (30)
    
*   gainlimit (50)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ec:

### ZeroLagIndicatorEnvelope

Alias:

*   ZLIndicatorEnvelope, ZLIndEnvelope, ECEnvelope, ErrorCorrectingEnvelope

ZeroLagIndicator and envelope bands separated “perc” from it

Formula:

*   ec (from ZeroLagIndicator)
    
*   top = ec \* (1 + perc)
    
*   bot = ec \* (1 - perc)
    

See also:

*   [http://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:moving\_average\_envelopes](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)

Lines:

*   ec
    
*   top
    
*   bot
    

Params:

*   period (30)
    
*   gainlimit (50)
    
*   \_movav (EMA)
    
*   perc (2.5)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (False)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ec:
    
*   top:
    
    *   \_samecolor (True)
*   bot:
    
    *   \_samecolor (True)

### ZeroLagIndicatorOscillator

Alias:

*   ZeroLagIndicatorOsc, ZLIndicatorOscillator, ZLIndicatorOsc, ZLIndOscillator, ZLIndOsc, ECOscillator, ECOsc, ErrorCorrectingOscillator, ErrorCorrectingOsc

Oscillation of a ZeroLagIndicator around its data

Lines:

*   ec

Params:

*   period (30)
    
*   gainlimit (50)
    
*   \_movav (EMA)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   ec:
    
*   \_0:
    
    *   \_name (osc)

### haDelta

Alias:

*   haD

Heikin Ashi Delta. Defined by Dan Valcu in his book “Heikin-Ashi: How to Trade Without Candlestick Patterns “.

This indicator measures difference between Heikin Ashi close and open of Heikin Ashi candles, the body of the candle.

To get signals add haDelta smoothed by 3 period moving average.

For correct use, the data for the indicator must have been previously passed by the Heikin Ahsi filter.

Formula:

*   haDelta = Heikin Ashi close - Heikin Ashi open
    
*   smoothed = movav(haDelta, period)
    

Lines:

*   haDelta
    
*   smoothed
    

Params:

*   period (3)
    
*   movav (SMA)
    
*   autoheikin (True)
    

PlotInfo:

*   plot (True)
    
*   plotmaster (None)
    
*   legendloc (None)
    
*   subplot (True)
    
*   plotname ()
    
*   plotskip (False)
    
*   plotabove (False)
    
*   plotlinelabels (False)
    
*   plotlinevalues (True)
    
*   plotvaluetags (True)
    
*   plotymargin (0.0)
    
*   plotyhlines (\[\])
    
*   plotyticks (\[\])
    
*   plothlines (\[\])
    
*   plotforce (False)
    

PlotLines:

*   haDelta:
    
    *   color (red)
*   smoothed:
    
    *   color (grey)
    *   \_fill\_gt ((0, ‘green’))
    *   \_fill\_lt ((0, ‘red’))

var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("\_\_tabbed\_"))

(C) 2015-2024 Daniel Rodriguez

[](https://github.com/backtrader/backtrader "github.com")[](https://www.linkedin.com/in/daniel-rodriguez-66a6047/ "www.linkedin.com")

{"base": "../..", "features": \["content.code.copy", "navigation.path", "navigation.tabs", "navigation.tabs.sticky", "navigation.tracking", "search.highlight", "search.share", "search.suggest"\], "search": "../../assets/javascripts/workers/search.b8dbb3d2.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}} document$.subscribe(() => {document.querySelectorAll('.glightbox').forEach(function(element) { var imgSrc = element.querySelector('img').src; element.setAttribute('href', imgSrc); }); const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});})