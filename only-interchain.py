#script to retrieve only interchain hbonds of selected chains, excluding waters
#the input file is a .hb2 file (hbplus output file)
#usage: python only-interchain.py <hbplus output file> <list of chains space separated>
import os,sys
lista=sys.argv[2:] #create a list of chains we are interested in
filename=sys.argv[1] #assaing a variable to the input file
linee=[] 
with open(filename) as file: #open, read and store the file as a list of lists 
  for line in file:
    linee.append(line.rstrip())
#linee[i] is the whole ith line of the file
#linee[i][0] correspond to donor chain id in ith line
#linee[i][14] correspond to acceptor chain id in ith line
#linee[i][6:9] correspond to donor 3 letters residue in ith line
#linee[i][20:23] correspond to acceptor 3 letters residue in ith line
#.hb2 files have 8 loine header, so we start filtering from the 8th line on
#if we want to keep the 8 lines header, uncomment line 18-19
#for i in range(0,8):
#  print(linee[i])
for i in range(8, len(linee)): #iterate through the list of lists
	if linee[y][0]!=linee[y][14] and linee[y][6:9]!="HOH" and linee[y][20:23]!="HOH": #check if chain ids are not equal and if both the 3 residue letters is not equal to water
		if linee[y][0] in lista and linee[y][14] in lista: #check if chain ids are in our selection list
			print(linee[y])
