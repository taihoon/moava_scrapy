# -*- coding: utf-8 -*-

SETTINGS = {
    "site": "ddanzi",
    "page_urls": [
        "http://www.ddanzi.com/index.php?mid=free&page=1",
        "http://www.ddanzi.com/index.php?mid=free&page=2",
        "http://www.ddanzi.com/index.php?mid=free&page=3"
    ],
    "post_href_query": ".board_list tr[class!=notice] .title a::attr(href)",
    "title_query": ".read_header h1 a::text",
    "iframe_srcs_query": "div.xe_content iframe::attr(src)",
    "id_match_reg": r".*document_srl=([^&]*)"
}
