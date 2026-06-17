# -*- coding: utf-8 -*-
"""
passenger_wsgi.py  (entrée o2switch)
====================================
Point d'entrée pour l'hébergement o2switch (Passenger).
On ajoute le dossier back/ au chemin d'import, puis on expose l'app Flask
sous le nom "application" (ce que Passenger attend).
"""

import sys
import os

# Ajoute back/ au chemin pour pouvoir importer app.py et ses couches.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "back"))

from app import app as application  # noqa: E402
