import sys
from DoGenerateSingleHTML import *
from constants import *

DoGenerateSingleHTML(FILE_CACHE_COLLECT, sys.argv[1]).execute()
