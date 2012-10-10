#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.08.30

from twilio.rest import TwilioRestClient
from twilio_creds import account, token

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
    client = xmpp.Client('gmail.com', debug=[])
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


def clean_phone(num_str):
    return ''.join(re.findall("\d+", num_str))
