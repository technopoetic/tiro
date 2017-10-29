#!/usr/bin/env python2.7
import ConfigParser
import os

# Convert config file settings into CONSTANTS
home = os.path.expanduser('~')
Config = ConfigParser.ConfigParser()
#TODO: Create a default set of configs.  If the file isn't there, then errors are thrown.
Config.read(os.path.join(home,'.tiro'))

NOTE_HOME = os.path.join(home,Config.get('compose', 'home'))
LOG_FILE = os.path.join(home,Config.get('compose', 'home'),Config.get('compose', 'logfile'))
DEFAULT_NOTE_TYPE = Config.get('compose', 'default_note_type')
DATE_FORMAT = Config.get('date', 'format')
JOURNAL_DAY = Config.get('date', 'journal_day')
JOURNAL_DIR = os.path.join(home,Config.get('compose', 'journal_def_dir'))
NOTE_EXT = Config.get('compose', 'extension')
DEBUG = Config.getboolean('devel', 'debug')
EDITOR = Config.get('compose', 'editor')
