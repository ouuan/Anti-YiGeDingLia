# -*- coding:utf-8 -*-

import json

with open('..\\data\\idiom.json', "r", encoding = 'utf-8') as idiomjson:
	idioms = json.load(idiomjson)

vowels = {
	'ā': 'a',
	'á': 'a',
	'ǎ': 'a',
	'à': 'a',
	'ō': 'o',
	'ó': 'o',
	'ǒ': 'o',
	'ò': 'o',
	'ē': 'e',
	'é': 'e',
	'ě': 'e',
	'è': 'e',
	'ī': 'i',
	'í': 'i',
	'ǐ': 'i',
	'ì': 'i',
	'ū': 'u',
	'ú': 'u',
	'ǔ': 'u',
	'ù': 'u',
	'ǖ': 'v',
	'ǘ': 'v',
	'ǚ': 'v',
	'ǜ': 'v',
	'ü': 'v',
	'ɡ': 'g'
}

graph = {}

def processTones(s):
	for vowel, letter in vowels.items():
		pos = s.find(vowel)
		while pos != -1:
			s = s[:pos] + letter + s[pos + len(vowel):]
			pos = s.find(vowel)
	return s

for idiom in idioms:
	pinyin = idiom['pinyin'].split(' ')
	if len(pinyin) != 4:
		continue
	first = processTones(pinyin[0])
	last = processTones(pinyin[3])
	if not first in graph:
		graph[first] = {}
	if not last in graph:
		graph[last] = {}
	graph[last][first] = idiom['word']
	
with open('..\\data\\yigedinglia.json', "w", encoding='utf-8') as processedjson:
	processedjson.write('var graph = ' + json.dumps(graph, ensure_ascii = False) + ';');