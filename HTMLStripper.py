import re

def stripTags(html):
	tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
	return tag_re.sub('', html)
	
def cleanText(text):
	regex = [r'>+.*(\b|\r|\n)', r'Content-Type:\s[A-Za-z/]+;',r'charset=\"[A-Za-z\-0-9]*\"', r'Content-Transfer-Encoding:\s[A-Za-z0-9]*', r'&[a-z]+;']
	new_text = text
	for rgx_match in regex:
		new_text = re.sub(rgx_match, '', new_text)
	return new_text