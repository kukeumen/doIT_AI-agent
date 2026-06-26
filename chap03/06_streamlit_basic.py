import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

with st.sidebar:
    openai_api_key=os.getenv("OPENAI_API_KEY")

    "[Get an OpenAI API key](http://platform.openai.com/account/api_keys)"
    "[View the source code](http://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in Github Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")

#Steamlit에서 사용자의 세션 상태를 관리하는 기능
if "messges" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content":"How can I help you?"}] #초기 응답

#대화 기록을 웹 브라우저에 출력하는 부분
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

#사용자의 입력을 받아 prompt 변수에 담는 부분
if prompt := st.chat_input():
    # openai_api_key가 정의되지 않았을 때 오류 메시지를 보여주기 위한 부분
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue. ")
        st.stop()

    #사용자 입력을 st.session_state.messages에 추가
    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)
    #GPT의 답변을 받아와서 st.session_state.messages에 추가하고 답변을 화면에 출력
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)