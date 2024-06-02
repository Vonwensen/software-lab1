from ProcessText import process_text

def find_bridge_words(graph, word1, word2):  
     #查询输入的两个词是否在图中
     if word1 not in graph.graph and word2 not in graph.graph: 
        return f"No '{word1}' and '{word2}' in the graph!"  
     if word1 not in graph.graph:  
        return f"No '{word1}' in the graph!"  
     if word2 not in graph.graph:  
        return f"No '{word2}' in the graph!"  
      
     bridge_words = set()  
     #遍历word1的邻居节点，对于它的每个邻居，检查word是不是在word1邻居的邻居中
     for neighbor in graph.graph[word1]:  
        if word2 in graph.graph[neighbor]:  
            bridge_words.add(neighbor)  
   
     if not bridge_words:  
        return "No bridge words from {} to {}!".format(word1, word2)  
      
     bridge_words_list = list(bridge_words)  
     bridge_words_str = ', '.join(bridge_words_list[:-1]) + bridge_words_list[-1]  
     return "The bridge words from {} to {} is: {}.".format(word1, word2, bridge_words_str) 
'''
if __name__ == "__main__":  
    file_path = 'input.txt'   
    word_graph = process_text(file_path)  
    word1 = input("Enter the first word: ").strip().lower()  
    word2 = input("Enter the second word: ").strip().lower()  
    bridge_words_result = find_bridge_words(word_graph, word1, word2)  
    print(bridge_words_result)
    '''