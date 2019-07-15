import random
import networkx as nx


class Queue():
    # Constructor creates a list
    def __init__(self):
        self.queue = list()

    # Adding elements to queue
    def enqueue(self, data):
        # Checking to avoid duplicate entry (not mandatory)
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    # Removing the last element from the queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            # plt.show()
            exit()

    # Getting the size of the queue
    def size(self):
        return len(self.queue)

    # printing the elements of the queue
    def printQueue(self):
        y = self.queue
        x = len(self.queue)
        return self.queue


class Snowball():
    def __init__(self):
        self.G1 = []

    def snowball(self, G, inital_set, size):
        k = len(inital_set)
        list_nodes = list(G.nodes())
        q = Queue()
        dictt = set()

        for nodes in inital_set:
            q.enqueue(nodes)
        a = inital_set
        while len(self.G1) < size:
            if q.size() > 0:
                id = q.dequeue()
                self.G1.append(id)
                if id not in dictt and len(self.G1) < size:
                    dictt.add(id)
                    list_neighbors = list(G.neighbors(id))
                    if len(list_neighbors) > k and (len(self.G1) + k <= size):
                        for x in list_neighbors[:k]:
                            q.enqueue(x)
                    elif len(list_neighbors) > k and (len(self.G1) + k > size):
                        tmpk = size - (len(self.G1) + k)
                        for x in list_neighbors[:tmpk]:
                            q.enqueue(x)
                    elif (len(list_neighbors) <= k and len(list_neighbors) > 0) and (len(self.G1) + k <= size):
                        for x in list_neighbors:
                            q.enqueue(x)
                    elif (len(list_neighbors) <= k and len(list_neighbors) > 0) and (len(self.G1) + k > size):
                        tmpk = size - (len(self.G1) + k)
                        for x in list_neighbors[:tmpk]:
                            q.enqueue(x)
                elif id not in dictt and len(self.G1) >= size:
                    break
                else:
                    continue
            else:
                initial_nodes = random.sample(list(G.nodes()) and list(dictt), k)
                no_of_nodes = len(initial_nodes)
                for id in initial_nodes:
                    q.enqueue(id)
        return self.G1


class InducedGraph():

    def induced_graph(self, G, nodes):
        g = G.subgraph(nodes)
        return g



