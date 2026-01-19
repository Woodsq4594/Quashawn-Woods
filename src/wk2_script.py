
'''
Week Two Assignment 1 - File Processing and Hashing
'''

'''
Scenario:

Your cyber team has noticed a firewall log file has gone missing.
Your cyber team reviewed the back up data and found the missing firewall log file.
To be safe, they obtained the file from 4 different system snapshots all taken a few moments from each other.
The files are:

   -redhat.txt - Taken at 11:00 AM
   -redhat_2.txt  - Taken at 11:10 AM
   -redhat_3.txt - Taken at 11:20 AM
   -redhat_4.txt - Taken at 11:30 AM
   
The files are really long and it would take a human quite some time to make sense of them. 
Let's use Python to gather some key pieces of information and write up a report of what these files tell us.
   
Part 1:

Log File Processing:

Write a script to

1) Open the file redhat.txt 
   a) Iterate through each line of the file
   b) Split each line into individual fields (Hint: str.split() method)
   c) Examine each field of the resulting field list
   d) If the word "worm" appears in the field, then add the worm name to the set of worms
   e) Once you have processed all the lines in the file
      - sort the set 
      - iterate through the set of worm names
      - print each unique worm name
   f) Screencapture your results
   
Once this part is complete - commit and push it to GitHub
                 
Part 2:

 Using the os library and the os.walk() method 
   a) Create a list of all files in the logs directory
   b) Create an empty dictionary named fileHashes 
   c) Iterate through the list of files and
      - calculate the sha256 hash of each file
      - create a dictionary entry where:
        key   = filename
        value = sha256 hash
    d) Iterate through the dictionary
       - print out each key, value pair in a PrettyTable format
    e) Screencapture your results
    
Once this part is complete - commit and push it to GitHub

Part 3:
 - Review your results and adjust your script to gather additional details you think would be useful for your report.
 - Write a reflection.md file and save it to your docs/ folder.
 - In the reflection file explain:
    - What do the file hashes tell us about the log files?
    - Based on the information the cyber team told us, what could have happened to this log file?
    - Did you gather any additional information about this log file? If so, what did you gather and why?
 
3) Submit your repository in GitHub Classroom with this file edited and screenshots.
   include:      src/wk2_script.py - this file edited
                 docs/results_screenshot_1.jpg
                 docs/results_screenshot_2.jpg
                 docs/reflection.md
'''


        
        
