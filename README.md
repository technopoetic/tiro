Tiro
====

Tiro is a command line note taking application written in python.  It attempts to sorta, kinda emulate that cool note taking system with the Elephant.  Basically, notebooks are directories on the file system, and notes are text files, located in those notebook/directories.  Tiro can create new notes, and search existing notes.  Your notes are just files, so you're always free to modify them and move them around.  Also, right now it kind of leans toward Markdown, but you can use plain text formats as well.

Features implemented right now:
* Create new notes based on templates. 
* Search notes for text strings.  Right now, this is just grep with some sane defaults.
* Open existing notes.  Right now, the way you do this is to search for a given term, then open the best match.  A side effect of the current implementation is that if you attempt to create a new note with the same name as an existing note, then you just open the existing note with a new entry.  

Possible features for the longer term include:
* Tagging?  Right now, I don't even know what that would look like.  Maybe file metadata, but that isn't really well supported across filesystems.  Maybe just adding a metadata field to the note itself. 
* More powerful templates.

Installation
============
Just clone the repo, and copy (or symlink) the .tiro file to your home directory.  You could also add tiro to your path, but what I've been doing is just create an alias in my .bashrc like this:  
alias tiro='~/code/python/tiro/tiro.py' 

Usage
=====
The general pattern is:
`tiro <template> --notebook <Title text>`

Create a new note in the default notebook:
`tiro note Some text for a title` 

Create a new Journal type note:
`tiro journal`

List the contents of a notebook:
`tiro search -n NOTEBOOK_NAME`

Interactively search for notes containing some text in a specific notebook:
`tiro search -n NOTEBOOK_NAME text to search for`

Templates
=========
You can define templates to be used for your note types.  Tiro will search the 'templates' directory for a file that matches the <template> passed in, so for instance, if you have a file called 'note_template.txt' in the templates directory, then `tiro note Some text` will use that template, to create a file called Some-text.md in the default notebook.

Templates are python string Templates (https://docs.python.org/2/library/string.html#template-strings).

**Note:** the search functionality just uses grep with some sane default parameters to search all notes in the notebook, recursively, and case-insensitively.  It doesn't do any parsing of the text that you pass to it.  It just treats the search text as a phrase.
