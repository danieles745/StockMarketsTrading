# StockMarketsTrading
This is a project that makes a ETL process in order to dispose stock market data in AWS and to be consumed by the traders.

To run this code, is necessary that the user executes this command: "\venv\Scripts\activate.bat" (if user use   s windows) in order to activate virtual environment where is hosted all of dependencies and libraries. Could happen that %PATH% environment variable doesnt change the location of the project when is ran in another server. User must take care.

Before to execute coordinator.py file, the user must edit the config.json file. This file contains some parameters that are necessaries to allow to enter to aws and downloading data from Yahoo Finance API since these parameters will indicate us the way in terms of period of time and frequency that we have to get info.  

Execute coordinator.py file

Finally, we use some of the symbols hat has been taken from yahoo finance API cause of the aws limitations in terms of costs that we have if we exceded capacities.