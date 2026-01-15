'''
Week One Assignment - Simple String Searching 
'''

'''
Part 1:

Create a GitHub account with your arizona email.
 - Make sure you name it something easy for your instructor to match to you.
 - Perhaps: FirstNameLastName or your University Identifier
 - Avoid generic names like: Coolguy1 or Arizona123

Watch the videos in D2L to get PyCharm set up and connected to your GitHub.
Pull the repository from GitHub Classroom.

Part 2:

You are given an excerpt from the hacker manifesto. 
The excerpt is assigned to the variable 'excerpt'.

Complete the script below to do the following for a report to your cyber team:

1) Convert the string to all lowercase - Once You Complete This Section Commit it to GitHub 
2) Count the number of characters in the string - Once You Complete This Section Commit it to GitHub 
3) Count the number of words in the string - Once You Complete This Section Commit it to GitHub 
4) Sort the words in alphabetical order
    - Choose how you are going to handle various cases in the words. 
    - Explain your justification in the comments.
    - Once You Complete This Section Commit it to GitHub 
5) Report how many occurrences of each of the following are found:
       scandal
       arrested
       er
       good
       tomorrow
   - Once You Complete This Section Commit to GitHub 
   
6) Submit your repository in GitHub Classroom with this file edited and screenshots.
   for example:  src/wk1_script.py
                 docs/results_screenshot.jpg
                 
    Your repository should show at least 5 commits and have your completed script.

   It should also have:
   A) A screenshot of the results in PyCharm.py dropped into the docs folder.
   B) A short video using Zoom or a Screen Recorder of your choice showing you committing the screenshot to GitHub using PyCharm.
        - Ensure your video is the appropriate size to be committed to GitHub. 
        - If it is too large (it shouldn't be, try to compress it first) you may upload it to D2L.

In D2L Submit a link to your GitHub repository.
   
'''

excerpt = " Another one got caught today, it's all over the papers. Teenager Arrested in Computer Crime Scandal, Hacker Arrested after Bank Tampering kids. They're all alike"

''' Your work starts here '''

"""
Script Name: wk1_script.py
Author: Quashawn Woods
Purpose: Text analysis report for cyber operations team
"""

excerpt = "Another one got caught today, it's all over the papers. Teenager Arrested in Computer Crime Scandal, Hacker Arrested after Bank Tampering kids. They're all alike"

# ======================================
# 1) Convert the string to all lowercase
# =======================================
# We convert the entire string to lowercase so analysis is consistent
# and case-insensitive (e.g., 'Arrested' vs 'arrested').
lower_excerpt = excerpt.lower()

print("Lowercase Text:")
print(lower_excerpt)
print("-" * 50)

# ===============================================
# 2) Count the number of characters in the string
# ================================================
# This count includes spaces and punctuation, which is important
# in digital forensics when analyzing raw text data.
char_count = len(lower_excerpt)

print(f"Character Count: {char_count}")
print("-" * 50)

# ==========================================
# 3) Count the number of words in the string
# ===========================================
# Splitting on whitespace gives a basic but effective word count.
words = lower_excerpt.split()
word_count = len(words)

print(f"Word Count: {word_count}")
print("-" * 50)

# =======================================
# 4) Sort the words in alphabetical order
# =======================================
# Handling decision:
# - Punctuation is removed so words like 'scandal,' and 'scandal'
#   are treated as the same word.
# - This improves accuracy for sorting and frequency analysis.
# - Apostrophes are also removed for consistency.
import string

clean_words = []
for word in words:
    cleaned = word.strip(string.punctuation)
    clean_words.append(cleaned)

sorted_words = sorted(clean_words)

print("Alphabetically Sorted Words:")
print(sorted_words)
print("-" * 50)

# ======================================
# 5) Count occurrences of specific terms
# ======================================
# Searching is done on the cleaned, lowercase text to ensure
# consistent and reliable results.

search_terms = [
    "scandal",
    "arrested",
    "er",
    "good",
    "tomorrow"
]

print("Keyword Occurrences:")
for term in search_terms:
    count = lower_excerpt.count(term)
    print(f"{term}: {count}")

print("-" * 50)