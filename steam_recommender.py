import streamlit as st
import pandas as pd
import numpy as np
#
#import timeit

 

def app():
	st.write("""
	# Steam Game Recommender
	- Data obtained from the Steam Store raw dataset from [Kaggle](https://www.kaggle.com/tamber/steam-video-games) by Tamber.com.
	- Data cleaning and EDA presented here: [link](https://www.kaggle.com/fivewheeler/steam-video-games-eda)

	### Welcome! 

	Can't decide what game to play next? Have a favourite game and want to know what other users who've also played your favourite are playing?

	
	""")
	#start = timeit.default_timer()

	# 1. Setup cache function - brought down data load 
	# runtime from 35 to 0.003 seconds
	@st.cache(allow_output_mutation=True)
	def load_data(file_name):
		data_file = pd.read_csv(file_name)
		return data_file
	
	# 2. Upload dataframe with clustered user data
	steam = load_data('steam_clean_recommender.csv')
	pivot = load_data('steam_recommender_pivot.csv')
	df_recommender = load_data('steam_recommender.csv')

	st.write("""
	Input a game title or part of a game title to get a list of games other users have purchased together.
	""")

	# 3. User input of game
	def user_input_features():
		search = st.text_input("Search Game Title")
		data = {'search': search}
		features = pd.DataFrame(data, index=[0])
		return features
	
	user_input = user_input_features()
	
	# 4. save user_input and convert to lower case to make case insensitive
	search = user_input['search'][0]
	steam['game_lower'] = [i.lower() for i in steam['game']]
	
	#stop = timeit.default_timer()
	#st.write('Search Runtime: ', stop - start)

	# 5. print tables
	count = 0
	for title in steam.loc[steam['game_lower'].str.contains(search.lower()), 'game']:
		st.write(title)
		st.write(f"Number of Players: {pivot.T[title].count()}")
		st.write("10 closest titles:")
		st.write(round(df_recommender[title].sort_values(ascending=False)[1:11], 2))
		if count > 1:
			break
		else:
			count+=1
	
