import pandas as pd

# Sets the max width of each column to 90 characters
pd.options.display.max_colwidth = 90

# Creates a DataFrame called 'puzzles' thats reads from the 'lichess_db_puzzle.csv'
puzzles = pd.read_csv("lichess_db_puzzle.csv")

# Creates a DataFrame called 'mateIn1' thats an exact copy of 'puzzles'
temp_mateIn1 = puzzles

keyword = "mateIn1"

# Finds every occurrence of the keyword and creates a new DataFrame called 'occurrences'
# where every time the keyword is found
mateIn1 = temp_mateIn1[temp_mateIn1["Themes"].str.contains(keyword)]

# Only displays the PuzzleID, FEN, Moves, and Rating for every occurrence of the keyword
mateIn1 = mateIn1.loc[:, ['PuzzleId', 'FEN','Moves', 'Rating']]

#The JavaScript chess library can only read the moves with a hyphen between the moves,
#therefore this goes in and replaces the space between the moves with a hyphen.
#It also has to take promotions into consideration
mateIn1['Moves'] = mateIn1['Moves'].str.replace("(?<=[a-zA-Z]\d)(?=[a-zA-Z])", "-", regex=True)
mateIn1['Moves'] = mateIn1['Moves'].apply(lambda x: x.replace("8-q","8q").replace("8-r","8r").replace("8-b","8b").replace("8-k","8k"))

#Adds a column to the DataFrame called 'Themes' and for each row it says the theme of puzzle
mateIn1['Themes'] = "mateIn1"

# Sorts the DataFrame by ascending Rating
mateIn1.sort_values(by=['Rating'], inplace=True)

#------------------------------------------------------------------

# Creates a DataFrame called 'mateIn2' thats an exact copy of 'puzzles'
temp_mateIn2 = puzzles

keyword = "mateIn2"

# Finds every occurrence of the keyword and creates a new DataFrame called 'occurrences'
# where every time the keyword is found
mateIn2 = temp_mateIn2[temp_mateIn2["Themes"].str.contains(keyword)]

# Only displays the PuzzleID, FEN, Moves, and Rating for every occurrence of the keyword
mateIn2 = mateIn2.loc[:, ['PuzzleId', 'FEN','Moves', 'Rating']]

#The JavaScript chess library can only read the moves with a hyphen between the moves,
#therefore this goes in and replaces the space between the moves with a hyphen.
#It also has to take promotions into consideration
mateIn2['Moves'] = mateIn2['Moves'].str.replace("(?<=[a-zA-Z]\d)(?=[a-zA-Z])", "-", regex=True)
mateIn2['Moves'] = mateIn2['Moves'].apply(lambda x: x.replace("8-q","8q").replace("8-r","8r").replace("8-b","8b").replace("8-k","8k"))

#Adds a column to the DataFrame called 'Themes' and for each row it says the theme of puzzle
mateIn2['Themes'] = "mateIn2"

# Sorts the DataFrame by ascending Rating
mateIn2.sort_values(by=['Rating'], inplace=True)

#------------------------------------------------------------------

# Creates a DataFrame called 'mateIn3' thats an exact copy of 'puzzles'
temp_mateIn3 = puzzles

keyword = "mateIn3"

# Finds every occurrence of the keyword and creates a new DataFrame called 'occurrences'
# where every time the keyword is found
mateIn3 = temp_mateIn3[temp_mateIn3["Themes"].str.contains(keyword)]

# Only displays the PuzzleID, FEN, Moves, and Rating for every occurrence of the keyword
mateIn3 = mateIn3.loc[:, ['PuzzleId', 'FEN','Moves', 'Rating']]

#The JavaScript chess library can only read the moves with a hyphen between the moves,
#therefore this goes in and replaces the space between the moves with a hyphen.
#It also has to take promotions into consideration
mateIn3['Moves'] = mateIn3['Moves'].str.replace("(?<=[a-zA-Z]\d)(?=[a-zA-Z])", "-", regex=True)
mateIn3['Moves'] = mateIn3['Moves'].apply(lambda x: x.replace("8-q","8q").replace("8-r","8r").replace("8-b","8b").replace("8-k","8k"))

#Adds a column to the DataFrame called 'Themes' and for each row it says the theme of puzzle
mateIn3['Themes'] = "mateIn3"

# Sorts the DataFrame by ascending Rating
mateIn3.sort_values(by=['Rating'], inplace=True)

#------------------------------------------------------------------

# Creates a DataFrame called 'mateIn4' thats an exact copy of 'puzzles'
temp_mateIn4 = puzzles

keyword = "mateIn4"

# Finds every occurrence of the keyword and creates a new DataFrame called 'occurrences'
# where every time the keyword is found
mateIn4 = temp_mateIn4[temp_mateIn4["Themes"].str.contains(keyword)]

# Only displays the PuzzleID, FEN, Moves, and Rating for every occurrence of the keyword
mateIn4 = mateIn4.loc[:, ['PuzzleId', 'FEN','Moves', 'Rating']]

#The JavaScript chess library can only read the moves with a hyphen between the moves,
#therefore this goes in and replaces the space between the moves with a hyphen.
#It also has to take promotions into consideration
mateIn4['Moves'] = mateIn4['Moves'].str.replace("(?<=[a-zA-Z]\d)(?=[a-zA-Z])", "-", regex=True)
mateIn4['Moves'] = mateIn4['Moves'].apply(lambda x: x.replace("8-q","8q").replace("8-r","8r").replace("8-b","8b").replace("8-k","8k"))

#Adds a column to the DataFrame called 'Themes' and for each row it says the theme of puzzle
mateIn4['Themes'] = "mateIn4"

# Sorts the DataFrame by ascending Rating
mateIn4.sort_values(by=['Rating'], inplace=True)

#------------------------------------------------------------------

# Creates a DataFrame called 'mateIn5' thats an exact copy of 'puzzles'
temp_mateIn5 = puzzles

keyword = "mateIn5"

# Finds every occurrence of the keyword and creates a new DataFrame called 'occurrences'
# where every time the keyword is found
mateIn5 = temp_mateIn5[temp_mateIn5["Themes"].str.contains(keyword)]

# Only displays the PuzzleID, FEN, Moves, and Rating for every occurrence of the keyword
mateIn5 = mateIn5.loc[:, ['PuzzleId', 'FEN','Moves', 'Rating']]

#The JavaScript chess library can only read the moves with a hyphen between the moves,
#therefore this goes in and replaces the space between the moves with a hyphen.
#It also has to take promotions into consideration
mateIn5['Moves'] = mateIn5['Moves'].str.replace("(?<=[a-zA-Z]\d)(?=[a-zA-Z])", "-", regex=True)
mateIn5['Moves'] = mateIn5['Moves'].apply(lambda x: x.replace("8-q","8q").replace("8-r","8r").replace("8-b","8b").replace("8-k","8k"))

#Adds a column to the DataFrame called 'Themes' and for each row it says the theme of puzzle
mateIn5['Themes'] = "mateIn5"

# Sorts the DataFrame by ascending Rating
mateIn5.sort_values(by=['Rating'], inplace=True)