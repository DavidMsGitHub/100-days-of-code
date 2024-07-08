from twilio.rest import Client

account_sid = 'AC68fb2ed945063898a8b833ce6723cfd3'
auth_token = '29fb9bccd6fef386293c11261f9c91aa'

def send_rain_message():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_ = '+12255905385',
        body = 'dges iwvimebs bro amitomac mtlad zafxulic ar gegonos☔️',
        to = '+995599544130'
    )

    print(message.status)