import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.piece import Piece
from pymada.classes.ship import Ship

print("launching...")

shipA = Ship(name="", faction="", model="", upgrades="")
shipA.position = Position(x=5.0, y=5.0, theta=0.0)

print("finishing...")
