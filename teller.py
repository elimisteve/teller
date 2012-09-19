#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.09.18

import simplejson
import sys

CREDENTIALS_FILENAME = './credentials.js'
MEDIUMS = ["aim", "cloakcast", "email", "gtalk", "sms"]

USAGE = """Usage syntax: friend message"""

def get_email_credentials():
    creds = simplejson.loads(open(CREDENTIALS_FILENAME, 'r').read())
    username = creds["username"]
    password = creds["password"]
    if password == "" and len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        print "Include email password in credentials.js or at command line"
        sys.exit(1)
    return username, password


def tell(medium, friend, msg):
    if medium not in MEDIUMS:
        return "Medium '%s' not recognized" % (medium,)

    config = CONFIG[friend]
    # TODO: Fill in these stubs
    if medium == "aim":
        print "IMing %s over AIM" % (friend,)
    elif medium == "cloakcast":
        print "Clandestinely messaging %s via Cloakcast" % (friend,)
    elif medium == "email":
        print "Emailing", friend
    elif medium == "gtalk":
        print "IMing %s via GTalk" % (friend,)
    elif medium == "sms":
        print "Texting", friend
    return ""


def main():
    username, password = get_email_credentials()
    while True:
        try:
            from_user = raw_input("> ")
        except EOFError:
            print
            break
        try:
            first_space = from_user.index(' ')
        except ValueError:
            print "Bad input"
            print USAGE
            continue

        friend, msg = from_user[:first_space], from_user[first_space+1:]
        if friend in CONFIG:
            for medium in CONFIG[friend]["try_order"]:
                error = tell(medium, friend, msg)
                if error:
                    print error,
                    print "(%s didn't work; trying next medium)" % (medium,)
                    continue
                else:
                    print "Message successfully sent to", friend
                    break
        else:
            print "Friend '%s' not found; try again" % (friend,)
            print "TODO: search CONFIG aliases"


if __name__ == '__main__':
    CONFIG = simplejson.loads(open('./config.js', 'r').read())
    main()
