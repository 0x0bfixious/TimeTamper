# TimeTamper
 TimeTamper is a file timestamp modifier written in python. The script is made for Penetration Testers & Red Teamers.

# Functionality
 The script modifies ONLY the 'accessed' and 'modified' file timestamps. Not the 'created' timestamp.
 Very useful for covering your tracks & evading detection, after you have modified a file. :)
 And also, the script won't work if you don't have appropriate permissions on the target files & directories.

# USAGE:
To indicate recursive processing of directories, you can use the -r or --recursive flag.
```
python TimeTamper.py path/to/file_or_directory "MM/DD/YYYY" -r
```
For example: 
```
python TimeTamper.py ./privatestuff "09/13/2017" -r
```
This command will modify the timestamps of all files in the ./privatestuff directory (recursively) to September 13, 2017.

 # DISCLAIMER
 The tool is for Educational Purposes Only. 
 I am not responsible for any illegal/harmful activities done by those who use it.
 
