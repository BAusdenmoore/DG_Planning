import streamlit as st
from DisplayQueue import writeQueue
import json
import numpy as np
import pandas as pd

@st.cache_data
def LoadData():
    st.session_state['BuildQueue'] = {} # Will be a dictionary of turn, building name
    st.session_state['ShipQueue'] = {} # Will be a dictionary of turn, ship name
    st.session_state['Buildings'] = {} # Will be a dictionary of turn, list of dictionary containing building and count
    st.session_state['Resources'] = { "Metal": 0, "Mineral": 0, "Food": 0, "Energy": 0 }
    # Load game parameters from the JSON file
    with open("game_parameters.json", "r") as f:
        game_params = json.load(f)
    
    # Load data from game_params
    for key in game_params.keys():
        if key == 'StartingMaterials':            
            for building in game_params[key]['Buildings'].keys():
                st.session_state['Buildings'][building] = game_params[key]['Buildings'][building]
            for resource in game_params[key]['Stores'].keys():
                st.session_state['Resources'][resource] = game_params[key]['Stores'][resource]
        else:
            if game_params[key]['Type'] == 'Building':
                st.write('Building')
            elif game_params[key]['Type'] == 'Ship':
                st.write('Ship')

LoadData()
st.title("DarkGalaxy Build List Generator")
col1, col2 = st.columns([.4, .6])
col1.subheader("Settings and Controls")
col2.subheader("Current Buildlist")
st.write(st.session_state)

st.session_state['endTurn'] = col1.number_input("Number of turns to evaluate: ", value=10)

writeQueue(col2)
