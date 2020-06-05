+++
title = "Chopsticks in Prolog"
description = ""
tags = [
    "Prolog",
]
date = "2020-06-05"
categories = [
    "Development",
]
+++

## The Game
Chopsticks is a simple game of many variations played by children and college students. The variation I play is:
1. two players start by each sticking both index fingers out to represent a count of one on each hand
2. players alternate turns until someone loses by having a count of zero on both hands
3. on a player's turn, he must either:
    1. use one of his hands with positive count $H1$ to tap one of the other player's hands $H2$. The other player updates the count on $H2$ to $(H1+H2) \bmod 5$ by changing the number of fingers sticking out
    2. redistribute aka "split" his fingers in one of two ways: $(4,0)-->(2,2)$ or $(2,0)-->(1,1)$

For example, we can visualize the first turn of the game like so:
* each cell is a player's hand
* \* designates whose turn it is
* LL means top player used his left hand (wrt us, so actually his right hand) to tap bottom player's left hand

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20200605-prolog-chopsticks-first-move.svg|First move of the game" 
>}}

Like many games, Chopsticks is well-suited to being modeled in Prolog. I was particularly interested in determining whether the first or second player has a forced win. Unfortunately, for the variation given above, there is no forced win for either player. Let's see how I modeled this in Prolog ([source code](https://github.com/charlesjlee/prolog/blob/master/chopsticks.pl), [run online](https://swish.swi-prolog.org/p/Chopsticks.swinb)).

My original vision was to test *all* possible variations to find rulesets (there is at least [one](https://kipkis.com/Always_Win_Chopsticks)) with forced wins. I actually got as far as implementing all the variations with configurable toggles everywhere, but the code was horribly bug-infested and I threw it in the garbage. I might return to this one day when I'm better at Prolog. In the meantime, this simple, straightforward code will have to suffice.

## The Program
We first define helper predicate `tap/3` that calculates new finger counts and some facts about valid `split` and `lost` states.
```prolog
tap(From, To, ToNew) :-
	From \= 0,
	Total is From + To,
	ToNew is mod(Total, 5).

split(0, 4, 2).
split(4, 0, 2).
split(0, 2, 1).
split(2, 0, 1).

lost(0, 0).
```

There are five possible moves (LL, RR, LR, RL, split) on a player's turn. `get_next/3` is comprised of a rule for each move for each player for a total of ten rules.
```prolog
% get_next(hand(TopLeft,TopRight,BottomLeft,BottomRight,Turn), Next, Seen)
% calculates the Next unSeen state given it is Turn's move
get_next(hand(TL,TR,BL,BR,bottom), Next, Seen) :- tap(BL,TL,TL_New), Next=hand(TL_New,TR,BL,BR,top), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,bottom), Next, Seen) :- tap(BR,TR,TR_New), Next=hand(TL,TR_New,BL,BR,top), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,bottom), Next, Seen) :- tap(BL,TR,TR_New), Next=hand(TL,TR_New,BL,BR,top), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,bottom), Next, Seen) :- tap(BR,TL,TL_New), Next=hand(TL_New,TR,BL,BR,top), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,top), Next, Seen) :- tap(TL,BL,BL_New), Next=hand(TL,TR,BL_New,BR,bottom), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,top), Next, Seen) :- tap(TR,BR,BR_New), Next=hand(TL,TR,BL,BR_New,bottom), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,top), Next, Seen) :- tap(TR,BL,BL_New), Next=hand(TL,TR,BL_New,BR,bottom), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,top), Next, Seen) :- tap(TL,BR,BR_New), Next=hand(TL,TR,BL,BR_New,bottom), \+member(Next,Seen).

get_next(hand(TL,TR,BL,BR,bottom), Next, Seen) :- split(BL,BR,S), Next=hand(TL,TR,S,S,top), \+member(Next,Seen).
get_next(hand(TL,TR,BL,BR,top), Next, Seen) :- split(TL,TR,S), Next=hand(S,S,BL,BR,bottom), \+member(Next,Seen).
```

The final and most interesting predicate `forced_win/2` has two base cases and one recursive case. I was proud of myself 😂 for figuring out the recursive case and feel that it nicely captures the expressive power of Prolog.

The `\+` operator can be read as "not". The `!` operator is a "cut", which means "don't try to re-satisfy any of the previous clauses". We use this because we are interested in only the first forced win.
```prolog
% current player already won
forced_win(hand(TL,TR,_,_,bottom), _) :- lost(TL, TR), !.
forced_win(hand(_,_,BL,BR,top), _) :- lost(BL, BR), !.

% current player can win in a single move
forced_win(hand(TL,TR,BL,BR,bottom), Seen) :-
	\+ lost(BL, BR),
	get_next(hand(TL,TR,BL,BR,bottom), hand(TL_2,TR_2,BL,BR,top), Seen),
	lost(TL_2, TR_2),
	!.
forced_win(hand(TL,TR,BL,BR,top), Seen) :-
	\+ lost(TL, TR),
	get_next(hand(TL,TR,BL,BR,top), hand(TL,TR,BL_2,BR_2,bottom), Seen),
	lost(BL_2, BR_2),
	!.

% current player has a branch that always ends in a win
forced_win(H1, Seen) :-
	% can the current player choose a move...
	get_next(H1, H2, Seen),
	append(Seen, H1, NewSeen),

	% s.t. all of the opponent's possible moves result in a forced win?
	setof(H3, get_next(H2, H3, NewSeen), Hs),
	forall(member(H, Hs), forced_win(H, NewSeen)),
	!.
```

## The Query
Finally we run our completed program to see if there exist forced wins for the first or second players.

```prolog
?- forced_win(hand(1,1,1,1,top), []).
false.

?- forced_win(hand(1,1,2,1,bottom), []).
false.
```