'''
Created on Oct 14, 2014

@author: Ofer14
'''

import os
# import logging

# sys.setrecursionlimit(100000)

PATH = r"."
MY_FILE = r"SCC.txt"
DEBUG_FILE = r"test_SCC.txt"

_debug = False
# _debug = True


class Node(object):
    # TODO: reorganize so that input can be either arrays or single vertex
    # values.
    def __init__(self, node_name, incoming_edges=[], target_nodes=[]):
        # self._incoming_edges: sources that use node as target
        # TODO: add incoming_edges + target_nodes
        # -- isinstance(int) and isinstance(list)
        if not node_name:
            msg = "ValueError: node_name input argument = {}".format(node_name)
            raise ValueError(msg)
        self._name = node_name
        self._incoming_edges = incoming_edges
        self._targets = target_nodes

    def add_targets(self, target_nodes):
        if isinstance(target_nodes, int):
            self._targets.append(target_nodes)
        elif isinstance(target_nodes, list):
            self._targets.extend(target_nodes)
        else:
            msg = ("unimplemented for target_nodes of type: " +
                   type(target_nodes))
            raise ValueError(msg)

    def add_incoming_edges(self, incoming_edges):
        if isinstance(incoming_edges, int):
            self._incoming_edges.append(incoming_edges)
        elif isinstance(incoming_edges, list):
            self._targets.extend(incoming_edges)
        else:
            msg = ("unimplemented for incoming_edges of type: " +
                   type(incoming_edges))
            raise ValueError(msg)

    def get_targets(self):
        # return a tuple with Node._name, Node._targets
        return self._name, self._targets

    def get_incoming_edges(self):
        # return a tuple with Node._name, Node._incoming_edges
        return self._name, self._incoming_edges

    def __str__(self):
        print(self._name)


class Graph:
    SOURCE = 0       # edge source index
    TARGET = 1       # edge target index
    INF = float('inf')

    def __init__(self):
        self._number_of_edges = 0
        self._number_of_nodes = 0
        self._nodes = {}

    def increase_edge_counter(self):
        self._number_of_edges += 1

    def increase_vertex_counter(self):
        self._number_of_nodes += 1

    def populate_directed_pair(self, directed_edge):
        source_node, target_node = directed_edge
        if _debug:
            print(source_node, target_node)
#             logging.debug('source_node: {},
#                           target_node: {}'.format(source_node, target_node))

        self.increase_edge_counter()

        # hash nodes in graph._nodes:
        if source_node not in self._nodes:
            self._nodes[source_node] = Node(source_node, [], [])
            self.increase_vertex_counter()
        self._nodes[source_node].add_targets([target_node])

        if target_node not in self._nodes:
            self._nodes[target_node] = Node(target_node, [], [])
            self.increase_vertex_counter()
        self._nodes[target_node].add_incoming_edges(source_node)

    def __rstr__(self):
        """return a representation of the reversed graph"""
        string = ''
        for key, node in self._nodes.items():
            string += (repr(key) + " : " +
                       repr(node.get_incoming_edges()) + "\n")
        return string

    def __str__(self):
        string = ''
        for key, node in self._nodes.items():
            string += repr(key) + " : " + repr(node.get_targets()) + "\n"
        return string

    def dfs(self, direction_func, dfs_data):
        '''A vertex stack is updated with DFS vertices.
           Once a vertex has nowhere to go, it is marked as complete
           (finishing_times[last_node_index] = t). '''

        node_stack = [dfs_data.get_current_node_index()]
        explored_nodes = dfs_data.get_explored_nodes()
        while True:
            last_node_index = node_stack[-1]
            if last_node_index in explored_nodes:
                # backtrack to previous vertex index

                if not dfs_data.get_finishing_time(last_node_index):
                    dfs_data.increment_t()
                    dfs_data.set_finishing_time(last_node_index,
                                                dfs_data.get_t_data())

                node_stack.pop()
                if not node_stack:
                    return    # leave dfs()
                else:
                    continue  # back to while loop

            # last_node_index not in explored nodes
            dfs_data.set_was_explored(last_node_index)
            explored_nodes = dfs_data.get_explored_nodes()
            dfs_data.set_leader(last_node_index, dfs_data.get_s_data())

            if _debug:
                print("update was_explored, leader")
                print('node {}, is it in explored_nodes? {}'.format(last_node_index, last_node_index in explored_nodes))
                print('s_value: {}\nnode {}, leader: {}'.format(dfs_data.get_s_data(), last_node_index, dfs_data.get_leader(last_node_index)))

            # vertex_checker is later used to test if current node had unexplored connections (vertex_checker will change value)
            vertex_checker = last_node_index

            # explore current vertex for outgoing edges
            # TODO: filter get_next to only get unexplored vertices
            # TODO: should I change outgoing_edges to a set/generator ?
            #   Ok. maybe not. outside dfs, other algorithms might need duplicate edges.
            outgoing_edges = direction_func.get_next(self._nodes[last_node_index])[1]   #get_next returns [node_index, list_of_connections]
            outgoing_edges.sort(reverse=True)   # reverse keeps old order of things

            for j_index in outgoing_edges:
                if j_index not in explored_nodes:
                    # append j_index to stack and deep search it 
                    node_stack.append(j_index)
                    vertex_checker = j_index
                    continue
            # check for unexplored vertices
            if last_node_index != vertex_checker:
                continue  # go back to beginning of while loop

            # vertex exhausted its edges, mark it as complete
            dfs_data.increment_t()
            dfs_data.set_finishing_time(last_node_index, dfs_data.get_t_data())

            node_stack.pop()

            if _debug:
                print("vertex_index: {}, t {}".format(last_node_index, dfs_data.get_t_data()))

            if not node_stack:
                    break    # leave dfs()

    # TODO: how do I impose StandardDFSDirection as the default for firection_func?
    def dfs_loop(self, order_func, direction_func, dfs_data=None):

        # TODO: is there a way to do this in a prettier way?
        if not dfs_data:
            dfs_data = DFSData(self)
            order = order_func.get_order(dfs_data) 
        else:
            order = order_func.get_order(dfs_data) 
            dfs_data.scc_reset(self)

        #TODO: change the order to a generator function (better use of memory)
        print("DFS Loop order received...")
#         logging.info("DFS Loop order received...")
        print("Length:", len(order))
        if _debug:
            print(type(order_func))
            print(order)

        for order_index, current_node_index in enumerate(order):
            # Follow progress prints
            if not (order_index % 50000):
                print("order_index: {} ...".format(order_index)) 
            dfs_data.set_s(current_node_index)     # s = current_node_index
            dfs_data.set_current_node_index(current_node_index)

            self.dfs(direction_func, dfs_data)

        return dfs_data

    def scc(self):
        if _debug:
            print("Reveresed graph:")
            print(self.__rstr__())

        # DFS-Loop(Graph<reversed>) - 1st iteration:
        # Run on reversed graph -> find finishing times.  
        scc_data = SCCData(self)     
        self.dfs_loop(StandardDFSChooser(), ReversedDFSDirection(), scc_data)

        print("SCC First DFS Loop complete...")
        if _debug:
            print("SCC dfs_data:")
            print(scc_data.get_finishing_data())

        # DFS-Loop(graph G) - 2nd iteration:
        # Run order based on 1st iteration finishing times ->
        # find SCCs
        # TODO: test new_dfs_data and if it works, rename it to dfs_data (no need to keep the old data)
        self.dfs_loop(ReversedFTimeDFSChooser(), StandardDFSDirection(), scc_data)

        print("SCC Second DFS Loop complete...")

        scc_data.set_scc_db()       # inhabit scc_data._scc_db<leader_key: [leader[, follwoers]]> 
        scc_sizes = scc_data.get_scc_sizes()

        if _debug:
            print(scc_sizes)

        return scc_data

    def get_directed_edge_input(self, file_input):
        """  open file, populate self<Graph> with nodes (adj_list)  """ 
        with open(file_name) as fh:
            if _debug:
                fh.readline()  # get rid of first answer line from debug file
            if _debug:
                print("file input:")
            for line in fh:
                edge_pair = list(map(int, line.strip().split()))  # edge pair integers
                self.populate_directed_pair(edge_pair)

            print("Graph populated...")
#             logging.info("Graph populated...")
            if _debug:
                print("Graph:")
                print(self)
#                 logging.info("Graph:\n{}".format(self))


class DFSChooser:
    pass


class StandardDFSChooser(DFSChooser):
    name = "standard"

    def get_order(self, dfs_data):
        all_the_nodes = list(dfs_data.get_nodes())
        all_the_nodes.sort(reverse=True)
        order = [f_time_key for f_time_key in all_the_nodes]
        return order


class ReversedFTimeDFSChooser(DFSChooser):
    name = "special_scc"

    def get_order(self, dfs_data):
        # returns the order based on finishing times
        order = [f_time_key for (finishing_time, f_time_key) in sorted(dfs_data.get_finishing_data(), reverse=True)]
        return order


class DFSDirection:
    pass


class StandardDFSDirection(DFSDirection):
    name = "standard_digraph_order"

    def get_next(self, node):
        """  self<Node> : return the node's target list  """
        return node.get_targets()


class ReversedDFSDirection(DFSDirection):
    name = "reverse_digraph_order"

    def get_next(self, node):
        """  self<Node> : return the node's input_edges list  """
        return node.get_incoming_edges()


class DFSData:
    def __init__(self, graph):
        self._current_node_index = None
        self._t = 0
        self._s = None
        self._explored_nodes = set()
        self._exploration_db = {}       # node_index: ExplorationData
        self._all_the_nodes = graph._nodes.keys()

    def get_nodes(self):
        return self._all_the_nodes

    def get_current_node_index(self):
        return self._current_node_index

    def set_current_node_index(self, current_node_index):
        self._current_node_index = current_node_index

    def get_s_data(self):
        return self._s

    def set_s_data(self, new_s):
        self._s = new_s

    def get_t_data(self):
        return self._t

    def set_t_data(self, new_t):
        self._t = new_t

    def set_was_explored(self, node_indices):
        if isinstance(node_indices, int):
            self._explored_nodes.add(node_indices)
        else:
            msg = "not implemented for node_indices type: " + type(node_indices)
            raise ValueError(msg)

    def get_leader(self, node_index):
        return self._exploration_db[node_index].get_leader()  # node_index: ExplorationData

    def set_leader(self, node_index, leader):
        if node_index not in self._exploration_db:      # node_index: ExplorationData
            self._exploration_db[node_index] = ExplorationData(node_index)
        self._exploration_db[node_index].set_leader(leader)

    def get_explored_nodes(self):
        return self._explored_nodes

    def get_finishing_time(self, last_node_index):
        if last_node_index in self._exploration_db:     # last_node_index: ExplorationData
            return self._exploration_db[last_node_index].get_finishing_time()
        else:
            return None

    def set_finishing_time(self, node_index, finishing_time):
        if node_index not in self._exploration_db:      # node_index: ExplorationData
            self._exploration_db[node_index] = ExplorationData(node_index)
        self._exploration_db[node_index].set_finishing_time(finishing_time)

    def increment_t(self):
        self._t += 1

    def set_s(self, current_node_index):
        self._s = current_node_index

    def get_finishing_data(self):
        """  return (finishing_time, f_time_key) pairs  """
        ret = []
        for f_time_key, key_data in self._exploration_db.items():
            finishing_time = key_data.get_finishing_time()
            ret.append((finishing_time, f_time_key))
        return ret


class SCCData(DFSData):
    def __init__(self, graph):
        self._scc_db = {}
        super().__init__(graph)

    def scc_reset(self, graph):
        self.__init__(graph)

    def get_scc_db_items(self):
        return self._scc_db.items()

    def set_scc_db(self):
        for node_index in self.get_nodes():
            leader = self.get_leader(node_index)
            if leader not in self._scc_db:
                self._scc_db[leader] = [leader]
            else:
                self._scc_db[leader].append(node_index)

    def get_scc_sizes(self):
        if "_scc_sizes" not in dir(self):
            self.set_scc_sizes()
        return self._scc_sizes

    def set_scc_sizes(self):
        self._scc_sizes = []
        for leader_key, leader_followers_data in self.get_scc_db_items():
            self._scc_sizes.append(len(leader_followers_data))
        self._scc_sizes.sort(reverse=True)


class ExplorationData:
    def __init__(self, owner_index):
        self._owner_index = owner_index
        #self._was_explored = False
        self._finishing_time = None
        self._leader = None

#    def set_was_explored(self):
#        self._was_explored = True

#    def get_was_explored(self):
#        return self._was_explored

    def set_finishing_time(self, finishing_time):
        self._finishing_time = finishing_time

    def get_finishing_time(self):
        return self._finishing_time

    def set_leader(self, leader):
        self._leader = leader

    def get_leader(self):
        return self._leader


def main(argv):
    file_input = argv   # TODO: arrange more execution through argparse
    if _debug:
        print(file_input)
    graph_g = Graph()
    graph_g.get_directed_edge_input(file_input)

    # run SCC method on graph_g<Graph> instance object
    scc_data = graph_g.scc()

    printout = ""
    scc_sizes = scc_data.get_scc_sizes()
    for index in range(5):
        try:
            add_str = str(scc_sizes[index]) + ","
        except IndexError:
            add_str = "0,"
        printout += add_str

    printout = printout[:-1]    # lose the last superfluous comma

    print("Final result:\n{}".format(printout))


if __name__ == '__main__':
    """
    The file contains the edges of a DIRECTED graph.
    Vertices are labeled as positive integers from 1 to 875714.
    Every row indicates an edge, the vertex label in first
    column is the tail and the vertex label in second column
    is the head (recall the graph is directed, and the
    edges are directed from the first column vertex to
    the second column vertex). So for example,
    the 11th row looks liks : "2 47646".
    This just means that the vertex with label 2 has an outgoing
    edge to the vertex with label 47646

    Code up the algorithm from the video lectures
    for computing strongly connected components (SCCs),
    and to run this algorithm on the given graph. 

    Output Format: You should output the sizes of the 5 largest SCCs
    in the given graph, in decreasing order of sizes, separated
    by commas (avoid any spaces). So if your algorithm computes
    the sizes of the five largest SCCs to be 500, 400, 300, 200
    and 100, then your answer should be "500,400,300,200,100".
    If your algorithm finds less than 5 SCCs, then write 0 for
    the remaining terms. Thus, if your algorithm computes only
    3 SCCs whose sizes are 400, 300, and 100, then your answer
    should be "400,300,100,0,0".
    """

    file_name = os.path.join(PATH,
                             (MY_FILE, DEBUG_FILE)[_debug])
    #logging(filename='log_file.log', filemode='w', level=logging.DEBUG)
    main(file_name)
#     import cProfile
#     cProfile.run('main(file_name)')
    
#     logging.shutdown()
