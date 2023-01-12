# baseball_elimination_problem

In a full season, each team plays the other team plays two matches with every other team in the league, one at and one away from home. Hence, each team plays 10 matches. Each match is identified by the first letters of the two teams, e.g., (B, C)

If a match ends in regulation time with a winner, the winner and loser are awarded 3 points and 0 points, respectively. If a match ends in regulation time with a tie, there is a shootout, and the winner and loser are awarded 2 points and 1 point, respectively. (This point system is not what is currently used in most national and international soccer leagues, but has been used in the past.) The mini-IvyLeague champion(s) is (are) the team(s) that has (have) been awarded the most points after
the completion of the 30 scheduled matches that season. Suppose that after 19 matches have been played the following results about these matches is known.

![image](https://user-images.githubusercontent.com/95487129/211945912-a7bd1f24-8db3-4aa7-b634-d6cac29e2c4d.png)

![image](https://user-images.githubusercontent.com/95487129/211946107-f6408d39-dd99-4870-8a8b-2da41573cdc2.png)

We'd like to answer these questions:
1. it is possible for B to win or tie for the championship;
2. it is possible for C to win the championship;
3. it is possible for Y, P, H, and D to end the season tied for the championship, each having earned 20 points, with C and B tied for last place, each with 5 points.

Approach:
1. We can see this problem as a maximum flow computation throughout a network based on each scenario above.
2. As we defined the network, we can implement algorithm "Edmond-Karps" to compute the maximum flow for each scenario to answer the question above.
3. In this case, we created a python script of "Edmond-Karps" to help computing the maximum flow.
