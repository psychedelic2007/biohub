import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
import pathlib
from collections import Counter
import csv

def feature1_calc():
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
		st.write(len(sequence))
	
		st.write('''***''')
		st.header("Sequence Count") 
		X = Counter(sequence)
	
		fig, ax = plt.subplots(figsize=(18,10))
		ax.bar(X.keys(), X.values(), color='green')
		ax.set_xlabel("Nucleotide")
		ax.set_ylabel("Frequency")
		st.pyplot(fig)
	
		fn = 'aa_count.pdf'
		plt.savefig(fn)
		with open(fn, "rb") as img:
			btn = st.download_button(label="Download image",
			data = img, file_name=fn, mime="image/pdf")
	
		st.write('''***''')
		
		aa = sequence
		aa_pair = ['AA','AC','AD','AE','AF','AG','AH','AI','AK','AL','AM','AN','AP','AQ','AR','AS','AT','AV','AW','AY',
		'CA','CC','CD','CE','CF','CG','CH','CI','CK','CL','CM','CN','CP','CQ','CR','CS','CT','CV','CW','CY',
		'DA','DC','DD','DE','DF','DG','DH','DI','DK','DL','DM','DN','DP','DQ','DR','DS','DT','DV','DW','DY',
		'EA','EC','ED','EE','EF','EG','EH','EI','EK','EL','EM','EN','EP','EQ','ER','ES','ET','EV','EW','EY',
		'FA','FC','FD','FE','FF','FG','FH','FI','FK','FL','FM','FN','FP','FQ','FR','FS','FT','FV','FW','FY',
		'GA','GC','GD','GE','GF','GG','GH','GI','GK','GL','GM','GN','GP','GQ','GR','GS','GT','GV','GW','GY',
		'HA','HC','HD','HE','HF','HG','HH','HI','HK','HL','HM','HN','HP','HQ','HR','HS','HT','HV','HW','HY',
		'IA','IC','ID','IE','IF','IG','IH','II','IK','IL','IM','IN','IP','IQ','IR','IS','IT','IV','IW','IY',
		'KA','KC','KD','KE','KF','KG','KH','KI','KK','KL','KM','KN','KP','KQ','KR','KS','KT','KV','KW','KY',
		'LA','LC','LD','LE','LF','LG','LH','LI','LK','LL','LM','LN','LP','LQ','LR','LS','LT','LV','LW','LY',
		'MA','MC','MD','ME','MF','MG','MH','MI','MK','ML','MM','MN','MP','MQ','MR','MS','MT','MV','MW','MY',
		'NA','NC','ND','NE','NF','NG','NH','NI','NK','NL','NM','NN','NP','NQ','NR','NS','NT','NV','NW','NY',
		'PA','PC','PD','PE','PF','PG','PH','PI','PK','PL','PM','PN','PP','PQ','PR','PS','PT','PV','PW','PY',
		'QA','QC','QD','QE','QF','QG','QH','QI','QK','QL','QM','QN','QP','QQ','QR','QS','QT','QV','QW','QY',
		'RA','RC','RD','RE','RF','RG','RH','RI','RK','RL','RM','RN','RP','RQ','RR','RS','RT','RV','RW','RY',
		'SA','SC','SD','SE','SF','SG','SH','SI','SK','SL','SM','SN','SP','SQ','SR','SS','ST','SV','SW','SY',
		'TA','TC','TD','TE','TF','TG','TH','TI','TK','TL','TM','TN','TP','TQ','TR','TS','TT','TV','TW','TY',
		'VA','VC','VD','VE','VF','VG','VH','VI','VK','VL','VM','VN','VP','VQ','VR','VS','VT','VV','VW','VY',
		'WA','WC','WD','WE','WF','WG','WH','WI','WK','WL','WM','WN','WP','WQ','WR','WS','WT','WV','WW','WY',
		'YA','YC','YD','YE','YF','YG','YH','YI','YK','YL','YM','YN','YP','YQ','YR','YS','YT','YV','YW','YY']
		
		aa_counts = []
		
		for pairs in aa_pair:
			count = aa.count(pairs)
			aa_counts.append(count)
		#st.write(len(aa_counts))
		
		first = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
		second = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
		final = []
		
		for i in first:
			for j in second:
				x = aa.count(i)*aa.count(j)/len(sequence)
				final.append(x)
		
		diff = [x1-x2 for (x1,x2) in zip(aa_counts, final)]
		
		rounded = []
		for a in diff:
			r = round(a)
			rounded.append(r)
			
		f1 = []
		for i in range(0,len(sequence)-2):
			a = sequence[i]
			b = sequence[i+1]
			c = sequence[i+2]
			d = a + b
			e = b + c
			
			if(i==0):
				x1 = (aa.count(d) - round((aa.count(a)*aa.count(b))/len(sequence)))
				f1.append(x1)
			if(d,e in aa_pair):
				x = (aa.count(d) - round((aa.count(a)*aa.count(b))/len(sequence))) + (aa.count(e) - round((aa.count(b)*aa.count(c))/len(sequence)))
				f1.append(x)
		
		list1 = np.arange(0,len(sequence)-1)
		list2 = f1[0:len(sequence)-1]
		
		data = 'feature1.csv'
		
		st.write("""***""")
		st.write("### Your Data file Looks Something Like This")
		
		df = pd.read_csv(data)
		s = df.shape
		st.dataframe(df)
		
		st.download_button(label="Download Feature 1 Dataset",data = data, file_name="Feature1.csv", mime="text/csv")
