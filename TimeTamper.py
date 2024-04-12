import os
import datetime
import argparse

print ("""\
       
$$$$$$$$\ $$\                      $$$$$$$$\                                                    
\__$$  __|\__|                     \__$$  __|                                                   
   $$ |   $$\ $$$$$$\$$$$\   $$$$$$\  $$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
   $$ |   $$ |$$  _$$  _$$\ $$  __$$\ $$ | \____$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
   $$ |   $$ |$$ / $$ / $$ |$$$$$$$$ |$$ | $$$$$$$ |$$ / $$ / $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
   $$ |   $$ |$$ | $$ | $$ |$$   ____|$$ |$$  __$$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
   $$ |   $$ |$$ | $$ | $$ |\$$$$$$$\ $$ |\$$$$$$$ |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
   \__|   \__|\__| \__| \__| \_______|\__| \_______|\__| \__| \__|$$  ____/  \_______|\__|      
                                                                  $$ |                          
                                                                  $$ |                          
                                                                  \__|     Written by: 0x0bfixious

       """)

print(" This python script is made for Penetration Testers & Red Teamers.")
print(" The script modifies ONLY the 'accessed' and 'modified' file timestamps. Not the 'created' timestamp.")
print(" Useful for covering your tracks and evading detection.")
print(" The tool is for Educational Purposes Only. Do not condone in illegal activities.")
print(" I am not responsible for any illegal/harmful activities done by those who use it.")
print("""
      
      """)

def timetamper(file_path, new_timestamp):
    if os.path.exists(file_path):
        timestamp = datetime.datetime.strptime(new_timestamp, "%m/%d/%Y").timestamp()
        os.utime(file_path, (timestamp, timestamp))
        print(f"Timestamp of {file_path} modified to {new_timestamp}")
    else:
        print(f"File {file_path} not found.")

def process_directory(directory, new_timestamp):
    for root, dirs, files in os.walk(directory):
        for name in files:
            timetamper(os.path.join(root, name), new_timestamp)

parser = argparse.ArgumentParser(description='Modify file timestamps.')
parser.add_argument('path', help='Path to the file or directory')
parser.add_argument('timestamp', help='New timestamp (MM/DD/YYYY)')
parser.add_argument('-r', '--recursive', action='store_true', help='Apply recursively for directories')

args = parser.parse_args()

if args.recursive and os.path.isdir(args.path):
    process_directory(args.path, args.timestamp)
else:
    timetamper(args.path, args.timestamp)