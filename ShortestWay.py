import re
import random
from collections import deque
from ProcessText import process_text

def shortest_path_from_words(graph, start_word, end_word):
    visited = set()  # 存储已访问节点
    predecessors = {}  # 字典存储前驱节点
    queue = deque([start_word])  # 创建队列，加入起始单词
    found = False  # 用于标识找到终点
    path_length = 0

    while queue:
        current_word = queue.popleft()  # 左侧弹出
        if current_word == end_word:  # 如果是终点，设置标志位退出
            found = True
            break
        # 遍历当前节点所有邻居，记录当前节点为邻居的前驱，将邻居加入队列
        for neighbor, weight in graph.get_neighbors(current_word):
            if neighbor not in visited:
                visited.add(neighbor)
                predecessors[neighbor] = current_word
                queue.append(neighbor)

    if not found:
        return None, float('inf')

    # 从最后弹出的节点（终点），往前回溯，直到遇到起始节点
    path = []
    current_word = end_word
    while current_word != start_word:
        path.append(current_word)
        current_word = predecessors[current_word]
    path.append(start_word)
    path.reverse()  # 反转路径

    # 计算路径长度
    #path_length = sum(graph.get_edge_weight(path[i], path[i + 1]) for i in range(len(path) - 1))
    for i in range(len(path) - 1):
        edge_weight = graph.get_edge_weight(path[i], path[i + 1])
        path_length += edge_weight

    return path, path_length

def shortest_paths_from_word(graph, start_word):
    paths = {}
    for end_word in graph.graph.keys():
        if end_word != start_word:
            path, path_length = shortest_path_from_words(graph, start_word, end_word)
            if path is not None:
                paths[end_word] = (path, path_length)
    return paths

def main():
    file_path = "input.txt"
    word_graph = process_text(file_path)

    user_input = input("请输入一个单词或者两个单词用空格隔开:").lower().split()
    if len(user_input) == 1:
        start_word = user_input[0]
        paths = shortest_paths_from_word(word_graph, start_word)
        if paths:
            for end_word, (path, path_length) in paths.items():
                print(f"'{start_word}' 到 '{end_word}' 的最短路径是:", " → ".join(path))
                print(f"长度: {path_length}")
        else:
            print(f"'{start_word}'没有可达路径。")
    elif len(user_input) == 2:
        start_word, end_word = user_input
        path, path_length = shortest_path_from_words(word_graph, start_word, end_word)
        if path:
            print(f"'{start_word}' 倒 '{end_word}' 的最短路径是:", " → ".join(path))
            print(f"长度: {path_length}")
        else:
            print(f"输入的两个单词之间不可达。")
    else:
        print("无效输入。")

if __name__ == "__main__":
    main()
