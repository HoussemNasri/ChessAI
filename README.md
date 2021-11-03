# Introduction

# Mini-Max

The Mini-Max algorithm is a decision rule used in artificial intelligence, decision theory, game theory, statistics,
and philosophy for minimizing the possible loss for a worst-case scenario. In simple words, at each step, it assumes
that player A is trying to **maximize** its chances of winning, and in the next turn player B is trying to **minimize** the
chances of winning.

# Evaluation Function

Applying MiniMax on a TicTacToe game will play every possibility in the game and pick the move that will 100% make you win or at least
Draw, winning against such algorithm is impossible, but chess unlike TicTacToe has an infinite number of possibilities so we can't keep playing the games until
finding the move that will guarantie winning, for that reason we use an **evaluation function**, this function takes the board state after playing a move
and returns a score of how likely you'll win, the MiniMax algorithm uses this function to evaluate and compare moves.

## Piece Square Tables (PST)

An extremely effective evaluation technique is called piece square tables. A PST's value indicates if a square is a good
square for a piece, or it isn't.

## Counting Materials

Counting the material on the board is the most basic way of evaluating a chess position. You can just compare
material: "I have one bishop and 2 knights, while my opponent has two bishops and one knight. So light pieces are equal.
We both have a queen, and one rook, so that is equal as well. He has four pawns and I have five... so in the end, I'm
one pawn up." That is basically it, with counting material.

### Implementation

## The Technique We Used
We used a combination of PST and Material couting to achieve the highest precision
### Material Counting Parameters
- **Queen:** 900 points
- **Rook:** 500 points


  
