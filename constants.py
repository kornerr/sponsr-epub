ARTICLE_DATE_MARKER = "post-date-value"
ARTICLE_PREFIX_DATE = "SPONSR_DATE "
ARTICLE_PREFIX_NEXT = "SPONSR_NEXT "
ARTICLE_PREFIX_SRC = "SPONSR_SRC "
ARTICLE_PREFIX_URL = "SPONSR_URL "
CSS_PICKER = "div[class^='datepicker--cells datepicker--cells-days']"
FILE_CACHE_TOC = "/tmp/sponsr-toc"
FILE_CACHE_VISIT = "/tmp/sponsr-visit"
FIRST_POST = "https://sponsr.ru/marahovsky/?post_date=1585688400000"
SELENIUM_DRIVER = "/Volumes/MOE/bin/geckodriver"
VISIT_LIMIT = 33
TEMPLATE_ARTICLE_XPATH = "/html/body/div[1]/div[1]/div[6]/div[2]/div[3]/div/div/div/div/div/div[2]/div[%ARTICLE_ID%]"
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
