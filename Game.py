import random

def simulate_balls():
    balls_outcome = [0, 1, 2, 3, 4, 6, 'W']
    return random.choice(balls_outcome)

def play_innings(team_name, total_balls, target=None):
    total_runs = 0
    wickets = 0
    balls_played = 0
    
    for ball in range(total_balls):
        input(f"Press Enter To Deliver Next Ball for {team_name} . . .")
        outcome = simulate_balls()
        
        if outcome == "W":
            wickets += 1
            print(f"Ball {ball+1}: Wicket! Total wickets: {wickets}")
            if wickets == 3:
                print(f"Team {team_name} is all out for {total_runs} runs")
                break
        else:
            total_runs += outcome
            print(f"Ball {ball+1}: {outcome} runs. Total runs: {total_runs}")
        balls_played += 1
        
        if target and total_runs >= target:
            print(f"Team {team_name} has reached the target of {target} runs in {balls_played} balls")
            break
        
    return total_runs, wickets, balls_played

def toss():
    return random.choice(['user', 'computer']) 

def play_cricket_game():
    print("Welcome To The Cricket Game! ......")
    
    user_team_name = input("Enter your team name: ")
    computer_team_name = "Computer"
    
    while True:
        overs = input("Choose Number Of Overs (2 or 5): ")
        
        if overs in ['2', '5']:
            overs = int(overs)
            break
        else:
            print("Invalid choice. Please choose 2 or 5 overs.")
            
    total_balls = overs * 6
    
    user_choice = ''
    computer_choice = ''
    
    toss_winner = toss()
    if toss_winner == 'user':
        print(f"{user_team_name} won the toss!")    
        while True:
            choice = input("Do you want to bat or bowl first? (bat/bowl): ").lower()
            if choice in ['bat', 'bowl']:
                user_choice = choice
                computer_choice = 'bowl' if user_choice == 'bat' else 'bat'
                break
            else:
                print("Invalid choice. Please choose bat or bowl.")
    else:
        print("Computer won the toss!")
        computer_choice = random.choice(['bat', 'bowl'])
        user_choice = 'bowl' if computer_choice == 'bat' else 'bat'
        print(f"{computer_team_name} chose to {computer_choice}.")
        
    # Play First Innings:
    if user_choice == 'bat':
        print(f"{user_team_name} will bat first")
        user_runs, user_wickets, user_balls = play_innings(user_team_name, total_balls)           
        print(f"\nEnd of innings! {user_team_name} scored {user_runs} runs with {user_wickets} wickets.")
        print(f"\n{computer_team_name} needs {user_runs + 1} runs to win.")
        
        computer_runs, computer_wickets, computer_balls = play_innings(computer_team_name, total_balls, user_runs + 1)
    else:
        print(f"{computer_team_name} will bat first.")
        computer_runs, computer_wickets, computer_balls = play_innings(computer_team_name, total_balls)
        print(f"\nEnd of innings! {computer_team_name} scored {computer_runs} runs with {computer_wickets} wickets.")
        
        print(f"\n{user_team_name} needs {computer_runs + 1} runs to win.")
        user_runs, user_wickets, user_balls = play_innings(user_team_name, total_balls, computer_runs + 1)
    
    # Determine Winner
    if user_runs > computer_runs:
        wickets_remaining = 3 - user_wickets
        print(f"\n{user_team_name} won by {wickets_remaining} wickets")
    elif computer_runs > user_runs:
        runs_remaining = computer_runs - user_runs
        print(f"\n{computer_team_name} won by {runs_remaining} runs")
    else:
        print(f"\nIt's a tie! Both teams scored {user_runs} runs.")

if __name__ == '__main__':
    play_cricket_game()
