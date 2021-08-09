# Game Recommender System

## Sample Output of Recommender

This game recommender system uses cosine similarity to make game recommendations for users based on users with similar purchase or play time profiles.

**Purchase Similarity**
|Thomas Was Alone|
|Average Play Time (Hrs): 1.0|
|Number of Players: 27|
|10 closest titles:|
|game|
|Little Inferno|0.38|
|Botanicula|0.34|
|Joe Danger 2 The Movie|0.32|
|Dear Esther|0.31|
|Antichamber|0.30|
|Tiny and Big Grandpa’s Leftovers|0.29|
|Gone Home|0.27|
|Reus|0.27|
|English Country Tune|0.27|
|Papers, Please|0.27|
|Name: Thomas Was Alone, dtype: float64|


**Play Time Similarity**
|Thomas Was Alone|
|Number of Players: 27|
|10 closest titles:|
|game|
|Portal 2 - The Final Hours|0.52|
|Oozi Earth Adventure|0.52|
|Cloud Chamber|0.52|
|Return to Mysterious Island 2|0.52|
|Critical Mass|0.52|
|Mission Control NanoMech|0.52|
|Fester Mudd Curse of the Gold - Episode 1|0.52|
|GEARCRACK Arena|0.52|
|Defense Grid 2 A Matter of Endurance|0.52|
|Dreamfall Chapters|0.49|
|Name: Thomas Was Alone, dtype: float64|

## Recommender Review

Play time isn’t necessarily the best indicated of similar tastes in the Steam world. This is because of the vast variety of game genres to choose from on the platform that are of varying lengths. Some smaller, but popular, independent games could have a completion time of a couple hours while there are also free-to-play games that users dedicate hundreds of hours on that game, but this does not mean that a user would necessarily like a game any less because of the shorter overall playtime. (Every gaming forum on the internet may convince that every game under 100 hrs is too short, but I at least have the bias of loving games under 10 hrs.) Therefore, purchase similarity may be a better indicator of game similarity based on similar purchase profiles between two users. However, this assumes that the player enjoys playing every game they purchase.

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



