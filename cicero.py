#!/usr/bin/env python2.7
import os
import shutil
import datetime
import settings
import tempfile, subprocess
from string import Template
from os import listdir
from os.path import isfile, join

# Creates a dict to map the note type to it's template.  This lets me use a different template for a regular note, vs a Journal entry.
template_map = {
        'note': settings.NOTE_TEMPLATE,
        'journal': settings.JOURNAL_TEMPLATE,
        'spec': settings.SPEC_TEMPLATE
        }

def new_note(notetype, notebook, text):
    """ Build and open a new note or journal in the specified (or default) notebook. """
    if settings.DEBUG:
        print "Note home is: " + settings.NOTE_HOME
        print "Note template is: " + settings.NOTE_TEMPLATE
        print "Journal template is: " + settings.JOURNAL_TEMPLATE
        print "Text args are: " + ' '.join(text)
        print "Notebook is:  {0}".format(notebook)
        print "Note Type is:  {0}".format(notetype)
    title = get_title(text, notetype)
    filename = get_filename_for_title(title, notetype, notebook )
    if os.path.isfile(filename):
        exist_action = raw_input("Tiro found an already existing file.  Type o to open the existing file, or n to open a new one.")
        if exist_action == 'o':
            open_file(filename)
        elif exist_action == 'n':
            last, summary = template_init(notetype, notebook, filename, title)
            open_file(filename, last)
            print summary
    else:
        last, summary = template_init(notetype, notebook, filename, title)
        open_file(filename, last)
        print summary

def list_notes_matching(notebook,search_text):
    """ Given a notebook, and a text string to search for, lists the notes that contain the search string.
        Without a notebook, it searches recursively from NOTE_HOME.
        Without text, it just lists the contents of the given (or default) notebook.
        Uses grep & ls to perform these actions.
    """
    output = search_notes(search_text, notebook)
    if type(output) == list:
        for index,filename in enumerate(output):
            if filename and os.path.isfile(filename):
                print "[{0}]: {1}".format(index, filename)
        to_open = raw_input("Enter the number of the file to open (c to cancel): ")
        if to_open != 'c':
            open_file(output[int(to_open)])
    else:
        print "No files found that match the query string: {0}".format(search_text[0])
        os._exit(1)

def getOutput(command):
    """ Returns the output of a shell command. """
    #TODO: Should be able to get rid of this using 'check_output' instead of Popen and communicate..
    p1 = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
    output = p1.communicate()[0]
    return output

def get_filename_for_title(topic, note_type, notes_dir=None ):
    """ Converts the text argument into a filesystem safe name and path.
        For Journal entries, it also checks to see if there's a default journal directory defined.  Also for journal entries, if the text argument is empty, then it creates a new Journal title based on the date."""
    if notes_dir:
        note_path = os.path.join(settings.NOTE_HOME, notes_dir)
    elif note_type == 'journal':
        try:
            note_path = os.path.join(settings.JOURNAL_DIR)
        except AttributeError:
            print "No Default Journal Directory defined"
            note_path = settings.NOTE_HOME
    else:
        note_path = settings.NOTE_HOME
    if not os.path.exists(note_path):
        os.mkdir(note_path)

    topic_filename = string_to_file_name(topic)

    filename = "%s/%s" %(note_path, topic_filename)

    return filename


def string_to_file_name(text, ext=settings.NOTE_EXT):
    """ Strips trailing & leading whitespace, replaces slashes and spaces with dashes."""
    text = text.strip()
    new_name = text.replace(' ', '-').replace('/', '-')
    if not new_name.endswith(ext):
        new_name = '%s%s' % (new_name, ext)
    return new_name

def open_file(filename,
        line=0,
        multiple = False,
        graphical = False):
    print "Opening %s" % filename
    subprocess.call([settings.EDITOR, filename] )
    return

def get_title(text, note_type):
    """ Builds a title from the text argument.  If the text arg is missing for a note, then it prompts for a title, for a Journal, it generates a title."""
    title = ' '.join(text)
    if len(title) == 0 and note_type == 'journal':
        title = make_journal_title()
    elif len(title) == 0:
        print getOutput('cal')
        title = raw_input("Note Title? ")
    return title

def make_journal_title():
    """ My journal is weekly.  There's a config option 'journal_day' that lets me set the day of the week that my journal is based on.  So, if I don't pass in a specific title, it will just create a new journal titled 'Journal-date-of-next-journal-day.md'. """
    #TODO: Make the generated journal title a configurable pattern
    daymap = {
            'monday':0,
            'tuesday':1,
            'wednesday':2,
            'thursday':3,
            'friday':4,
            'saturday':5,
            'sunday':6
            }
    today = datetime.date.today()
    journal_day = today + datetime.timedelta( (daymap[settings.JOURNAL_DAY.lower()]-today.weekday()) % 7 )
    return 'Journal {0}'.format(journal_day);

def get_template_text(note_type):
    #See if we have a template that matches
    template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates')
    onlyfiles = [f for f in listdir(template_path) if isfile(join(template_path, f))]
    template_match = [t for t in onlyfiles if t.split('_',1)[0] == note_type]
    template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates',template_match[0])
    template_text = ''
    if template_path != None:
        """ Reads the text of the template. """
        try:
            f = open(template_path, 'r')
            template_text = f.readlines()
            f.close()
            template_text = ''.join(template_text)
        except IOError:
            print "Can't open template file: {0}".format(template_path)
            template_text = ''
    return template_text

def template_init(note_type, notebook, filename, title):
    template_text = get_template_text(note_type)

    today = datetime.date.today()
    today = today.strftime(settings.DATE_FORMAT)
    summary = "{0}\nCreated {1}".format(title, today)

    data = {}
    data['title'] =  title
    data['filename'] = filename
    data['today'] = today

    t = Template(template_text)
    file_text = t.safe_substitute(data)

    f = open(filename, 'a')
    f.write(file_text)
    f.close()

    last = len('\n'.split(file_text)) + 1
    return (last, summary)

def search_notes(search_text,notebook=None):
    if notebook:
        note_path = os.path.join(settings.NOTE_HOME, notebook)
    else:
        note_path = settings.NOTE_HOME
    if search_text:
        try:
            output = subprocess.check_output(["grep", "-R","-i", "-l", ' '.join(search_text), note_path])
            outarray = output.split('\n')
            return outarray
        except subprocess.CalledProcessError, e:
            return e
    else:
        try:
            output = subprocess.check_output(["find", note_path])
            outarray = output.split('\n')
            return outarray
        except subprocess.CalledProcessError, e:
            return e
