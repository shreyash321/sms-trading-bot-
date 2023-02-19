# sms-trading-bot-
This is a python code for a trading bot which sends you sms notifications to your phone for buying or selling stocks using trading view indicators 
it uses twilio to send you sms ,so you have to make one account if you dont have , obtain the account_sid ,auth token and a phone number given by twilio for your account and put it inside the given code
it also uses tradingview-ta library to fetch the given stock price details ,then it applies different indicators to it and takes a majority voting of different indicators for buying or selling the stock
and twilio only sends sms to the verified numbers on this site - twilio.com/user/account/phone-numbers/verified , so get the receiver's number verified on it .
Once you have done all the steps ,your trading bot can send the sms to other person .

![image](https://user-images.githubusercontent.com/78251506/219942219-462f316a-d13b-4f4c-9bb4-0cfd79b1489e.png)
Here i have used tesla stock , you can experiment with any stock .
