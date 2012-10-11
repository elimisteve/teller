#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.08.30

from twilio.rest import TwilioRestClient
from twilio_creds import account, token

import oauth2 as oauth
import re
import smtplib
import time
import twilio
import xmpp


def send_sms(recipient, msg):
    client = TwilioRestClient(account, token)
    FROM = '+14155992671'
    if len(recipient) == 10:
        recipient = "+1"+recipient
    try:
        message = client.sms.messages.create(to=recipient, from_=FROM, body=msg)
        # print message.body
    except twilio.TwilioRestException, e:
        return e

    # TODO: Legitimately check for errors
    return ""


def send_im(username, password, recipient, msg):
    # Create client
    client = xmpp.Client('gmail.com')
    client.connect( ('talk.google.com', 5223) )

    # Connect/Authenticate
    jid = xmpp.protocol.JID(username)
    client.auth(jid.getNode(), password)

    # Send IM
    message = xmpp.protocol.Message(recipient, msg, typ="chat")
    error_code = client.send(message)
    if error_code == "1":
        return "Failed SASL authentification: not-authorized"
    elif error_code == "3":
        print "GTalk IM sent successfully (these sometimes show up a bit late)"
        return ""
    else:
        return "Something bad happened! :-\ Tell elimisteve@gmail.com"


def send_email(username, password, recipients, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)

    body = """\
From: %s
To: %s
Subject: %s

%s
""" % (username, ", ".join(recipients), "Sent via Teller", msg)

    server.sendmail(username, recipients, body)
    server.quit()
    # TODO: Legitimately check for errors
    return ""


## NOT YET BEING USED. Doesn't quite work...
def twitter_tokens(consumer_key, consumer_secret):
    # Create your consumer with the proper key/secret.
    consumer = oauth.Consumer(key=consumer_key,
                              secret=consumer_secret)

    # Request token URL for Twitter.
    request_token_url = "http://twitter.com/oauth/request_token"

    # Create our client.
    client = oauth.Client(consumer)

    # The OAuth Client request works just like httplib2 for the most part.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] == '200':
        pairs = content.split('&')
        for pair in pairs:
            if pair.startswith('oauth_token='):
                oauth_token = pair.split('=')[-1]
            elif pair.startswith('oauth_token_secret='):
                oauth_secret = pair.split('=')[-1]
        return oauth_token, oauth_secret
    else:
        return content


def send_tweet(consumer_key, consumer_secret, url, key, secret,
              http_method="GET", post_body=None, http_headers=None):
    consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)

    resp, content = client.request(
        url,
        method=http_method,
        body=post_body,
        headers=http_headers,
        force_auth_header=True
    )
    if resp['status'] == '200':
        return ""
    else:
        return resp, content


def clean_phone(num_str):
    return ''.join(re.findall("\d+", num_str))
