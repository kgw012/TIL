# 파일을 실행한 후, test_case.txt를 복사해서 터미널에 입력해주시면 됩니다!


class Node:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value
        self.c_nodes = []
        self.prefix = ''
        self.level = 0


def dfs(node):
    print(f'{node.prefix}[{str(node.value).zfill(3)}]', end='')

    for c_node in node.c_nodes:
        c_node.level = node.level + 1

    if len(node.c_nodes) == 0:
        print()
        return
    
    if len(node.c_nodes) == 1:
        c_node = node.c_nodes[0]
        c_node.prefix += '-----'
        dfs(c_node)
        return
    
    first_c_node = node.c_nodes[0]
    first_c_node.prefix += '--+--'
    dfs(first_c_node)

    for i in range(1, len(node.c_nodes) - 1):
        c_node = node.c_nodes[i]
        c_node.prefix = '     ' * (2 * c_node.level - 1) + '  +--'
        dfs(c_node)
    
    last_c_node = node.c_nodes[-1]
    last_c_node.prefix = '     ' * (2 * last_c_node.level - 1) + '  L--'
    dfs(last_c_node)

    return


if __name__ == '__main__':
    N = int(input())        # 노드의 갯수
    nodes = []              # 노드들이 담길 리스트

    for _ in range(N):
        idx, value = map(int, input().split())
        nodes.append(Node(idx, value))
    
    K = int(input())        # 간선의 갯수

    for _ in range(K):
        p_idx, c_idx = map(int, input().split())
        nodes[p_idx].c_nodes.append(nodes[c_idx])
    
    root_node = nodes[0]
    dfs(root_node)