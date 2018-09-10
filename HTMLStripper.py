import re

def stripTags(html):
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    return tag_re.sub('', html)