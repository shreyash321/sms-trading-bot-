from twilio.rest import Client
from tradingview_ta import TA_Handler, Interval, Exchange
# Your Twilio account SID and auth token
account_sid = "your account sid"
auth_token = "your auth token"

# Initialize the Twilio client
client = Client(account_sid, auth_token)
output = TA_Handler(
        symbol='TSLA',
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_5_MINUTES
        )
jd=str(output.get_analysis().summary['RECOMMENDATION']+' Tesla STOCK')
kd=str("Hello i am your stock market BOT , RECOMMENDATION - ")
# Send a message
message = client.messages.create(
    to="+919325879549",  # The phone number you want to send the message to
    from_="+18038860806",  # Your Twilio phone number
    body= kd+jd)
print("Message SID:", message.sid)