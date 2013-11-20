Tiro
====

Tiro is a command line note taking application written in python.  It attempts to sorta, kinda emulate that cool note taking system with the Elephant.  Basically, notebooks are directories on the file system, and notes are text files, located in those notebook/directories.  Tiro can create new notes, and search existing notes.  Your notes are just files, so you're always free to modify them and move them around.  Also, right now it kind of leans toward Markdown, but you can use plain text formats as well.

Features planned in the short term include:
* Open existing notes.  Right now, the way you do this is just list the notes, then open a specific one.  A side effect of the current implementation is that if you attempt to create a new note with the same name as an existing note, then you just open the existing note with a new entry.  Hmmm...  That actually seems like opening an existing note.  Have to work on that one.

Possible features for the longer term include:
* Tagging?  Right now, I don't even know what that would look like.  Maybe file metadata, but that isn't really well supported across filesystems.  Maybe just adding a metadata field to the note itself.  Since 

Installation
============
Just clone the repo, and copy (or symlink) the .tiro file to your home directory.  You could also add tiro to your path, but what I've been doing is just create an alias in my .bashrc like this:  
alias tiro='~/code/python/tiro/tiro.py' 

Usage
=====
Create a new note in the default notebook:
tiro note Some text for a title 

List the contents of a notebook:
tiro search -n NOTEBOOK_NAME

Interactively search for notes containing some text in a specific notebook:
tiro search -n NOTEBOOK_NAME text to search for
**Note** the search functionality just uses grep with some sane default parameters to search all notes in the notebook, recursively, and case-insensitively.  It doesn't do any parsing of the text that you pass to it.  It just treats the search text as a phrase.
