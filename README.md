# Teller README

Teller is the fastest way to tell anyone anything via the command line

## Quickstart

1. Run these commands:

    `git clone git://github.com/elimisteve/teller.git`

    `cd teller`

    `sudo pip install -r requirements.txt`

2. Add your friends'/contactees' contact info to `contacts.js`

3. (Optional) Add your Twilio account and token credentials to
`twilio_creds.py` to send SMS messages

4. (Optional) Add your Gmail credentials to `credentials.js` (at least
define your username) to send emails

5. Now run `teller.py`, optionally including your Gmail password in
case you didn't want it saved to `credentials.js`, like this:

    `python teller.py optional_gmail_password`

That's it! Now you're ready to tell Teller who to tell what, all with
this syntax:

    bob Hey Bob! Dude, flask rocks http://flask.pocoo.org/docs/quickstart/


## TODO

* Look at friend's shared Google Calendar and don't send IMs if s/he
  is busy

* Check to see if GTalk IM recipient is online, and only send the IM
  if s/he is.  Otherwise, go on to the next medium.

* Add support for `--via` syntax so we can type `bob --via sms Urgent
  message: ...`

* Make Teller easily callable ad-hoc from the command line as
  originally envisioned: symlink `teller.py` to `~/bin/tell` so one
  can run `$ tell bob See you at 3?`

* Start actually using the `aliases` field within each `contacts.js`
  entry

* Add scrollback (i.e., pressing the up arrow or C-p should scroll up
  through user's command history)

* Replace the crappy, noisy `xmpppy` with a new module

* Support sending emails via something other than Gmail 

* Add Gmail contact import support so `contacts.js` need not be made
  manually

* Turn Teller into a SaaS product with the CLI and a Google Chrome
  extension as interfaces(???)
