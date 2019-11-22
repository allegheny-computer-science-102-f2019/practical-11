#!/usr/bin/env python3

DATE = "21 November 2019"
VERSION = "i"
AUTHOR = " myName"
AUTHORMAIL = "@allegheny.edu"



# program to find word freqs in a text.

def openAndCleanData(inFile):
    """ loads a text file and returns a string of contents"""
    data_str = open(inFile,"r").read().lower() #return a string in lowercase
    #print("type :",type(data_str))
    punct_str = "!.,'\""
    for i in punct_str:
        data_str = data_str.replace(i,"") #remove the punctuation
    return data_str
#end of openFile()


def onlineHelp():
    """ online help function"""
    h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
    print("  "+len(h_str) * "-")
    print(h_str)
    print("  "+len(h_str) * "-")

    print("\t Program to load a text file of text")
    print("\t and to return a frequency plot of the word freqs")
    if getCurrentOS() != "windows":
        print("\t  + \U0001f600  USAGE: program <wordFile.txt>") # unix print
    else:
        print("\t  + :-) USAGE: program <wordFile.txt>") # windows print

#end of onlineHelp()

def getCurrentOS():
    """ function to determine which os python is using"""
    if platform == "linux2" or platform == "linux":
        # This is a linux OS
        return "linux"
    elif platform == "darwin":
        # This is OS X
        return "macOS"
    elif platform == "win32":
        # This is s a Windows machine
        return "windows"
#end of whichOS()

def collectFreqs(data_str):
    """collect the numbers of words and return a dictionary of freqs"""
    #print("  collectFreqs()")
    data_list = sorted(data_str.split()) # return an abc-sorted list
    freq_list = [] # we will store the freqs in a list
    count_dic = {} # store words and counts
    for i in data_list:
        if i not in count_dic: count_dic[i] = 1
        else: count_dic[i] = count_dic[i] + 1
    #print("  Count_dic :",count_dic)

    # place freqs in the list
    for i in count_dic:
        freq_list.append(count_dic[i]/len(data_list))
    #print("  freq_list :",freq_list)

    return freq_list
#end of collectFreqs()


def plotter(in_list, inFile_str):
    """ plots the freq data"""

#
#
#TODO: x, y axes code
#      plot command to draw the points on the canvas.
#
#
    print("\t Plotter is not placing points on canvas ... :-(")
#
#


    title("Frequency of words used")
    xlabel("Words")
    ylabel("Magnitude of Frequency")

    fname_str = inFile_str.replace(".txt",".png")
    fname_str = "out_" + fname_str

    print(" Saving new filename:", fname_str)
    savefig(fname_str) #save in root directory
    show()

#end of plotter()


def begin(inFile):
    """ Driver function """

    print(" Loading file :", inFile)
    data = openAndCleanData(inFile)
    #print("  Contents :",data)
    collectedFreqs_list = collectFreqs(data)
    #print(" collectedFreqs_list :",collectedFreqs_list)
    plotter(collectedFreqs_list,inFile)
    print("  Program finished")
#end of begin()


# command line paramters code
###################################
import itertools, os, sys
from sys import platform  # for whichOS()
from pylab import plot, show, title, savefig, xlabel, ylabel, legend
if __name__ == '__main__':

    if len(sys.argv) == 2: #one option added to command line
       begin(sys.argv[1])
    else:
       onlineHelp()
       sys.exit(0)
