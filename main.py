from random import *
import networkx as nx
# import matplotlib.pyplot as plt

# Get Followers as much as possible
followers={}
with open('res.txt', 'r') as fr:
    for line in fr:
       pos = line.find(' ')
       index = int(line[:pos])
       cnt = int(line[pos+1:])
       followers[index]=cnt

def get(index):
	if index in followers:
		return followers[index]
	return randint(1, 500)

for key in followers:
    print key, followers[key]

G = nx.Graph()
with open('AMiner-Coauthor.txt', 'r') as f:
	j = 0
	for line in f:
		if line[0] != '#':
			continue
		pos_tab = 0
		u = int(line[1 : line.find('\t', pos_tab)])
		pos_tab = line.find('\t', pos_tab)
		v = int(line[pos_tab + 1 : line.find('\t', pos_tab + 1)])
		pos_tab = line.find('\t', pos_tab + 1)
		w = int(line[pos_tab + 1])
		G.add_edge(u, v, weight=w)
		# print("%d %d %d" % (u, v, w))
		if u not in followers:
			followers[u]=randint(1,500)
		if v not in followers:
			followers[v]=randint(1,500)
		if j == 1000:
			break
		j += 1


# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()
pr = nx.pagerank(G, alpha=0.9, max_iter = 10000)

kardesian={}
for index in pr:
	actual = followers[index]
	calc = 43.3*(pr[index] ** 0.32)
	res = actual/calc
	kardesian[index]=res
	# print (index, res)

for x in kardesian:
	if kardesian[x]<5:
		print str(x) + "-> under-rated"
	elif kardesian[x] > 20:
		print str(x) + "-> over-rated"
	else:
		print str(x) + "-> ok"
