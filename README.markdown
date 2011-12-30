# Chatter

Chatter is a quick and dirty realtime chat application written with Flask and
Juggernaut.


## Installation

Start by cloning this repository:

    $ git clone git://github.com/maxcountryman/chatter.git

This application does assume you have Node.js installed so that you can make
use of npm and run Juggernaut. You will need npm to install Juggernaut if not
already installed:

    $ curl http://npmjs.org/install.sh | sh

Now you should be able to install Juggernaut:

    $ npm install -g juggernaut 

Once installed you will now need to run Juggernaut. Juggernaut serves as an
interface between the frontend of the application and the backend.

Finally before you can use the included runner you will need to install gevent.
Gevent is a coroutine-based module for concurrency. Here it serves the simple
task of reading off a file without blocking execution:

    $ pip install -U gevent

At this point you should be able to execute the runner script and point your
browser to `http://127.0.0.1:5000`.

## Usage

Once set up, ensure the Juggernaut server is already running and then simply
execute the runner script:

    $ python runner.py
