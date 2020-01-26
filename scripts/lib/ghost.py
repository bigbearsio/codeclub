import xml.etree.ElementTree as ET
import re
import requests

rss_url = "https://codeclub.bigbears.io/rss/"
episode_pattern = re.compile('EP[^\\d]*(\\d*)[^\\d]*') #EP 16 - Cucumber

def get_latest_episode():
    return get_latest_episode_from_content(requests.get(rss_url).text)

def get_latest_episode_from_content(xmlContent):
    root = ET.fromstring(xmlContent)
    t = root.find("channel/item/title").text
    m = episode_pattern.match(t)
    return int(m.group(1))