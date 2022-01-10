""" Wrapper for urllib.request """

import random
import ssl
from typing import Any
from urllib.request import Request, urlopen, ProxyHandler, build_opener, install_opener, HTTPBasicAuthHandler, HTTPHandler

from .user_agent import user_agents


def get(url: str, sessionid=None) -> Any:
    """
    Function send the HTTP requests to Instagram and
    Login into Instagram with session id
    and return the Html Content
    """
    # session = urllib.request.Session()

    proxy_support = ProxyHandler({'http': 'http://c81f35e9601a4f2f87a93774038a6660b8a8b7c77b7:render=false&customHeaders=false@proxy.scrape.do:8080',
                                                 'https': 'http://c81f35e9601a4f2f87a93774038a6660b8a8b7c77b7:render=false&customHeaders=false@proxy.scrape.do:8080'})
    #auth = HTTPBasicAuthHandler()
    #opener = build_opener(proxy_support,  auth, HTTPHandler)
    #install_opener(opener)

    proxies = {
        'http': 'https://c81f35e9601a4f2f87a93774038a6660b8a8b7c77b7@proxy.scrape.do:8080',
        'https': 'https://c81f35e9601a4f2f87a93774038a6660b8a8b7c77b7@proxy.scrape.do:8080',
    }

    #ctx = ssl.create_default_context()
    #ctx.check_hostname = False
    #ctx.verify_mode = ssl.CERT_NONE

    print('com proxy')

    request = Request(
        url=url, headers={"User-Agent": f"user-agent: {random.choice(user_agents)}"}
    )
    # proxy_host = 'https://3b29f053ef87453d9182834278fb9f416536a2a0358@proxy.scrape.do:8080'
    # request.set_proxy(proxy_host, 'https')
    if sessionid:
        request.add_header("Cookie", f"sessionid={sessionid}")
    #with urlopen(request, context=ctx) as response:
    with urlopen(request) as response:
        html = response.read()

    return html.decode("utf-8")