#!/usr/bin/env python2.7
import ConfigParser
import os

home = os.path.expanduser('~')
Config = ConfigParser.ConfigParser()
Config.read(os.path.join(home,".tiro"))
NOTE_HOME = os.path.join(home,Config.get("notes", "home"))
NOTE_TEMPLATE = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates',Config.get("compose", "note_template")) 
JOURNAL_TEMPLATE = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates',Config.get("compose", "journal_template")) 
DATE_FORMAT = Config.get("date", "format")
