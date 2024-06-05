import json
import pickle
from collections import defaultdict
import sys

# 增加遞歸深度限制
sys.setrecursionlimit(100000)

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.root, file, protocol=pickle.HIGHEST_PROTOCOL)

def build_trie_from_segmented_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    trie = Trie()
    for item in data:
        segmented_content = item['segmented_content']
        for word in segmented_content:
            trie.insert(word)
    
    return trie

# 建立 Trie 並保存
trie = build_trie_from_segmented_json('segmented_data.json')
trie.save('trie.pkl')