import pymada
import pymada.errors
from pymada.classes.game import Game
from pymada.classes.player import Player
from pymada.classes.fleet import Fleet

print("launching...")

species='random'

player1=Player(name='a',species=species,faction='imp')
armada1=Fleet()
armada1.add_ship(model='test_ship', name='a', faction='imp', upgrades=None)

player2=Player(name='b',species=species,faction='reb')
armada2=Fleet()
armada2.add_ship(model='test_ship', name='b', faction='reb', upgrades=None)

game=Game(players=[player1,player2],fleets=[armada1,armada2])

winner=game.play()

if winner:
    print(f'winner={winner.name}')

print("finishing...")
