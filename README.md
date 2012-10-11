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

5. (Optional) Create a Twitter app at <https://dev.twitter.com/apps>,
then fill in the empty Twitter-related variables in `credentials.js`.
(Yes, this will soon be fixed so you're tweeting with a 'Teller'
Twitter client.)

6. Now run `teller.py`:

    `python teller.py bob "Hey Bob! Dude, flask rocks
    http://flask.pocoo.org/docs/quickstart/"`

where `bob` is the name of one of your friends whose contact info is
in `contacts.js`.

7. (Optional) Symlink the `teller.py` 

    chmod u+x ~/path/to/this/repo/teller/teller.py
    ln -s ~/path/to/this/repo/teller/teller.py ~/bin/teller

Ensure that `~/bin` is in your `$PATH`, then run Teller as originally
intended!

    tell bob "The inventor of the wiki just invented the federated
    wiki! https://github.com/WardCunningham/Smallest-Federated-Wiki"


## TODO

* Turn Teller into a web app that uses OAuth for authentication,
  listens for commands as a GTalk bot, and more

* Turn Teller into a SaaS product with the CLI and a Google Chrome
  extension as interfaces(???)

* Look at friend's shared Google Calendar and don't send IMs if s/he
  is busy

* Add Gmail contact import support so `contacts.js` need not be made
  manually

* Check to see if GTalk IM recipient is online, and only send the IM
  if s/he is.  Otherwise, go on to the next medium.

* Add support for `--via` syntax so we can type `bob --via sms Urgent
  message: ...`

* Add scrollback (i.e., pressing the up arrow or C-p should scroll up
  through user's command history)

* Replace the crappy, noisy `xmpppy` with a better module

* Support sending emails via something other than Gmail 

* Add support for the following recipients:

  * "twitter", "facebook", "tent.io" or "tent.is", "irc"

* Make it possible to send messages to named groups

* Start actually using the `aliases` field within each `contacts.js`
  entry


## DONE (completed TODO items)

* Make Teller easily callable ad-hoc from the command line as
  originally envisioned: symlink `teller.py` to `~/bin/tell` so one
  can run `$ tell bob "See you at 3?"`

* Add support for sending to multiple people at once with
  comma-separated syntax (e.g., `tell bob,aj "See you at 3?"`)
