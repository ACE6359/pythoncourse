#player dictionary
Player={
    "player_id":7,
    "name":"M.S.Dhoni",
    "date_of_birth":"July 7, 1981",
    "Nationality":"Indian",
    "Role":"wicket_keeper",
    "Teams":[],
    "Formats":[]
}
#Team Dictionary
Team={
         "Team_name": "India",
         "start_year":"2004",
         "end_year":"2020",
        } # type: ignore
Player['Teams'].append(Team)

#match_format_stats
match_format_stats={
    "format_type":"ODI",
    "batting_stats":None,
    "bowiling_stats":None
} # type: ignore
Player['Formats'].append(match_format_stats)

#batting_stats
batting_stats={
    "matches": 254,
    "innings": 245,
    "runs": 12040,
    "average": 59.31,
    "strike_rate": 93.18,
    "centuries": 43,
    "half_centuries": 62,
    "highest_score": 183,
    "not_outs": 39
} # type: ignore
match_format_stats['batting_stats']=batting_stats
#bowling_stats
bowling_stats={
    "matches": 254,
    "overs": 1024.5,
    "wickets": 134,
    "average": 32.43,
    "economy_rate": 4.5,
    "five_wicket_hauls": 2,
    "best_bowling": "5/21"
} # type: ignore
match_format_stats['bowling_stats']=bowling_stats
print(Player)




