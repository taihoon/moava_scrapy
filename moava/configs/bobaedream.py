# -*- coding: utf-8 -*-

SETTINGS = {
    "site": "bobaedream",
    "page_urls": [
        "http://www.bobaedream.co.kr/list?code=freeb&page=1",
        "http://www.bobaedream.co.kr/list?code=freeb&page=2",
        "http://www.bobaedream.co.kr/list?code=freeb&page=3"
    ],
    "post_href_query": "tr[itemscope] .pl14 a.bsubject::attr(href)",
    "title_query": ".writerProfile dt::attr(title)",
    "iframe_srcs_query": ".bodyCont iframe::attr(src)",
    "id_match_reg": r".*No=([^&]*)"
}
