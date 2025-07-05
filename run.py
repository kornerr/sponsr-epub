from DoGenerateTOC import *
from DoVisitArticles import *
from constants import *

tasks = [
    #DoVisitArticles(FILE_CACHE_VISIT),
    DoGenerateTOC(FILE_CACHE_VISIT),
]

for task in tasks:
    taskName = task.__class__.__name__
    print(f"Executing '{taskName}'")
    task.execute()
