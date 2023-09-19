import streamlit as st

def writeQueue(writeTarget):
    writeTarget.write(st.session_state['endTurn'])