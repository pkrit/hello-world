#Task1: Calculate OR and p-value

#This program calculates the odds ratio and p-value for each row in the CaseControlInput.txt 
#file, using the Fisher's exact test. The output is a file (CaseControlOutput.txt) 
#containing the input values along with odds ratio and p-value for each row
#Command structure is python Task1.py 

#Import required modules
import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
from pandas import *

#Read input file into a data frame
file_in = pd.read_table('CaseControlInput.txt', sep = '\t')
file2_in = file_in

#Create additional columns for creating a contingency table for each row 
#'NA_Cases' and 'NA_Controls refer to the 'no outcome' counts
file2_in['NA_Cases'] = file2_in['Total_N_Cases'] - file2_in['N_Cases']
file2_in['NA_Controls'] = file2_in['Total_N_Controls'] - file2_in['N_Controls']

#Organize input file
file2_in = file2_in[['N_Cases', 'N_Controls', 'NA_Cases', 'NA_Controls']]

#Create empty lists to store odds ratios and p-values for each row
oddsratios = []
pvals = []

#This function takes a series of four values and puts them into a nested list
#It then calculates odds ratio and p-value using Fisher's Exact Test on the nested list
#and appends them to the empty lists created above
def fisher_test(L):
	L2 = L.tolist()
	L2_nested = [L2[:2], L2[2:]]
	o, p = sp.stats.fisher_exact(L2_nested)
	oddsratios.append(o)
	pvals.append(p)

#Apply the fisher_test function to each row of input file. This results in filling of 
#the empty lists created above.	
file2_in.apply(fisher_test, axis = 1)

#Append columns for odds ratio and p-values to input file
file_in['oddsratio'] = oddsratios
file_in['p-value'] = pvals
file_in = file_in[['N_Cases','Total_N_Cases','N_Controls','Total_N_Controls','oddsratio','p-value']]

#Write output to file
file_in.to_csv('CaseControlOutput_Python.txt', sep = '\t')