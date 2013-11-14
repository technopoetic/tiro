#!/usr/bin/env python2.7
import os
#import optparse
import shutil
#import random
import datetime
import sys
import settings
import tempfile, subprocess
from string import Template

def new_note(text):
    print "Note home is: " + settings.NOTE_HOME
    print "Note template is: " + settings.NOTE_TEMPLATE
    print "Journal template is: " + settings.JOURNAL_TEMPLATE
    print "Text args are: " + ' '.join(text)

    f = open(settings.NOTE_TEMPLATE, 'r')
    template_text = f.readlines()
    f.close()
    template_text = ''.join(template_text)
    print template_text
    
    data = {}
    title = ' '.join(text)
    if len(topic) == 0:
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
    print summary

    open_file(filename, 
                # editor=editor, 
            line=last)
    print summary

    # with tempfile.NamedTemporaryFile(suffix='md') as temp:
    #     subprocess.call(['vim', temp.name])
    #     text = open(temp.name, 'r').read()
    # print "Your text was: \n" + text 

def list_notes_matching(search_text):
    output = subprocess.check_output(["grep", "-R","-l", ''.join(search_text), settings.NOTE_HOME])
    print "Output of list is: " + output
    print "Type of output is: " 
    print type(output)

def getOutput(command):
        p1 = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
        output = p1.communicate()[0]
        return output

def get_filename_for_title(topic, notes_dir=None):
    if not os.path.exists(notes_dir):
        os.mkdir(notes_dir)

    topic_filename = string_to_file_name(topic)

    filename = "%s/%s" %(notes_dir, topic_filename)

    return filename


def string_to_file_name(text, ext='.md'):
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
