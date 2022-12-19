import streamlit as st
from PIL import Image

st.set_page_config(page_title="BioHub",page_icon="👋", layout="wide")

def home_page():
	#Homepage
	image = Image.open('model.jpg')
	st.image(image, use_column_width=True)

	st.write("# Welcome to BioHub! 👋")

	st.markdown("""
		BioHub is a website that offers all the necessary calculation required for a protein/genomic sequences
		
		**👈 Select an analysis from the sidebar** to start your journey of Biological Analysis!
			""")
	#About the Authors
	st.markdown("""
		### Authors
		Please feel free to contact me if you have any issue, comments or questions!

		### Satyam Sangeet
		- Email : satyam85cool@gmail.com
		- [GitHub](https://github.com/psychedelic2007)
		- [WebPage](https://sites.google.com/view/satyamsangeet) 
			""")

	st.write("""***""")

	#Development Field
	st.markdown("""
		## Developed and Maintained by Satyam Sangeet & Dr. Susmita Roy
		[Dr. Roy lab](https://www.drsusmitaroy.com/)

		Copyright (c) 2022 Satyam Sangeet
			""")
