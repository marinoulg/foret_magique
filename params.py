import os
from pathlib import PosixPath
import sys

LOCAL_PATH = PosixPath(os.path.join(os.path.expanduser('~'), "code"))
PATH_FORET_MAGIQUE = PosixPath(os.getcwd())
SRC = PosixPath("src")
PATH_SRC = PosixPath(LOCAL_PATH, PATH_FORET_MAGIQUE, SRC)

# Ajouter le chemin de "src" au Python path
sys.path.append(str(PATH_SRC))
