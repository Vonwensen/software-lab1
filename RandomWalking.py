import re
import random
from ProcessText import process_text

def random_traversal(word_graph):
    visited_nodes = set()
    visited_edges = []

    # 从图中随机选择一个起始节点
    start_node = random.choice(list(word_graph.graph.keys()))
    current_node = start_node
    visited_nodes.add(current_node)

    while True:
        out_edges = list(word_graph.get_neighbors(current_node))
        if not out_edges:  # 如果当前节点不存在出边，停止遍历
            print(f"节点 '{current_node}' 没有出边，停止遍历。")
            break

        next_node, _ = random.choice(out_edges)  # 随机选择一个下一个节点
        next_edge = (current_node, next_node)

        if next_edge in visited_edges:  # 如果下一个边已经访问过，停止遍历
            visited_edges.append(next_edge)
            break

        visited_edges.append(next_edge)
        visited_nodes.add(next_node)
        current_node = next_node  # 更新当前节点为下一个节点

    return visited_edges

def write_traversal_to_file(visited_edges, file_path):
    with open(file_path, 'w') as file:
        for edge in visited_edges:
            file.write(" -> ".join(edge) + "\n")
'''
if __name__ == "__main__":
    word_graph = process_text("input.txt")  
    visited_edges = random_traversal(word_graph)  # 进行随机遍历

    if visited_edges:
        write_traversal_to_file(visited_edges, "traversal_result.txt") 
        traversal_text = " ".join([edge[0] for edge in visited_edges] + [visited_edges[-1][1]])
        print("随机遍历的节点路径：", traversal_text)
    else:
        print("图中没有可用的边进行游走。")
'''