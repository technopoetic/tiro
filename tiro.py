#!/usr/bin/env python2.7
"""Creates and manages markdown, file based note system.

Usage: 
    tiro note -t <note-type> [-n <notebook>] [--editor=<editor>] [<text> ...]  
    tiro log <text>
    tiro cat -s <start> -n <display-num>
    tiro search [--max=<max>] [--notebook=<notebook>] [<text> ...]
    tiro open [--editor=<editor>] [--max=<max>] <text> ...
    tiro summary [--max=<max>] 

Options:
    -h --help                 Show this help.
    -t --type=<note-type>     Specify note type
    -n --notebook=<notebook>  Specify a specific notebook. 
    --max=<max>               Maximum results to display. [default: 10]
    --version                 Show version.

Command descriptions:
    search - list files matching keywords
    log - append <text> with the current date and time to a file
    note - create a new note and then open it - <text> becomes filename
    open - open an existing note that matches <text>
    summary - list all notebooks and the note counts in each

"""
import os
import shutil
import datetime
import sys
import cicero
import settings

# DocOpt is awesome. https://github.com/docopt/docopt
from docopt import docopt
args = docopt(__doc__, version='1.0')

#def note(args):
#    cicero.new_note('note',args['--notebook'],args['<text>'])

def gen_note(args):
    cicero.new_note(args['--type'],args['--notebook'],args['<text>'])

def journal(args):
    cicero.new_note('journal',args['--notebook'],args['<text>'])

def spec(args):
    cicero.new_note('spec',args['--notebook'],args['<text>'])

def search(args):
    cicero.list_notes_matching(args['--notebook'],args['<text>'])

def log(args):
    cicero.log(args['<text>'])

def cat(args):
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    start = args.get('<start>', today)
    cicero.cat(start)

def tiro_open(args):
    print(args)

def summary(args):
    print(args)

# Run all the things!!!!
if __name__ == '__main__':
    if args.get('search',False):
        search(args)
    elif args.get('log',False):
        log(args)
    elif args.get('cat',False):
        cat(args)
    elif args.get('open',False):
        tiro_open(args)
    elif args.get('summary',False):
        summary(args)
    elif args.get('note',False):
        gen_note(args)
    else:
        gen_note(args)

sys.exit(0)
