#!/usr/bin/env python2.7
"""Creates and manages markdown, file based note system.

Usage: 
    tiro journal [--notebook=<notebook>] [--editor=<editor>] [<text> ...]
    tiro search [--max=<max>] [--notebook=<notebook>] [<text> ...]
    tiro log <log> <comment> ...
    tiro note [--notebook=<notebook>] [--editor=<editor>] [<text> ...]  
    tiro open [--editor=<editor>] [--max=<max>] <text> ...
    tiro summary [--max=<max>] 

Options:
    -e --editor=<editor>      Open files with the specified editor. [default: vim]
    -h --help                 Show this help.
    -n --notebook=<notebook>  Specify a specific notebook. 
    --max=<max>               Maximum results to display. [default: 10]
    --version                 Show version.

Command descriptions:
    journal - open a new or existing file named journal.<today>.txt
    search - list files matching keywords
    log - add a line with the current date and time to a file.
    note - create a new note and then open it - <text> becomes filename
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

def journal(args):
    print(args)
    cicero.new_note('journal',args['--notebook'],args['<text>'])

def search(args):
    print(args)
    cicero.list_notes_matching(args['--notebook'],args['<text>'])

def log(args):
    print(args)

def note(args):
    print(args)
    cicero.new_note('note',args['--notebook'],args['<text>'])

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
    for method in dir():
        argname = method.replace('minion_', '')
        if (argname in args) and args[argname]:
            print "ARGNAME: " + argname
            if hasattr(locals()[method], '__call__'):
                locals()[method](args)

sys.exit(0)
