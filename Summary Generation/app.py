import os
import streamlit as st
from utils import clean_text
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader

def split_text(text, chunk_size=6000):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def getLLamaresponse(chunk, no_words, content_type, llm):
    prompt = PromptTemplate.from_template(
        """
        Generate a summary for this content {data}. \n The content is type of {content_type}
        within {no_words} words.
        """
    )
    chain_extract = prompt | llm
    response = chain_extract.invoke(input={"content_type": content_type, "data": chunk, "no_words": no_words})
    return response.content

load_dotenv()

st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')
st.header("Generate Summary 🤖")

link = st.text_input("Enter link")
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    content_type = st.selectbox('Link is of', ('NewsLetter/Blog', 'Research Work', 'Online doc'), index=0)

submit = st.button("Generate")

if submit:
    llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")
    loader = WebBaseLoader([link])
    data = clean_text(loader.load().pop().page_content)
    
    chunks = split_text(data, chunk_size=2000)
    summaries = [getLLamaresponse(chunk, no_words, content_type, llm) for chunk in chunks]
    combined_summary = " ".join(summaries)
    
    # Final summary request to Llama
    final_summary = getLLamaresponse(combined_summary, no_words, content_type, llm)
    
    st.write(final_summary)
