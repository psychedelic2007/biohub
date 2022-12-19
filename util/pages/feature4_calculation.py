import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
import pathlib
from collections import Counter
import csv
import pandas as pd
import math

def feature4_calc():
	st.header("Welcome to the Feature Calculation Page!")
	st.subheader("Feature 4 - Entropy of Amino Acid")
	st.write("Enter the sequence in FASTA format")
	
	sequence_input = ""
	
	sequence = st.text_area("Sequence Input", sequence_input, height=250)
	sequence = sequence.splitlines()
	sequence = sequence[1:]
	sequence = ''.join(sequence)
	
	show_submit = st.button("Submit")
	
	# Initialize the current index
	if "current_index" not in st.session_state:
		st.session_state.current_index = 0
		
	st.write("""***""")
	
	if show_submit:
		st.header("Input")
		st.write(sequence)
		#st.write(len(sequence))
	
		st.write('''***''')
		st.header("Current Count")
		
		aa_list = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
		length = len(sequence)
		
		aa_prob = []
		for i in aa_list:
			new = sequence.count(i)
			prob = float(new/length)
			aa_prob.append(prob)
		
		final = []
		for i in aa_prob:
			if(i==0):
				ent = 0
				final.append(ent)
			else:
				ent = (-i)*(math.log(i,2))
				final.append(ent)
		
		x = np.arange(0,20)
		fig, ax = plt.subplots(figsize=(18,10))
		ax.bar(x, final, color='green')
		ax.set_xlabel("Nucleotide")
		ax.set_ylabel("Frequency")
		st.pyplot(fig)
