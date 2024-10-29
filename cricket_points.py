# cricket_points.py

def calculating_batting_points(runs, balls_faced, boundaries, sixes):
    points = 0
    points += runs // 2  
    if runs >= 100:
        points += 10 
    elif runs >= 50:
        points += 5  
    strike_rate = (runs / balls_faced) * 100
    if 80 <= strike_rate <= 100:
        points += 2  
    elif strike_rate > 100:
        points += 4  
    
    points += boundaries  
    points += sixes * 2  
    
    return points


def calculating_bowling_points(wickets, overs_bowled, runs_conceded):
    points = 0
    points += wickets * 10 
    
    if wickets >= 5:
        points += 10 
    elif wickets >= 3:
        points += 5 
    
    economy_rate = runs_conceded / overs_bowled
    if 3.5 <= economy_rate <= 4.5:
        points += 4 
    elif 2 <= economy_rate <= 3.5:
        points += 7 
    elif economy_rate < 2:
        points += 10  
    
    return points


def calculating_fielding_points(catches):
    return catches * 10  
