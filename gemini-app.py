import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment
load_dotenv()

# Title
st.title("🤖 Gemini Chatbot with LangChain")

# Input
question = st.text_input("Ask me anything:")

# Define model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and honest AI assistant."),
    ("human", "Question: {question}")])

# Chain
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Generate answer
if question:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"question": question})
            st.markdown(f"### ✨ Answer:\n{response}")
        except Exception as e:
            st.error("Something went wrong:")
            st.exception(e)
