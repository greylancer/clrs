def transpose(G):
    if len(G) == 0:
        return None

    n = len(G)
    T = [[0 for x in range(n)] for x in range(n)]
    for i, v in enumerate(G):
        for j, vv in enumerate(v):
            if vv > 0:
                T[j][i] = vv

    return T

class ListNode:
    def __init__(self, vertex, val):
        self.vertex = vertex
        self.val = val
        self.next = None

def transpose2(G):
    if len(G) == 0:
        return None

    n = len(G)
    T = n * [None]
    cur_node = n * [None]
    for i, v in enumerate(G):
        while v:
            if not cur_node[v.vertex]:
                T[v.vertex] = ListNode(i, v.val)
                cur_node[v.vertex] = T[v.vertex]
            else:
                cur_node[v.vertex].next = ListNode(i, v.val)
            v = v.next

    return T

