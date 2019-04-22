# baseball
baseball in python

This program is intended to solve the baseball puzzle described in an Mar 22, 2019 article entitled "Can You Turn America’s Pastime Into A Game Of Yahtzee?" Here, we'll describe the approach used in this program, as well as how to play.

A game of baseball typically consists of 9 innings, each with a top and a bottom. The game begins at the top of the 1st inning with one team. The team continues to send batters to the batter's mound so long as batters are able to get successful base hits, get walked, or hit a home run. When three of them have either struck out, fouled out, fly out, fail to get to 1st base, or advance to other bases, the bottom of the inning begins and the opposing team comes to bat.    

In this game, the batter's performance is determined strictly by chance. A routine with a random number generator will select two numbers, each from one to six. That is, a dice roll. The sum will provide a key for the outcome for the batter.

The Game_Status_Board is a dictionary that contains details of the situation. This includes the inning, whether top or bottom, number of outs, what players are on what bases, scores.

TODO:
Doc's
Test's
f-string messaging for game transcription. example f"{name} runs to first base."

FEATURE IDEAS:
Web frontend in flask.
