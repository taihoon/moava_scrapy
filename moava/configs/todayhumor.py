# -*- coding: utf-8 -*-

SETTINGS = {
    "site": "todayhumor",
    "page_urls": [
        "http://www.todayhumor.co.kr/board/list.php?table=total&page=1&kind=total",
        "http://www.todayhumor.co.kr/board/list.php?table=total&page=2&kind=total",
        "http://www.todayhumor.co.kr/board/list.php?table=total&page=3&kind=total"
    ],
    "post_href_query": ".table_list .subject a::attr(href)",
    "title_query": ".viewSubjectDiv div::text",
    "iframe_srcs_query": ".viewContent iframe::attr(src)",
    "id_match_reg": r".*no=([^&]*)"
}
