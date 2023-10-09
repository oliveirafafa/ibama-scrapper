import os
import sys


class Config:
    DIR_ROOT = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)