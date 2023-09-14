
import streamlit as st
import json

# Load game parameters from the JSON file
with open("game_parameters.json", "r") as f:
    game_params = json.load(f)

print(game_params)

# # Initialize game variables
# players = game_params["players"]
# turns = game_params["turns"]
# scores = game_params["initial_score"]
# score_increment = game_params["score_increment"]

# st.title("Turn-Based Game Simulator")

# # Sidebar
# st.sidebar.header("Game Parameters")
# current_turn = st.sidebar.slider("Select Turn", 1, turns, 1)
# current_player = st.sidebar.selectbox("Current Player", players)

# # Main content
# st.write(f"Current Turn: {current_turn}")
# st.write(f"Current Player: {current_player}")
# st.write(f"{players[0]} Score: {scores[0]}")
# st.write(f"{players[1]} Score: {scores[1]}")

# # Simulate turn
# if st.button("Simulate Turn"):
#     if current_player == players[0]:
#         scores[0] += score_increment[0]
#     else:
#         scores[1] += score_increment[1]
#     current_turn += 1

# # Save updated scores to the JSON file
# game_params["initial_score"] = scores
# with open("game_parameters.json", "w") as f:
#     json.dump(game_params, f)

# # Display game parameters in the sidebar
# st.sidebar.write("Updated Game Parameters")
# st.sidebar.write(f"Current Turn: {current_turn}")
# st.sidebar.write(f"{players[0]} Score: {scores[0]}")
# st.sidebar.write(f"{players[1]} Score: {scores[1]}")

# # Reset the game
# if st.sidebar.button("Reset Game"):
#     scores = game_params["initial_score"]
#     current_turn = 1

#     # Save the reset scores to the JSON file
#     game_params["initial_score"] = scores
#     with open("game_parameters.json", "w") as f:
#         json.dump(game_params, f)

# # Close the sidebar
# st.sidebar.write("")

# # Add an option to quit the game
# if st.sidebar.button("Quit Game"):
#     st.sidebar.warning("Game Quit")

# # Show the app
# st.sidebar.write("")
# st.sidebar.write("Developed by Your Name")
