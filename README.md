File_And_Music_Sorter 1.3
===========

This program allows the user to sort through subdirectories without having to deal
with the tedious mouse and keyboard labor that is usually associated with file/folder
organization.

Dependencies: this program uses the eyeD3 library for the music metadata processing, so please
make sure that you have it before you use it.

Notes: There may be bugs that doesn't let it copy/move everything. If you can report that to me, I
will gladly fix it up.

Functions:
  -Full directory copy: this copies everything in the original directory (subdirectories)
  and outputs it into a single compiled directory with all the files. (This is great for
  when you want to read mangas that are separated into chapters and you want to to constantly
  change folders every 16 images or so.)
  
  -Full directory move: this works the same way as the copy mode, just that it deletes the
  original files. Use this when you are sure that you don't want to have a backup.
  
  -Selective copy: this copy function askses the user the type of files that they want to sort,
  and then sorts the files in the directory into a new directory that contains labeled subdirectories
  of the file type that you wanted to sort. ( this is great for sorting through your download folder
  that you did not touch for ages, and just let it build up)
  
  -Selective Move: again this is the same as selective copy but deletes the original files. Use this
  only when you are sure that you do not want the orignal files as backup.
  
  -Artist Sort: this sorts your music files by the ID3 artist tag, it will output each artist into its
  own folder. If it doesn't have an artist tag, then it will be output into a seperate folder.
  
  Album Sort: works the same as artist sort but sorts it by albums.
  
  -Emptydir: This parses through the directory and its subdirectories, and deletes any empty directories
  that it finds.
