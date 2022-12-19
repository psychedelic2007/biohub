import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
import pathlib
from collections import Counter
import csv
import pandas as pd

def feature3_calc():
	st.header("Welcome to the Feature Calculation Page!")
	st.subheader("Feature 3 - Future Count of Amino Acid")
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
		
		A = sequence.count("A")
		C = sequence.count("C")
		D = sequence.count("D")
		E = sequence.count("E")
		F = sequence.count("F")
		G = sequence.count("G")
		H = sequence.count("H")
		I = sequence.count("I")
		K = sequence.count("K")
		L = sequence.count("L")
		M = sequence.count("M")
		N = sequence.count("N")
		P = sequence.count("P")
		Q = sequence.count("Q")
		R = sequence.count("R")
		S = sequence.count("S")
		T = sequence.count("T")
		V = sequence.count("V")
		W = sequence.count("W")
		Y = sequence.count("Y")
		
		A_cur = A/len(sequence)
		C_cur = C/len(sequence)
		D_cur = D/len(sequence)
		E_cur = E/len(sequence)
		F_cur = F/len(sequence)
		G_cur = G/len(sequence)
		H_cur = H/len(sequence)
		I_cur = I/len(sequence)
		K_cur = K/len(sequence)
		L_cur = L/len(sequence)
		M_cur = M/len(sequence)
		N_cur = N/len(sequence)
		P_cur = P/len(sequence)
		Q_cur = Q/len(sequence)
		R_cur = R/len(sequence)
		S_cur = S/len(sequence)
		T_cur = T/len(sequence)
		V_cur = V/len(sequence)
		W_cur = W/len(sequence)
		Y_cur = Y/len(sequence)
		
		A_fut = (((12*A) + (2*D) + (2*E) + (4*G) + (4*P) + (4*S) + (4*T) + (4*V))/(36*len(sequence)))
		C_fut = (((2*R) + (2*C) + (2*G) + (2*F) + (4*S) + (2*W) + (2*Y))/(18*len(sequence)))
		D_fut = (((2*A) + (2*N) + (2*D) + (4*E) + (2*G) + (2*H) + (2*Y) + (2*V))/(18*len(sequence)))
		E_fut = (((2*A) + (4*D) + (2*E) + (2*Q) + (2*G) + (2*K) + (2*V))/(18*len(sequence)))
		F_fut = (((2*C) + (2*I) + (6*L) + (2*F) + (2*S) + (2*Y) + (2*V))/(18*len(sequence)))
		G_fut = (((4*A) + (6*R) + (2*D) + (2*C) + (2*E) + (12*G) + (2*S) + (1*W) + (4*V))/(36*len(sequence)))
		H_fut = (((2*R) + (2*N) + (2*D) + (4*Q) + (2*H) + (2*L) + (2*P) + (2*Y))/(18*len(sequence)))
		I_fut = (((1*R) + (2*N) + (6*I) + (4*L) + (1*K) + (3*M) + (2*F) + (2*S) + (3*T) + (3*V))/(27*len(sequence)))
		K_fut = (((2*R) + (4*N) + (2*E) + (2*Q) + (1*I) + (2*K) + (1*M) + (2*T))/(18*len(sequence)))
		L_fut = (((4*R) + (2*Q) + (2*H) + (4*I) + (18*L) + (2*M) + (6*F) + (4*P) + (2*S) + (1*W) + (6*V))/(54*len(sequence)))
		M_fut = (((1*R) + (3*I) + (2*L) + (1*K) + (1*T) + (1*V))/(9*len(sequence)))
		N_fut = (((2*N) + (2*D) + (2*H) + (2*I) + (4*K) + (2*S) + (2*T) + (2*Y))/(18*len(sequence)))
		P_fut = (((4*A) + (4*D) + (2*Q) + (2*H) + (4*L) + (12*P) + (4*S) + (4*T))/(36*len(sequence)))
		Q_fut = (((2*R) + (2*E) + (2*Q) + (4*H) + (2*L) + (2*K) + (2*P))/(18*len(sequence)))
		R_fut = (((18*R) + (2*C) + (2*Q) + (6*G) + (2*H) + (1*I) + (4*L) + (2*K) + (1*M) + (4*P) + (6*S) + (2*T) + (2*W))/(54*len(sequence)))
		S_fut = (((4*A) + (6*R) + (2*N) + (4*C) + (2*G) + (2*I) + (2*L) + (2*F) + (4*P) + (14*S) + (6*T) + (1*W) + (2*Y))/(54*len(sequence)))
		T_fut = (((4*A) + (2*R) + (2*N) + (3*I) + (2*K) + (1*M) + (4*P) + (6*S) + (12*T))/(36*len(sequence)))
		V_fut = (((4*A) + (2*D) + (2*E) + (4*G) + (3*I) + (6*L) + (1*M) + (2*F) + (12*V))/(36*len(sequence)))
		W_fut = (((2*R) + (2*C) + (1*G) + (1*L) + (1*S))/(9*len(sequence)))
		Y_fut = (((2*N) + (2*D) + (2*C) + (2*H) + (2*F) + (2*S) + (2*Y))/(18*len(sequence)))
		
		A_ratio = A_fut/A_cur
		C_ratio = C_fut/C_cur
		D_ratio = D_fut/D_cur
		E_ratio = E_fut/E_cur
		F_ratio = F_fut/F_cur
		G_ratio = G_fut/G_cur
		H_ratio = H_fut/H_cur
		I_ratio = I_fut/I_cur
		K_ratio = K_fut/K_cur
		L_ratio = L_fut/L_cur
		M_ratio = M_fut/M_cur
		N_ratio = N_fut/N_cur
		P_ratio = P_fut/P_cur
		Q_ratio = Q_fut/Q_cur
		R_ratio = R_fut/R_cur
		S_ratio = S_fut/S_cur
		T_ratio = T_fut/T_cur
		V_ratio = V_fut/V_cur
		W_ratio = W_fut/W_cur
		Y_ratio = Y_fut/Y_cur
		
		x = np.arange(0,20)
		aa_count_list = [A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y]
		aa_curr_count_list = [A_cur,C_cur,D_cur,E_cur,F_cur,G_cur,H_cur,I_cur,K_cur,L_cur,M_cur,N_cur,P_cur,Q_cur,R_cur,S_cur,T_cur,V_cur,W_cur,Y_cur]
		aa_fut_count_list = [A_fut,C_fut,D_fut,E_fut,F_fut,G_fut,H_fut,I_fut,K_fut,L_fut,M_fut,N_fut,P_fut,Q_fut,R_fut,S_fut,T_fut,V_fut,W_fut,Y_fut]
		
		xticks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
		xlabel = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
		fig, ax = plt.subplots(figsize=(18,10))
		ax.bar(x, aa_curr_count_list, label="Current Count")
		ax.bar(x, aa_fut_count_list, width=0.5*0.8, label="Future Count")
		ax.set_xlabel("Amino Acids",fontsize=20)
		ax.set_ylabel("Frequency", fontsize=20)
		ax.legend(fontsize=15)
		ax.tick_params(labelsize=15)
		ax.set_xticks(xticks, xlabel)
		st.pyplot(fig)
	
		fn = 'f3.pdf'
		plt.savefig(fn)
		with open(fn, "rb") as img:
			btn = st.download_button(label="Download image",
			data = img, file_name=fn, mime="image/pdf")
	
		st.write('''***''')
