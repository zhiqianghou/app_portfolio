import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
	st.image("images/photo.png")

with col2:
	st.title("Zhiqiang Hou")
	content = """
	Hi, I am Zhiqiang Hou and you can call me Mark! I am a Ph.D. of Computational Biophysics with 10+ years building pipeline to accurate protein structure prediction to facilitate protein engineering in drug discovery.
	As a data scientist, I spanned six years characterized by proficiency in Python programming and machine learning modeling, specifically tailored for biology, implantable medical device analysis, and healthcare sectors.
	I pride myself on being an enthusiastic learner, capable of swiftly adapting to emerging data science technologies. My unique blend of skills and passion propels me to continuously innovate and make meaningful contributions in the data science realm.
	"""
	st.info(content)

