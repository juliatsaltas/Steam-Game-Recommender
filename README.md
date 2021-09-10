# Game Recommender System

Check out the app here: https://steam-streamlit-app.herokuapp.com/

This recommender system uses a collaborative filtering technique that makes recommendations to users based on other user profiles with similar preferences. In this case, user purchases are compared to other user purchases and games that are commonly purchased with other games are linked with higher similarity scores than games that are less likely to be purchased by multiple users.

Comparing similar purchases instead of a similar game playtimes is a better predictor for comparing games of similar genre rather than comparing total play time. Someone might really enjoy a free-to-play battle game while also loving smaller, quick to finish titles. By comparing play time values might have the player miss out on shorter games if they also play some longer form games as well, and the recommender ends up only recommending other games with high play times.

Play time may be a better recommendation feature for games of similar genre or length. For instance, successful hyper-casual games may only engage users for a short time each day for a few before a user moves onto a new game. Therefore the download itself may not be the only good indicator that the user enjoys a title, but rather games that the user played over time. However, even in this case, the pace of advertisement might outpace the interest of the user in the hyper-casual field. 

What about longer battle royal games? Maybe recommending similar games to a user who enjoys paying these endless running games could be a good tactic for sales as well?

These sorts of questions would need to be explored with greater data exploration for genre and production specific game development. 


## Notebooks

The notebooks are not interdependent as long as the ‘steam_clean.csv’ file is in the datasets folder.

|Notebook|Description|
|---|---|
|01-Clean_and_EDA.ipynb|Dataset cleaning saved to ‘steam_clean.csv’ file and exploratory analysis provided for game popularity, game play time, and user purchasing and play time distributions. Images of plots are in the ‘images folder’|
|02-Game_Recommender_PurchaseOnly.ipynb|Uses cosine similarity of pivot tables to recommend games based on purchase profiles.|
|03-Game_Recommender_PlayTime.ipynb|Uses cosine similarity of pivot tables to recommend games based on similar play times.|


### Data Dictionary

The following dictionary is for the ‘steam_clean.csv’ file containing a modified format to the Steam dataset from Kaggle.
Data from Kaggle: https://www.kaggle.com/tamber/steam-video-games


|Feature|Type|Dataset|Description|
|---|---|---|---|
|user|int|Kaggle|Unique user identifier|
|game|object|Kaggle|Game title|
|purchase|int|Kaggle|Value is 1 if game is purchased for specific user|
|play_time|float|Kaggle|Time user has played game in hours|



