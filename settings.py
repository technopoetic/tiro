#!/usr/bin/env python2.7
import ConfigParser
import os

home = os.path.expanduser('~')
Config = ConfigParser.ConfigParser()
Config.read(os.path.join(home,".tiro"))
NOTE_HOME = os.path.join(home,Config.get("compose", "home"))
NOTE_TEMPLATE = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates',Config.get("compose", "note_template")) 
JOURNAL_TEMPLATE = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates',Config.get("compose", "journal_template")) 
SPEC_TEMPLATE = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates',Config.get("compose", "spec_template")) 
DATE_FORMAT = Config.get("date", "format")
JOURNAL_DAY = Config.get("date", "journal_day")
JOURNAL_DIR = os.path.join(home,Config.get("compose", "journal_def_dir"))
NOTE_EXT = Config.get("compose", "extension")
DEBUG = Config.getboolean("devel", "debug")
