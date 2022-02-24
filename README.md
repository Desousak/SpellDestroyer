# Spell Destroyer
### A script for purposely messing up text - like the opposite of a spell checker.
<br />

## How it works:
Three techniques are used to mess up your inputted text:
1. Words are replaced with their common spelling mistakes (generated from <a href="https://www.dcs.bbk.ac.uk/~ROGER/corpora.html">this</a> corpora, found in `./misspelled`)
2. Random letters within a word are capitalized
3. Spaces are generated randomly in the middle of, and in-between, words

Each of the above can be commented out to turn on/off a technique. Probabilities can also be changed to mess up the text more, or less.


## How to use:
1. Place your text within the `input.txt` file
2. Tweak `spelld.py` to fit your needs
3. Run `spelld.py` 
4. Get the messed up text within the `output.txt` file

## Todo:
1. Rework each technique so that they can all be done in a single pass
2. Implement a smarter algorithm for generating spelling mistakes (maybe use an additional corpora?)
3. Flesh out the text filter to normalize inputted text