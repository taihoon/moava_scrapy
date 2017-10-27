# -*- coding: utf-8 -*-

SETTINGS = {
    "site": "clien",
    "page_urls": [
        "https://www.clien.net/service/board/park?&od=T31&po=0",
        "https://www.clien.net/service/board/park?&od=T31&po=1",
        "https://www.clien.net/service/board/park?&od=T31&po=2"
    ],
    "post_href_query": ".post-list a.list-subject::attr(href)",

    "title_query": ".title-subject > div::text",
    "iframe_srcs_query": ".post-content iframe::attr(src)",
    "id_match_reg": r".*\/park\/([^?&]*)"
}
