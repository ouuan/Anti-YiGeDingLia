# -*- coding:utf-8 -*-

import json
from collections import OrderedDict

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

graph = OrderedDict()
igraph = OrderedDict()

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
		graph[first] = OrderedDict()
		igraph[first] = OrderedDict()
	if not last in graph:
		graph[last] = OrderedDict()
		igraph[last] = OrderedDict()
	graph[first][last] = igraph[last][first] = idiom['word']

def sortedDict(x):
	keys = sorted(x.keys())
	out = OrderedDict()
	for key in keys:
		out[key] = x[key]
	return out

for u in graph:
	graph[u] = sortedDict(graph[u])
	igraph[u] = sortedDict(igraph[u])

graph = sortedDict(graph)
igraph = sortedDict(igraph)

nodis = OrderedDict()
nopre = OrderedDict()
q = []
ql = 0
qr = -1

for u in graph:
	if len(graph[u]) == 0:
		nodis[u] = 0
		q.append(u)
		qr = qr + 1

while ql <= qr:
	u = q[ql]
	ql = ql + 1
	for v in igraph[u]:
		if not v in nodis:
			nodis[v] = nodis[u] + 1
			nopre[v] = u
			q.append(v)
			qr = qr + 1

nodis = sortedDict(nodis)
nopre = sortedDict(nopre)

loopdis = OrderedDict()
looppre = OrderedDict()
q = []
ql = 0
qr = -1

for u in graph:
	if u in graph[u]:
		loopdis[u] = 0
		q.append(u)
		qr = qr + 1

while ql <= qr:
	u = q[ql]
	ql = ql + 1
	for v in igraph[u]:
		if not v in loopdis:
			loopdis[v] = loopdis[u] + 1
			looppre[v] = u
			q.append(v)
			qr = qr + 1

loopdis = sortedDict(loopdis)
looppre = sortedDict(looppre)

def getShortest(u):
	if nodis[u] == 0:
		return '已经无法接下去了'
	if nodis[u] == 1:
		return graph[u][nopre[u]]
	return graph[u][nopre[u]] + ' → ' + getShortest(nopre[u])

def getFarthest(u):
	if nodis[u] == 0:
		return '已经无法接下去了'
	farthest_dis = -1
	farthest_v = 0
	for v in graph[u]:
		if nodis[v] > farthest_dis:
			farthest_dis = nodis[v]
			farthest_v = v
	return graph[u][farthest_v] + ' (' + getShortest(farthest_v) + ')'

def getLoop(u):
	if not u in loopdis:
		return '无法接到任何循环'
	if loopdis[u] == 0:
		return graph[u][u]
	return graph[u][looppre[u]] + ' → ' + getLoop(looppre[u])

shortest = OrderedDict()
farthest = OrderedDict()
loop = OrderedDict()

for u in graph:
	shortest[u] = getShortest(u)
	farthest[u] = getFarthest(u)
	loop[u] = getLoop(u)

shortest = sortedDict(shortest)
farthest = sortedDict(farthest)
loop = sortedDict(loop)

with open('..\\data\\dis.json', "w", encoding = 'utf-8') as disjson:
	disjson.write('var nodis = ' + json.dumps(nodis, ensure_ascii = False) + ';\n');
	disjson.write('var loopdis = ' + json.dumps(loopdis, ensure_ascii = False) + ';\n');

with open('..\\data\\graph.json', "w", encoding = 'utf-8') as graphjson:
	graphjson.write('var graph = ' + json.dumps(graph, ensure_ascii = False) + ';\n');
	graphjson.write('var igraph = ' + json.dumps(igraph, ensure_ascii = False) + ';\n');

with open('..\\data\\yigedinglia.json', "w", encoding = 'utf-8') as processedjson:
	processedjson.write('var shortest = ' + json.dumps(shortest, ensure_ascii = False) + ';\n');
	processedjson.write('var farthest = ' + json.dumps(farthest, ensure_ascii = False) + ';\n');
	processedjson.write('var loop = ' + json.dumps(loop, ensure_ascii = False) + ';\n');