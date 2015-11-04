'''
Created on Oct 14, 2014

@author: Ofer14
'''

import os
import copy
import random

PATH = r""
MY_FILE = r"kargerMinCut.txt"
DEBUG_FILE = r"test_kargerMinCut.txt"

vertex_total = 0

_debug = False
# _debug = True


def randomly_choose_edge(adj_list):
    vertex1 = 0
    vertex2 = 0
    while vertex1 == vertex2:
        vertex1 = random.choice(list(adj_list.keys()))
        # follow vertex1 to head merger partner
        while isinstance(adj_list[vertex1], str):
            vertex1 = adj_list[vertex1]
        vertex2 = str(random.choice(adj_list[vertex1]))
        while isinstance(adj_list[vertex2], str):
            # TODO replace items in list[vertex1] to the merged vertex
            while True:
                try:
                    index_to_fix = adj_list[vertex1].index(vertex2)
                    adj_list[vertex1][index_to_fix] = int(adj_list[vertex2])
                # TODO: should I handle this for instances of faulty input?
                except ValueError:
                    break
            vertex2 = adj_list[vertex2]
    return vertex1, vertex2


def remove_index(adj_list, list_head_vertex, vertex_for_removal):
    while True:
        try:
            adj_list[list_head_vertex].remove(int(vertex_for_removal))
        # TODO: should I handle this for instances of faulty input?
        except ValueError:
            break


def merge_vertices(adj_list, merger_pair):
    if _debug:
        print("Merger pair:", merger_pair)

    for index, vertex in enumerate(sorted(merger_pair)):
        if index == 0:
            merger_vertex = vertex
        else:
            # remove merger vertices from each other's adj_list
            remove_index(adj_list, vertex, merger_vertex)
            remove_index(adj_list, merger_vertex, vertex)
            if _debug:
                print(vertex, ":", adj_list[vertex])
                print(merger_vertex, ":", adj_list[merger_vertex])
            # transfer connections to lower vertex
            while adj_list[vertex]:
                pop_item = adj_list[vertex].pop()
                adj_list[merger_vertex].append(pop_item)
            if _debug:
                print(vertex, ":", adj_list[vertex])
                print(merger_vertex, ":", adj_list[merger_vertex])
            adj_list[vertex] = merger_vertex
    if _debug:
        print("New order:")
        for index in range(1, vertex_total+1):
            print(index, ":", adj_list[str(index)])
    return merger_vertex


def find_connections(adj_list, vertex_total):
    vertex_count = vertex_total
    while vertex_count > 2:
            # randomly select 2 vertices to merge
            # do it by randomly selecting v, and randomly
            # selecting one of its adjacency buddies
            # this is similar to randomly choosing an edge
            merger_pair = randomly_choose_edge(adj_list)
            merger_vertex = merge_vertices(adj_list, merger_pair)
            vertex_count -= 1

    # find connections between two mergers and print their number
    if _debug:
        print("Merger_vertex_item:")
        print(merger_vertex, adj_list[merger_vertex])

    connections = 0
    for index, value in enumerate(adj_list[merger_vertex]):
        if _debug:
            print("index, value:", index, value)
        if str(value) is merger_vertex:
            continue
        if str(value) is not merger_vertex and isinstance(adj_list[str(value)], list):
            connections += 1
            continue
        while isinstance(adj_list[str(value)], str):
            value = int(adj_list[str(value)])
            adj_list[merger_vertex][index] = int(value)
        if str(value) != merger_vertex:
            connections += 1
        if _debug:
            print("Reestablished order:")
            print(index, ":", adj_list[merger_vertex])
    if _debug:
        print("Merger_vertex_item:")
        print(merger_vertex, adj_list[merger_vertex])
        print("connections:", connections)
    return connections


def main():
    # open file and list input into dictionary structure.
    # Note: in order to be able to update information for all edges efficiently
    # I will keep a reference from the larger vertices to their smallest numbered
    # buddy they are merged to.
    # I also need to keep count on the number of vertices so I can stop the iteration
    # once there are only 2 unmerged vertices.
    with open(file_name) as fh:
        if _debug:
            fh.readline()  # get rid of first answer line from debug file
        vertex_count = 0
        adj_list={}
        for line in fh:
            vertex_count += 1
            stripped_line = line.strip().split()
            adj_list[stripped_line[0]] = list(map(int, stripped_line[1:]))
            if _debug:
                print(stripped_line[0]+":", adj_list[stripped_line[0]])
        global vertex_total
        vertex_total = vertex_count

        # completed transfer from input file -> adj_list
        # run algorithm n^2 times:
        connections = float('inf') 
        times_to_run = vertex_total^2
        for _ in range(times_to_run):
            adj_list_copy = copy.deepcopy(adj_list)
            temp_connections = find_connections(adj_list_copy, vertex_total)
            if temp_connections < connections:
                connections = temp_connections

        print("Final result:", connections, "connections.")


if __name__ == '__main__':
    """
    The file contains the adjacency list representation of a simple
    undirected graph. There are 200 vertices labeled 1 to 200.
    The first column in the file represents the vertex label,
    and the particular row (other entries except the first column)
    tells all the vertices that the vertex is adjacent to.
    So for example, the 6th row looks like :
    "6 155 56 52 120 ......". 
    This just means that the vertex with label 6 is adjacent
    to (i.e., shares an edge with) the vertices with
    labels 155,56,52,120,......,etc

    Your task is to code up and run the randomized contraction
    algorithm for the min cut problem and use it on the above
    graph to compute the min cut (i.e., the minimum-possible
    number of crossing edges). (HINT: Note that you'll have
    to figure out an implementation of edge contractions.
    Initially, you might want to do this naively, creating
    a new graph from the old every time there's an edge
    contraction. But you should also think about more
    efficient implementations.) 
    (WARNING: As per the video lectures, please make sure
    to run the algorithm many times with different random seeds,
    and remember the smallest cut that you ever find.)
    """

    file_name = os.path.join(PATH,
                             (MY_FILE, DEBUG_FILE)[_debug])
    main()
