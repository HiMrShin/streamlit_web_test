# 실행하기 : !streamlit run jocoding_web.py

# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("한국의 역사적 인물3명은 누가 있을까")
# print(result)
import time
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title(':blue[인공지능] 시인 :sunglasses:')
content = st.text_input('시의 주제를 제시하세요')

st.write('시의 주제는 = ', content)

st.button("Reset", type="primary")
if st.button('작성 시작'):
    with st.spinner('Wait for it...'):
        time.sleep(1)    
        result = chat_model.predict(content + "에 대한 시를 3줄로 써줘")
        st.write(result)
else:
    st.write('다시 작성 하세요')
    
    






         