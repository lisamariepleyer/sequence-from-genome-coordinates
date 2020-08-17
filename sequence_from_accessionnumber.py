#! /anaconda3/bin/python3.7

from Bio import Entrez
Entrez.email = "lisamarie.free333@gmail.com"

accessionumberfile = "/Users/lisa-marie/Documents/githubprojects/sequence-from-genome-coordinates/accessionnumbers.txt"
accessionnumbers = []
with open (accessionumberfile, 'r') as accessionnumberinput:
    for line in accessionnumberinput:
        accessionnumbers.append (line.partition('\n')[0])
