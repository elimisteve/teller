#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.09.18

from helpers import send_sms, send_im, send_email, clean_phone

import os
import simplejson
import sys

# Set paths and file locations
TELLER_PATH = os.path.dirname(os.path.realpath(__file__)) + '/'
CREDENTIALS_FILENAME = TELLER_PATH + 'credentials.js'
CONTACTS_FILENAME = TELLER_PATH + 'contacts.js'

VALID_MEDIUMS = ["cloakcast", "email", "gtalk", "sms"]

USAGE = "Usage syntax:\n\n" + \
    "    tell bob Duuude news.ycombinator.com rocks, check it\n\n" + \
    "where 'bob' is your friend's name and the rest is the message\n" + \
    "(and don't forget to add your friends' contact info to contacts.js!)"


def get_email_credentials():
    creds = simplejson.loads(open(CREDENTIALS_FILENAME, 'r').read())
    username = creds["username"]
    password = creds["password"]
    if password == "":
        print "Add email password to", CREDENTIALS_FILENAME
        sys.exit(1)
    return username, password


def tell(medium, friend, msg):
    if medium not in VALID_MEDIUMS:
        return "Medium '%s' not recognized" % (medium,)

    config = CONFIG[friend]
    if medium == "cloakcast":
        # TODO: Add cloakcast support
        print "Clandestinely messaging %s via Cloakcast" % (friend,)
    elif medium == "email":
        return send_email(EMAIL_USERNAME, EMAIL_PASSWORD, [config[medium]], msg)
    elif medium == "gtalk":
        return send_im(EMAIL_USERNAME, EMAIL_PASSWORD, config[medium], msg)
    elif medium == "sms":
        return send_sms(config[medium], msg)
    return ""


def main():
    # User input contains a space, and therefore includes his/her
    # friend's name as well as the message to said friend
    if len(sys.argv) < 3:
        print USAGE
        sys.exit(1)

    friends, msg = sys.argv[1], ' '.join(sys.argv[2:])
    friends = friends.lower()

    for friend in friends.split(','):
        if friend in CONFIG:
            for medium in CONFIG[friend]["try_order"]:
                error = tell(medium, friend, msg)
                if error:
                    print error,
                    print "(%s didn't work; trying next medium)" % (medium,)
                    continue
                else:
                    print "Message successfully sent to", friend, "via", medium
                    break
        else:
            # TODO: search CONFIG aliases
            print "Friend '%s' not found; try again" % (friend,)


if __name__ == '__main__':
    EMAIL_USERNAME, EMAIL_PASSWORD = get_email_credentials()
    CONFIG = simplejson.loads(open(CONTACTS_FILENAME, 'r').read())
    for friend in CONFIG:
        # Clean phone numbers in contacts.js into sequences of digits
        CONFIG[friend]["sms"] = clean_phone( CONFIG[friend]["sms"] )
    main()
