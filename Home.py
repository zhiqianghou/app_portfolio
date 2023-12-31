import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
	st.image("images/photo.jpeg")

with col2:
	st.title("Zhiqiang Hou")
	content = """
	Hi, I am Zhiqiang Hou and you can call me Mark! I am a Ph.D. of Computational Biophysics with 10+ years building pipeline and applying Machine Learning to accurate protein structure prediction to facilitate protein engineering in drug discovery.
	As a data scientist, I spanned six years characterized by proficiency in Python programming and machine learning modeling, specifically tailored for biology, implantable medical device analysis, and healthcare sectors.
	I pride myself on being an enthusiastic learner, capable of swiftly adapting to emerging data science technologies. My unique blend of skills and passion propels me to continuously innovate and make meaningful contributions in the data science realm.
	"""
	st.info(content)

content2 = "<h4>Below you can find some of the apps I have built in Python. Feel Free to Contact Me!</h2>"
st.write(content2, unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
	for index, row in df[:10].iterrows():
		st.header(row['title'])
		st.write(row['description'])
		st.image("images/" + row["image"])
		st.write(f"[Source Code]({row['url']})")

with col4:
	for index, row in df[10:].iterrows():
		st.header(row['title'])
		st.write(row['description'])
		st.image("images/" + row["image"])
		st.write(f"[Source Code]({row['url']})")