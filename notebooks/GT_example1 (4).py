#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:56:21 2022

@author: peterkroon
"""
import networkx as nx

graph = nx.Graph()
graph.add_nodes_from(range(6))
print(graph.nodes)
print(dict(graph.nodes))
graph.nodes[0]['colour'] = 'orange'
print(dict(graph.nodes))

graph.add_edges_from([(0, 2), (0, 3), (0, 4), (1, 5), (3, 5)])
graph.edges[(0, 2)]['length'] = 1.5
print(graph.edges(data=True))
print(graph[0])
graph.add_edge(5, 5, length=3)
print(graph[5])
nx.draw(graph)

