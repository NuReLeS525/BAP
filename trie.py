class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def autocomplete(self, prefix):
        node = self.root
        results = []
        
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return results

        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)

        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, results)

trie = Trie()
trie.insert("apple")
trie.insert("appetizer")
trie.insert("apricot")
trie.insert("banana")

print(trie.autocomplete("app"))  # ["apple", "appetizer"]
print(trie.autocomplete("ap"))   # ["apple", "appetizer", "apricot"]
print(trie.autocomplete("ban"))  # ["banana"]
print(trie.autocomplete("cat"))  # []