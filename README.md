# the_HungMan_exercice_pyton
We want to program the hangman game. The goal of this game is to find a hidden word of which you know the size, and this by proposing a character on each try.
If the player suggests a character that exists in the word, it is displayed where it is in the word (for all its occurrences) and this try is not counted. If the
character does not exist in the word, this counts as a try.
The objective is to discover the word in a maximum number of tries (5 tries).
To program this game, the idea is to use 2 character tables. A first Tcar table to place the word to find and another Testai table containing the state
Game.
Tssais is the same length as Tcar but filled with the character ‘*’. When a character is found, the Testai table is updated: we place the character found at the
place the ‘*’ for each of its occurrences.
