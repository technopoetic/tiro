#!/usr/bin/env python2.7
import os
import shutil
import datetime
import settings
import tempfile, subprocess
from string import Template

template_map = {
        'note': settings.NOTE_TEMPLATE,
        'journal': settings.JOURNAL_TEMPLATE
        }

def new_note(notetype, notebook, text):
    """ Build and open a new note in the specified (or default) notebook. """
    print "Note home is: " + settings.NOTE_HOME
    print "Note template is: " + settings.NOTE_TEMPLATE
    print "Journal template is: " + settings.JOURNAL_TEMPLATE
    print "Text args are: " + ' '.join(text)
    print "Notebook is:  {0}".format(notebook)
    filename, last, summary = template_init(notetype, settings.NOTE_HOME, text)
    open_file(filename, line=last)
    print summary

def list_notes_matching(notebook,search_text):
    output = search_notes(notebook, search_text) 
    for index,filename in enumerate(output):
        if filename:
            print "[{0}]: {1}".format(index, filename)
    to_open = int(raw_input("Enter the number of the file to open: "))
    open_file(output[to_open])

def getOutput(command):
        p1 = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
        output = p1.communicate()[0]
        return output

def get_filename_for_title(topic, notes_dir=settings.NOTE_HOME):
    if not os.path.exists(notes_dir):
        os.mkdir(notes_dir)

    topic_filename = string_to_file_name(topic)

    filename = "%s/%s" %(notes_dir, topic_filename)

    return filename


def string_to_file_name(text, ext=settings.NOTE_EXT):
    new_name = text.replace(' ', '-').replace('/', '-')
    # if not (new_name.endswith('.txt') or new_name.endswith('.pdf')):
    if not new_name.endswith(ext):
        new_name = '%s%s' % (new_name, ext)
    return new_name

def open_file(filename, 
        line=0, 
        multiple = False, 
        graphical = False):
    print "Opening %s" % filename
    program = 'vim'
    subprocess.call([program, filename, "+%d" % (line + 2)])
        # subprocess.Popen([program, filename])
        # subprocess.Popen([editor, filename, "+%d" % (line + 2)])

def template_init(note_type, notebook, text):
    f = open(template_map[note_type], 'r')
    template_text = f.readlines()
    f.close()
    template_text = ''.join(template_text)
    
    data = {}
    title = ' '.join(text)
    if len(title) == 0:
        print getOutput('cal')
        title = raw_input("Note Title? ")

    filename = get_filename_for_title(title, settings.NOTE_HOME)
    today = datetime.date.today()
    today = today.strftime(settings.DATE_FORMAT)
    summary = "%s\nCreated %s" % (title, today)

    data['title'] =  title
    data['filename'] = filename 
    data['today'] = today

    t = Template(template_text)
    file_text = t.safe_substitute(data)

    f = open(filename, 'a')
    f.write(file_text)
    f.close()

    last = len('\n'.split(file_text)) + 1
    return (filename, last, summary)

def search_notes(notebook,search_text):
    output = subprocess.check_output(["grep", "-R","-i", "-l", ' '.join(search_text), settings.NOTE_HOME])
    outarray = output.split('\n')
    return outarray

