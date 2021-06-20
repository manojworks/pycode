import math

# A priority queue is an abstract data type similar to a regular queue or stack data structure in which each element
# additionally has a "priority" associated with it. In a priority queue, an element with high priority is served before
# an element with low priority. If two elements have the same priority, they are served according to the order in which
# they were enqueued
# is_empty: check whether the queue has no elements.
# insert_with_priority: add an element to the queue with an associated priority.
# peek_at_lowest_priority_element: return the element (do not remove) with the lowest priority
# peek_at_highest_priority_element: return the element (do not remove) with the highest priority
# delete_with_priority: Delete the element with priority p and return it
# merge: merging two or more queues into one


class Node:
    __slots__ = '_priority', '_value'

    def __init__(self, p, v):
        self._priority = p
        self._value = v

    def __lt__(self, other):
        return self._priority < other.get_priority()

    def __str__(self):
        return f"[p: {self._priority} v: {self._value}]"

    def get_value(self):
        return self._value

    def get_priority(self):
        return self._priority


class PriorityQueue:
    def __init__(self):
        self._pq_list = []

    def delete_with_priority(self, p) -> Node:
        node = None
        for ind in range(len(self._pq_list)):
            if self._pq_list[ind].get_priority() == p:
                node = self._pq_list[ind]
                del(self._pq_list[ind])
                return node
        return node

    def insert_with_priority(self, p, v):
        newest = Node(p, v)
        if self.is_empty():
            self._pq_list.append(newest)
            return

        walk_ind = len(self._pq_list) - 1
        while walk_ind >= 0 and newest < self._pq_list[walk_ind]:
            walk_ind -= 1
        if walk_ind == -1:
            self._pq_list.insert(0, newest)
        else:
            self._pq_list.insert(walk_ind + 1, newest)

    def peek_at_lowest_priority_element(self):
        return self._pq_list[0]

    def peek_at_highest_priority_element(self):
        return self._pq_list[-1]

    def __str__(self):
        s = ",".join([str(el) for el in self._pq_list])
        return s

    def length(self):
        return len(self._pq_list)

    def is_empty(self):
        return len(self._pq_list) == 0

    def max_priority(self):
        return self._pq_list[len(self._pq_list)-1].get_priority()

    def min_priority(self):
        return self._pq_list[0].get_priority()

    def extract_min_priority_node(self) -> Node:
        min_priority = self.min_priority()
        return self.delete_with_priority(min_priority)

    def __iter__(self):
        for el in self._pq_list:
            yield el

    def merge_q(self, other):
        for el in other:
            self.insert_with_priority(el.get_priority(), el.get_value())


class GraphDS:

    def __init__(self):
        self._graph = {}
        self._vertices_no = 0

    # Add a vertex to the dictionary
    def add_vertex(self, v):
        if v in self._graph:
            print("Vertex ", v, " already exists.")
        else:
            self._vertices_no = self._vertices_no + 1
            self._graph[v] = []

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e):
        # Check if vertex v1 is a valid vertex
        if v1 not in self._graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self._graph:
            print("Vertex ", v2, " does not exist.")
        else:
            # Since this code is not restricted to a directed or
            # an undirected graph, an edge between v1 v2 does not
            # imply that an edge exists between v2 and v1
            temp = [v2, e]
            self._graph[v1].append(temp)

    def num_vertices(self):
        return self._vertices_no

    # neighbors of vertex v
    def neighbors_of_vertex(self, v):
        return [el[0] for el in self._graph[v]]

    # get weight u -> v
    def get_weight(self, u, v):
        for node in self._graph[u]:
            if node[0] == v:
                return node[1]
        return None

    # Print the graph
    def __str__(self):
        for vertex in self._graph:
            for edges in self._graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


# driver code
def graph_driver():

    gds = GraphDS()

    gds.add_vertex(1)
    gds.add_vertex(2)
    gds.add_vertex(3)
    gds.add_vertex(4)
    gds.add_vertex(5)
    # Add the edges between the vertices by specifying
    # the from and to vertex along with the edge weights.
    gds.add_edge(1, 2, 2)
    gds.add_edge(2, 5, 5)
    gds.add_edge(2, 3, 4)
    gds.add_edge(1, 4, 1)
    gds.add_edge(4, 3, 3)
    gds.add_edge(3, 5, 1)

    return gds

# You are given a weighted undirected graph. The vertices are enumerated from 1 to n. Your task is to find the shortest
# path between the vertex 1 and the vertex n.


def dijkstra():
    source = 1

    g = graph_driver()

    # Initialize distances of all vertices as infinite.
    dist = [math.inf] * (g.num_vertices() + 1)
    # Create an empty priority_queue pq.  Every item of pq is a pair (weight, vertex). Weight (or distance) is
    # used as first item of pair is by default used to compare two pairs
    pq = PriorityQueue()
    # Insert source vertex into pq
    pq.insert_with_priority(0, source)
    #  and make its distance as 0.
    dist[source] = 0
    # While either pq doesn't become empty
    while not pq.is_empty():
        # Extract minimum distance vertex from pq.
        min_priority_node = pq.extract_min_priority_node()
        # Let the extracted vertex be u.
        u = min_priority_node.get_value()
        # Loop through all adjacent vertices of u
        for v in g.neighbors_of_vertex(u):
            # If there is a shorter path to v through u.
            if dist[v] > dist[u] + g.get_weight(u, v):
                dist[v] = dist[u] + g.get_weight(u, v)
                pq.insert_with_priority(dist[v], v)

    print("Shortest distances from ", str(source))
    print("Destination\tDistance")
    for ind in range(1, len(dist)):
        if ind != source:
            print(ind, "\t\t\t", dist[ind])


dijkstra()


def build_pq():
    pq = PriorityQueue()
    pq.insert_with_priority(4, 2)
    pq.insert_with_priority(5, 3)
    pq.insert_with_priority(11, 4)
    pq.insert_with_priority(8, 23)
    pq.insert_with_priority(3, 30)
    pq.insert_with_priority(1, 13)
    pq.insert_with_priority(3, 20)

    print(pq)

    pq1 = PriorityQueue()
    pq1.insert_with_priority(4, 2)
    pq1.insert_with_priority(5, 3)
    pq1.insert_with_priority(11, 4)
    pq1.insert_with_priority(8, 23)
    pq1.insert_with_priority(3, 30)
    pq1.insert_with_priority(1, 13)
    pq1.insert_with_priority(3, 20)

    pq.merge_q(pq1)

    print(pq)


build_pq()