import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parents[1].absolute()))

from playsound2 import playsound

playsound("test.mp4")
