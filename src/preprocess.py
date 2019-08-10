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
	'ü': 'v'
}

dis = {}
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
	if not first in dis:
		#print(first, idiom['word'])
		dis[first] = {first: {'dist': 0, 'word': []}};
		graph[first] = set()
	if not last in dis:
		#print(idiom['word'], last)
		dis[last] = {last: {'dist': 0, 'word': []}};
		graph[last] = set()
	if first != last:
		dis[first][last] = {'dist': 1, 'word': [idiom['word']]}
	else:
		dis[first][last] = {'dist': 0, 'word': [idiom['word']]}
	graph[first].add(last)

cnt = 0
for k in dis.keys():
	cnt = cnt + 1
	print(k, str(cnt) + '/' + str(len(dis)))
	for i in dis.keys():
		for j in dis.keys():
			if k in dis[i] and j in dis[k]:
				newdis = dis[i][k]['dist'] + dis[k][j]['dist']
				if (not j in dis[i]) or (newdis < dis[i][j]['dist']):
					if not j in dis[i]:
						dis[i][j] = {}
					dis[i][j]['dist'] = newdis
					dis[i][j]['word'] = dis[i][k]['word'] + dis[k][j]['word']

graph_list = {}

for u, adj in graph.items():
	graph_list[u] = []
	for v in adj:
		graph_list[u].append(v)

with open('..\\data\\yigedinglia.json', "w", encoding='utf-8') as processedjson:
	processedjson.write('var dis = ' + json.dumps(dis, ensure_ascii = False) + ';\n');
	processedjson.write('var graph = ' + json.dumps(graph_list, ensure_ascii = False) + ';\n');