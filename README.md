Tiro
====

Tiro is a command line note taking application written in python.  It attempts to sorta, kinda emulate that cool note taking system with the Elephant.  Basically, notebooks are directories on the file system, and notes are text files, located in those notebook/directories.  Tiro can create new notes, and search existing notes.  Your notes are just files, so you're always free to modify them and move them around.  Also, right now it kind of leans toward Markdown, but you can use plain text formats as well.

Features planned in the short term include:
* A more interactive note search.  Right now, it just lists matching notes, but some kind of interaction is planned.
* Open existing notes.  Right now, the way you do this is just list the notes, then open a specific one.  A side effect of the current implementation is that if you attempt to create a new note with the same name as an existing note, then you just open the existing note with a new entry.  Hmmm...  That actually seems like opening an existing note.  Have to work on that one.

Possible features for the longer term include:
* Tagging?  Right now, I don't even know what that would look like.  Maybe file metadata, but that isn't really well supported across filesystems.  Maybe just adding a metadata field to the note itself.  Since 
