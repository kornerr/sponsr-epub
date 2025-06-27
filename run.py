from DoVisitArticles import *

tasks = [
    DoVisitArticles(),
]

for task in tasks:
    taskName = task.__class__.__name__
    print(f"Executing '{taskName}'")
    task.execute()
