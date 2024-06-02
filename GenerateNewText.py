import re
import random
from ProcessText import process_text

def find_bridge_wordsa(graph, word1, word2):  
     
     bridge_words = set()  
     if word1  in graph.graph and word2  in graph.graph:
      for neighbor in graph.graph[word1]:  
        
         if word2 in graph.graph[neighbor]:  
            bridge_words.add(neighbor)  
     return bridge_words  
  
def insert_bridge_words(graph, text):   
    words = text.split()  
    new_text = []    
    # 遍历相邻的单词对  
    for i in range(len(words) - 1):  
        word1 = words[i]  
        word2 = words[i + 1]  
        # 查找桥接词  
        bridge_words = find_bridge_wordsa(graph, word1, word2)  
        # 如果存在桥接词，则随机选择一个并插入  
        if bridge_words:  
            bridge_word = random.choice(list(bridge_words))  
            new_text.append(word1)  
            new_text.append(bridge_word)  
        else:  
            # 如果没有桥接词，则直接添加单词  
            new_text.append(word1)  
    # 添加最后一个单词  
    new_text.append(words[-1])  
    return ' '.join(new_text) 
'''
if __name__ == "__main__":  
     file_path = 'input.txt' 
     word_graph = process_text(file_path)  
  
new_text_input = input("Enter a new text: ")  
result = insert_bridge_words(word_graph, new_text_input)  
print("The result is:",result)

'''





