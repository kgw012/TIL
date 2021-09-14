# 양과 늑대 이진트리. 18개중 13개정답

class Node:
    def __init__(self, num, wolf):
        self.num = num
        self.is_wolf = bool(wolf)
        self.is_visit = False
        self.wolves = 0
        self.p_node = None
        self.c_nodes = list()


def solution(info, edges):
    nodes = []
    for num, wolf in enumerate(info):
        nodes.append(Node(num, wolf))

    for edge in edges:
        p_node_num, c_node_num = edge
        p_node = nodes[p_node_num]
        c_node = nodes[c_node_num]

        p_node.c_nodes.append(c_node)
        c_node.p_node = p_node

    flag = True
    sheep_cnt = 0
    wolf_cnt = 0

    while flag:
        flag = False
        for node in nodes:
            if node.is_visit or node.is_wolf:
                continue

            cnt = 0
            node_num = node.num
            while True:
                p_node = nodes[node_num].p_node
                if p_node is None or p_node.is_visit or not p_node.is_wolf:
                    break

                cnt += 1
                node_num = p_node.num

            node.wolves = cnt
            if node.wolves == 0:
                node.wolves = -1
            if (not node.is_wolf) and (sheep_cnt - wolf_cnt) > node.wolves:
                node.is_visit = True
                sheep_cnt += 1
                flag = True

                node_num = node.num
                while True:
                    p_node = nodes[node_num].p_node
                    if p_node is None or p_node.is_visit or not p_node.is_wolf:
                        break

                    p_node.is_visit = True
                    wolf_cnt += 1
                    node_num = p_node.num

    answer = sheep_cnt
    return answer


if __name__ == '__main__':
    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    print('answer : ' + str(solution(info, edges)))