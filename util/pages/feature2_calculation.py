import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import pathlib
from collections import Counter
import csv

def feature2_calc():
	st.header("Welcome to the Feature Calculation Page!")
	st.subheader("Feature 1 - Pair Predictibility of Amino Acid")
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
		length = len(sequence)
		
		aa_list = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
		aa_count = []
		
		for i in aa_list:
			new = sequence.count(i)
			aa_count.append(new)
			
		def factorial(n):
			if(n==0 or n==1):
				return 1
			else:
				return n*factorial(n-1)
		
		def distribution_probability(R,r,q,n):
			first_part = factorial(R)
			for qi in q:
				first_part = first_part/factorial(qi)
			
			second_part = factorial(R)
			for ri in r:
				second_part = second_part/factorial(ri)
				
			third_part = n**(-R)
			
			return (first_part*second_part*third_part)
		
		def integer_partition(n):
			partitions = []
			
			def generate_partitions(n, max_val, current_partition):
				if(n==0):
					partitions.append(current_partition)
				else:
					for i in range(1, min(n,max_val) +1):
						generate_partitions(n-i, i, current_partition + [i])
			generate_partitions(n, n, [])
			
			return partitions
		
		max_pdp = []
		
		for i in range(len(aa_count)):
			R = aa_count[i]
			n = aa_count[i]
			
			partitions = integer_partition(n)
			for p in partitions:
				while(len(p)<n):
					p.append(0)
					
			q_list = []
			for p in partitions:
				q_temp = []
				for i in range(len(p)+1):
					qu = p.count(i)
					q_temp.append(qu)
				q_list.append(q_temp)
				
			final_dp = []
			for p,a in zip(partitions,q_list):
				r = [i for i in p]
				q = [i for i in a]
				prob = distribution_probability(R,r,q,n)
				final_dp.append(prob)
			max_pdp.append(max(final_dp))
		
		x = np.arange(0,20)
		fig, ax = plt.subplots(figsize=(18,10))
		ax.bar(x, max_pdp, color='green')
		ax.set_xlabel("Nucleotide")
		ax.set_ylabel("Frequency")
		st.pyplot(fig)
