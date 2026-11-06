#ALGORITHM
1. Start
2. Input the runs scored by the player.
3. Input the balls faced by the player.
4. Input the total fours hit by the player.
5. Input the total sixes hit by the player.
6. Input the wickets taken by the player.
7. Input the runs conceded by the player.
8. Input the overs bowled by the player.
9. Input the catches taken by the player.
10. Calculate the batting strike rate using:
- Strike Rate = (Runs Scored / Balls Faced) × 100

11. Calculate the bowling economy using:

- Economy = Runs Conceded / Overs Bowled

12. Check the batting performance:
- If runs ≥ 50 and strike rate ≥ 120, display Excellent Batter.
- Else if runs ≥ 30 and strike rate ≥ 100, display Good Batter.
- Else if runs ≥ 20, display Average Batter.
- Otherwise, display Poor Batter.
13. Check the bowling performance:
- If wickets ≥ 3 and economy ≤ 6, display Excellent Bowler.
- Else if wickets ≥ 2 and economy ≤ 8, display Good Bowler.
- Else if wickets ≥ 1, display Average Bowler.
- Otherwise, display Poor Bowler.
14. Check the fielding performance:
- If catches ≥ 2, display Outstanding Fielder.
- Else if catches = 1, display Active Player.
- Otherwise, display Need Improvement.
15. Display the overall all-rounder decision.
16. Stop.


#CODE
run_scored=int(input("Enter the Run scorted by Player :"))
print(run_scored)
ball_faced=int(input("Enter the Ball faced by Player :"))
print(ball_faced)
fours=int(input("Enter the total Fours hits  by Player :"))
print(fours)
sixes=int(input("Enter the Total Sixes hits by Player :"))
print(sixes)
wickets_taken=int(input("Enter the wicket taken by Player :"))
print(wickets_taken)
run_conc=int(input("Enter the Run conceeded by Player :"))
print(run_conc)
overs_bowled=int(input("Enter the over bowled by Player :"))
print(overs_bowled)
catch_taken=int(input("Enter the catch taken by Player :"))
print(catch_taken)

print("Calculating the batting strike rate of player:")
sr=(run_scored/ball_faced)*100
print(sr)
print("Calculating the Balling Economy of player:")
eco=(run_conc/overs_bowled)
print(eco)

batter=1
if run_scored>=50 and sr>=120:
    print("Execellent Batter:")
elif run_scored>=30 and sr>=100:
    print("Good Batter")
elif run_scored>=20:
    print("Average Batter")
else :
    print("Poor Batter")

bowler=1
if wickets_taken>=3 and eco<=6:
    print("Execellent Bowler:")
elif wickets_taken>=2 and eco<=8:
    print("Good Bowler")
elif wickets_taken>=1:
    print("Average Bowler")
else :
    print("Poor Bowler")

if catch_taken>=2:
    print("Outstanding Fielder")
elif catch_taken == 1:
    print("Active Player")
else :
    print("Need improvement")


print("Overall All-Rounder Decission:")
if batter==1 and bowler==1:
    print("Star All-rounder")
elif batter==2 and bowler==2:
    print("Strong All-Rounder")
elif batter==3 and bowler==3:
    print("Supporting All-Rounder")


#OUTPUT
Enter the Run scorted by Player : 60
60
Enter the Ball faced by Player : 40
40
Enter the total Fours hits  by Player : 6
6
Enter the Total Sixes hits by Player : 3
3
Enter the wicket taken by Player : 3
3
Enter the Run conceeded by Player : 20
20
Enter the over bowled by Player : 4
4
Enter the catch taken by Player : 2
2

Calculating the batting strike rate of player:
150.0

Calculating the Balling Economy of player:
5.0

Execellent Batter:
Execellent Bowler:
Outstanding Fielder

Overall All-Rounder Decission:
Star All-rounder


