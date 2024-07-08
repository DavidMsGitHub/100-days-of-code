from twilio.rest import Client

account_sid = 'AC68fb2ed945063898a8b833ce6723cfd3'
auth_token = '29fb9bccd6fef386293c11261f9c91aa'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12255905385',
  body='zd davit es me var twilio',
  to='+995599544130'
)

print(message.sid)