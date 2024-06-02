import re
import random
from ProcessText import process_text, DirectedGraph, draw_graph
from FindBridge import find_bridge_words
from GenerateNewText import insert_bridge_words
from ShortestWay import shortest_path_from_words, shortest_paths_from_word
from RandomWalking import random_traversal, write_traversal_to_file


def main():
    while True:
        print("请选择一个功能进行测试：")
        print("1: 生成有向图")
        print("2: 查找桥接词")
        print("3: 插入桥接词到新文本")
        print("4: 计算两个单词之间的最短路径")
        print("5: 随机遍历有向图")
        print("q: 退出")
        file_path = "input.txt"

        choice = input("请输入选择: ").strip().lower()

        if choice == '1':
            word_graph = process_text(file_path)
            print("有向图生成完毕。")
            # 输出有向图结构
            print("有向图结构:")
            for node, edges in word_graph.graph.items():
                print(
                    f"{node} -> {', '.join([f'{dest}({weight})' for dest, weight in edges.items()])}")

        elif choice == '2':
            word1 = input("请输入第一个单词: ").strip().lower()
            word2 = input("请输入第二个单词: ").strip().lower()
            bridge_words_result = find_bridge_words(word_graph, word1, word2)
            print(bridge_words_result)

        elif choice == '3':
            new_text_input = input("Enter a new text: ")
            result = insert_bridge_words(word_graph, new_text_input)
            print("The result is:", result)

        elif choice == '4':
            user_input = input("请输入一个单词或者两个单词用空格隔开:").lower().split()
            if len(user_input) == 1:
                start_word = user_input[0]
                paths = shortest_paths_from_word(word_graph, start_word)
                if paths:
                    for end_word, (path, path_length) in paths.items():
                        print(f"'{start_word}' 到 '{end_word}' 的最短路径是:"," → ".join(path))
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

        elif choice == '5':
            visited_edges = random_traversal(word_graph)  # 进行随机遍历
            if visited_edges:
                write_traversal_to_file(visited_edges, "traversal_result.txt")
                traversal_text = " ".join(
                    [edge[0] for edge in visited_edges] + [visited_edges[-1][1]])
                print("随机遍历的节点路径：", traversal_text)
            else:
                print("图中没有可用的边进行游走。")

        elif choice == 'q':
            print("退出程序。")
            break

        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
