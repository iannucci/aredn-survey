# Component of AREDN Survey by Bob Iannucci
#
# See LICENSE.md for license information

import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

class Collector():
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        
    def query(self):
        '''
        Accesses the node's WiFi survey page, scrapes it, and
        returns a dictionary of the surveyed stations
        '''
        url = 'http://%s/cgi-bin/scan?rescan=1' % (self.host,)
        headers = {
            "Cache-Control": "no-cache"
        }
        html = requests.get(url, headers=headers, auth=(self.username, self.password))
        soup = BeautifulSoup(html.text, 'html.parser')
        tables = pd.read_html(StringIO(str(soup)))
        table = tables[0].transpose().to_dict()
        return table
