import sys
import pickle
from collections import defaultdict

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

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_from_node_iterative(node, prefix)

    def _find_words_from_node_iterative(self, node, prefix):
        stack = [(node, prefix)]
        words = []
        while stack:
            current_node, current_prefix = stack.pop()
            if current_node.is_end_of_word:
                words.append((current_prefix, current_node.frequency))
            for char, next_node in current_node.children.items():
                stack.append((next_node, current_prefix + char))
        words.sort(key=lambda x: x[1], reverse=True)
        return words[:5]

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            root = pickle.load(file)
        trie = Trie()
        trie.root = root
        return trie

def main():
    if len(sys.argv) != 3:
        print("Usage: python load_trie_and_search.py <trie_file> <prefix>")
        sys.exit(1)

    trie_file = sys.argv[1]
    prefix = sys.argv[2]

    trie = Trie.load(trie_file)
    suggestions = trie.search(prefix)
    print(f"Suggestions for '{prefix}': {suggestions}")

if __name__ == "__main__":
    main()
