# -*- coding: utf-8 -*-

from urllib.parse import urlparse, parse_qs

def get_youtube_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get("v")
    if quer_v:
        return quer_v[0]
    path = u_pars.path.split("/")
    if path:
        return path[-1]
