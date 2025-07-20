from DoCollectArticles import *
from DoExtractContent import *
from DoGenerateContent import *
from DoGenerateHTML import *
from DoGenerateTOC import *
from DoVisitArticles import *
from constants import *

tasks = [
#    DoCollectArticles(FILE_CACHE_COLLECT),
    DoGenerateHTML(FILE_CACHE_COLLECT, FILE_CACHE_HTML),
#    DoVisitArticles(FILE_CACHE_VISIT),
#    DoExtractContent(FILE_CACHE_CONTENT, FILE_CACHE_VISIT),
#    DoGenerateTOC(FILE_CACHE_CONTENT, FILE_CACHE_TOC),
#    DoGenerateContent(FILE_CACHE_CONTENT, FILE_CACHE_HTML_CONTENT),
]

for task in tasks:
    taskName = task.__class__.__name__
    print(f"Executing '{taskName}'")
    task.execute()
