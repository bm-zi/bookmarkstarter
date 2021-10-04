#!/usr/bin/env python3

"""
--- ACCESS FIREFOX BOOKMARKS FROM COMMAND LINE ---
This script can be used to open a url at a time, from an index 
list of urls. The list is built from the exported bookmarks 
from firefox.

"""

from bs4 import BeautifulSoup
import os, sys, subprocess
# from tui import Screen

htmlfile = './bookmarks.html'


def clear():
    subprocess.call('clear' if os.name == 'posix' else 'cls')


def get_url_text(url):
    """
    Returns url description
    """
    fh = open(htmlfile, 'r')
    html = fh.read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.findAll('a')
    for link in links:
        if link.name == 'a' and link['href'] == url:
            return(link.text)

clear()
fh = open(htmlfile, 'r')
html = fh.read()
soup = BeautifulSoup(html, 'html.parser')
links = soup.findAll(['a', 'h3'])
final_list = []
links_list = []
n = 1
for link in links:
    if link.name == 'a':
        append_str = str(n) + "\t" + link.text + "\n\t" + link['href'] + "\n\n"
        links_list.append(link['href'])
        final_list.append(append_str)
        n += 1
    if link.name == 'h3':
        append_str =  "\n\t||||||||||  " + link.text + "  ||||||||||\n"
        final_list.append(append_str)

with open('/tmp/file.txt', "w") as f:
    for elem in final_list:
        f.write(elem)

with open('/tmp/file.txt') as f:
    lines = [line.rstrip() for line in f]

# screen = Screen(lines)
# screen.run()
paginating_file = '/usr/bin/less /tmp/file.txt'
os.system(paginating_file)

while True:
#    os.system("tput smso")
    n = input("number | q | Enter >> ")
#    os.system("tput rmso")
    
    try:
        int(n)
        m = int(n) - 1 
        runstr = '/usr/bin/firefox ' + str(links_list[m]) + "&"
        os.system(runstr)
        print("\nOpened URL: \n", get_url_text(links_list[m]), "\n", links_list[m], "\n")
    except:
        if n == "q" or n == "Q":
            exit(0)
        else:
            os.execv(sys.argv[0], sys.argv)
