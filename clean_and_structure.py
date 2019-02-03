
# Read in data from the scrape
df = pd.read_csv("chess_scrape_data.csv")

# Check
df.tail()

# Looks like there are 4 options for a win, abandonment, checkmate, resignation, time
from collections import Counter

wins = []

for row in df['game_result']:
    if 'eono' in row:
        wins.append(row)

Counter(wins)

# Looks like there are 5 options for a draw, agreement, insufficient material, repitition, stalemate, timeout w/ no material
draws = []

for row in df['game_result']:
    if 'drawn' in row:
        draws.append(row)

Counter(draws)

# Clean all of the results 
for idx, row in df.iterrows():
    if 'abandoned' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'abandoned'
    if 'checkmate' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'checkmate'    
    if 'resignation' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'resignation'  
    if 'time' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'time' 
    if 'agreement' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'agreement' 
    if 'insufficient material' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'insufficient material' 
    if 'repetition' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'repetition'
    if 'stalemate' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'stalemate'
    if 'timeout vs insufficient material' in df.loc[idx,'game_result']: 
        df.loc[idx,'game_result'] = 'timeout vs insufficient material'

# Check        
df['game_result'].value_counts()

# Grab times only   
for idx, row in df.iterrows():
    df.loc[idx,'game_time'] = df.loc[idx,'game_time'].split(', ')[2].replace(' PST', '').strip()
