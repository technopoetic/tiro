#!/usr/bin/env python2.7
"""Creates and manages markdown, file based note system.

Usage: 
    tiro <note-type> [--notebook=<notebook>] [--editor=<editor>] [<text> ...]  
    tiro search [--max=<max>] [--notebook=<notebook>] [<text> ...]
    tiro open [--editor=<editor>] [--max=<max>] <text> ...
    tiro summary [--max=<max>] 

Options:
    -h --help                 Show this help.
    -n --notebook=<notebook>  Specify a specific notebook. 
    --max=<max>               Maximum results to display. [default: 10]
    --version                 Show version.

Command descriptions:
    search - list files matching keywords
    log - add a line with the current date and time to a file.
    note - create a new note and then open it - <text> becomes filename
    journal - create a new journal and then open it - <text> becomes filename
    open - open an existing note that matches <text>
    summary - list all folders and the item counts in those folders

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
    cicero.new_note(args['<note-type>'],args['--notebook'],args['<text>'])

def journal(args):
    cicero.new_note('journal',args['--notebook'],args['<text>'])

def spec(args):
    cicero.new_note('spec',args['--notebook'],args['<text>'])

def search(args):
    cicero.list_notes_matching(args['--notebook'],args['<text>'])

def log(args):
    print(args)

def open(args):
    print(args)

def summary(args):
    print(args)

# Run all the things!!!!
if __name__ == '__main__':
# Run any method named in the keyword args.
# Cool hack: use DocOpt args to call methods in this file.
#      Note that this only avails those methods whose name matches a
#      documented arg.
#    for method in dir():
    # Specials like 'search' and 'log' will get caught here
#        if (method in args) and args[method]:
#            if hasattr(locals()[method], '__call__'):
#                locals()[method](args)
#                sys.exit(0)

    if args['<note-type>'] == 'search':
        search(args)
    elif args['<note-type>'] == 'log':
        log(args)
    elif args['<note-type>'] == 'open':
        open(args)
    elif args['<note-type>'] == 'summary':
        summary(args)
    else:
        gen_note(args)

sys.exit(0)
