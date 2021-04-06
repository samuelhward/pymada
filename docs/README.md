[![Deployment/Testing](https://github.com/armoured-moose/pymada/actions/workflows/deployment_testing.yml/badge.svg)](https://github.com/armoured-moose/pymada/actions/workflows/deployment_testing.yml)

# Pymada

Solving Armada with AI.

Ongoing project, excuse to learn some Python.

# Guide

Clone then install with: 

```shell
pip install pymada
```

Run a complete game with:

```python
import pymada
from pymada.classes.game import Game
from pymada.classes.player import Player
from pymada.classes.fleet import Fleet

print("launching...")

species = "human"

player1 = Player(name="player 1", species=species, faction="imp")
armada1 = Fleet()
armada1.add_ship(model="test_ship", name="a", faction="imp", upgrades=None)

player2 = Player(name="player 2", species=species, faction="reb")
armada2 = Fleet()
armada2.add_ship(model="test_ship", name="b", faction="reb", upgrades=None)

game = Game(players=[player1, player2], fleets=[armada1, armada2])

winner = game.play()

print(f"winner={winner.name}")

print("finishing...")
```


# Contributing

* Formatting by Black
* CI by Github actions
* Units in cm/degrees
* Tests with Pytest

# To-do

- transfer settings to file to be read at runtime
- add code coverage monitor
- update docstrings
- add plotting to `extras_require` in `setup.py`
- Kingston fleet list reader
- game saves with pickle?
- replay function using logger