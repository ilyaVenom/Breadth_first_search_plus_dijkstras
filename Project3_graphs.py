# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:15:06 2022
@author: segal
"""
# project 3 graphs # add comments !
priorityQ = 0

import numpy as np # for use of inf
posInf = np.inf
# a global to store how large !
How_large_min_heap_is = 0
# 3 funtions:    
# 1st implement insert:
    # sudo code of how it will look:
    # like max-heap-insert(A, key)
#A.heap-size = A.heap + 1
#A[A.heap-size] = -inf
#heap-increase-KEY(A, A.heap-size, key)
   # A is list and key the value being inserted in 
def insert( A, key ):
    A.heap_size = A.heap_size + 1
    posInf = np.inf
    A[A.heap_size] = posInf 
    
    # fix!
    
    heap_decrease_key(A, A.heap_size, key)   
#2nd function
# Extract Min
# like max -extract-Max:
def extractMin(A): # add to Dij
    global priorityQ 
    
    if priorityQ < 1:
        print("\nHeap underflow\n")
    min = A[0]
    A[0] = A[ priorityQ - 1 ] # so it starts at 0  
    priorityQ = priorityQ - 1
    minHeapify(A,0)
    return min
#3rd
# decrease key:   
# like book sudo code:
def heap_decrease_key( A, i, key ):
    dictionary_distances[A[i]] = key
    #if key < A[i]:
        #print("\nnew key is smaller than current key\n")    
    #remove A[i] = key 
    while i > 0 and dictionary_distances[A[parent(i)]] > dictionary_distances[A[1]]:
        A[i], A[parent(i)] = A[parent(i)] , A[i]
        i = parent(i)
 # comment how each works 4 -lines on how:   
def parent (i):
    return (i//2)

def minHeapify (A,i):
    global priorityQ
    
    l = lefty (i)
    r = righty (i)
    if l <= priorityQ and dictionary_distances[A[l]] < dictionary_distances[A[i]]: # swapped signs from like max-heapify
        smallest = l
    else:
        smallest = i
    if r <= priorityQ and dictionary_distances[A[r]] < dictionary_distances[A[l]]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
     
        minHeapify(A,smallest)
     
def lefty(i): # test with dijkstra or make an array or list and put nums in and min by hand.
    return (i*2)

def righty(i):
    return ((i*2) + 1)
# test 
# make a class and
# make graphs with dictionaries 
# 1st: BFS:
dictionary_adj_list = { "arad" : ["zerind", "timisoara", "sibiu"],
                       "bucharest": ["urziceni", "giurgiu", "pitesti", "fagaras"],
                       "craiova" : ["dobreta", "pitesti", "rimnicuVilcea"],
                       "dobreta" : ["mehadia", "craiova"],
                       "eforie" : ["hirsova"],
                       "fagaras" : ["bucharest", "sibiu"],
                       "giurgiu" : ["bucharest"],
                       "hirsova" : ["urziceni" , "eforie"],
                       "iasi" : ["neamt", "vaslui"],
                       "lugoj" : ["timisoara", "mehadia"],
                       "mehadia" : ["lugoj", "dobreta"],
                        "neamt" : ["iasi"],
                       "oradea" : ["zerind", "sibiu"],
                       "pitesti" : ["rimnicuVilcea", "bucharest", "craiova"],
                       
                       "rimnicuVilcea" : ["sibiu", "pitesti", "craiova"],
                       
                       "urziceni" : ["vaslui" , "bucharest" , "hirsova"],
                       
                       "zerind" : ["oradea", "arad"],
                       
                       "timisoara" : [ "arad", "lugoj"],
                       
                      
                       "sibiu" : ["fagaras", "rimnicuVilcea", "oradea", "arad"],
                       
                       "vaslui" : ["iasi", "urziceni"]
}
# next the dictionary with distances: no edge weights yet
dictionary_distances = { "arad": 0,
                        "bucharest": posInf,
                        "craiova" : posInf,
                        "dobreta" : posInf,
                        "eforie" : posInf,
                        "fagaras" : posInf,
                        "giurgiu" : posInf,
                        "hirsova" : posInf,
                        "iasi" : posInf,
                        "lugoj" : posInf,
                        "mehadia" : posInf,
                    
                        "neamt" : posInf,
                        "oradea" : posInf,
                        "pitesti" : posInf,
                        "rimnicuVilcea" : posInf,
                        "urziceni" : posInf,
                        "zerind" : posInf,
                        "timisoara" : posInf,
                        "sibiu" : posInf,
                        "vaslui" : posInf                                                                
}
# 1st none, then update them:
dict_predecessor = {"arad": 0,
                  "bucharest": None,
                   "craiova" : None,
                   "dobreta" : None,
                   "eforie" : None,
                   "fagaras" : None,
                   "giurgiu" : None,
                   "hirsova" : None,
                   "iasi" : None,
                   "lugoj" : None,
                   "mehadia" : None,
                 
                   "neamt" : None,
                   "oradea" : None,
                   "pitesti" : None,
                   "rimnicuVilcea" : None,
                   "urziceni" : None,
                   "zerind" : None,
                   "timisoara" : None,
                   "sibiu" : None,
                   "vaslui" : None          
}
    # white - not discovered or not see it yet , gray - discovered, black - visited
dict_color = {"arad": "gray", # set gray at 1st
                  "bucharest": "white",
                   "craiova" : "white",
                   "dobreta" : "white",
                   "eforie" : "white",
                   "fagaras" : "white",
                   "giurgiu" : "white",
                   "hirsova" : "white",
                   "iasi" : "white",
                   "lugoj" : "white",
                   "mehadia" : "white",
                 
                   "neamt" : "white",
                   "oradea" : "white",
                   "pitesti" : "white",
                   "rimnicuVilcea" : "white",
                   "urziceni" : "white",
                   "zerind" : "white",
                   "timisoara" : "white",
                   "sibiu" : "white",
                   "vaslui" : "white"  
}
# test 0
'''
for i in dictionary_adj_list["arad"]:
    print(i)
'''
# write a que !
# finish bfs !
# to add:
# que.append(s)
# to remove:
# que.
# and try writing the BFS:
def BFS( G, s ):    
    Q = []    
    Q.append( s )    
    while (len(Q) != 0):
        u = Q.pop(0) 
        for v in G[u]:
            if dict_color[v] == "white":
                dict_color[v] = "gray"
                dictionary_distances[v] = dictionary_distances[u] + 1
                dict_predecessor[v] = u
                Q.append(v)
        dict_color[u] = "black"
# and 2nd the print of the bfs:
def print_path ( G , s , v ):    
    if v == s:
        print(s)
    elif (dict_predecessor[v] == None):
        print("no path from", s, "to", v, "exists")
    else:
        print_path( G , s , dict_predecessor[v]) # and p is for the pi - or predicessor
        print(v)
# test 2:  
# a to c
print("the shortest path from arad to craiova is: \n")
BFS (dictionary_adj_list, "arad")     
print_path( dictionary_adj_list, "arad", "craiova")
# test a to B:
print("\n\n")
print("the shortest path from arad to bucharest is: \n")
print_path( dictionary_adj_list, "arad", "bucharest")
print("\n")
#test 3 a to s
print("the shortest path from arad to sibui is: \n")
print_path( dictionary_adj_list, "arad", "sibiu")
print("\n\n")
print("the display of graph in pathway form is: \n")
print(dictionary_adj_list) # to display the graph and I want to add -> 
                           # (->) arrows to path
# dijkstra next:
    
print("\nnext is seeing dijkstras\n\n")

# maybe switch it:
    
graph = {"arad": {"zerind": 75, "timisoara": 118, "sibiu": 151}, # a to "arad"
         "bucharest": {"urziceni": 85, "giurgiu": 90, "pitesti": 101, "fagaras": 211}, 
         "craiova": {"dobreta": 120, "pitesti": 138, "rimnicuVilcea": 146}, 
         "dobreta": {"mehadia": 75, "craiova": 120}, 
         "eforie": {"hirsova": 86},
         "fagaras": {"bucharest": 211, "sibiu": 99},
         "giurgiu": {"bucharest":90},
         "hirsova": {'urziceni':98, "eforie": 86},
         "iasi": {"neamt": 87, "vaslui": 92},
         "lugoj": {"timisoara": 111, "mehadia": 70},
         "mehadia": {"lugoj": 70, "dobreta": 75},
         "neamt": {"iasi": 87},
         "oradea": {"zerind": 71, "sibiu": 151},
         "pitesti": {"rimnicuVilcea": 97, "bucharest": 101, "craiova": 138},
         "rimnicuVilcea": {"sibiu": 80, "pitesti": 97, "craiova": 146},
         "urziceni": {"vaslui": 142, "bucharest": 85, "hirsova": 98},
         "zerind": {"oradea": 71, "arad": 75},
         "timisoara": {"arad": 118, "lugoj": 111},
         "sibiu": {"fagaras": 99, "rimnicuVilcea": 80, "oradea": 151, "arad": 140},
         "vaslui":{"iasi": 92, "urziceni": 142}}

def dijkstras( G , s): # stick with this one and the list opt. ? 
    global priorityQ 
    
    initialize_single_source( G ,s) # G - graph, s - source
    S = [] # segt that is used, that tracks, what is known
    # the source should start at 0
    #s = 0
    dictionary_distances[s] = 0 # making a value = 0 
    
    Q= []
    Q.append("arad")
    priorityQ += 1
    
    for i in G.keys():
        if i != "arad":
            Q.append(i)
            priorityQ += 1
        
    print(Q)
    #print("\n", priorityQ,"\n") num of elements
    # move extraction 
    while priorityQ > 0: # maybe ?
        u = extractMin(Q) # different than before
        
        s = S.append(u) # may not be needed
        for x in G[u]: # inserting into priority que

            
            relax ( u , x, Q ) # u and v are vertices

def relax(u, x, Q):
    global graph
  
    
    if dictionary_distances[x] > dictionary_distances[u] + graph[u][x]: # how to get
        
        # the weight in?      
        
        if x not in Q:  
            return 0
        
        index = Q.index(x) 
        
        heap_decrease_key(Q, index, (dictionary_distances[u] + graph[u][x]))                                                
        #dictionary_distances[v] = dictionary_distances[u] + graph[u][v] # decreaseKey
        
        dict_predecessor[x] = u # different predissor !
        
def initialize_single_source (graph, s):

    for key in graph:
        dictionary_distances[key] = posInf
        dict_predecessor[key] = None
    dictionary_distances[s] = 0
    
# then call dijkstras 
dijkstras(dictionary_adj_list, "arad")

print("\n")
print("Dijkstras from arad to bucharest comes out as: \n")
print_path(dictionary_adj_list,"arad", "bucharest")
# idea print(dictionary_adj_list, "arad", "bucharest")
# maybe get to:
    
#print_path(dijkstras(graph, s))

#
# try primas: ? needs completing
'''
def mst_prim (G, w, r):
    
    for u in G[v]:
        key[u] = posInf
        dict_predecessor = 
        '''