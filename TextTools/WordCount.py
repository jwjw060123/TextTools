import streamlit as st

st.title('Word Count')
text = st.session_state.get('text','')
text = st.text_area('Type or Copy & Paste:', height=300, key='text')
if text:
    st.write(f'''
            Words: {len(text.split(' '))}\n
            Letters (excl. space): {len(text.replace(' ','').replace('\n',''))}\n
            Letters (incl. space): {len(text.replace('\n',''))}
            ''')