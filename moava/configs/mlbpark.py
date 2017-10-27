# -*- coding: utf-8 -*-

SETTINGS = {
    "site": "mlbpark",
    "page_urls": [
        "http://mlbpark.donga.com/mp/b.php?p=1&m=list&b=bullpen&query=&select=&user=",
        "http://mlbpark.donga.com/mp/b.php?p=31&m=list&b=bullpen&query=&select=&user=",
        "http://mlbpark.donga.com/mp/b.php?p=61&m=list&b=bullpen&query=&select=&user="
    ],
    "post_href_query": ".tbl_box a.bullpenbox::attr(href)",
    "title_query": ".titles::text",
    "iframe_srcs_query": "#contentDetail iframe::attr(src)",
    "id_match_reg": r".*id=([^&]*)"
}
