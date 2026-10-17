from collections import defaultdict

def solution(tournament, results):
    
    winners = defaultdict(int)

    for i in range(len(results)):
        if results[i] == 0:
            winner = tournament[i][1]
            winners[winner] += 3
        else:
            winner = tournament[i][0]
            winners[winner] += 3
            
    p = 0
    my_winner = ""

    for winner, score in winners.items():
        if score > p:
            my_winner = winner
        else:
            p = score

    return my_winner
    
tournament = [
    ["HTML", "C#"],
    ["C#", "PYTHON"],
    ["PYTHON", "HTML"]
]   

results = [0,0,1]

print(solution(tournament, results))