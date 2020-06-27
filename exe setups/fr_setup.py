import cx_Freeze
from cx_Freeze import *

setup(name="Fantasy Fight", 
      options={'build_exe': {'packages': ['pygame']}}, 
      executables=[Executable('fr_fantasy_fight.py')])