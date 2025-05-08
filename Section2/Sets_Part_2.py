'''
In a competitive gaming tournament, players participate in different matches.
Your task is to analyze player participation across three matches using Python sets.

You'll be given three sets of players:

match1: Players who participated in Match 1
match2: Players who participated in Match 2
match3: Players who participated in Match 3
Your task is to:

Find players who participated in all three matches
Identify players who participated in exactly two matches
Determine players who participated in only one match
Count the total number of unique players in the tournament
Find players who participated in Match 1 but not in Match 2 or Match 3
Print the results in the following format:

Use sorted(list(set_name)) to display players in alphabetical order
Print the exact output format shown in the example
Example Input:
{"Alice", "Bob", "Charlie", "Diana"}
{"Charlie", "Diana", "Eve", "Frank"}
{"Alice", "Diana", "Frank", "George"}
Example Output:
Players in all matches: ['Diana']
Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
Players in only one match: ['Bob', 'Eve', 'George']
Total unique players: 7
Players in Match 1 only: ['Bob']
'''


# Read input for the three matches
# match1 = eval(input())
# match2 = eval(input())
# match3 = eval(input())

match1 = {"Alice", "Bob", "Charlie", "Diana"}
match2 = {"Charlie", "Diana", "Eve", "Frank"}
match3 = {"Alice", "Diana", "Frank", "George"}

# 1. Find players who participated in all three matches
players_in_all_matches = match1.intersection(match2, match3)
print(f'Players in all matches: {sorted(list(players_in_all_matches))}')

# 2. Find players who participated in exactly two matches
players_in_exactly_two_matches = match1 & match2 - match3 | match2 & match3 - match1 | match3 & match1 - match2
print(f'Players in exactly two matches: {sorted(list(players_in_exactly_two_matches))}')

# 3. Find players who participated in only one match
players_in_only_one_match = match1 - match2 - match3 | match2 - match3 - match1 | match3 - match1 - match2
print(f'Players in only one match: {sorted(list(players_in_only_one_match))}')

# 4. Count total unique players
total_unique_players = match1 ^ match2 | match2 ^ match3 | match3 ^ match1 | match1.intersection(match2, match3)
print(f'Total unique players: {len(total_unique_players)}')

# 5. Find players in Match 1 only
players_in_match_one_only = match1 - match2 - match3
print(f'Players in Match 1 only: {sorted(list(players_in_match_one_only))}')

# Print results in the specified format
'''
Players in all matches: ['Diana']
Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
Players in only one match: ['Bob', 'Eve', 'George']
Total unique players: 7
Players in Match 1 only: ['Bob']
'''