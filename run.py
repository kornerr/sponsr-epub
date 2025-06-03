from DoListMonthArticles import *

tasks = [
    DoListMonthArticles(),
]

for task in tasks:
    taskName = task.__class__.__name__
    print(f"Executing '{taskName}'")
    task.execute()
