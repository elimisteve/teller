# Teller README

Teller is the fastest, easiest way to tell anyone anything via the
command line

## Quickstart

    git clone git://github.com/elimisteve/teller.git
    cd teller
    sudo pip install -r requirements.txt

Now add your friend's/contactee's contact info to `config.js` and, optionally, your Twilio account and token credentials to `twilio_creds.py`. You'll probably want to add your Gmail credentials to `credentials.js` (at least define your username). Now run `teller.py`, optionally including your Gmail password in case you didn't want it saved to `credentials.js`

    python teller.py [optional_gmail_password]

That's it! Now you're ready to tell Teller who to tell what with this
syntax:

    bob Hey Bob! Dude, flask rocks http://flask.pocoo.org/docs/quickstart/


## TODO

* Add support for `--via` syntax so we can type `bob --via sms Urgent
  message: ...`

* Make Teller easily callable ad-hoc from the command line as originally envisioned: symlink to `~/bin/` so one can run `$ tell aj See you at 3?`

* Add scrollback (i.e., pressing the up arrow or C-p should scroll up
  through user's command history)

* Replace the crappy, noisy `xmpppy` with a new module

* Support sending emails via something other than Gmail 

* Add Gmail contact import support so `config.js` need not be made
  manually

* Check to see if GTalk IM recipient is online, and only send the IM
  if s/he is.  Otherwise, go on to the next medium.
