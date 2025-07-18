ARTICLE_TEXT_PBRP = "<p><br></p>"
ARTICLE_TEXT_START_MARKER = "show-more-gradient"
ARTICLE_TEXT_END_MARKER = "</div>"
ARTICLE_TEXT_UNICODE_MARKER1 = "\u200e"
ARTICLE_TEXT_UNICODE_MARKER2 = "\u200f"
ARTICLE_DATE_MARKER = "post-date-value"
ARTICLE_PREFIX_CONTENT = "SPONSR_CONTENT "
ARTICLE_PREFIX_DATE = "SPONSR_DATE "
ARTICLE_PREFIX_ID = "SPONSR_ID "
ARTICLE_PREFIX_TITLE = "SPONSR_TITLE "
ARTICLE_PREFIX_NEXT = "SPONSR_NEXT "
ARTICLE_PREFIX_NEXT_ID = "SPONSR_NEXT_ID "
ARTICLE_PREFIX_SRC = "SPONSR_SRC "
ARTICLE_PREFIX_TEXT = "SPONSR_TEXT "
ARTICLE_PREFIX_URL = "SPONSR_URL "
BASE_URL = "https://sponsr.ru/marahovsky/"
CSS_PICKER = "div[class^='datepicker--cells datepicker--cells-days']"
EXCLUDED = [
    """<img loading="lazy" src="/project/183/post/674/image/1113/imagesprojects183183kox8zi31j11bdbf9.webp?1585989070641">""",
]
FILE_CACHE_COLLECT = "/tmp/sponsr-collect"
FILE_CACHE_CONTENT = "/tmp/sponsr-content"
FILE_CACHE_HTML = "/tmp/sponsr-html"
FILE_CACHE_HTML_CONTENT = "/tmp/sponsr-html-content"
FILE_CACHE_TOC = "/tmp/sponsr-toc"
FILE_CACHE_VISIT = "/tmp/sponsr-visit"
# 2020-3-22
#FIRST_POST = "https://sponsr.ru/marahovsky/588"
FIRST_POST = "593"
# 2020-5-1
#FIRST_POST = "https://sponsr.ru/marahovsky/?post_date=1588280400000"
# 2020-5-30
#FIRST_POST = "https://sponsr.ru/marahovsky/?post_date=1590786000000"
# 2020-6-1
#FIRST_POST = "https://sponsr.ru/marahovsky/?post_date=1590958800000"
# 2020-7-1
#FIRST_POST = "https://sponsr.ru/marahovsky/?post_date=1593550800000"
# 2020-8-1
#FIRST_POST = "https://sponsr.ru/marahovsky/?post_date=1596229200000"
# 2020-9-1
#FIRST_POST = "https://sponsr.ru/marahovsky/?post_date=1598907600000"
SELENIUM_DRIVER = "/Volumes/MOE/bin/geckodriver"
VISIT_LIMIT = 2
TEMPLATE_ARTICLE_XPATH = "/html/body/div[1]/div[1]/div[6]/div[2]/div[3]/div/div/div/div/div/div[2]/div[%ARTICLE_ID%]"
TEMPLATE_HTML = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
    </head>
	<body>
%CONTENT%
    </body>
</html>
"""
TEMPLATE_HTML_CONTENT = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html
	xmlns="http://www.w3.org/1999/xhtml"
	xmlns:xlink="http://www.w3.org/1999/xlink"
	xmlns:fb="http://www.gribuser.ru/xml/fictionbook/2.0">
	<head>
		<meta http-equiv="content-type" content="text/xhtml; charset=UTF-8"></meta>
		<link rel="stylesheet" type="text/css" href="style.css"></link>
		<link rel="stylesheet" type="text/css" href="unicode_fonts.css"></link>
	</head>
	<body>
%CONTENT%
    </body>
</html>
"""
TEMPLATE_HTML_CONTENT_ITEM = """
<h3 id="%ID%">%TITLE%</h3>
%TXT%
"""
TEMPLATE_HTML_ITEM = """
<h1 id="%ID%">%TITLE%</h1>
%TXT%
"""
TEMPLATE_TOC = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx
    xmlns="http://www.daisy.org/z3986/2005/ncx/"
    xmlns:fo="http://www.w3.org/1999/XSL/Format"
    xmlns:fb="http://www.gribuser.ru/xml/fictionbook/2.0"
    xmlns:xlink="http://www.w3.org/1999/xlink" version="2005-1">
    <head>
        <meta name="dtb:uid" content="7884d7d2-efe1-11e3-871d-0025905a0812"/>
        <meta name="dtb:depth" content="3"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <navMap>
%TOC%
    </navMap>
</ncx>
"""
TEMPLATE_TOC_NAV_POINT = """
<navPoint id="%ID%" playOrder="%ORDER%">
    <navLabel>
        <text>%TITLE%</text>
    </navLabel>
    <content src="content.html#%ID%"/>
</navPoint>
"""
XPATH_NEXT_MONTH = "/html/body/div[1]/div[1]/div[6]/div[2]/div[3]/div/div/div/nav/div[3]"
