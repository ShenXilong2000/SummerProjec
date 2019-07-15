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
        self.G1 = nx.Graph()

    def snowball(self, G, size, k):
        q = Queue()
        list_nodes = list(G.nodes())
        m = k
        dictt = set()
        while (m):
            id = random.sample(list_nodes, 1)[0]
            q.enqueue(id)
            m = m - 1
        x = q.printQueue()
        while len(self.G1.nodes()) <= size:
            if q.size() > 0:
                id = q.dequeue()
                self.G1.add_node(id)
                if id not in dictt and self.G1.number_of_nodes() < size:
                    dictt.add(id)
                    list_neighbors = list(G.neighbors(id))
                    if len(list_neighbors) > k and (self.G1.number_of_nodes() + k <= size):
                        for x in list_neighbors[:k]:
                            q.enqueue(x)
                            self.G1.add_edge(id, x)
                    elif len(list_neighbors) > k and (self.G1.number_of_nodes() + k > size):
                        tmpk = size - (self.G1.number_of_nodes() + k)
                        for x in list_neighbors[:tmpk]:
                            q.enqueue(x)
                            self.G1.add_edge(id, x)
                    elif (len(list_neighbors) <= k and len(list_neighbors) > 0) and (self.G1.number_of_nodes() + k <= size):
                        for x in list_neighbors:
                            q.enqueue(x)
                            self.G1.add_edge(id, x)
                    elif (len(list_neighbors) <= k and len(list_neighbors) > 0) and (self.G1.number_of_nodes() + k > size):
                        tmpk = size - (self.G1.number_of_nodes() + k)
                        for x in list_neighbors[:tmpk]:
                            q.enqueue(x)
                            self.G1.add_edge(id, x)
                elif id not in dictt and self.G1.number_of_nodes() >= size:
                    break
                else:
                    continue
            else:
                initial_nodes = random.sample(list(G.nodes()) and list(dictt), k)
                no_of_nodes = len(initial_nodes)
                for id in initial_nodes:
                    q.enqueue(id)
        return self.G1


