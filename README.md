# Yahoo World Indices Scraper

This is a demo project that uses python - request and behave to scrape the world indices published by yahoo finance. This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

* Python 3.7 above
* requests==2.23.0
* lxml==4.5.0
*urlib3==1.25.9`

Steps for installation:

1. git clone repo
1. pip install -r requirements.txt
1. run script

Results:

|Symbol    |Name                                    |Last Price     |Change         |%change        |
|----------|-------------------|---------------|---------------|---------------|
|^GSPC     |S&P 500             |2,836.74       |+38.94         |+1.39%         |
|^DJI      |Dow 30              |23,775.27      |+260.01        |+1.11%         |
|^IXIC     |Nasdaq              |8,634.52       |+139.77        |+1.65%         |
|^NYA      |NYSE COMPOSITE (DJ) |11,017.90      |+101.22        |+0.93%         |
|^XAX      |NYSE AMEX COMPOSITE INDEX|1,791.18       |+15.27         |+0.86%         |
|^BUK100P  |Cboe UK 100 Price Return|9,732.30       |-118.98        |-1.21%         |
|^RUT      |Russell 2000        |1,233.05       |+18.99         |+1.56%         |
|^VIX      |Vix                 |35.93          |-5.45          |-13.17%        |
|^FTSE     |FTSE 100            |5,752.23       |-74.38         |-1.28%         |
|^GDAXI    |DAX PERFORMANCE-INDEX|10,336.09      |-177.70        |-1.69%         |
|^FCHI     |CAC 40              |4,393.32       |-57.68         |-1.30%         |
|^STOXX50E |ESTX 50 PR.EUR      |2,809.07       |-43.39         |-1.52%         |
|^N100     |EURONEXT 100        |865.80         |-12.11         |-1.38%         |
|^BFX      |BEL 20              |2,942.98       |-74.78         |-2.48%         |
|IMOEX.ME  |MOEX Russia Index   |2,562.03       |-37.38         |-1.44%         |
|^N225     |Nikkei 225          |19,262.00      |-167.44        |-0.86%         |
|^HSI      |HANG SENG INDEX     |23,831.33      |-145.99        |-0.61%         |
|000001.SS |SSE Composite Index |2,808.53       |-29.97         |-1.06%         |
|^STI      |STI Index           |2,518.16       |-24.21         |-0.95%         |
|^AXJO     |S&P/ASX 200         |5,242.60       |+25.50         |+0.49%         |
|^AORD     |ALL ORDINARIES      |5,300.70       |+27.90         |+0.53%         |
|^BSESN    |S&P BSE SENSEX      |31,327.22      |-535.86        |-1.68%         |
|^JKSE     |Jakarta Composite Index|4,496.06       |-97.49         |-2.12%         |
|^KLSE     |FTSE Bursa Malaysia KLCI|1,369.85       |-11.79         |-0.85%         |
|^NZ50     |S&P/NZX 50 INDEX GROSS|10,419.48      |-26.63         |-0.25%         |
|^KS11     |KOSPI Composite Index|1,889.01       |-25.72         |-1.34%         |
|^TWII     |TSEC weighted index |10,347.36      |-19.15         |-0.18%         |
|^GSPTSE   |S&P/TSX Composite index|14,420.36      |+169.27        |+1.19%         |
|^BVSP     |IBOVESPA            |75,330.61      |-4,342.69      |-5.45%         |
|^MXX      |IPC MEXICO          |34,586.82      |+346.22        |+1.01%         |
|^IPSA     |S&P/CLX IPSA        |5,058.88       |0.00           |0.00%          |
|^MERV     |MERVAL              |38,390.84      |+233.89        |+0.61%         |
|^TA125.TA |TA-125              |1,381.28       |+38.12         |+2.84%         |
|^CASE30   |EGX 30 Price Return Index|10,377.20      |+575.87        |+5.88%         |
|^JN0U.JO  |Top 40 USD Net TRI Index|2,582.86       |-1.38          |-0.05%         |
