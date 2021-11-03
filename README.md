# Introduction

# Mini-Max

The Mini-Max algorithm is a decision rule used in artificial intelligence, decision theory, game theory, statistics,
and philosophy for minimizing the possible loss for a worst-case scenario. In simple words, at each step, it assumes
that player A is trying to **maximize** its chances of winning, and in the next turn player B is trying to **minimize** the
chances of winning.

## Evaluation Function

Using the MiniMax algorithm to decide the next move can't tell us for sure if we are going to win the game, because
there is so many possibilities and unless you have a galaxy sized super-computer it's impossible, for that reason we use
heuristics, an evaluation function to help us compare two moves and decide the one that's likely to contribute to us
winning the game.

### Piece Square Tables (PST)

An extremely effective evaluation technique is called piece square tables. A PST's value indicates if a square is a good
square for a piece, or it isn't.

### Counting Materials

Counting the material on the board is the most basic way of evaluating a chess position. You can just compare
material: "I have one bishop and 2 knights, while my opponent has two bishops and one knight. So light pieces are equal.
We both have a queen, and one rook, so that is equal as well. He has four pawns and I have five... so in the end, I'm
one pawn up." That is basically it, with counting material.

#### Implementation

### Our Technique of Evaluation


  