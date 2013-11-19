#!/usr/bin/env python2.7
"""Creates and manages markdown, file based note system.

Usage: 
    tiro journal [--notebook=<notebook>] [--editor=<editor>] [<text> ...]
    tiro list [--max=<max>] [--notebook=<notebook>] [--files] <text> ...
    tiro log <log> <comment> ...
    tiro note [--notebook=<notebook>] [--editor=<editor>] [<text> ...]  
    tiro open [--editor=<editor>] [--max=<max>] <text> ...
    tiro summary [--max=<max>] 

Options:
    -e --editor=<editor>      Open files with the specified editor. [default: vim]
    -h --help                 Show this help.
    -n --notebook=<notebook>  Specify a specific notebook. [default: default]
    --max=<max>               Maximum results to display. [default: 10]
    --version                 Show version.

Command descriptions:
    journal - open a new or existing file named journal.<today>.txt
    list - list files matching keywords
    log - add a line with the current date and time to a file.
    note - create a new note and then open it - <text> becomes filename
    open - open an existing note that matches <text>
    summary - list all folders and the item counts in those folders

"""
import os
#import optparse
import shutil
#import random
import datetime
import sys
import cicero
import settings

# DocOpt is awesome. https://github.com/docopt/docopt
from docopt import docopt
args = docopt(__doc__, version='1.0')

def journal(args):
    print(args)

def list(args):
    print(args)
    cicero.list_notes_matching(args['--notebook'],args['<text>'])

def log(args):
    print(args)

def note(args):
    print(args)
    type = 'note'
    cicero.new_note(type,args['--notebook'],args['<text>'])

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
