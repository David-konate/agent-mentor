import sys
import os

# o2switch (passenger) : on ajoute back/ au path et on expose "application"
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "back"))

from app import app as application
