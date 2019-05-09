"""
Simulation of table unition.
Input: n - number of tables, m - number of queries.
r - initial sizes of the tables.
queries - queries in the type of [destination_i, source_i]
"""

class JointSets(object):
    def __init__(self, n, m, r, queries):
        self.n = n
        self.m = m
        self.r = r
        self.parent = [None] + [i+1 for i in range(n)]
        self.rank = [None] + [0]*n
        self.queries = queries
        self.max_size = max(r[1:])

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        global max_size

        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id: return
        if self.rank[i_id] >= self.rank[j_id]:
            self.parent[j_id] = i_id
            self.r[i_id] += self.r[j_id]
            self.r[j_id] = 0
            if r[i_id] > self.max_size:
                self.max_size = self.r[i_id]

            if self.rank[i_id] == self.rank[j_id]:
                self.rank[i_id] += 1
        else:
            self.parent[i_id] = j_id
            r[j_id] += self.r[i_id]
            r[i_id] = 0
            if r[j_id] > self.max_size:
                self.max_size = r[j_id]




if __name__ == "__main__":
    # Number of tables
    n = 6
    # Number of queries
    m = 4
    # Sizes of the tables
    r = [None] + [10, 0, 5, 0, 3, 3]
    # Queries in form of destination_i, source_i
    queries = [[6, 6], [6, 5], [5, 4], [4, 3]]

    dj = JointSets(n, m, r, queries)
    for q in queries:
        dest_i = q[0]
        source_i = q[1]
        dj.union(dest_i, source_i)
        print(dj.max_size)
