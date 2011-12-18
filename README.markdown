# Chatter

Chatter is a quick and dirty realtime chat application written with Flask and
Juggernaut.


## Requirements

Chatter needs a running juggernaut server which itself needs redis. Beyond that
Flask is of course needed. Additionally the runner script makes use of gevent
so that might also be needed.

Running should be as simple as:
    
    $ python runner.py
